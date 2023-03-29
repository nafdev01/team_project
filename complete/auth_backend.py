import sqlite3
import hashlib
from validation import *
import pyotp
import qrcode
import sqlite3
import random
import string


class Session:
    def __init__(self):
        self.username = None
        self.status = None

    def set_online(self, username):
        self.username = username
        self.status = "online"
        self.update_session(username, self.status)

    def set_offline(self):
        self.status = "offline"
        self.update_session(self.username, self.status)

    def update_session(self, username, status):
        # connect to the database
        conn = sqlite3.connect("secure_chat.db")
        # create a cursor object
        c = conn.cursor()
        # execute the update query
        c.execute(
            "UPDATE user_sessions SET status = ? WHERE username = ?", (status, username)
        )
        # commit the changes to the database
        conn.commit()
        # close the database connection
        conn.close()
        self.reset

    def reset(self):
        self.__init__()


class Log:
    def submit_log(self, username, action):
        # connect to the database
        conn = sqlite3.connect("secure_chat.db")
        # create a cursor object
        c = conn.cursor()
        # execute the update query
        c.execute(
            "INSERT INTO user_logs (username, action) VALUES (?, ?)",
            (username, action),
        )
        # commit the changes to the database
        conn.commit()
        # close the database connection
        conn.close()


class SignUp:
    def __init__(self):
        self.username = None
        self.password = None
        self.confirm_password = None
        self.secret_key = None
        self.form_data = None
        self.hashed_password = None
        self.salt = self.generate_salt()
        self.VALIDATORS = [
            UserNameValidator,
            PasswordValidator,
            ConfirmPasswordValidator,
            SecretKeyValidator,
        ]
        self.errors = dict()
        self.is_valid = False

    def generate_salt(self):
        letters = string.ascii_letters
        return "".join(random.choice(letters) for i in range(12))

    def process_form(self, username, password, confirm_password):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

        self.form_data = {
            "username": self.username,
            "password": self.password,
            "confirm_password": self.confirm_password,
            "secret_key": self.secret_key,
        }

    def validate_form(self):
        self.errors.clear()
        for validator_class in self.VALIDATORS:
            validator = validator_class(self.form_data)
            if not validator.is_valid():
                self.errors.update(validator.errors)

        if self.errors:
            # Handle validation errors
            self.is_valid = False
        else:
            # Process form data
            self.is_valid = True

    def generate(self, nickname):
        self.secret_key = pyotp.random_base32()
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        # The provisioning_uri is used to create the QR code
        provisioning_uri = pyotp.totp.TOTP(self.secret_key).provisioning_uri(
            name=f"{nickname}", issuer_name="Secure LAN Chat"
        )
        # Add the provisioning_uri data to the QR code object
        qr.add_data(provisioning_uri)
        qr.make(fit=True)
        # Create an image of the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        return [img, self.secret_key]

    def get_user(self, username):
        conn = sqlite3.connect("secure_chat.db")
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS "user_logs" (
                "log_id"	INTEGER,
                "username"	TEXT NOT NULL,
                "action"	TEXT NOT NULL,
                FOREIGN KEY("username") REFERENCES "users"("username"),
                PRIMARY KEY("log_id" AUTOINCREMENT)
);
        """
        )
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS "user_sessions" (
            "session_id"	INTEGER,
            "username"	TEXT NOT NULL,
            "status"	TEXT NOT NULL DEFAULT 'offline',
            FOREIGN KEY("username") REFERENCES "users"("username"),
            PRIMARY KEY("session_id" AUTOINCREMENT)
            );
            """
        )
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS "users" (
            "user_id" INTEGER,
            "username" TEXT,
            "password" TEXT,
            "salt" TEXT,
            "secret_key" TEXT,
            PRIMARY KEY("user_id" AUTOINCREMENT)
        );
    """
        )
        c.execute("SELECT username FROM users WHERE username=?", (username,))
        user = c.fetchone()
        conn.close()
        if user:
            return True
        else:
            return False

    def hash_password(self):
        # Hash the password using the salt
        hashed_password = hashlib.sha256(
            (self.password + self.salt).encode()
        ).hexdigest()
        return hashed_password

    def store_user_info(self):
        self.hashed_password = self.hash_password()
        conn = sqlite3.connect("secure_chat.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO users (username, password, salt, secret_key) VALUES (?, ?, ?, ?)",
            (
                self.username,
                self.hashed_password,
                self.salt,
                self.secret_key,
            ),
        )
        c.execute(
            "INSERT INTO user_sessions (username, status) VALUES (?, ?)",
            (self.username, "offline"),
        )
        conn.commit()
        conn.close()
        return "User information stored successfully"

    def reset(self, username, password, confirm_password):
        self.__init__()
        username.setText("")
        password.setText("")
        confirm_password.setText("")


class LogIn:
    def __init__(self):
        self.username = None
        self.password = None
        self.db_password = None
        self.two_factor_code = None
        self.secret_key = None
        self.form_data = None
        self.errors = dict()
        self.is_valid = False
        self.user = None
        self.salt = None

    def process_form(self, username, password, two_factor_code):
        self.username = username
        self.password = password
        self.two_factor_code = two_factor_code

        self.form_data = {
            "username": self.username,
            "password": self.password,
            "two_factor_code": self.two_factor_code,
        }

    def authenticate_2fa(self):
        # Create the TOTP object
        totp = pyotp.TOTP(self.secret_key)
        # Verify the user's code
        if totp.verify(self.two_factor_code):
            return True
        else:
            return False

    def hash_password(self):
        # Hash the password using the salt
        hashed_password = hashlib.sha256(
            (self.password + self.salt).encode()
        ).hexdigest()
        return hashed_password

    def get_user(self):
        # Connect to the database
        conn = sqlite3.connect("secure_chat.db")
        c = conn.cursor()

        # Query the database for the user with the given username
        c.execute("SELECT * FROM users WHERE username=?", (self.username,))
        user = c.fetchone()

        # If the user was found, return their details as a dictionary
        if user is not None:
            self.username = user[1]
            self.db_password = user[2]
            self.salt = user[3]
            self.secret_key = user[4]
            return user
        else:
            return None

    def authenticate_user(self):
        authenticated = False
        user = self.get_user()
        if user:
            if self.hash_password() == self.db_password:
                tfa = self.authenticate_2fa()
                if tfa:
                    authenticated = True

        # If the user was not found, return None
        return authenticated

    def reset(self, username, password, two_factor_code):
        self.__init__()
        username.setText("")
        password.setText("")
        two_factor_code.setText("")

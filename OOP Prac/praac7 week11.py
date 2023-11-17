import hashlib

class User:
    def __init__(self, username, password):
        # Create a user object. The password is encrypted before storing.
        self.__username = username
        self.__password = self._encryptPassword(password)
        self.loggedIn = False

    def _encryptPassword(self, password):
        # Encrypt the password with the username and return the sha digest.
        hash_string = self.__username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def checkPassword(self, password):
        # Returns True if the password is valid for this user, false otherwise.
        encrypted = self._encryptPassword(password)
        return encrypted == self.__password
    
    
class Authenticator:
    def __init__(self):
        self.__users = dict()
    
    def addUser(self, username, password):
        newUser = username
        userPassword = password
        
        if len(userPassword) <= 6:
            raise PasswordTooShort(username)
        
        if username in self.__users:
            raise UsernameAlreadyExists(username)
        else:    
            self.__users[newUser] = userPassword
    
    
    def login(self, username, password):
        loginUsername = username
        loginPassword = password

            if loginUsername not in self.__users:
                raise InvalidUsername(loginUsername)
        
            checkpassword()

class AuthenticationException(Exception):
    def __init__(self, username):
        super().__init__(username)
        self.username = username
    
class InvalidUsername(AuthenticationException):
    
    
    pass

class InvalidPassword(AuthenticationException):
    
    
    pass

class UsernameAlreadyExists(AuthenticationException):
    
    
    pass

class PasswordTooShort(AuthenticationException):
    
    
    pass


authenticator = Authenticator()
print("\n-------------------------------------------------")
try:
    authenticator.addUser("x_EliteSniperz_x", "password123")
    print(authenticator.isLoggedIn("x_EliteSniperz_x"))
    authenticator.login("x_EliteSniperz_x", "password321")
except AuthenticationException as e:
    print("A user attempted to login: " + type(e).__name__, e.username)
try:
    authenticator.login("x_EliteSniperz_x", "password123")
    print(authenticator.isLoggedIn("x_EliteSniperz_x"))
    authenticator.addUser("x_EliteSniperz_x", "NewPassword123!")
except AuthenticationException as e:
    print("A user attempted to be added: " + type(e).__name__, e.username)
try:
    authenticator.login("360NoScopeGod", "123")
except AuthenticationException as e:
    print("A user attempted to login: " + type(e).__name__, e.username)
try:
    authenticator.addUser("360NoScopeGod", "123")
except AuthenticationException as e:
    print("A user attempted to be added: " +type(e).__name__, e.username)
    print("-------------------------------------------------\n")
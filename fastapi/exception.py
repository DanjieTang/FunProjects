class AuthenticationError(Exception):
    """
    Exception raised for errors in the authentication process.
    """

    def __init__(self, message="Username or password is incorrect"):
        self.message = message
        super().__init__(self.message, status_code=401)
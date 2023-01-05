class JutgeDataError(Exception):
    """base exception for this package"""


class ProblemError(JutgeDataError):
    """trying to access public data cases"""


class LoginError(JutgeDataError):
    """the auth is expired/incorrect"""


class UnknownUserError(JutgeDataError):
    """user not configured"""

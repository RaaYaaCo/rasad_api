import random

from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens(user) -> dict:
    """
        The function "get_tokens()" takes in "user" and returns a "dict".
        The "dict" gives us 'access token' and 'refresh token'.
    """
    refresh = RefreshToken.for_user(user)

    return {
        "Refresh": str(refresh),
        "Access": str(refresh.access_token)
    }


def code(length: int = 5) -> str:
    """
        The function "code()" takes in "length" and returns a five-length string for default.
    """
    chars = "0123456789"
    ret = ""
    for i in range(length):
        rand = random.choice(chars)
        # print(rand)
        ret += rand

    return ret

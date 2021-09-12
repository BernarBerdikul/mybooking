from ..models import AllowedUser


def is_user_allowed(username: str) -> bool:
    """ Search user in DB by username from Telegram """
    return AllowedUser.objects.filter(username=username).exists()

from domain.User import User
from typing import Dict, List

class UniqueConstraintError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

_users: Dict[str, User] = {
    "admin": User("admin", "adminpass", "Admin", "Admin", 0.0)
}

_logged_in_user: User|None = None

def get_logged_in_user() -> User|None:
    return _logged_in_user

def set_logged_in_user(user: User):
    global _logged_in_user # anti-pattern but ok for this simple app
    _logged_in_user = user

def reset_logged_in_user():
    global _logged_in_user
    _logged_in_user = None

def query_user(username: str) -> User|None:
    try:
        return _users[username]
    except KeyError:
        return None

def query_all_users() -> List[User]:
    return list(_users.values())

def create_new_user(user: User):
    if user.username in _users:
        raise UniqueConstraintError(f"User with username {user.username} already exists")
    _users[user.username] = user

def delete_user(username: str):
    if username not in _users:
        raise Exception(f"User with username {username} does not exist")
    if username == "admin":
        raise Exception("Cannot delete admin user")
    del _users[username]
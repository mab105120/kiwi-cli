from domain.User import User
from typing import Dict, List

_users: Dict[str, User] = {
    "admin": User("admin", "adminpass", "Admin Firstname", "Admin Lastname", 0.0)
}

def query_user(username: str) -> User|None:
    try:
        return _users[username]
    except KeyError:
        return None

def query_all_users() -> List[User]:
    return list(_users.values())

def create_new_user(user: User):
    _users[user.username] = user
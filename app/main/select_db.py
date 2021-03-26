from app import db
from ..models import User


def select_name_user():
    user = User.query.all()
    return user


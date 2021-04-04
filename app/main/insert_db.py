import sqlite3


def insert_user(name):
    user = models.User(name=name)
    db.session.add(user)
    db.session.commit()


if __name__ == "__main__":
    insert_user('Selivan')

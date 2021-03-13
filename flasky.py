import os
import click
from flask_migrate import Migrate
from app import create_app, db, admin
from app.models import User, Role, Permission
from flask_admin.contrib.sqla import ModelView

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


'''
for key in dict_models:

    admin.add_view(ModelView(dict_models[key], db.session))
'''

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

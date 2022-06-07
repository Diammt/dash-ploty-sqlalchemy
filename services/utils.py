from services.server import server
from services.db import db
import logging as lg

class LaunchCommand(object):
    BASE_API_SWAGGER_URL = '/static/swagger.json'
    DEPLOYEMENT_BASE_PATH = server.config.get("DEPLOYEMENT_BASE_PATH", "/")

    def __init__(self, *args):
        super(LaunchCommand, self).__init__(*args)

    @classmethod
    def init_db(cls):
        db.engine.execute("SET foreign_key_checks = 0")
        db.drop_all()
        db.create_all()
        db.engine.execute("SET foreign_key_checks = 1")
        db.session.commit()
        lg.warning('Database initialized!')

    @classmethod
    def clear(cls):
        db.engine.execute("SET foreign_key_checks = 0")
        db.drop_all()
        db.engine.execute("SET foreign_key_checks = 1")
        db.session.commit()
        lg.warning('Database clear successfully!')

    @classmethod
    def basic_migration(cls):
        pass

    @classmethod
    def advanced_migration(cls):
        pass

    @classmethod
    def dev_migration(cls):
        cls.basic_migration()
        cls.advanced_migration()
        # lg.warning("All pairs generate successfully")
        lg.warning("Data initialize for developpement")

    @classmethod
    def migrate(cls, model):
        # click.echo('Cc')
        pass

from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from app import create_app
from app.models import db
from app.migrations.create_db import create_movie_db_data

settings = 'app.settings.local'
app = create_app(settings_path=settings)

manager = Manager(app)
manager.add_command('server', Server(threaded=True))
manager.add_command('db', MigrateCommand)

@manager.command
def createdb():
	db.create_all()
	print("All tables creates successfully")

@manager.command
def insert_basic_data():
	create_movie_db_data()

if __name__ == '__main__':
	manager.run()


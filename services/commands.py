from services.server import server
from services.utils import LaunchCommand
import logging as lg
import click


def register_all_commands():
    lg.warning("Commands starting")

    @server.cli.command()
    def init_db():
        LaunchCommand.init_db()

    @server.cli.command()
    def clear():
        LaunchCommand.clear()

    @server.cli.command()
    def dev_migration():
        LaunchCommand.dev_migration()

    @server.cli.command()
    def basic_migration():
        LaunchCommand.basic_migration()

    @server.cli.command()
    def advanced_migration():
        LaunchCommand.advanced_migration()

    @server.cli.command()
    @click.option('-m', '--model-to-echo', 'model')
    def migrate(model):
        LaunchCommand.migrate(model)

    @server.cli.command()
    def api_generate():
        LaunchCommand.api_generate()

    @server.cli.command()
    def assign_logo_pm():
        LaunchCommand.assign_logo_pm()

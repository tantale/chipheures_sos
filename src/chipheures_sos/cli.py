# coding: utf-8
"""
Command Line Interface
"""
import sys

import click

from chipheures_sos import __version__
from chipheures_sos.app import App


@click.group()
@click.version_option(__version__)
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    """
    Tool for database maintenance of the Chip'heures web application.

    \f
    :param ctx:
    :param debug: debug flag
    """
    ctx.ensure_object(App)
    ctx.obj.debug = debug


@cli.command(name="list")
@click.argument("database", metavar="DB")
@click.pass_context
def list_tables(ctx, database):
    """
    List the database tables and show record counts.

    \b
    DB   path to the SQlite database to read.

    \f
    :param ctx:
    :param database: path to the database
    """
    #: :type app: chipheures_sos.app.App
    app = ctx.obj
    app.list_tables(database)


if __name__ == '__main__':
    cli(sys.argv[1:])

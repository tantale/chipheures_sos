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
@click.option("--debug/--no-debug", default=False)
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


@cli.command(name="close_orders")
@click.argument("database", metavar="DB")
@click.option(
    "-d",
    "--date",
    "max_date",
    type=click.DateTime(["%Y-%m-%d"]),
    default=None,
    help=u"Close orders which are older than this date, if missing the date is detected by examining the tracked times",
)
@click.option(
    "--dry-run/--no-dry-run", default=True, help=u"Dry run", show_default=True,
)
@click.pass_context
def close_orders(ctx, database, max_date, dry_run):
    """
    Close the "old" orders.

    \b
    DB   path to the SQlite database to read.

    \f
    :param ctx:
    :param database: path to the database
    :param max_date: maximum date use to close an order (UTC time).
    """
    #: :type app: chipheures_sos.app.App
    app = ctx.obj
    app.dry_run = dry_run
    app.close_orders(database, max_date)


if __name__ == "__main__":
    cli(sys.argv[1:])

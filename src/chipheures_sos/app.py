# coding: utf-8
"""
Main Application Class
"""
import click

from chipheures_sos.db import Database


class App(object):
    debug = False

    def __init__(self):
        pass

    def list_tables(self, database):
        if self.debug:
            click.secho("Running show_stats...", fg="yellow")
        with Database(database) as db:
            db.list_tables()

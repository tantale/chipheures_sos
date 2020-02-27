# coding: utf-8
"""
Chip'Heures Database
"""
import sqlite3

import click


class Database(object):
    """Database Connection"""

    excluded_table_names = {u"alembic_version"}

    def __init__(self, database):
        self._database = database
        self._conn = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._database)
        return self

    def __exit__(self, type_, value_, traceback_):
        if self._conn is not None:
            conn = self._conn
            self._conn = None
            conn.close()

    def list_tables(self):
        cursor = self._conn.cursor()
        names = sorted(
            row[0]
            for row in cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"')
            if row[0] not in self.excluded_table_names
        )
        count = len(names)
        msg = {0: u"No tables found.", 1: u"{count} table found:", 2: u"{count} tables found:"}[min(2, count)]
        click.secho(msg.format(count=count), fg="green")
        name_len = max(map(len, names))
        for name in names:
            rows = cursor.execute('SELECT COUNT(*) FROM `{name}`'.format(name=name)).fetchall()
            count = rows[0][0]
            click.echo(u"- {name:<{name_len}} : {count:>6}".format(name=name, count=count, name_len=name_len))

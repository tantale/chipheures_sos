# coding: utf-8
"""
Main Application Class
"""
import datetime

import click

from chipheures_sos.db import Database


class App(object):
    debug = False
    dry_run = False

    def list_tables(self, database):
        if self.debug:
            click.secho("Running list_tables...", fg="yellow")
        #: :type db: chipheures_sos.db.Database
        with Database(database) as db:
            db.list_tables()

    def close_orders(self, database, max_date):
        max_date = max_date or datetime.date.today() - datetime.timedelta(days=365 // 2)
        if self.debug:
            click.secho("Running close_orders...", fg="yellow")
        #: :type db: chipheures_sos.db.Database
        with Database(database) as db:
            orders = db.get_orders()
            for order in orders:
                if order.close_date:
                    click.echo(u"{order} already close at {order.close_date}".format(order=order))
                    continue
                last_even_date = db.get_last_event_date(order) or order.creation_date
                if last_even_date < max_date:
                    close_date = last_even_date + datetime.timedelta(days=1)
                    click.echo(u"{order} is closed at {close_date}".format(order=order, close_date=close_date))
                    if not self.dry_run:
                        db.close_order(order, close_date)
                else:
                    click.echo(u"{order} is not closed".format(order=order))

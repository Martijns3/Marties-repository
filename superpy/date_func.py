from datetime import datetime, timedelta, date
import pandas as pd
import argparse
from rich.console import Console
from rich.table import Table
import os

# yesterday's date/ today's date/ tomorrow's date /back date - advance date (-99/+99)
class Datefunctions1(argparse.Action):
    def __call__(self, parser, namespace, shift=0, option_strings=None):
        if -100 <= shift >= 100:
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column("SuperPy Date", justify="center", style="red")
            t.add_row(
                "ERROR, please enter an amount between -99 and 99. Date set to today... "
            )
            console.print(t)
            return
        now = datetime.now()
        dateshift = timedelta(days=shift)
        new_date = [str(now.date() + dateshift)]
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str(new_date))


# get this week until now
class Datefunctions2(argparse.Action):
    def __call__(self, parser, namespace, shift, option_strings=None):

        now = datetime.now()
        timeframe = [str(now.date())]
        delta = now.weekday() - 0
        dateshift = timedelta(days=-delta)
        begin_week = str(now.date() + dateshift)
        timeframe.append(begin_week)
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str(timeframe))


# get this month until now
class Datefunctions3(argparse.Action):
    def __call__(self, parser, namespace, shift, option_strings=None):

        now = datetime.now()
        timeframe = [str(now.date())]
        delta_slice = str(now)[:-18] + "01"
        timeframe.append(delta_slice)
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str(timeframe))


# get this year until now
class Datefunctions4(argparse.Action):
    def __call__(self, parser, namespace, shift, option_strings=None):

        now = datetime.now()
        timeframe = [str(now.date())]
        delta_slice = str(now)[:-21] + "01-01"
        timeframe.append(delta_slice)
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str(timeframe))


# set a specific period range, or one month block, startting from the first day
class Datefunctions5(argparse.Action):
    def __call__(self, parser, namespace, date_list, option_strings=None):

        min_date = date_list[0]
        try:
            max_date = date_list[1]
        except:
            date_convert = pd.Timestamp(date_list[0])
            max_date = date_convert + pd.DateOffset(months=1, days=-1)
        timeframe = []
        t1 = str(pd.Timestamp(max_date))
        t2 = str(pd.Timestamp(min_date))
        timeframe.append(t1[:-9]),
        timeframe.append(t2[:-9])
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str(timeframe))


# set a period range of one year, from jan 01 until dec 31
class Datefunctions6(argparse.Action):
    def __call__(self, parser, namespace, date_list, option_strings=None):

        min_date = date_list[0]
        try:
            max_date = date_list[1]
        except:
            date_convert = pd.Timestamp(date_list[0])
            max_date = date_convert + pd.DateOffset(years=1, days=-1)
        timeframe = []
        t1 = str(pd.Timestamp(max_date))
        t2 = str(pd.Timestamp(min_date))
        timeframe.append(t1[:-9]),
        timeframe.append(t2[:-9])
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str(timeframe))


# set any specific date and check input
class Datefunctions7(argparse.Action):
    def __call__(self, parser, namespace, date_str, option_strings=None):
        try:
            date.fromisoformat(date_str)
        except ValueError:
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column("SuperPy Date", justify="center", style="red")
            t.add_row("ERROR, please enter a correct date. Date set to today... ")
            console.print(t)
            return
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str([date_str]))


# set range from certain date until now
class Datefunctions8(argparse.Action):
    def __call__(self, parser, namespace, date_str, option_strings=None):

        min_date = date_str
        max_date = dateinfo.get_date(0)
        timeframe = []
        t1 = str(pd.Timestamp(max_date))
        t2 = str(pd.Timestamp(min_date))
        timeframe.append(t1[:-9]),
        timeframe.append(t2[:-9])
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str(timeframe))


# set range for one day: yesterday's date/ today's date
class Datefunctions9(argparse.Action):
    def __call__(self, parser, namespace, shift=0, option_strings=None):
        if -2 <= shift >= 2:
            return
        now = datetime.now()
        dateshift = timedelta(days=shift)
        new_date = str(now.date() + dateshift)
        timeframe = []
        t1 = new_date
        t2 = new_date
        timeframe.append(t1)
        timeframe.append(t2)
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str(timeframe))


class dateinfo:
    def __init__(self, shift):
        self.shift = shift

    def get_date(shift=0):
        now = datetime.now()
        dateshift = timedelta(days=shift)
        return str(now.date() + dateshift)

    def date_range():
        try:
            with open((os.path.join(os.getcwd(), "date.txt")), "r") as f:
                lines = f.read()
        except:
            now = datetime.now()
            new_date = [str(now.date())]
            with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
                f.write(str(new_date))

        with open("date.txt", "r") as f:
            lines = f.read()
            end_date = lines[2:12]
            if len(lines) <= 14:
                start_date = "1970-01-01"
            else:
                start_date = lines[16:26]
            dates = [end_date, start_date]
            return dates

    def date_reset(shift=0):

        now = datetime.now()
        dateshift = timedelta(days=shift)
        new_date = [str(now.date() + dateshift)]
        with open((os.path.join(os.getcwd(), "date.txt")), "w") as f:
            f.write(str(new_date))

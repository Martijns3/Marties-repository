# Imports
import argparse
import csv
import os
from datetime import date
from rich.console import Console
from rich.table import Table
import pandas as pd
import collections
import functools
import operator
import itertools
from date_func import *
from matplotlib_func import matplotlib_print

__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.


def main():
    inputs = parse_args()


class bought:
    def __init__(self, prod_name, amount, price, exp_date):
        self.prod_name = prod_name
        self.amount = amount
        self.price = price
        self.exp_date = exp_date

    # generates a new line to batch list
    def buy_inventory(self, prod_name, amount, price, exp_date):
        # buy inventory, first check if amounts are bigger then zero
        if amount <= 0:
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column("SuperPy Sales", justify="center", style="red")
            t.add_row("   ERROR, please enter an amount greater then 0.          ")
            console.print(t)
            return
        elif price <= 0:
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column("SuperPy Sales", justify="center", style="red")
            t.add_row("   ERROR, please enter a price greater then 0.          ")
            console.print(t)
            return
        else:
            pass
        # date range import, open csv and check last used batch ID number; add 1 to latest ID
        date_info = dateinfo.date_range()
        date_purch = date_info[0]
        date_exp = date.fromisoformat(str(exp_date))
        try:
            reader = csv.DictReader(
                open(os.path.join(os.getcwd(), "bought.csv"), newline="")
            )
        except:
            with open(
                os.path.join(os.getcwd(), "bought.csv"), "a", newline=""
            ) as csvfile:
                header = (
                    "id",
                    "product",
                    "amount",
                    "purch_date",
                    "price",
                    "expired",
                    "spare",
                )
                SuperPyWriter = csv.writer(
                    csvfile,
                    delimiter=",",
                )
                SuperPyWriter.writerow(header)
        reader = csv.DictReader(
            open(os.path.join(os.getcwd(), "bought.csv"), newline="")
        )

        for row in reader:
            pass
        try:
            last_row = int(row["id"])
            line_id = last_row + 1
        except:
            line_id = 0
            print(line_id)
        # write new batch line to "bought.csv" and reset date to "now"
        with open(os.path.join(os.getcwd(), "bought.csv"), "a", newline="") as csvfile:
            SuperPyWriter = csv.writer(
                csvfile, delimiter=",", quotechar=";", quoting=csv.QUOTE_MINIMAL
            )
            SuperPyWriter.writerow(
                [line_id]
                + [prod_name]
                + [amount]
                + [date_purch]
                + [price]
                + [date_exp]
                + [""]
            )
            console = Console(color_system="auto")
            t1 = Table(title="", title_justify="center", width=80)
            t1.add_column("Message", justify="center", style="green")
            t1.add_row("Batchlist update success!")
            console.print(t1)
        os.remove(os.path.join(os.getcwd(), "date.txt"))

    # uses 2 functions in order to generate a batch list to the state that it was on a given date and then print
    def open_inventory_batch():
        bought.build_list_to_date()
        bought.print_batchlist()

    # generate a batch list to the state that it was on a given date
    def build_list_to_date():
        try:
            os.remove(os.path.join(os.getcwd(), "temp.csv"))
        except:
            pass
        with open((os.path.join(os.getcwd(), "bought.csv")), "r") as csvfile:
            date_info = dateinfo.date_range()
            today = date_info[0]
            start_date = date_info[1]
            heading = next(csvfile)
            reader = csv.reader(csvfile)

            # this code calls the batch_mutations function, which grabs all mutations from the sold.csv file made AFTER the given date
            mutations_list = bought.batch_mutations()
            try:
                totals = dict(
                    functools.reduce(
                        operator.add, map(collections.Counter, mutations_list)
                    )
                )
            except:
                totals = {}

            # This code checks if batches are in the given data range and adds an "expired" flag to a batch when appropriate.
            # It also writes the currently collected and generated info in a temp.csv file.
            # I decided to use a temp file for this, because I wanted to leave bought.csv, the "heart" where all actual stock positions are stored, unharmed.
            with open(
                os.path.join(os.getcwd(), "temp.csv"), "a", newline=""
            ) as csvfile:
                header = [
                    "id",
                    "product",
                    "amount",
                    "purch_date",
                    "price",
                    "expired",
                    "spare",
                ]
                SuperPyWriter = csv.writer(
                    csvfile,
                    delimiter=",",
                )
                SuperPyWriter.writerow(header)
            for row in reader:
                if len(row):
                    if start_date <= row[3] <= today:
                        if row[5] < today:
                            row[6] = "Expired"
                        with open(
                            os.path.join(os.getcwd(), "temp.csv"), "a", newline=""
                        ) as csvfile:
                            SuperPyWriter = csv.writer(
                                csvfile,
                                delimiter=",",
                                quotechar=";",
                                quoting=csv.QUOTE_MINIMAL,
                            )
                            SuperPyWriter.writerow(row)

            # this code calculates and writes the new amounts per batch (amounts minus cumulative mutations per batch) to the temp.csv)
            with open((os.path.join(os.getcwd(), "temp.csv")), "r") as csvfile:
                reader = csv.reader(csvfile)
                batch_adjustment = []
                next(reader)
                for row in reader:
                    for tt in totals:
                        if (tt) == int(row[0]):
                            amount = row[2]
                            batch_adjustment.append(
                                {int(tt): float(amount) + totals[tt]}
                            )

            with open((os.path.join(os.getcwd(), "temp.csv")), "r") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    for data in batch_adjustment:
                        for k in data:
                            if len(row) > 0:
                                if k == int(row[0]):
                                    amount = "amount"
                                    df = pd.read_csv(
                                        (os.path.join(os.getcwd(), "temp.csv")),
                                        usecols=[i for i in range(7)],
                                    )
                                    df.loc[int(k), amount] = data[k]
                                    df.to_csv(
                                        (os.path.join(os.getcwd(), "temp.csv")),
                                        index=False,
                                    )

    # print the generated batch list
    def print_batchlist():
        # this code reopens the temp.csv file with corrected amounts, resets date to TODAY and deletes temp file
        date_info = dateinfo.date_range()
        today = date_info[0]

        console = Console(color_system="auto")
        t = Table(
            title=f"SuperPy Inventory by batch, at {today}",
            title_justify="center",
            width=90,
        )
        t.add_column("ID", justify="right", style="cyan")
        t.add_column("Product", justify="right", style="cyan")
        t.add_column("Amount / kg", justify="right", style="cyan")
        t.add_column("Purchase Date", justify="center", style="cyan")
        t.add_column("Unit Price", justify="right", style="cyan")
        t.add_column("Expiration Date", justify="center", style="cyan")
        t.add_column("Expired", justify="center", style="red")
        with open((os.path.join(os.getcwd(), "temp.csv")), "r") as csvfile:
            reader2 = csv.reader(csvfile)
            next(reader2)
            for row2 in reader2:
                if float(row2[2]) != 0:
                    t.add_row(*row2)
            console.print(t)
        os.remove(os.path.join(os.getcwd(), "temp.csv"))
        os.remove(os.path.join(os.getcwd(), "date.txt"))

    # batch mutations is a helper function to build_list_to_date,
    # that gets all mutations from "sold.csv" after a given date
    def batch_mutations():
        # this code gets all mutations from the sold.csv file after the given date
        with open((os.path.join(os.getcwd(), "sold.csv")), "r") as csvfile:
            date_info = dateinfo.date_range()
            today = date_info[0]
            start_date = date_info[1]
            heading = next(csvfile)
            reader = csv.reader(csvfile)
            mutations_list = []
            for row in reader:
                if len(row) > 0:
                    if today < row[4]:
                        mutations_list.append({int(row[5]): float(row[2])})
        return mutations_list

    # generates a list with expired items from "bought.csv", on a given date
    def open_inventory_expired():
        reader = csv.DictReader(
            open(os.path.join(os.getcwd(), "bought.csv"), newline="")
        )
        expired_list = []

        date_info = dateinfo.date_range()
        today = date_info[0]
        for row in reader:
            if row["expired"] < today:
                if float(row["amount"]) > 0:
                    expired_list.append(
                        [
                            row["id"],
                            row["product"],
                            row["amount"],
                            row["purch_date"],
                            row["price"],
                            row["expired"],
                        ]
                    )
        console = Console(color_system="auto")
        t = Table(
            title=f"SuperPy Expired batches, at {today}",
            title_justify="center",
            width=80,
        )
        t.add_column("ID", justify="left", style="cyan")
        t.add_column("Product", justify="right", style="cyan")
        t.add_column("Amount / kg", justify="right", style="cyan")
        t.add_column("Purchase Date", justify="center", style="cyan")
        t.add_column("Unit Price", justify="right", style="cyan")
        t.add_column("Expiration Date", justify="center", style="red")
        for x in expired_list:
            flatten_list = list(itertools.chain(x))
            t.add_row(*flatten_list)
        if t.rows:
            console.print(t)
        else:
            t5 = Table(title="", title_justify="center", width=80)
            t5.add_column("Message", justify="center", style="green")
            t5.add_row("No expired batches found.")
            console.print(t5)
            os.remove(os.path.join(os.getcwd(), "date.txt"))
            return
        # this code exports the "expired items" list to an external csv file "expired batch -date"
        t = Table(title="", title_justify="center", width=80)
        t.add_column("Message", justify="center", style="yellow")
        t.add_row(
            "Press y + enter to create a file with expired batch info, or enter to continue."
        )
        console.print(t)
        q1 = input(":")
        if q1 == "y":
            header = ["id", "product", "amount", "purchase_date", "price", "expired"]
            expired_items = f"expired batch-{today}.csv"
            with open(
                os.path.join(os.getcwd(), expired_items), "w", newline=""
            ) as csvfile:
                SuperPyWriter = csv.writer(csvfile)
                SuperPyWriter.writerow(header)
                SuperPyWriter.writerows(expired_list)
            t1 = Table(title="", title_justify="center", width=80)
            t1.add_column("Message", justify="center", style="green")
            t1.add_row("Expired batch info file created!")
            console.print(t1)
        else:
            pass
        # after user confirmation, this code sets expired items amount to 0 and registers the buying price as costs
        # on the sold.csv. After that, date reset to current date.
        t2 = Table(title="", title_justify="center", width=80)
        t2.add_column("Message", justify="center", style="yellow")
        t2.add_row(
            "Press y + enter to write-off the expired batch(es), or enter to continue."
        )
        console.print(t2)
        q2 = input(":")
        if q2 == "y":
            dateinfo.date_reset()
            exp_item = sold("product", "amount", "0")
            for row in expired_list:

                exp_item.register_sales(row[1], float(row[2]), 0)
            t3 = Table(title="", title_justify="center", width=80)
            t3.add_column("Message", justify="center", style="green")
            t3.add_row("Write-off expired batch(es) success!")
            console.print(t3)
        try:
            os.remove(os.path.join(os.getcwd(), "date.txt"))
        except:
            pass

    # this function creates a batchlist on given date re-using the buil_list_to_date function.
    # after that, the print_inventory function consolidates batches by product and generates a list.
    def open_inventory():
        bought.build_list_to_date()
        bought.print_inventory()

    def print_inventory():
        date_info = dateinfo.date_range()
        today = date_info[0]
        with open(os.path.join(os.getcwd(), "temp.csv"), newline="") as csv_file2:
            reader = csv.DictReader(csv_file2)
            stock_list = []
            for row in reader:
                stock_list.append({row["product"]: float(row["amount"])})
            try:
                totals = dict(
                    functools.reduce(operator.add, map(collections.Counter, stock_list))
                )
            except:
                console = Console(color_system="auto")
                t = Table(title="", title_justify="center", width=80)
                t.add_column(
                    "SuperPy Inventory",
                    justify="center",
                    style="cyan",
                )
                t.add_row(f"No inventory found.")
                console.print(t)
                os.remove(os.path.join(os.getcwd(), "temp.csv"))
                os.remove(os.path.join(os.getcwd(), "date.txt"))
                return
            totals_list = ",  ".join(str(k) + ", " + str(v) for k, v in totals.items())
            split_rows = totals_list.split(",  ")
            console = Console(color_system="auto")
            t = Table(
                title=f"SuperPy Inventory Totals, at {today} ",
                title_justify="center",
                width=80,
            )
            t.add_column("Product", justify="left", style="cyan")
            t.add_column("Amount / kg", justify="right", style="cyan")
            for value in split_rows:
                value = [value]
                z = [i.split(",", 1) for i in value]
                flatten_list = list(itertools.chain(*z))
                t.add_row(*flatten_list)
            console.print(t)
            os.remove(os.path.join(os.getcwd(), "temp.csv"))
            os.remove(os.path.join(os.getcwd(), "date.txt"))

    # uses pandas to edit a given row, based on 'batch id" number.
    def edit_inventory(line_id, update, value):

        if update in ("amount", "price"):
            value = float(value)
        df = pd.read_csv(
            (os.path.join(os.getcwd(), "bought.csv")), usecols=[i for i in range(7)]
        )
        df.loc[line_id, update] = value
        df.to_csv((os.path.join(os.getcwd(), "bought.csv")), index=False)

    # This function is based on foregoing function. However this function contains checks if the correct input was given.
    # The edit_inventory function is also used by other functions. In order to reduce unwanted messages, these functions were separated from each other.
    def edit_inventory2(line_id, update, value):

        check = []
        reader = csv.DictReader(
            open(os.path.join(os.getcwd(), "bought.csv"), newline="")
        )
        for row in reader:
            check.append(int(row["id"]))
        if line_id in check:
            pass
        else:
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column("SuperPy Batch", justify="center", style="red")
            t.add_row("   ERROR, please enter an existing batch ID. ")
            console.print(t)
            return
        if update in ("expired", "purch_date"):
            try:
                value = date.fromisoformat(str(value))
            except:
                console = Console(color_system="auto")
                t = Table(title="", title_justify="center", width=80)
                t.add_column("SuperPy Batch", justify="center", style="red")
                t.add_row("   ERROR, please enter a correct date. ")
                console.print(t)
                return
        if update in ("amount", "price"):
            value = float(value)
        if update not in ("price", "amount", "product", "purch_date", "expired"):
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column("SuperPy Batch", justify="center", style="red")
            t.add_row("   ERROR, please enter a valid value to edit. ")
            console.print(t)
            return
        df = pd.read_csv(
            (os.path.join(os.getcwd(), "bought.csv")), usecols=[i for i in range(7)]
        )
        df.loc[line_id, update] = value
        df.to_csv((os.path.join(os.getcwd(), "bought.csv")), index=False)
        console = Console(color_system="auto", width=80)
        t = Table(width=80)
        t.add_column("SuperPy Batch", justify="center", style="green")
        t.add_row("Batch edit complete!")
        console.print(t)


class sold:
    def __init__(self, prod_name, sold_amount, price_sold):
        self.prod_name = prod_name
        self.sold_amount = sold_amount
        self.price_sold = price_sold

    # registers the sale of items; it takes sold products from the lowest "bought_ID" first
    # and registers batch by batch, until the sold amount is reached. This first code checks if
    # there will be enough stock to sell and if logical data is entered.
    def sell_items(self, prod_name, sold_amount, price_sold):

        reader = csv.DictReader(
            open(os.path.join(os.getcwd(), "bought.csv"), newline="")
        )
        inventory_check = []
        for row in reader:
            if row["product"] == prod_name:
                inventory_check.append(row.get("amount"))
        floats = sum([float(x) for x in inventory_check])

        if floats < float(sold_amount):
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column(
                "SuperPy Sales",
                justify="center",
                style="red",
            )
            t.add_row(f"ERROR, not enough stock! Only {floats} {prod_name}s available.")
            console.print(t)
        elif sold_amount <= 0:
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column("SuperPy Sales", justify="center", style="red")
            t.add_row("   ERROR, please enter an amount greater then 0.          ")
            console.print(t)

        else:
            console = Console(color_system="auto", width=80)
            t = Table(width=80)
            t.add_column("SuperPy Sales", justify="center", style="green")
            t.add_row("***                      Sale ok!                      ***")
            console.print(t)
            sold.register_sales(self, prod_name, sold_amount, price_sold)

    def register_sales(self, prod_name, sold_amount, price_sold):

        # this code looks in what batches the product can be found and controls "edit_inventory and print_sales in order to adjust the stock
        # amounts in "bought.csv" and register the sale in "sold.csv"
        date_info = dateinfo.date_range()
        todaysdate = date_info[0]
        try:
            reader = csv.DictReader(
                open(os.path.join(os.getcwd(), "sold.csv"), newline="")
            )
        except:
            with open(
                os.path.join(os.getcwd(), "sold.csv"), "a", newline=""
            ) as csvfile:
                header = (
                    "id_sold",
                    "product",
                    "sold_amount",
                    "price_sold",
                    "selling_date",
                    "bought_id",
                    "bought_price",
                    "sales_id",
                    "spare",
                )
                SuperPyWriter = csv.writer(
                    csvfile,
                    delimiter=",",
                )
                SuperPyWriter.writerow(header)
        reader = csv.DictReader(open(os.path.join(os.getcwd(), "sold.csv"), newline=""))
        for row in reader:
            pass
        try:
            last_row = int(row["sales_id"])
            line_id3 = last_row + 1
        except:
            line_id3 = 0

        reader = csv.DictReader(
            open(os.path.join(os.getcwd(), "bought.csv"), newline="")
        )
        new_amount = sold_amount
        while new_amount > 0:
            for row in reader:
                if row["product"] == prod_name:
                    if float(row["amount"]) >= new_amount:

                        if new_amount > 0:
                            bought_id = int(row["id"])
                            bought_price = row["price"]
                            sold.print_sales(
                                self,
                                prod_name,
                                new_amount,
                                price_sold,
                                todaysdate,
                                bought_id,
                                bought_price,
                                line_id3,
                            )
                            bought.edit_inventory(
                                bought_id,
                                "amount",
                                ((float(row["amount"])) - new_amount),
                            )
                            new_amount = new_amount - (float(row["amount"]))
                    else:
                        if new_amount > 0:
                            bought_id = int(row["id"])
                            bought_price = row["price"]
                            sold_amount = float(row["amount"])
                            if (float(row["amount"])) > 0:
                                sold.print_sales(
                                    self,
                                    prod_name,
                                    (float(row["amount"])),
                                    price_sold,
                                    todaysdate,
                                    bought_id,
                                    bought_price,
                                    line_id3,
                                )
                                bought.edit_inventory(bought_id, "amount", 0)
                            new_amount = new_amount - (float(row["amount"]))

    # print sales to "sold.csv"
    def print_sales(
        self,
        prod_name,
        sold_amount,
        price_sold,
        todaysdate,
        bought_id,
        bought_price,
        line_id3,
    ):
        reader = csv.DictReader(
            open(os.path.join(os.getcwd(), "bought.csv"), newline="")
        )
        reader = csv.DictReader(open(os.path.join(os.getcwd(), "sold.csv"), newline=""))
        for row in reader:
            pass
        try:
            last_row = int(row["id_sold"])
            line_id2 = last_row + 1
        except:
            line_id2 = 0
        with open(os.path.join(os.getcwd(), "sold.csv"), "a", newline="") as csvfile:
            SuperPyWriter = csv.writer(
                csvfile, delimiter=",", quotechar=";", quoting=csv.QUOTE_MINIMAL
            )
            SuperPyWriter.writerow(
                [line_id2]
                + [prod_name]
                + [sold_amount]
                + [price_sold]
                + [todaysdate]
                + [bought_id]
                + [bought_price]
                + [line_id3]
            )
        try:
            os.remove(os.path.join(os.getcwd(), "date.txt"))
        except:
            pass

    # shows sales transaction list and asks for sale id and amount to return
    def show_sales():
        reader = csv.DictReader(open(os.path.join(os.getcwd(), "sold.csv"), newline=""))
        sales_list = []
        for row in reader:
            sales_list.append({row["sales_id"]: float(row["sold_amount"])})
            totals = dict(
                functools.reduce(operator.add, map(collections.Counter, sales_list))
            )
        sales_list_total = []
        reader = csv.DictReader(open(os.path.join(os.getcwd(), "sold.csv"), newline=""))
        checklist = []
        for row in reader:
            for k, v in totals.items():
                if k not in checklist:
                    if k == row["sales_id"]:
                        if float(row["sold_amount"]) > 0:
                            if float(row["price_sold"]) > 0:
                                sales_list_total.append(
                                    [
                                        k,
                                        row["selling_date"],
                                        row["product"],
                                        row["price_sold"],
                                        str(v),
                                    ]
                                )
                                checklist.append(k)

        console = Console(color_system="auto")
        t = Table(title=f"SuperPy Sales List", title_justify="center", width=80)
        t.add_column("Sale ID", justify="right", style="cyan")
        t.add_column("Sale date", justify="center", style="cyan")
        t.add_column("Product", justify="right", style="cyan")
        t.add_column("Unit price", justify="right", style="cyan")
        t.add_column("Amount", justify="right", style="cyan")

        for i in sales_list_total:
            t.add_row(*i)
        console.print(t)

        t2 = Table(title="", title_justify="center", width=80)
        t2.add_column("Message", justify="center", style="yellow")
        t2.add_row("Please enter the sale ID.")
        console.print(t2)
        check_list = []
        sold_id = input((":"))
        for k in totals.items():
            if sold_id in k:
                check_list.append("ok")
        if len(check_list):
            pass
        else:
            t2 = Table(title="", title_justify="center", width=80)
            t2.add_column("Message", justify="center", style="red")
            t2.add_row("ERROR: Please enter a correct sale ID.")
            console.print(t2)
            return

        t3 = Table(title="", title_justify="center", width=80)
        t3.add_column("Message", justify="center", style="yellow")
        t3.add_row("Please enter the returned amount")
        console.print(t3)
        try:
            amount_returned = float(input((":")))
            sold.return_sales(sold_id, amount_returned)
        except:
            t3 = Table(title="", title_justify="center", width=80)
            t3.add_column("Message", justify="center", style="red")
            t3.add_row("Error: Amount not recognized")
            console.print(t3)
            return

    # books a return of a product with quality issue. Opens sale list first for user to pick the right sales ID.
    def return_sales(sold_id, amount_returned):
        date_info = dateinfo.date_range()
        todaysdate = date_info[0]
        reader = csv.DictReader(open(os.path.join(os.getcwd(), "sold.csv"), newline=""))
        trans_sold_items = []
        for row in reader:
            if (row["sales_id"]) == str(sold_id):
                trans_sold_items.append(float(row["sold_amount"]))
                prod_name = row["product"]
                price_sold = row["price_sold"]
                sold_amount = -(amount_returned)
                totals = sum(trans_sold_items)
        if amount_returned < 1:
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column(
                "SuperPy Sales",
                justify="center",
                style="red",
            )
            t.add_row(f"ERROR, please enter an amount greater than 0.")
            console.print(t)
            os.remove(os.path.join(os.getcwd(), "date.txt"))
            return
        if amount_returned > totals:
            console = Console(color_system="auto")
            t = Table(title="", title_justify="center", width=80)
            t.add_column(
                "SuperPy Sales",
                justify="center",
                style="red",
            )
            t.add_row(
                f"ERROR, only {totals} {prod_name}s can be returned on this sale."
            )
            console.print(t)
            os.remove(os.path.join(os.getcwd(), "date.txt"))
            return

        try:
            last_row = int(row["id_sold"])
            line_id2 = last_row + 1
        except:
            line_id2 = 0

        with open(os.path.join(os.getcwd(), "sold.csv"), "a", newline="") as csvfile:
            SuperPyWriter = csv.writer(
                csvfile, delimiter=",", quotechar=";", quoting=csv.QUOTE_MINIMAL
            )
            SuperPyWriter.writerow(
                [line_id2]
                + [prod_name]
                + [sold_amount]
                + [price_sold]
                + [todaysdate]
                + ["-1"]
                + ["0"]
                + [sold_id]
            )
            console = Console(color_system="auto", width=80)
            t = Table(width=80)
            t.add_column("SuperPy Sales", justify="center", style="green")
            t.add_row("Return product ok!")
            console.print(t)
        os.remove(os.path.join(os.getcwd(), "date.txt"))

    # calculates revenue and profit by product and totals. This function also makes use of a "temp.csv" file
    # it also trggers the matplotlib function on user request.
    def calculate_revenue_profit():
        try:
            os.remove(os.path.join(os.getcwd(), "temp2.csv"))
        except:
            pass
        with open((os.path.join(os.getcwd(), "sold.csv")), "r") as csvfile:
            date_info = dateinfo.date_range()
            today = date_info[0]
            start_date = date_info[1]
            heading = next(csvfile)
            reader = csv.reader(csvfile)
            list1 = []
            for row in reader:
                if len(row) > 0:
                    if start_date <= row[4] <= today:
                        turnover = float(row[2]) * float(row[3])
                        profit = (float(row[3]) - float(row[6])) * float(row[2])
                        list1.append([(row[1]), turnover, profit])

        # generates a list with productnames and a lsit with product name as key and dictionaries per sold line,
        # containing revenue and profit per sold line
        prod_list = []
        for item1 in list1:
            if (item1[0]) not in prod_list:
                prod_list.append(item1[0])
        dict_list = []
        for a in prod_list:
            y = {a: []}
            dict_list.append(y)
        for item1 in list1:
            for d in dict_list:
                for k, v in d.items():
                    if k == item1[0]:
                        d[k].append([item1[1], item1[2]])

        # generates a profit and revenue list by product and writes to "temp2.csv"
        financial_list = []
        for d in dict_list:
            for k, v in d.items():
                result = [
                    sum(x)
                    for x in zip(
                        *map(
                            lambda x: x + [0] * max(map(len, v))
                            if len(x) < max(map(len, v))
                            else x,
                            v,
                        )
                    )
                ]
                result_formatted = [round(float(elem), 2) for elem in result]
                financial_list.append([k, result_formatted])

        with open(os.path.join(os.getcwd(), "temp2.csv"), "a", newline="") as csvfile:
            header = ["product", "revenue", "profit"]
            SuperPyWriter = csv.writer(
                csvfile,
                delimiter=",",
            )
            SuperPyWriter.writerow(header)
            for i in financial_list:
                SuperPyWriter.writerow([i[0]] + [i[1][0]] + [i[1][1]])

        # generates a totals list for revenue and profit and prints tables.
        revenue = []
        profit = []
        totals = []
        for i in financial_list:
            revenue.append(i[1][0])
            profit.append(i[1][1])
        total_revenue = round(sum(revenue), 2)
        total_profit = round(sum(profit), 2)
        totals.append(str(total_revenue))
        totals.append(str(total_profit))
        console = Console(color_system="auto")
        if start_date == "1970-01-01":
            start_date = "start"

        t = Table(
            title=f"SuperPy Revenue and Profit per product, from {start_date} until {today} ",
            title_justify="center",
            width=80,
        )
        t.add_column("Product", justify="left", style="cyan")
        t.add_column("Revenue", justify="right", style="cyan")
        t.add_column("Profit", justify="right", style="cyan")
        t2 = Table(
            title=f"SuperPy Total Revenue and Profit, from {start_date} until {today}",
            title_justify="center",
            width=80,
        )
        t2.add_column("Total Revenue", justify="left", style="cyan")
        t2.add_column("Total Profit", justify="left", style="cyan")
        with open((os.path.join(os.getcwd(), "temp2.csv")), "r") as csvfile:
            reader2 = csv.reader(csvfile)
            next(reader2)
            for row2 in reader2:
                t.add_row(*row2)
            console.print(t)
        t2.add_row(*totals)
        console.print(t2)

        # controls matplotlib_func on user request
        if total_revenue > 0:
            t3 = Table(title="", title_justify="center", width=80)
            t3.add_column("Message", justify="center", style="yellow")
            t3.add_row("Press y + enter to create a matplotlib graphics tab.")
            console.print(t3)
            q1 = input(":")
            if q1 == "y":
                t4 = Table(title="", title_justify="center", width=80)
                t4.add_column("Message", justify="center", style="yellow")
                t4.add_row("Close matplotlib graphics tab to continue.")
                console.print(t4)
                matplotlib_print()
                t5 = Table(title="", title_justify="center", width=80)
                t5.add_column("Message", justify="center", style="green")
                t5.add_row("Matplotlib graphics tab closed.")
                console.print(t5)
        try:
            os.remove(os.path.join(os.getcwd(), "temp2.csv"))
        except:
            pass
        os.remove(os.path.join(os.getcwd(), "date.txt"))


# contains all the arg parsers
def parse_args():

    parser = argparse.ArgumentParser(
        add_help=True,
        usage="super.py [-h] {buy,batch,inventory,expired,edit,sell,return,revenue} ....",
        epilog='-->>See for examples and date options per function: python super.py "function" -h',
    )
    subparsers = parser.add_subparsers(dest="command", required=False)

    buy_parser = subparsers.add_parser(
        "buy",
        help="Buy inventory by batch. Give the following command: python super.py buy 'prod_name' 'amount' 'price' 'exp_date'",
        usage="python super.py buy prod_name amount price exp_date [-y [YESTERDAY]] [-t [TOMORROW]] [-d [DATE]] \nExample: python super.py buy bananas 10 1.34 2022-06-30 -y",
    )
    buy_parser.add_argument("prod_name", type=str, help="enter the product name")
    buy_parser.add_argument("amount", type=float, help="enter the amount or weight")
    buy_parser.add_argument("price", type=float, help="enter the buying price")
    buy_parser.add_argument(
        "exp_date", type=str, help="enter the expiration date in YYYY-MM-DD format"
    )
    buy_parser.add_argument(
        "-y",
        "--yesterday",
        nargs="?",
        const=-1,
        type=int,
        action=Datefunctions1,
        help="set purchase date to yesterday",
    )
    buy_parser.add_argument(
        "-t",
        "--tomorrow",
        nargs="?",
        const=1,
        type=int,
        action=Datefunctions1,
        help="set purchase date to tomorrow",
    )
    buy_parser.add_argument(
        "-d",
        "--date",
        nargs="?",
        action=Datefunctions7,
        help="set any specific date as purchase date",
    )

    batch_parser = subparsers.add_parser("batch", help="Opens inventory batch list")
    batch_parser.add_argument(
        "-y",
        "--yesterday",
        nargs="?",
        const=-1,
        type=int,
        action=Datefunctions1,
        help="Yesterdays date",
    )
    batch_parser.add_argument(
        "-d",
        "--date",
        nargs="?",
        action=Datefunctions7,
        help="set any specific date in YYYY-MM-DD format",
    )

    inventory_parser = subparsers.add_parser(
        "inventory", help="Shows list of totalized batches"
    )
    inventory_parser.add_argument(
        "-y",
        "--yesterday",
        nargs="?",
        const=-1,
        type=int,
        action=Datefunctions1,
        help="set date to yesterday",
    )
    inventory_parser.add_argument(
        "-d",
        "--date",
        nargs="?",
        action=Datefunctions7,
        help="set any specific date in YYYY-MM-DD format",
    )

    expired_parser = subparsers.add_parser(
        "expired", help="Shows list of expired batches"
    )
    expired_parser.add_argument(
        "-y",
        "--yesterday",
        nargs="?",
        const=-1,
        type=int,
        action=Datefunctions1,
        help="set date to yesterday",
    )
    expired_parser.add_argument(
        "-t",
        "--tomorrow",
        nargs="?",
        const=1,
        type=int,
        action=Datefunctions1,
        help="set date to tomorrow",
    )
    expired_parser.add_argument(
        "-ad",
        "--advance-date",
        nargs="?",
        type=int,
        action=Datefunctions1,
        help="advance or back date by set days (-99 / +99",
    )
    expired_parser.add_argument(
        "-d",
        "--date",
        nargs="?",
        action=Datefunctions7,
        help="set any specific date in YYYY-MM-DD format",
    )

    edit_parser = subparsers.add_parser(
        "edit",
        usage="super.py edit [-h] line_id update value.  \nExample: python super.py edit 10 amount 5",
        help="edit items in batch list. Give the following command: python super.py edit 'ID' 'column name' 'new value'",
    )
    edit_parser.add_argument(
        "line_id",
        type=int,
        help="Enter the batch ID (found in the batchlist) of the line you wat to edit",
    )
    edit_parser.add_argument(
        "update",
        type=str,
        help="Enter what you want to adjust. Options are: price,amount,product,purch_date,expired",
    )
    edit_parser.add_argument("value", type=str, help="Enter the new value or name")

    sell_parser = subparsers.add_parser(
        "sell",
        usage="super.py sell [-h] prod_name sold_amount price_sold \nExample for usage: python super.py sell bananas 10 2.99",
        help="sell items. Give the following command: python super.py sell 'product' 'amount' 'price per unit'",
    )
    sell_parser.add_argument("prod_name", type=str)
    sell_parser.add_argument("sold_amount", type=float)
    sell_parser.add_argument("price_sold", type=float)
    sell_parser.add_argument(
        "-y",
        "--yesterday",
        nargs="?",
        const=-1,
        type=int,
        action=Datefunctions1,
        help="set selling date to yesterday",
    )
    sell_parser.add_argument(
        "-t",
        "--tomorrow",
        nargs="?",
        const=1,
        type=int,
        action=Datefunctions1,
        help="set selling date to tomorrow",
    )
    sell_parser.add_argument(
        "-d",
        "--date",
        nargs="?",
        action=Datefunctions7,
        help="set any specific selling date in YYYY-MM-DD format",
    )

    return_parser = subparsers.add_parser(
        "return",
        usage="super.py return [-h]. \nExample for usage: python super.py return. CLI will ask for additional info.",
        help="return items. Give the following command: python super.py return 'sales_id' 'amount'",
    )

    revenue_parser = subparsers.add_parser(
        "revenue", help="Shows revenues and profit in given period"
    )
    revenue_parser.add_argument(
        "-td",
        "--today",
        nargs="?",
        const=0,
        type=int,
        action=Datefunctions9,
        help="Shows revenues and profit generated today",
    )
    revenue_parser.add_argument(
        "-y",
        "--yesterday",
        nargs="?",
        const=-1,
        type=int,
        action=Datefunctions9,
        help="Shows revenues and profit generated yesterday",
    )
    revenue_parser.add_argument(
        "-w",
        "--thisweek",
        nargs="?",
        type=int,
        action=Datefunctions2,
        help="Shows revenues and profit generated this week until now",
    )
    revenue_parser.add_argument(
        "-m",
        "--thismonth",
        nargs="?",
        type=int,
        action=Datefunctions3,
        help="Shows revenues and profit generated this month until now",
    )
    revenue_parser.add_argument(
        "-th",
        "--thisyear",
        nargs="?",
        type=int,
        action=Datefunctions4,
        help="Shows revenues and profit generated this year until now",
    )
    revenue_parser.add_argument(
        "-r",
        "--range",
        nargs="+",
        action=Datefunctions5,
        help="Shows revenues and profit generated in a set range(YYYY-MM-DD YYYY-MM-DD)",
    )
    revenue_parser.add_argument(
        "-year",
        "--year",
        nargs="+",
        action=Datefunctions6,
        help="Shows revenues and profit generated in a specific year (YYYY)",
    )
    revenue_parser.add_argument(
        "-f",
        "--from",
        nargs="?",
        action=Datefunctions8,
        help="Shows revenues and profit generated from set date (YYYY-MM-DD) until now. \nIt’s also possible to enter just a year (from is set to YYYY-01-01) or year-month (from is set to YYYY-MM-01)",
    )

    args = parser.parse_args()

    if args.command == "buy":
        c1 = bought(args.prod_name, args.amount, args.price, args.exp_date)
        c1.buy_inventory(args.prod_name, args.amount, args.price, args.exp_date)
    elif args.command == "inventory":
        bought.open_inventory()
    elif args.command == "batch":
        bought.open_inventory_batch()
    elif args.command == "revenue":
        sold.calculate_revenue_profit()
    elif args.command == "expired":
        bought.open_inventory_expired()
    elif args.command == "edit":
        bought.edit_inventory2(args.line_id, args.update, args.value)
    elif args.command == "sell":
        c2 = sold(args.prod_name, args.sold_amount, args.price_sold)
        c2.sell_items(args.prod_name, args.sold_amount, args.price_sold)
    elif args.command == "return":
        sold.show_sales()
    else:
        print(f"Command {args.command} does not exist.")


if __name__ == "__main__":
    main()

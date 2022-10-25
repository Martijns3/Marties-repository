import pandas as pd
import matplotlib.pyplot as plt
from date_func import *
import os


def matplotlib_print():
    date_info = dateinfo.date_range()
    today = date_info[0]
    start_date = date_info[1]
    if start_date == "1970-01-01":
        start_date = "start"
    if datetime.strptime(today, "%Y-%m-%d") > datetime.now():
        today = "now"
    df = pd.read_csv("temp2.csv")
    df.head()

    print_list = df.sort_values(by="profit", ascending=False)
    print_list.rename(
        columns={"product": "Product", "revenue": "Revenue", "profit": "Profit"},
        inplace=True,
    )

    plt.style.use("seaborn-whitegrid")

    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(8, 4))
    print_list.plot(kind="barh", y=("Revenue"), x="Product", ax=ax0)
    ax0.set(title="", xlabel="Revenue", ylabel=("Product"))

    avg = print_list["Revenue"].mean()
    ax0.axvline(x=avg, color="b", label="Average", linestyle="--", linewidth=1)

    print_list.plot(kind="barh", y="Profit", x="Product", ax=ax1)
    avg = print_list["Profit"].mean()
    ax1.set(title="", xlabel="Profit", ylabel="Product")
    ax1.axvline(x=avg, color="b", label="Average", linestyle="--", linewidth=1)

    fig.suptitle(
        f"SuperPy revenue and profit by product, from {start_date} until {today}",
        fontsize=14,
        fontweight="bold",
    )
    os.remove(os.path.join(os.getcwd(), "temp2.csv"))
    plt.show()

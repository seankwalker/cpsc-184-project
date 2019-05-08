"""
    parse_data.py

    Sean Walker

    CPSC 184, Spring 2019
    Final Project

    Parses data from USPTO granted patents database.
"""


import os

import numpy as np
import pandas as pd

DATA_DIR = "data"
DATA_FILE = "patent-clean.tsv"
PICKLE_FILE = "patent.pkl"


def run():
    """
    Main funciton.
    """
    # data format (from http://www.patentsview.org/data/ data dictionary):
    # id, type, number, country, date, abstract, title, kind, num_claims,
    # filename, withdrawn

    # force unbuffered output
    os.environ["PYTHONUNBUFFERED"] = "on"
    
    # see if Pickle file of patents data frame already exists
    print("checking for pre-existing dataframe file...", end="")
    if os.path.isfile(os.path.join(DATA_DIR, PICKLE_FILE)):
        print("found!\nreading dataframe from file...", end="")
        df = pd.read_pickle(os.path.join(DATA_DIR, PICKLE_FILE))
        print("done.")
    else:
        print("none found.\nparsing data...", end="")
        # read in patent data from source file, skipping any misformatted lines
        df = pd.read_csv(
                os.path.join(DATA_DIR, DATA_FILE),
                date_parser=lambda x: pd.datetime.strptime(x, "%Y-%m-%d"),
                error_bad_lines=False,
                index=["date"],
                parse_dates=["date"],
                sep="\t",
                usecols=["id", "date", "abstract"]
        )

        # save data frame to Pickle for speed (on subsequent runs)
        print("done. saving dataframe to file...", end="")
        df.to_pickle(os.path.join(DATA_DIR, PICKLE_FILE))
        print(f"done; dataframe saved to {os.path.join(DATA_DIR, PICKLE_FILE)}")


if __name__ == "__main__":
    run()

import os
import sys

import pandas as pd

import clean_data
import parse_data
import readability


CLEAN_FILE = "patent-clean.tsv"
DATA_DIR = "data"
DATA_FILE = "patent.tsv"
DATAFRAME_FILE = "patent.pkl"


def calc_readability(row):
    """
    Calculate FK Ease readability of this patent's abstract.
    """
    return readability.calculate_fk_ease(row["abstract"])


def main():
    # ensure raw data file exists
    if not os.path.isfile(os.path.join(DATA_DIR, DATA_FILE)):
        print("error: data file not found. please make sure that file", 
                f"{os.path.join(DATA_DIR, DATA_FILE)} exists and is a valid",
                "file!")
        sys.exit(1)

    # attempt to clean data if not already done
    if not os.path.isfile(os.path.join(DATA_DIR, CLEAN_FILE)):
        clean_data.run()

    # parse cleaned data file
    parse_data.run()

    # load dataframe, grouped by year
    df = pd.read_pickle(os.path.join(DATA_DIR, DATAFRAME_FILE))
    print(f"size of data set before date filter: {df.size}")

    # filter from 2000 onward
    _filter = df["date"] > "1999-12-31"
    df = df.loc[_filter]
    print(f"size of data set after date filter: {df.size}")

    # compute readability of all abstracts in data set
    df["readability"] = df.apply(calc_readability, axis=1)

    print(df.groupby(df.date.dt.year).mean())

if __name__ == "__main__":
    main()

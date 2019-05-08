"""
    clean_data.py

    Sean Walker

    CPSC 184, Spring 2019
    Final Project

    Cleans data from USPTO granted patents database.
"""


import csv
import os
import sys
import time

import numpy as np

DATA_DIR = "data"
DATA_FILE = "patent.tsv"
OUTPUT_FILE = "patent-clean.tsv"

# these files are THICC
csv.field_size_limit(sys.maxsize)


def run():
    with open(os.path.join(DATA_DIR, DATA_FILE), "r") as infile, open(os.path.join(DATA_DIR, OUTPUT_FILE), "x") as outfile:
        reader = csv.DictReader(infile, delimiter="\t")
        writer = csv.DictWriter(
                outfile,
                delimiter="\t",
                fieldnames=reader.fieldnames
        )

        # include only rows which have abstracts
        writer.writeheader()
        for row in reader:
            if (not row["abstract"] or row["abstract"] == "" or
                    row["abstract"].isspace() or row["abstract"] is np.nan or
                    row["abstract"] != row["abstract"] or
                    len(row["abstract"]) < 10):
                print(f"skipping malformed abstract ({row['abstract']})...")
                continue
            
            # ensure data has valid date column
            try:
                time.strptime(row["date"], "%Y-%m-%d")
            except:
                print(f"skipping malformed date row ({row['date']})...")
                continue

            try:
                writer.writerow(row)
            except ValueError:
                print("skipping malformed data row...")
                continue

    print(f"data saved to {os.path.join(DATA_DIR, OUTPUT_FILE)}")



if __name__ == "__main__":
    run()

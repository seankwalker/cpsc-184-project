# Analysis of US Patent Abstracts' Readability, 2000-2018

This project was written as a final project for Yale's CPSC 184: Intellectual
Property in the Digital Age, Spring 2019.

All code by Sean Walker.

## Front Matter

### Overview

This project explores various natural language-related properties of trademark
and patent applications from trademarks and patents which have been approved by
the United States Patent & Trademark Office (USPTO).

Additionally, we include data from Stanford Law School's new
[Non-Practicing Entity Litigation Database](http://npe.law.stanford.edu) for
cross-analysis. The data is not separately analyzed in this project.


### Data

USPTO data is widely avaiable in many forms. For this project, data was
downloaded directly from
[USPTO PatentsView](http://www.patentsview.org/download/).

Stanford Law's NPE Database is online in full as of May 2019 (when this project
was written!), however the data that was primarily used for this project is a
random sample of 20% of the cases in the full database. It is available for
download at 
[their website](https://law.stanford.edu/projects/stanford-npe-litigation-database/)
.

### Requirements

```
nltk
pandas
pyphen
```

This project was built running Python 3.7.3, although Python 3.X.X should work.

A large amount of disk space is also required; `patent.tsv` should take up about
5GB as should its "cleaned" version. A good processor helps to make computation
time feasible.

## Running

1. Download the dataset listed above. It should be saved to `patent.tsv` in the
`data` directory.

2. Run
```shell
python main.py
```

This will take a (very) long time to iterate through all the data, as there are
tens of millions of patents to be parsed through. There are three main steps,
cleaning data, parsing data, and then analysis. The first two can be performed
independently by running the `clean_data.py` and `parse_data.py` scripts
separately.

# Project Title TBD

This project was written as a final project for Yale's CPSC 184: Intellectual
Property in the Digital Age, Spring 2019.

All code by Sean Walker, except where noted.

## Front Matter

### Overview

This project explores various natural language-related properties of trademark
and patent applications from trademarks and patents which have been approved by
the United States Patent & Trademark Office (USPTO).

Additionally, we include data from Stanford Law School's new
[Non-Practicing Entity Litigation Database](http://npe.law.stanford.edu) for
cross-analysis.


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

#Waffle Importers/Exporters 

## Introduction

Python scripts that transform data and imports/exports into/onto waffle server. This project is independent from data kitchen project, 
however some computational procedures are similar in terms of logic.
  
##Modules
###Data
Data is where you can find data files for `dimensions`, `entities`, `regions`, `stats` and etc. 
###ws_export
There are the set of scripts that export data from `waffle server` in a way that is digestible for `Gapminder World` 
####util
#####name_match
This module checks the name of an entity (country) and returns the standard named used in ```Gapminder World```
####indic.py
This module creates the XML files for each indicator
####overview.py
This module creates the XML file `overview.xml` that includes meta data about set of entities and indicators
###log
###util
A set of modules that vary from `url` to `log`.
###ws_import
There are the set of scripts that import data from different sources and push them onto waffle server
###proc_runners
This is where you run your procedures that you can find in `procedures` module to produce data for indicators such as `pop`,`lex` and etc.
###procedures 
Set of procedures that each perform a required transformation on data. **Note** that the IDs are correspondent to `Data Kitchen` cooking recipe ID.

###Readers
Readers allow you to read the files that exist in data module in *EXCEL* and *JSON* formats.
###Writers
Writers write processed data in form of waffle to either local disk to to a remote server. 

###Getting Started

To ensure cross-platform consistency, run the following commands in a Docker shell started by:

```
docker-compose run shell /bin/bash
```

#### Push data to waffle 
Run the following command in the project directory to push data to Waffle Server

```
python ws_import/start.py
```

Browse to `data/out/waffle` to see the output files. If you pushed to staged version, browser to [Gapminder waffle server](https://waffle-server-stage.herokuapp.com/) 
and check for the data by its ID.

#### Import data from Google Spreadsheets

```
python ws_import/proc_runners/gw.py
```

Browse to `data/out/gw/indicators` and `data/out/gw/meta` to get the output files.
#### Export data for Gapminder World

```
python ws_export/start.py
```
Browse to `data/out/gw` to see the output files.




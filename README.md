Waffle Push Custom Scripts
------------
## Introduction

Python scripts that transform data and push it onto waffle server. This project is independent from data kitchen project, 
however computations logic is similar.
  
##Modules
###Data
Data is where you can find data files for `dimensions`, `entities`, `regions`, `stats` and etc. 
###ws_export
There are the set of scripts that export data that is digestible for `Gapminder World` 
####util
#####name_match
This module checks the name of an entity (country) and returns the standard named used in ```Gapminder World```
####indic.py
This module creates the XML files for each indicator
####overview.py
This module creates the XML file `overview.xml` that includes meta data about set of entities and indicators
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
#### Push data to waffle 
Run the following command in the project directory to push data to Waffle Server

```
python ws_import/start.py
```
Browse to `data/out/waffle` to see the output files. If you pushed to staged version, browser to [Gapminder waffle server](https://waffle-server-stage.herokuapp.com/) 
and check for the data by its ID.

#### Export data for Gapminder World

```
python ws_export/start.py
```
Browse to `data/out/gw` to see the output files.




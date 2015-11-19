README:

I assume you know Python and you know to install required dependencies and etc.

There are two steps that needs to be taken in order to receive 

## Update indicators one-by-one:

Step 1: First you import the google spreadsheets 

ws_import/procedures/gw/indicators.py and uncomment the following line at the end of the file:

```
#UNCOMMENT HERE:
#write_indicators('http://spreadsheets.google.com/pub?key=0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc', '0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc')
```

Then run indicators.py while being in the directory and you can find the data in waffle-import-export/data/out/gw/indicators/ as 0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc.json

```
python ws_import/procedures/gw/indicators.py
```

Step 2: Export to XML:

go to  ws_export/indic.py and uncommon the line at the end with appropriate key:

```
#UNCOMMENT HERE:
#write_indicator_file("0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc", entity_names)
```

and run indic.py and the data will be in data/out/gw/xml.

```
python ws_export/indic.py
```

As you can see, the same goes with area_categorization, indicator_categorization, X_COORDS and Y_COORDS and overview basically.

## Update indicators all-at-once:

1. Uncomment the following line in indicator_categorization.py which is in the end of ws_import/procedures/gw/

```
#UNCOMMENT HERE:
#callback(indicator_url=indicator_url, indicator_id=indicator_url[key_index:])
```

2. run gw.py in ws_import/proc_runners. This will put all files in Ws_import/procedures/gw/ as json.

```
python ws_import/proc_runners/gw.py
```

3. run ws_export/start.py and you will get the data in data/out/gw/xml

```
python ws_export/start.py
```

done.












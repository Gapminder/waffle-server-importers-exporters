README
======

## Get started

Check out the source code:

```
git clone -b world-legacy https://github.com/Gapminder/waffle-server-importers-exporters.git
```

To get a cross-platform Python environment with the required required dependencies installed, start the docker shell from within the repository's root folder:

```
cd waffle-server-importers-exporters
eval "$(docker-machine env default)"
docker-compose run shell /bin/bash
```

## Update indicators one-by-one:

Step 1: First you import the google spreadsheets 

ws_import/procedures/gw/indicators.py and change the google spreadsheet key in the following line at the end of the file:

```
#UNCOMMENT HERE:
write_indicators('http://spreadsheets.google.com/pub?key=0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc', '0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc')
```

Then run indicators.py while being in the directory and you can find the data in waffle-import-export/data/out/gw/indicators/ as 0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc.json

```
python ws_import/procedures/gw/indicators.py
```

Step 2: Export to XML:

go to  ws_export/indic.py and change the google spreadsheet key in the following line:

```
#UNCOMMENT HERE:
write_indicator_file("0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc", entity_names)
```

and run indic.py and the data will be in data/out/gw/xml.

```
python ws_export/indic.py
```

As you can see, the same goes with area_categorization, indicator_categorization, X_COORDS and Y_COORDS and overview basically.

## Update indicators all-at-once:

* (Skip this step, it is already done in this branch of the source code) Uncomment the following line in indicator_categorization.py which is in the end of ws_import/procedures/gw/

```
#UNCOMMENT HERE:
callback(indicator_url=indicator_url, indicator_id=indicator_url[key_index:])
```

* Run gw.py in ws_import/proc_runners. This will put all files in Ws_import/procedures/gw/ as json.

```
python ws_import/proc_runners/gw.py
```

* Run ws_export/start.py and you will get the data in data/out/gw/xml

```
python ws_export/start.py
```

## Publish the data

The xml data can be uploaded to the main Gapminder.org server by running:

```
export DATE=$(date +"%Y-%m-%d")
# via ssh
scp -r data/out/gw/xml/ root@wp.gapminder.org:/var/www/non-wordpress/communityproxy/xml-data/$DATE/pk7kRzzfckbzz4AmH_e3DNA/
# or via rsync (faster, requires rsync to be installed both locally and on the server)
ssh root@wp.gapminder.org mkdir -p /var/www/non-wordpress/communityproxy/xml-data/$DATE/pk7kRzzfckbzz4AmH_e3DNA/
rsync --delete -avzhe ssh data/out/gw/xml/ root@wp.gapminder.org:/var/www/non-wordpress/communityproxy/xml-data/$DATE/pk7kRzzfckbzz4AmH_e3DNA/
```
 
After upload, it can loaded into memcache by visiting [http://www.gapminder.org/communityproxy/xml-data/load-into-memcache.php]().

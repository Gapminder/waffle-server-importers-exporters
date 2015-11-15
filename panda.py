import pandas as pd
import urllib

## Source: Intern   ational Monetary Fund
## http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/download.aspx

import os
os.rename('WEOApr2015all.xls', 'WEOApr2015all.csv')
#urllib.urlretrieve("http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/WEOApr2015all.xls", "WEOApr2015all.csv")
weo_csv = pd.read_csv("WEOApr2015all.csv", error_bad_lines=False)
print weo_csv







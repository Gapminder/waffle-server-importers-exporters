import urllib2
import urllib


def save_remote_spreadsheet(url, path):
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    final_url = res.geturl()
    print 'fetching URL: ' + str(final_url)

    # The if-else works depending on the spreadsheet following old or new style of URL
    if final_url.find('pub?key=') == -1:
        final_url += '?output=xls'
    else:
        final_url += '&output=xls'

    urllib.urlretrieve(final_url, path)

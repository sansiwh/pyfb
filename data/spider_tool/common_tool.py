import urllib.request
from bs4 import BeautifulSoup

def get_soup(url):
    headers = {
        "authority":"www.whoscored.com",
        "Connection": "close",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Cookie": "visid_incap_774904=ITmb3E5gQkG8FhIF6IlXFamVvlkAAAAAQUIPAAAAAAAciEtKa9+kQOcD4ytW+1xx; permutive-id=cfb4ff64-f96a-4874-9f9a-9bcb79ff8619; __gads=ID=b04d007e9e38558d:T=1506186977:S=ALNI_MblHWBHHibDSkamBMNd9sX9cPHWLg; vl=1:-8.00|2:CN|3:HUBEI|4:|5:HUBEI/|6:HUBEI/WUHAN|7:430022|!0; vd=chinatelecom.com.cn; vq=4920,4920,4425,4920,4920,4920,4920,4425,4920,4920,4425,4920,4920,4425,4920,4920,4920; fq=1; vg=072a9421-a356-4e6f-a628-57b9d0f973fa; ip=1873766147; permutive-session=%7B%22session_id%22%3A%22eff418ee-4aa4-4462-afbe-112e0aa18a0f%22%2C%22last_updated%22%3A%222017-09-23T17%3A32%3A34.862Z%22%7D; _psegs=%5B1920%2C1930%2C2126%2C2441%2C2300%2C1956%2C1907%5D; incap_ses_431_774904=BKARSCHO51t4PnDPzjj7BdOwx1kAAAAA+NyJ+TUX2qWKi3CleKFrKQ==; _gat=1; _gat_subdomainTracker=1; _ga=GA1.2.199745529.1505662476; _gid=GA1.2.394306518.1506187067"
    }
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    return soup
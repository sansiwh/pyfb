from data.spider_tool.common_tool import *

def get_match_list():
    url = "https://www.whoscored.com/Matches/1190320/Preview/England-Premier-League-2017-2018-Arsenal-Tottenham"

    headers1 = {
        "authority": "www.whoscored.com",
        #":method": "GET",
        # "referer": "https://www.whoscored.com/Regions/252/Tournaments/2/England-Premier-League",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Cookie": "visid_incap_774904=ITmb3E5gQkG8FhIF6IlXFamVvlkAAAAAQUIPAAAAAAAciEtKa9+kQOcD4ytW+1xx; permutive-id=cfb4ff64-f96a-4874-9f9a-9bcb79ff8619; __gads=ID=b04d007e9e38558d:T=1506186977:S=ALNI_MblHWBHHibDSkamBMNd9sX9cPHWLg; vl=1:-8.00|2:CN|3:HUBEI|4:|5:HUBEI/|6:HUBEI/WUHAN|7:430022|!0; vd=chinatelecom.com.cn; incap_ses_798_774904=TRrPN6yLAy1+22pQ2BATC3NRDFoAAAAAaIJG8ugdM43gPLInOv9/KA==; vg=072a9421-a356-4e6f-a628-57b9d0f973fa; ip=1873766147; OX_plg=pm; vq=4919,4919; fq=1; _ga=GA1.2.199745529.1505662476; _gid=GA1.2.13"
    }

    soup = get_soup(headers1, url);
    print(soup)

if __name__ == '__main__':
    get_match_list();
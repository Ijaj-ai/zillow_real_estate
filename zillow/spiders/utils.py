from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json


URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.456276%2C%22east%22%3A-80.139157%2C%22south%22%3A25.596685%2C%22north%22%3A25.855773%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22],%22cat2%22:[%22total%22]}&requestId=3'


def cookie_parser():
    cookie_string = "zguid=23|%2493166451-1ae1-4ca9-b7fa-a6c24351d276; zgsession=1|d9868a39-c597-4cae-a170-d6311f7b7056; _pxvid=81293cbf-787b-11ec-ba7f-4e6f5a695677; g_state={'i_p':1643834556433,'i_l':1}; JSESSIONID=377204EC44C163BA78A47469846B972B; _pxff_rf=1; _pxff_bsco=1; _px3=79a603e39570be4d15aadf3a6aea3554733da148b0269cc23cb4bdca4308de89:SCIW86AYZ34DXEGgDt1H7O0PZpDun63pZ75lcF7hdSGNzk1L3U7qFBpy2qQQqB1yfEE06auhc7mtk1aw4BmERw==:1000:Ir5oFC65a4+aM01owq6Tx/uMt1E3jK7MY4VoJfWKcPp4ypD60xzv/gF7oGXqjNX/iOVXR4MkwCva7qU6y5CMx9ViLhez+0n17yjnQr+em3tXwnrUicjbfqLwNg+IdSISvEG2VEDYodTOzDlFcAnMSKh5pv5bo9nI/JXQO9k3p2QT8BvBCWpNqt5bcxz7eWTHMlBsfXQOStVU0/pnao5abw==; AWSALB=dwT6iJgXisJrVsPb2WdavVmkkiTHkhij7QAzSpXUtTJcKoRDDBZSuX6WYlxZZIbM7KIc/RqApt3f/31a5ZBJoESWpCIX9ThoEYbF0nmEPr8P2LzpNWSt+YUmpGoO; AWSALBCORS=dwT6iJgXisJrVsPb2WdavVmkkiTHkhij7QAzSpXUtTJcKoRDDBZSuX6WYlxZZIbM7KIc/RqApt3f/31a5ZBJoESWpCIX9ThoEYbF0nmEPr8P2LzpNWSt+YUmpGoO; search=6|1647242194300%7Crect%3D25.855773%252C-80.139157%252C25.596685%252C-80.456276%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26sort%3Ddays%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%0912700%09%09%09%09%09%09"
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    # print(cookie.items())

    cookies = {}

    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {'currentPage': page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url

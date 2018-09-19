import time
import datetime
import pprint
import googlemaps

DTU = 55.785628, 12.521531
NOERREPORT = 55.683742, 12.571618


def get_api_key():
    return open('api_key.txt', 'r').read()


def get_all_pois(circle_center_lat, circle_center_lng, circle_radius_meters):
    gmaps = googlemaps.Client(key=get_api_key(), queries_per_second=1, retry_over_query_limit=True, retry_timeout=2)
    pois = []
    next_page_token = ''
    while True:
        print('[%s] Querying, next page token is %s' % (datetime.datetime.now(), next_page_token))
        res = gmaps.places(query='', location=(circle_center_lat, circle_center_lng), radius=circle_radius_meters,
                       type='establishment', page_token=next_page_token)
        pois.extend(res['results'])
        if 'next_page_token' in res:
            next_page_token = res['next_page_token']
            time.sleep(5)
        else:
            pprint.pprint(res)
            print('Got total %d POIs' % len(pois))
            return pois


if __name__ == '__main__':
    get_all_pois(*NOERREPORT, 10000)

import requests
from lxml import html
import configs

class TopListScrapError(Exception):
    pass


class TopList(object):

    def __init__(self, config):
        self.entity = config.get('entity', 'tv_series')
        self.url = config.get('url')
        self.xpath = config.get('xpath')
        self.per_page = config.get('per_page', 50)
        self.sub_pages = config.get('sub_pages', 7)

    def fetch_body(self, data):
        query_url = self.url % data
        print query_url
        resp = requests.get(query_url)
        if resp.status_code != 200:
            raise TopListScrapError()
        return resp.text

    def get_list(self):
        ret = []
        for i in range(0, int(self.sub_pages)):
            current_start = self.per_page * i + 1
            body = self.fetch_body({'start': current_start})
            tree = html.fromstring(body)
            elems = tree.xpath(self.xpath)
            for el in elems:
                ret.append(self.format_output(main_title=el.text, entity=self.entity))
        return ret

    @staticmethod
    def format_output(main_title="", episode_title="", entity="tv_series"):
        return {"title": main_title, "subtitle": episode_title, "entity": entity}



tl = TopList(configs.list['imdb_higest_scifi_tv_series'])
print tl.get_list()

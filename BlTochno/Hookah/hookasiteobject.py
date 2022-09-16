from msilib.schema import Error
from BlTochno.common_utils.htmlcollector import HtmlCollector
from BlTochno.common_utils.htmlparser import HtmlParser
from BlTochno.common_utils.urlobject import UrlObject


class HookaSiteObject:

    def __init__(self, name: str, url: UrlObject, paginator: bool = None, parser_deep_level: int = 1) -> None:
        self.name = name
        self.url = url
        self.paginator = paginator
        self.parser_deep_level = parser_deep_level
        self.html_collector = HtmlCollector()
        self.html_parser: HtmlParser = HtmlParser()

    def parse(self) -> dict:
        final_result = dict()
        for i in range(self.parser_deep_level-1):
            self.url = self.html_collector.start(self.url)
            self.url = self.html_parser.parse_page(self.url)
        self.url=self.html_parser.parse_hooka_mix(self.url)
        for match in self.url.regex_matchs:
            try:
                final_result[match['mix_id']] = match['mix']
            except KeyError:
                print('html_parser parse_page возвращает не правильный словарь микса')
        # final_result={
        #     'mix_id':{
        #         'components':{
        #             'name':'',
        #             'percent':''
        #         },
        #         'desc':'',
        #         'img':''
        #     }
        # }
        return final_result

    # def parse_level(self, url_obj: UrlObject):
    #     url_obj = self.html_collector.start(url_obj)
    #     url_obj = self.html_parser.parse_page(url_obj)
    #     return url_obj
    #     #     else:
    #     #         raise Error('html_parser parse_page возвращает не правильный словарь микса')
    #     # else:
    #     #     url_obj = self.html_collector.start(url_obj)
    #     #     url_obj = self.html_parser.parse_page(url_obj)
    #     #     return url_obj

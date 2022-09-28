from typing import Any
from BlTochno.common_utils.htmlcollector import HtmlCollector
from BlTochno.common_utils.htmlparser import HtmlParser
from BlTochno.common_utils.log import LogDecorator
from BlTochno.common_utils.urlobject import UrlObject
from BlTochno.common_utils.parser import Parser
import requests


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



class Page:

    def __init__(self,parsers:list[Parser],url:str=None) -> None:
        self._url:str=url
        self._parsers:Parser=parsers
        self._html:str=None
        self._data:list[Page]=None
        self.get_html()
    
    @property
    def url(self):
        return self._url
    
    @property
    def data(self):
        return self._data

    @LogDecorator()
    def get_html(self):
        if self._url:
            _html=requests.get(self._url)
            self._html=_html.text

    @LogDecorator()
    def parse_data(self):
        if len(self._parsers)==1:
            self._data=self._parsers[0].start(self._html)
        else:
            _data=self._parsers[0].start(self._html)
            self._data=[Page(parsers=self._parsers[1:],url=url) for url in _data]
            for page in self._data:
                page.parse_data()

    def __repr__(self) -> str:
        if self._url:
            return self._url
        else:
            return self.data

def tree_traversal(page:Page)->list[str]:
    result=[]
    if page.url:
        for p in page.data:
            result+=tree_traversal(p)
        return result
    result+=page.data
    return result

    
class SiteTreeBuilder:


    def __init__(self,url_parsers:dict[str:list[Parser]]) -> None:
        self._main_url=None
        self._url_parsers=url_parsers
        self._tree:Page=None
        self.get_main_url()
        self.create_root()

    @property
    def tree(self):
        return self._tree

    def create_root(self):
        self._tree=Page(url=self._main_url,parsers=self._url_parsers[self._main_url])
        self._tree.parse_data()
    
    def get_main_url(self):
        self._main_url=list(self._url_parsers.keys())[0]


    def get_leaves_data(self,page:Page):
        if page.url:
            return 
        return page.data





url_parsers={
    'https://hookah-cat.online/today-we-smoke/?limit=80':[
        Parser(regex='class=\"caption\".*?href=\"(.*?)\"'),
        Parser(regex='(?:<span style=\"caret-color: rgb\(.*?\); text-size-adjust: auto;\">|)(?:<br>|)(.{3,20})<\/span><a.*?>(.*?)<\/a><span style=\"caret-color: rgb\(.*?\); text-size-adjust: auto;\">.*?(\d+|)%*|<br><\/span>(?:<span style=\"background-color: rgb\(.*?\);\">|)(.*?)\"(.*?)\".*?<span style=\"caret-color: rgb\(0, 0, 0\); text-size-adjust: auto;\">.*?(\d+)%|(?:<span style="caret-color: rgb\(.*?\); text-size-adjust: auto;">|<br>)(?:<br>|)([\w,\s]{1,15})-(.{1,19}) (\d\d)')
        ]
}

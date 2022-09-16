from msilib.schema import Error
from BlTochno.BlTochno.common_utils.htmlcollector import HtmlCollector
from BlTochno.BlTochno.common_utils.htmlparser import HtmlParser
from BlTochno.BlTochno.common_utils.urlobject import UrlObject


class HookaSiteObject:



    def __init__(self,name:str,url:UrlObject,paginator:bool=None,parser_deep_level:int=1) -> None:
        self.name=name
        self.url=url
        self.paginator=paginator
        self.parser_deep_level=parser_deep_level
        self.html_collector=HtmlCollector()
        self.html_parser:HtmlParser=HtmlParser()


    def parse(self)->dict:
        final_result=dict()
        url_object=self.html_collector.start(self.url)
        url_object=self.html_parser.parse_page(url_object)
        for i in range(self.parser_deep_level):
            url_object=self.parse_level(url_object)
            if type(url_object.regex_matchs[0])==str:
                url_object=self.html_collector.start(url_object.regex_matchs)
                url_object=self.html_parser.parse_page(url_object)
                continue
            elif type(url_object.regex_matchs[0])==dict:
                break
            else:
                raise Error('html_parser parse_page возвращает не правильный словарь микса')
        for match in url_object.regex_matchs:
            try:
                final_result[match['mix_id']]=match['mix']
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

    def parse_level(self,parse_target:list):
        if type(parse_target[0])==str:
            url_object=self.html_collector.start(parse_target)
            url_object=self.html_parser.parse_page(url_object)
        elif type(parse_target[0])==dict:
            return parse_target
        else:
            raise Error('html_parser parse_page возвращает не правильный словарь микса')


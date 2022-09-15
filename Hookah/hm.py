from hashlib import md5
from importlib.abc import SourceLoader
from BlTochno.Hookah.wordanalayzer import WordsAnalayzer
from BlTochno.common_utils.htmlcollector import HtmlCollector
from BlTochno.common_utils.htmlparser import HtmlParser
from BlTochno.common_utils.urlobject import UrlObject
from BlTochno.Hookah.hooka_settings import sites_with_mixes
from collections import defaultdict

class HookaMaster:


    def __init__(self,storage:list[str],word_analayzer:WordsAnalayzer=None) -> None:
        self.storage=storage
        self.mixes=dict()
        self.sites_with_mixes=[]
        self.urls:list[UrlObject]=[]
        self.html_collector:HtmlCollector=HtmlCollector()
        self.html_parser:HtmlParser=HtmlParser()
        self.word_analayzer=word_analayzer

    def check_recipe(self):
        for k,v in self.mixes.items():
            ingridients=list(v.values())
            check_ingridients=[ingridient in self.storage for ingridient in ingridients]
            if all(check_ingridients):
                print(f'Мы можем сделать микс: {v}')
    print('Приятного покура')

    def urls_to_mix(self):
        for url in self.urls:
            for mix_index in range(len(url.regex_matchs)):
                name_of_mix=url.regex_matchs[mix_index]
                name_of_mix.sort()
                name_of_mix=''.join(name_of_mix)
                self.mixes[name_of_mix]=dict()
                for component_index in range(len(url.regex_matchs[mix_index])):
                    self.mixes[name_of_mix][f'Component #{component_index+1}']=url.regex_matchs[mix_index][component_index]

    def parse_new_mixes(self)->None:
        self.prepare_sites()
        urls=self.html_collector.start(self.sites_with_mixes)
        urls=self.html_parser.parse_page(urls)
        self.urls.clear()
        self.urls=urls

    def prepare_sites(self)->None:
        self.sites_with_mixes=[]
        self.sites_with_mixes=[UrlObject(url=site,parsers=parsers) for site,parsers in sites_with_mixes.items()]

    def urlsobject_to_smokeobject(self):
        pass

    def analize_words(self):
        self.urls=self.word_analayzer.analize(self.urls)

    def count_components(self)->dict:
        components=defaultdict(int)
        for url in self.urls:
            matches=url.regex_matchs
            for match in matches:
                for component in match:
                    components[component]+=1
        return components
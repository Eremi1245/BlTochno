from BlTochno.Hookah.hookautils.parsemixes import parsemixes
from BlTochno.common_utils.htmlcollector import HtmlCollector
from BlTochno.common_utils.htmlparser import HtmlParser
from BlTochno.common_utils.urlobject import UrlObject
from BlTochno.Hookah.hooka_settings import sites_with_mixes

storage=['грейпфрут','патока','киви','вишня','','корица','кукуруза','молоко','deep blue sea','мед','лимон','орех','raf in the jungle','мороженное','adalia power','лед','энергетик','love 66','']
mixes={
    1:{'main':'апельсин','supplement':'персик','shade': 'ягоды'},
    2:{'main':'Банан','supplement':'клубника','shade': 'мята'},
    3:{'main':"Банан",'supplement':'кокос','shade':''},
    4:{'main':'Арбуз','supplement':'апельсин','shade': 'ваниль'},
    5:{'main':'ваниль','supplement':'апельсин','shade': 'кокос'},
    6:{'main':'Fresh Mist','supplement':' клубника', 'shade':'кокос','shade': 'мята'},
    7:{'main':'Ягоды','supplement': 'арбуз', 'shade':'лимон','shade': 'мята'},
    8:{'main':'Манго','supplement': 'мед', 'shade':'роза','shade': 'ваниль'},
    9:{'main':'вишня','supplement': 'слива', 'shade':'гранат','shade': 'лимон'},
    11:{'main':'Глинтвейн','supplement': 'мед', 'shade':'тархун','shade': 'базилик'},
    12:{'main':'Апельсин', 'supplement':'персик','shade': 'ягоды'},
    13:{'main':'Банан', 'supplement':'клубника','shade': 'мята'},
    14:{'main':'Арбуз', 'supplement':'апельсин','shade': 'ваниль'},
    15:{'main':'Двойное яблоко', 'supplement':'ваниль','shade': 'корица'},
    16:{'main':'Виноград', 'supplement':'гранат','shade': 'мята'},
    17:{'main':'Дыня', 'supplement':'вишня','shade': 'ананас'},
    18:{'main':'Персик', 'supplement':'гуава','shade': 'виноград'},
    19:{'main':'Лесные ягоды', 'supplement':'манго','shade': 'вишня'},
    20:{'main':'Шоколад', 'supplement':'кокос','shade': 'ваниль'},
    21:{'main':'киви', 'supplement':'клубника','shade': 'мята'},
    22:{'main':'Апельсин', 'supplement':'слива','shade': 'ваниль'},
    23:{'main':'Fresh Mint Flavour' , 'supplement':'кокос','shade': 'слива'},
    24:{'main':'Карамель', 'supplement':'фисташка','shade': 'шоколад'},
    25:{'main':'Тирамису', 'supplement':'орех','shade': 'чизкейк'},
    26:{'main':'Двойное яблоко', 'supplement':'капучино','shade': 'перечная мята'},
    27:{'main':'Ананас', 'supplement':'грейпфрут','shade': 'капучино'},
    28:{'main':'Карамель', 'supplement':'двойное яблоко','shade': 'земляника'},
    29:{'main':'вишня', 'supplement':'лимон','shade': 'мята'},
    30:{'main':'Яблоко', 'supplement':'кола','shade': 'капучино'},
    31:{'main':'Кофе', 'supplement':'мед','shade': 'ваниль'},
    32:{'main':'Кокосовый орех', 'supplement':'кола','shade': 'жасмин'},
    33:{'main':'Двойное яблоко', 'supplement':'персик','shade': 'фрукты'},
    34:{'main':'Фруктовый микс' , 'supplement':'апельсин','shade': 'двойное яблоко'},
    35:{'main':'Банан','supplement': 'кокос','shade':''},
    36:{'main':'Карамель','supplement': 'шоколад','shade':''},
    37:{'main':'Апельсин','supplement': 'шоколад','shade':''},
    38:{'main':'мед','supplement': 'лесные ягоды','shade':''},
    39:{'main':'Персик','supplement': 'жасмин','shade':''},
    40:{'main':'Ананас','supplement': 'ежевика','shade':''},
    41:{'main':'Кокос','supplement': 'малина','shade':''},
    42:{'main':'Слива','supplement': 'ананас','shade':''},
    43:{'main':'Персик','supplement': 'ежевика','shade':''},
    44:{'main':'лимон','supplement': 'ваниль','shade':''},
    45:{'main':'лимон','supplement': 'мята','shade':''},
    46:{'main':'Cola','supplement': 'лимон','shade':''},
    47:{'main':'Фруктовый микс', 'supplement': 'яблоко','shade':''},
    48:{'main':'Абрикос','supplement': 'мята','shade':''},
    49:{'main':'Виноград','supplement': 'банан','shade':''},
    50:{'main':'вишня','supplement': 'перечная мята','shade':''}, 
    51:{'main':'Двойное яблоко','supplement':'мята','shade':''},
    52:{'main':'Cola','supplement': 'вишня','shade':''},
    53:{'main':'Манго','supplement': 'вишня','shade':''},
    54:{'main':'Яблоко','supplement': 'апельсин','shade':''},
    55:{'main':'Жасмин','supplement': 'ваниль','shade':''},
    56:{'main':'Манго','supplement': 'арбуз','shade':''},
    57:{'main':'Персик','supplement': 'апельсин','shade':''},
}

class HookaMaster:


    def __init__(self) -> None:
        self.storage=[]
        self.mixes={}
        self.sites_with_mixes=[]
        self.html_collector=HtmlCollector()
        self.html_parser=HtmlParser()


    def check_recipe(self):
        for k,v in self.mixes.items():
            ingridients=list(v.values())
            check_ingridients=[ingridient in self.storage for ingridient in ingridients]
            if all(check_ingridients):
                print(f'Мы можем сделать микс: {v}')
    print('Приятного покура')


    def parse_new_mixes(self)->list[UrlObject]:
        self.prepare_sites()
        urls=self.html_collector.start(self.sites_with_mixes)
        urls=self.html_parser.parse_page(urls)
        urls=parsemixes(urls)
        return urls

    def prepare_sites(self)->None:
        self.sites_with_mixes=[]
        self.sites_with_mixes=[UrlObject(url=site,parsers=parsers) for site,parsers in sites_with_mixes.items()]


    def urlsobject_to_smokeobject(self):
        pass



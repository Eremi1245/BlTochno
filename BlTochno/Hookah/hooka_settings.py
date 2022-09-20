from BlTochno.common_utils.parser import NNKalyanDecorator

nn_kalyan_reg='<li>((\w+\s*\w*\s*\w*\s*\w*)\+*(\w+\s*\w*\s*\w*\s*\w*)*\+*(\w+\s*\w*\s*\w*\s*\w*)*\+*(\w+\s*\w*\s*\w*\s*\w*)*\+*(\w+\s*\w*\s*\w*\s*\w*)*).*?<\/li>'
hooka_cat='https://hookah-cat.online/today-we-smoke/?limit=80'

sites_with_mixes={
    'https://nn-kalyan.ru/100-vkusnyx-miksov-dlya-vashego-kalyana/':[NNKalyanDecorator(regex=nn_kalyan_reg),],
}

storage=['апельсин','персик','виноград',',банан','кокос','мята']


key_words={
    'апельсин':['апельс','orange'],
    'банан' :['банан','banana'],
    'персик':['peach','перс'],
    'виноград':['grape','виногра'],
    'клубника':['strawberry','strawb','клубни'],
    'лимон':['lemon','лeмон','лемонграсс'],
    'ананас':['ананас','pineapp'],
    'мята':['мят','mint'],
    'кокос':['коко','coconut','coco','кокс'],
    'ягоды':['лесные ягоды','ягод','berries'],
    'apple':['двойное яблоко','яблок','double apple'],
    'watermelon':['арбуз'],
    'ваниль':['vanilla','ванили','ванил'],
    'шоколад':['chocolate','choco','шоко'],
    'мед':['honey','мед'],
    'жасмин':['jasmine','жасмин'],
    'melon':['дыня','melon'],
    'вишня':['cherry','вишня','вишн'],
    'гуава':['guava','гуава'],
    'холодок':['fresh mist','mist','фрешмист','supernova','холод','лед','ice','супернова'],
    'манго':['mango','манго','манг'],
    'ежевика':['blackberry','еживика'],
    'корица':['cinnamon','корица'],
    'гранат':['pomegranate','гранат'],
    'киви':['kiwi','киви'],
    'слива':['plum','слива'],
    'роза':['rose flower','rose','роза'],
    'каппучино':['cappuccino','капучино'],
    'кола':['cola','кола'],
    'земляника':['strawberry','земляник'],
    'фисташки':['pistachios','фисташки'],
    'груша':['pear','груша'],
    'bounty hunter':['bounty hunter'],
    'жвачка':['gum','жвачка'],
    'лакрица':['liquorice','лакрица'],
    'грейпфрут':['грейпфрут','grapefruit'],
    'карамель':['карамель','caramel'],
    'смесь фруктов':['фрукты',''],
    'кофе':['кофе','coffee'],
    'nut':['opex',''],
    'чай':['эрл грей','чай','tea'],
    'вафли':['вафли','waffles'],
    'чёрная смородина':['чёрная','black currant'],
    'Must Have Mulled Wine':['глинтвейн мастхев','Mulled Wine'],
    'тархун':['тархун','tarragon'],
    'базилик':['basil','базилик'],
    'лайм':['lime','лайм'],
    'needles':['хвоя','елки','хвоя'],
    'молоко':['молоко','milk'],
    'кукуруза':['кукуруза','corn'],
    'Кленовый сироп':['кленовый','maple syrup','maple'],
    'печенье':['печенье','cookie'],
    'овсянка':['овсянка','oatmeal']
}
from BlTochno.common_utils.parser import NNKalyanDecorator

nn_kalyan_reg='<li>((\w+\s*\w*\s*\w*\s*\w*)\+*(\w+\s*\w*\s*\w*\s*\w*)*\+*(\w+\s*\w*\s*\w*\s*\w*)*\+*(\w+\s*\w*\s*\w*\s*\w*)*\+*(\w+\s*\w*\s*\w*\s*\w*)*).*?<\/li>'


sites_with_mixes={
    'https://nn-kalyan.ru/100-vkusnyx-miksov-dlya-vashego-kalyana/':[NNKalyanDecorator(regex=nn_kalyan_reg),],
}




key_words={
    'апельсин':['апельс','orange'],
    'банан' :['банан','banana'],
    'персик':['peach','перс'],
    'виноград':['grape','виногра'],
    'клубни':['strawberry','strawb'],
    'лемон':['lemon','лимон'],
    'ананас':['ананас','pineapp']
}
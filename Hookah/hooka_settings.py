from BlTochno.common_utils.parser import NNKalyanDecorator

nn_kalyan_reg='<li>((\w+\s*\w*\s*\w*\s*\w*)\+*(\w+\s*\w*\s*\w*\s*\w*)*\+*(\w+\s*\w*\s*\w*\s*\w*)*\+*(\w+\s*\w*\s*\w*\s*\w*)*\+*(\w+\s*\w*\s*\w*\s*\w*)*).*?<\/li>'

sites_with_mixes={
    'https://nn-kalyan.ru/100-vkusnyx-miksov-dlya-vashego-kalyana/':[NNKalyanDecorator(regex=nn_kalyan_reg),],
}
from BlTochno.common_utils.htmlcollector import HtmlCollector
from BlTochno.common_utils.htmlparser import HtmlParser
from BlTochno.common_utils.urlobject import UrlObject
from BlTochno.Hookah.hooka_settings import sites_with_mixes
from BlTochno.Hookah.smokeobject import SmokeObject


def parsemixes(urls:list[UrlObject])->list[UrlObject]:
    for url in urls:
        right_matches=[]
        for match in url.regex_matchs:
            right_components=[]
            components=match.split('+')
            for component in components:
                right_component=component.split(' ')
                right_component=list(filter(lambda a: a != '', right_component))
                if len(right_component)>1:
                    right_component=' '.join(right_component)
                else:
                    right_component=right_component[0]
                right_components.append(right_component)
            right_matches.append(right_components)
        url.regex_matchs=right_matches
    return urls
        


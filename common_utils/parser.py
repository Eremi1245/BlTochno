import re


class NNKalyanDecorator(object):


    def __init__(self, parser: object):
        self.parser=parser

    def __call__(self, *args, **kwds):
        self.parser=self.parser(*args, **kwds)
        return self

    def start(self,html:list[str])->list[str]:
        right_lst_components=[]
        components=self.parser.start(html=html)
        for component in components:
            right_components=[]
            component=component.split('+')
            for comp in component:
                right_component=comp.split(' ')
                right_component=list(filter(lambda a: a != '', right_component))
                if len(right_component)>1:
                    right_component=' '.join(right_component)
                else:
                    right_component=right_component[0]
                right_components.append(right_component.lower())
            right_lst_components.append(right_components)
        return right_lst_components


@NNKalyanDecorator
class Parser:
    """Base parser class.
    """
    
    def __init__(self, regex: str):
        self.regex = regex

    def start(self, html: str) -> list[str]:
        """Accepts html, parses, returns a list with results

        Args:
            html (str): html for parsing

        Returns:
            list [str]: list with results of parsing
        """
        html = html.replace('\n', '')
        result = re.findall(self.regex, html)
        return result







import re


class NNKalyanDecorator(object):

    def __init__(self, parser: object):
        self.parser = parser

    def __call__(self, *args, **kwds):
        self.parser = self.parser(*args, **kwds)
        return self

    def start(self, html: str) -> list[str]:
        try:
            right_lst_components = []
            components = self.parser.start(html=html)
            for component in components:
                right_components = []
                component = component.split('+')
                component=self.delete_extra_letters(component)
                for comp in component:
                    right_component = comp.split(' ')
                    right_component = list(filter(lambda a: a != '' or a != ' ', right_component))
                    if len(right_component) > 1:
                        right_component = ' '.join(right_component)
                    else:
                        right_component = right_component[0]
                    right_components.append(right_component.lower().strip())
                right_lst_components.append(right_components)
            return right_lst_components
        except Exception as er:
            print(er)

    def delete_extra_letters(self,str_obj:list[str])->list[str]:
        numbers_and_non_words = '\d+|\W'
        str_obj = [re.sub(numbers_and_non_words, ' ', right_comp) for right_comp in str_obj]
        return str_obj



@NNKalyanDecorator
class Parser:
    """Base parser class.
    """

    def __init__(self, regex: str):
        self.regex = regex

    def start(self, html: str)->list[str]:
        """Accepts html, parses, returns a list with results

        Args:
            html (str): html for parsing

        Returns:
            list [str]: list with results of parsing
        """
        html = html.replace('\n', '')
        result = re.findall(self.regex, html)
        return result

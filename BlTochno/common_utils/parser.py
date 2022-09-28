import re

from BlTochno.common_utils.errors import RegexErrror
from BlTochno.common_utils.log import LogDecorator


class Parser:
    """Base parser class.
    """

    def __init__(self, regex: str):
        self.regex = regex

    def start(self, html: str)->list[str]:
        __name__= self.regex[:10]
        """Accepts html, parses, returns a list with results

        Args:
            html (str): html for parsing

        Returns:
            list [str]: list with results of parsing
        """
        html = html.replace('\n', '')
        result = re.findall(self.regex, html)
        if not result:
            raise RegexErrror(f'Регулярка {self.regex} вернула None\nHtml\n{html}')
        return result

    def __str__(self) -> str:
        return self.regex


class MultiParser(Parser):

    def __init__(self, regexes: list[str]):
        self.regex=regexes


    def start(self, html: str) -> list[str]:
        html = html.replace('\n', '')
        for reg in self.regex:
            result = re.findall(reg, html)
            if not result:
                continue
            check_result=[all(match) for match in result]
            if all(check_result):
                print(result)
                return result
        raise RegexErrror(f'Все регуляки вернули плохой ответ')

class NNKalyanDecorator(Parser):

    def __init__(self, regex: str):
        super().__init__(regex)

    def start(self, html: str) -> list[str]:
        html=re.sub('\d+|\(|\)|%', '', html)
        html=re.sub('(\s*\+\s*)', '+', html)
        components=super().start(html=html)
        try:
            right_lst_components = []
            for component in components:
                component=component[1:]
                component=list(filter(lambda x: x != '', component))
                component=[comp.lower() for comp in component]
                right_lst_components.append(component)
            return right_lst_components
        except Exception as er:
            print(er)

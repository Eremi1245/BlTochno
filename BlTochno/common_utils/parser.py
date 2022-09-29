import re
from traceback import print_tb

from BlTochno.common_utils.errors import RegexErrror
from BlTochno.common_utils.log import LogDecorator


class RegexResultChecker:


    def kalyan_kot(self,results):
        if not results or len(results)<2:
            return False
        else:
            special_matchs=[]
            check_result=[all(match) if len(match)==3 else special_matchs.append(match) for match in results]
            if special_matchs:
                results=[(match[2],match[3],match[4]) for match in results]
                check_result=[all(match) if len(match)==3 else special_matchs.append(match) for match in results]
            if all(check_result):
                return True
            else:
                return False

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
        try:
            html = html.replace('\n', '')
            result = re.findall(self.regex, html)
            return result
        except Exception as er:
            print(er)

    def __str__(self) -> str:
        return self.regex


class KotParser(Parser):

    def __init__(self, regexes: list[str]):
        self.regex=regexes


    def start(self, html: str) -> list[str]:
        result=set(super().start(html))
        return result

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



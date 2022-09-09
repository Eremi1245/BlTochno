import re


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

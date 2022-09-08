import re


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
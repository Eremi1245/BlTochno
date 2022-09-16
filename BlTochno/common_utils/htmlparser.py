from BlTochno.BlTochno.common_utils.parser import Parser
from BlTochno.BlTochno.common_utils.urlobject import UrlObject


class HtmlParser:
    """Class parses incoming html, returns parsing results
    """

    def parse_page(self,url:UrlObject) -> UrlObject:
        """Main function of class.Parses incoming html, returns parsing results

        Args:
            html_lst (list[str]): list of html for parsing
            parser (IParser): parser_object

        Returns:
            list[UrlObject]: list of UrlObject
        """
        try:
            for parser in url.parsers:
                regex_matchs=parser.start(html=url.html)
                if regex_matchs:
                    url.regex_matchs+=regex_matchs
        except Exception as er:
            print(er)
        return url
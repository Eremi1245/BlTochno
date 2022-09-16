from collections import defaultdict

from BlTochno.common_utils.parser import Parser
from BlTochno.common_utils.urlobject import UrlObject


class HtmlParser:
    """Class parses incoming html, returns parsing results
    """

    def parse_page(self, url: UrlObject) -> UrlObject:
        """Main function of class.Parses incoming html, returns parsing results

        Args:
            html_lst (list[str]): list of html for parsing
            parser (IParser): parser_object

        Returns:
            list[UrlObject]: list of UrlObject
        """
        try:
            regex_matchs = url.parsers[0].start(html=url.html)
            if regex_matchs:
                url.regex_matchs += regex_matchs
        except Exception as er:
            print(er)
            return er
        return url

    def parse_hooka_mix(self, url: UrlObject) -> UrlObject:
        hooka_mix=defaultdict(str)
        try:
            for parser in url.parsers:
                regex_matchs = parser.start(html=url.html)
                hooka_mix['components']=''
        except Exception as er:
            print(er)
            return er
        return url

    #         'components':{
    #             'name':'',
    #             'percent':''
    #         },
    #         'desc':'',
    #         'img':''
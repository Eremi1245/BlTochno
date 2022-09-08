from BlTochno.common_utils.parser import Parser


class UrlObject:

    def __init__(self, url: str,parsers:Parser=[]) -> None:
        self.url=url
        self.html=''
        self.comment=''
        self.regex_matchs=[]
        self.parsers=parsers
 
    def __hash__(self) -> int:
        url=self.url
        return hash(url)
    
    def __call__(self) -> str:
        """When the UrlObject is called - returns string in format (https://netlock/path)

        Returns:
            str: string in format (https://netlock/path)
        """
        return self.url


    def __eq__(self, other) -> bool:
        """When UrlObject is compared with another UrlObject - two domains are compared

        Args:
            other (UrlObject): UrlObject

        Returns:
            bool: true if domains are equal
        """
        return self.url == other



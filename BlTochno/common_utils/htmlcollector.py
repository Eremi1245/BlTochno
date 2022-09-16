import datetime
import requests

from BlTochno.BlTochno.common_utils.urlobject import UrlObject

class HtmlCollector:
    """Base class for get Content from url
    """

    def start(self,url:UrlObject)->UrlObject:
        """Main function of class. Get content from url and return list of content

        Args:
            url_lst (list[UrlObject]): list of urls
            sleaper (bool, optional): Flag for sleep between requests. Defaults to None.

        Returns:
            list[str]: List of content
        """
        try:
            resp=requests.get(url(),timeout=20)  
            if resp.status_code==200:
                url.html=resp.text
            else:
                url.comment=f"{url.comment}\n{datetime.now()} - {resp.status_code}"
                print(f"url{url()} : {url.comment}")
        except ConnectionError:
            url.comment=f"{url.comment}\n{datetime.now()} - This site can’t be reached"
            print(f"url{url()} : {url.comment}")
        except Exception as er:
            url.comment=f"{url.comment}\n{datetime.now()} - {er}"
            print(f"url{url()} : {url.comment}")
        return url
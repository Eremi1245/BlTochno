





from BlTochno.common_utils.urlobject import UrlObject


class WordsAnalayzer:


    def __init__(self,word_dict:dict[str:str]) -> None:
        self.word_dict=word_dict


    def analize(self,urls:list[UrlObject])->list:
        try:
            for url in urls:
                for match in url.regex_matchs:
                    for word in match:
                        for k,v in self.word_dict.items():
                            for v1 in v:
                                if v1 in word:
                                    word=k
                                    break
        except Exception as er:
            print(er)
        return urls
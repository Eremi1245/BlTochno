





from BlTochno.common_utils.urlobject import UrlObject


class WordsAnalayzer:


    def __init__(self,word_dict:dict[str:str]) -> None:
        self.word_dict=word_dict


    def analize(self,urls:list[UrlObject])->list:
        try:
            for url in urls:
                for match_index in range(len(url.regex_matchs)):
                    for component_index in range(len(url.regex_matchs[match_index])):
                        word=url.regex_matchs[match_index][component_index]
                        url.regex_matchs[match_index][component_index]=self.check_word(word)
        except Exception as er:
            print(er)
        return urls

    def check_word(self,word:str):
        for original,alternatives in self.word_dict.items():
            if original==word:
                return original
            else:
                for alternativ in alternatives:
                    if alternativ in word:
                        return original
        print(f'Не нашли компонента "{word}" в словаре')
        return word
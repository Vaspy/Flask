import requests
from yandex_translate import YandexTranslate

class yaTranslation():
    #def __init__(self):
    def getrandom(self, much):
        bunch=''
        q=int(much)
        for i in range(0,q):
            word=requests.get('http://randomword.setgetgo.com/get.php').text
            bunch+=" {}".format(word)
        return(bunch[1:])

    def gettranslate(self, trans):
        if type(trans) is str:
            translate=YandexTranslate('trnsl.1.1.20160807T163932Z.f57cf5ac8b5daece.a4bfdf2addc8b214a91da651c04f3daa4fe46b7b')
            res=translate.translate('{0}'.format(trans), 'ru')
            ###RETURNS [] WITH WORDS
            return(res['text'][0].split(" "))
        else:
            return(None)

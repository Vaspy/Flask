import requests
from yandex_translate import YandexTranslate

def randomtorus(much):
    #Get random word (bunch of)
    bunch=''
    #How much words
    q=int(much)

    for i in range(0,q):
        word=requests.get('http://randomword.setgetgo.com/get.php').text
        bunch+=" {}".format(word)
    trans=bunch[1:]
    #print("Переводим:", trans)


    #Translate
    translate=YandexTranslate('trnsl.1.1.20160807T163932Z.f57cf5ac8b5daece.a4bfdf2addc8b214a91da651c04f3daa4fe46b7b')
    #Lang detect code
    #print('Язык:', translate.detect('{}'.format(trans)))
    #Translate to RU
    res=translate.translate('{0}'.format(trans), 'ru')
    #Print result
    #print("Перевод: ")
    #for m in range(0, len(res['text'])):
        #print(res['text'][m])
    result={'text':trans, 'translation':res['text']}
    return(result)

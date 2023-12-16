from googletrans import Translator

def tran(text):
    translator = Translator()
    en =  translator.translate(text,dest='en').text
    uz =  translator.translate(text,dest='uz').text
    ru =  translator.translate(text,dest='ru').text
    data = {'en':en,'ru':ru,'uz':uz}
    return data
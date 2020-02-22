from googletrans import Translator

sen=str(input("say......"))

trans=Translator()

# https://www.labnol.org/code/19899-google-translate-languages ------ codes for language
# need to use codes in src and dest. 
trans_sente=trans.translate(sen,src=input(''),dest=input(''))

print(trans_sente.text)


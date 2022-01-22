from logging import exception
import googletrans

from googletrans import Translator
translator = Translator()

#print(googletrans.LANGUAGES)
#text = 'This site is awesome'

try:
    with open('app/test.txt','r') as myFileTpRead:
        lineToTranslate = myFileTpRead.readline()
        print(f'Line is read from file is : {lineToTranslate}')
except FileNotFoundError as e:
        raise e
        print('Please check file path and retry')

#text = "My name is Priyadarshee Kumar"

Japannese_line = translator.translate(lineToTranslate , dest ='ja').text
Russina_line = translator.translate(lineToTranslate , dest ='ru').text
German_line = translator.translate(lineToTranslate , dest ='de').text
Arabic_line = translator.translate(lineToTranslate , dest ='ar').text
Odiya_line = translator.translate(lineToTranslate , dest ='or').text


transs = [Japannese_line,Russina_line,German_line,Arabic_line,Odiya_line]



translatedFile = 'app/translatedFile.txt'
print(f'Translated file can be found in : {translatedFile}\n')
try:
    with open(translatedFile, mode='w') as writeFile:
        for line in transs :
            writeFile.write(line + '\n')
            #print(f'After translation : {line}')
    with open(translatedFile, mode='r+') as transFile:
        print(transFile.read())
except FileNotFoundError as e:
    raise e
    print('Please verify the file path')



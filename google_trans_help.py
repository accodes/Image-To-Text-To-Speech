import googletrans 
from googletrans import Translator	

# print(googletrans.LANGUAGES)

# Detect lang
text1 = '''
A Római Birodalom (latinul Imperium Romanum) az ókori Róma által létrehozott 
államalakulat volt a Földközi-tenger medencéjében
'''
translator = Translator()
dt1 = translator.detect(text1)
print(dt1)

# Translate lang
translated = translator.translate('Бороди́нское сраже́ние')
translated = translator.translate('svízelná situace', src='cs', dest='hu')
print(translated.text)
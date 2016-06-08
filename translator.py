import sys, urllib2, json
from_lang = sys.argv[1]
to_lang = sys.argv[2]
yandex_API_KEY = "**************"
class YandexUrl:
   text = ""

   def __init__(self, key, from_lang, to_lang):
      self.key = key
      self.from_lang = from_lang
      self.to_lang = to_lang
   
   def setText(self, text):
      self.text = text

   def toString(self):
      return "https://translate.yandex.net/api/v1.5/tr.json/translate?key={0}&text={1}&lang={2}-{3}&format='plain'".format(yandex_API_KEY, self.text, self.from_lang, self.to_lang)  

url = YandexUrl(yandex_API_KEY, from_lang, to_lang)
while(True):
   print "Enter new text"
   new_text = raw_input()
   if new_text == ":q": break
   url.setText(new_text)
   print "*" * len(new_text)
   sock = urllib2.urlopen(url.toString())
   response = json.loads(sock.read())
   print response['text'][0]
   print  "*" * len(response['text'][0])




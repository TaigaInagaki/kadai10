import deepl

API_KEY = '***********' # 自身の API キーを指定

text = 'I hate that he is saying about school trip.'
source_lang = 'EN'
target_lang = 'JA'

# イニシャライズ
translator = deepl.Translator(API_KEY)

# 翻訳を実行
result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)

# print すると翻訳後の文章が出力される
print(result)
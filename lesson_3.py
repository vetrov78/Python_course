import requests, string, pymorphy2

def download_file_from_google_drive(id):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    response.encoding = 'utf-8'
    #print(response.encoding)
    return  response.text

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

file_id  = '15fBsTB1ZU_BzEw5SJmlOMX2uuyi1xN1-'
text = download_file_from_google_drive(file_id)
### пункт 1
exclude = list(string.punctuation) + ['«', '»']
clean_text = ''.join(e for e in text if e not in exclude)
print(clean_text)
### пункт 2
list_text = clean_text.split()
print(list_text)
### пункт 3
list_lower_text = list(map(str.lower, list_text))
print(list_lower_text)
### лемматизация
morph = pymorphy2.MorphAnalyzer()
parse_list = [morph.parse(w)[0] for w in list_lower_text]
lemm_list = list(map(lambda x: x.normal_form, parse_list))
print(lemm_list)
### пункт 4
dict_text = {x:list_lower_text.count(x) for x in list_lower_text}
print(dict_text)
### пункт 5
for key, value in sorted(dict_text.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(key)


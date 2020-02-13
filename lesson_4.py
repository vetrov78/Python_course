import random, requests

def F (names, N):
    result = []
    for i in range(0, N):
        result.append(names[random.randrange(len(names))])
    return result


def Q (names):
   return max(set(f), key=f.count)


def R(names):
    list_1_letter = list(map(lambda x: x[0], names))
    return min(set(list_1_letter), key=list_1_letter.count)


def download_file_from_google_drive(id):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    response.encoding = 'utf-8'

    return response.text

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None


f  = F(['qwe', 'rty', 'qw', 'tyu'], 12)

print(f)
print(Q(f))
print(R(f))

file = download_file_from_google_drive('1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8')
list_log = file.split('\n')
list_log_time = list(map(lambda x: x.split(',')[0], list_log))
print(list_log_time)
print(max(list_log_time))
import os
import requests

def get_filename(u):
    filename = ''
    split_list = u.split('//')
    for character in split_list[1]:
        if character.isalnum():
            filename += character
        else:
            filename += '-'
    return filename + '.html'

def download(u, p = os.getcwd()):
    response = requests.get(u)
    f_name = get_filename(u)
    res_path = os.path.join(p, f_name)
    with open(res_path, 'wb') as f:
        f.write(response.content)
    return res_path


if __name__ == '__main__':
    url = 'https://ru.hexlet.io/courses'
    # file_path = '/var/tmp'
    print(download(url))



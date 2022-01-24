#!/usr/bin/env python3

#from ast import arg
import os
import requests
import argparse


def get_filename(u):
    filename = ''
    split_list = u.split('//')
    for character in split_list[1]:
        if character.isalnum():
            filename += character
        else:
            filename += '-'
    return filename + '.html'


def download(u, p):
    response = requests.get(u)
    f_name = get_filename(u)
    res_path = os.path.join(p, f_name)
    with open(res_path, 'wb') as f:
        f.write(response.content)
    return res_path


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='A directory to download a webpage')
    parser.add_argument('-w', '--webpage', help='A webpage to download')
    return parser


def driver():
    args = create_parser().parse_args()
    url = 'https://ru.hexlet.io/courses'
    path = os.getcwd()
    
    if args.output:
        path =  args.output
    if args.webpage:
        url = args.webpage
    
    print(download(url, path))


if __name__ == '__main__':

    driver()
    



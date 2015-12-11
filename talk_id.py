#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get talkID from main page
"""
import sys
import re
import requests


def __parser_talk_id(raw_data):
    regex = re.compile(r'talkId\s*:\s*\"([\w=-]*)\",')
    result = regex.search(raw_data)
    return result.group(1)


def __parser_name(raw_data):
    regex = re.compile(r'og:title\" content=\"(.*)\"')
    result = regex.search(raw_data)
    return result.group(1)


def get_talk_id(url):
    session = requests.session()
    repo = session.get(url)

    if repo.status_code == 200:
        talk_id = __parser_talk_id(repo.text)
        username = __parser_name(repo.text)
        return talk_id, username

    return None

# For unit test
if __name__ == '__main__':
    url = sys.argv[1]
    print(get_talk_id(url))

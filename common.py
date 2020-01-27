import json


def load_play_lists(file_name):
    f = open(file=file_name, mode='r', encoding='utf-8')
    play_lists = json.load(f)
    return play_lists

import os
import random

from utils import processing_log_files, processing_log_file_topic


if __name__ == "__main__":

    click_action = processing_log_files()
    print(len(click_action.keys()))

    for k, v in click_action.items():
        print(k + "\t" + str(len(v)) + "\t" + "&&".join(v))

    category_items = processing_log_file_topic(
        save_file='../tmp/engineer/category_items.log')
    print(len(category_items.keys()))
    for k, v in category_items.items():
        print(k + "\t" + str(len(v)) + "\t" + "&&".join(v)+'\n')

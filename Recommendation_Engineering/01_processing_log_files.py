import os
import random

from utils import processing_log_files

if __name__ == "__main__":

    click_action = processing_log_files()
    print(len(click_action.keys()))

    for k, v in click_action.items():
        print(k + "\t" + str(len(v)) + "\t" + "&&".join(v))

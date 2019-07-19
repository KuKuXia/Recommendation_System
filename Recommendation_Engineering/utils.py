import os

# processing log files
def processing_log_files(filename="../tmp/engineer/log_file.txt"):
    file = open(filename)
    # click action of a user: key: uid value: video_id
    click_action = {}

    for line in file.readlines():
        ls = line.strip().split("&")
        if ls[7] != "1":
            continue
        else:
            # print(ls[1] + "\t" + ls[4])
            if ls[1] not in click_action.keys():
                click_action[ls[1]] = []
            click_action[ls[1]].append(ls[4])
    return click_action

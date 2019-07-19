import os


# process log file
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
    file.close()
    return click_action


# process log files by topic
def processing_log_file_topic(filename="../tmp/engineer/log_file.txt", save_file=""):
    category_items = {}
    file = open(filename)
    for line in file.readlines():
        line = line.strip()
        ls = line.split("&")
        if ls[5] not in category_items.keys():
            category_items[ls[5]] = []
        category_items[ls[5]].append(ls[4])

    file.close()

    # Save the results
    if save_file != "":
        category_file = open(save_file, 'w')
        for k, v in category_items.items():
            line = k + "\t" + "&&".join(v) + '\r\n'
            category_file.write(line)
        category_file.close()
    return category_items

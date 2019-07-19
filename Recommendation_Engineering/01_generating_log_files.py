

"""
Using python to generate logs.
"""
import random


def produce(filename='../tmp/engineer/log_file.txt'):
    """
    Creating a log file.
    Args:
        filename: the name of the log file.
    """

    print("Start creating the log file......")
    file_object = open(filename, 'w')

    user_list = ['one', 'two', 'three', 'four', 'five']
    alphabet = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i)
                                                         for i in range(26)] + [str(i) for i in range(10)]

    number = [str(i) for i in range(0, 10)]

    # log type 1: 点击 2： 播放 3：点赞 4：收藏 5：付费观看 6：站外分享 7：评论
    log_type_array = [str(i) for i in range(1, 8)]

    # topic types
    topic_array = ["空气净化器", "净水器", "加湿器", "空气净化滤芯"]

    for num in range(0, 10000):
        cookie = "".join(random.sample(alphabet, 6))
        uid = "".join(random.sample(user_list, 1))
        user_agent = "Linux Chrome Safari"
        ip = "192.168.89.177"
        video_id = "".join(random.sample(number, 7))
        topic = "".join(random.sample(topic_array, 1))
        order_id = "0"
        log_type = "".join(random.sample(log_type_array, 1))

        final = cookie + "&" + uid + "&" + user_agent + "&" + ip + "&" + \
            video_id + "&" + topic + "&" + order_id + "&" + log_type + '\r'

        file_object.write(final)
        # print(final)
    file_object.close()
    print("Finished creating the log file and saved the file to " + filename)


produce()

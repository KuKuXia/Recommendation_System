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
    alphabet = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)] + [str(i)
                                                                                                  for i in range(10)]
    for num in range(0, 10000):
        cookie = "".join(random.sample(alphabet, 8))
        uid = "".join(random.sample(alphabet, 6))
        user_agent = "Linux_Chrome_Safari"
        ip = "1.1.1.1"
        video_id = "123456"
        topic = "苹果发布会"
        order_id = "0"
        log_type = "1"

        final = cookie + "&" + uid + "&" + user_agent + "&" + ip + "&" + \
            video_id + "&" + topic + "&" + order_id + "&" + log_type + '\r\n'

        file_object.write(final)
        # print(final)
    file_object.close()
    print("Finished creating the log file and saved the file to " + filename)


produce()

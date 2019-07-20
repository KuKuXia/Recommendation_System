# encoding=utf-8

import jieba


class Prefile():
    def __init__(self, file_dir, file_name):
        self.file = [file_dir + i + '.txt' for i in file_name]
        # 获取每个文件的词频统计
        self.word_cut_results = self.tag(count=5)
        # 保存每个文件的词频统计结果
        self.save()

    # 对文本进行分词，并且统计每个词的频数，如果词对应的频数小于count，就舍去
    def tag(self, count=5):
        print("Start word cut and count: ")
        word_cut_results = []
        for i in range(len(self.file)):
            sing_file_word_cut_result = {}
            lines = open(self.file[i])
            for line in lines.readlines():
                seg_list = jieba.cut(line.strip())
                for seg in seg_list:
                    if seg not in sing_file_word_cut_result.keys():
                        sing_file_word_cut_result[seg] = 1
                    elif seg in sing_file_word_cut_result.keys():
                        sing_file_word_cut_result[seg] += 1

            lines.close()
            result_filter = {}
            for k, v in sing_file_word_cut_result.items():
                if v <= count:
                    continue
                result_filter[k] = v
            # for k, v in result_filter.items():
            #     print(k + '\t' + str(v))
            word_cut_results.append(result_filter)
        print("Finished word cut and count.")
        return word_cut_results

    def save(self, file_name='../tmp/engineer/word_cut.log'):
        file = open(file_name, 'w')
        file_num = 0
        for single_file_word_cut_result in self.word_cut_results:
            for k, v in single_file_word_cut_result.items():
                line = 'filename : ' + \
                    self.file[file_num] + '\t' + k + \
                    '\t' + str(v) + '\r\n'
                file.write(line)
            file_num += 1
        file.close()
        print("Saved the word cut and count results to " + file_name)


if __name__ == "__main__":
    p = Prefile(file_dir='../tmp/engineer/',
                file_name=['document_1', 'document_2', 'document_3'])

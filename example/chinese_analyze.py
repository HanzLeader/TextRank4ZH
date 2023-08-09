import json

# 中文分析权重占比
def is_chinese(input_string):
    chinese_words = 0
    english_words = 0
    other_words = 0    # 其余语言、符号等
    blank_words = 0    # 空格
    for char in input_string:
        if ('\u4e00' <= char <= '\u9fff'):
            chinese_words += 1
        elif ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            english_words += 1
        elif char == ' ':
            blank_words += 1
        else:
            other_words += 1

    # 判定中文条件:汉字+其他字符不小于英文字符/4 并且 其他字符占比不是最多的
    language_flag = bool((chinese_words + other_words >= english_words / 4) and (other_words < chinese_words + english_words))
    if language_flag:
        language = 'Chinese'
    else:
        language = 'English'

    data = {'language': language, 'chinese_words': chinese_words, 'english_words': english_words, 'other_words': other_words}
    return json.dumps(data)
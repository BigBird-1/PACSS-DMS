# -*- coding: utf-8 -*-
import jieba
import numpy as np
import re

seg_str = "送到阿斯蒂芬撒地方"

print("/".join(jieba.lcut(seg_str)))    # 精简模式，返回一个列表类型的结果
print("/".join(jieba.lcut(seg_str, cut_all=True)))      # 全模式，使用 'cut_all=True' 指定
print("/".join(jieba.lcut_for_search(seg_str)))     # 搜索引擎模式


def get_word_vector(s1, s2):
    """
    :param s1: 句子1
    :param s2: 句子2
    :return: 返回句子的余弦相似度
    """
    # 分词
    cut1 = jieba.cut(s1)
    cut2 = jieba.cut(s2)
    list_word1 = (','.join(cut1)).split(',')
    list_word2 = (','.join(cut2)).split(',')

    # 列出所有的词,取并集
    key_word = list(set(list_word1 + list_word2))
    # 给定形状和类型的用0填充的矩阵存储向量
    word_vector1 = np.zeros(len(key_word))
    word_vector2 = np.zeros(len(key_word))

    # 计算词频
    # 依次确定向量的每个位置的值
    for i in range(len(key_word)):
        # 遍历key_word中每个词在句子中的出现次数
        for j in range(len(list_word1)):
            if key_word[i] == list_word1[j]:
                word_vector1[i] += 1
        for k in range(len(list_word2)):
            if key_word[i] == list_word2[k]:
                word_vector2[i] += 1

    # 输出向量
    print(word_vector1)
    print(word_vector2)
    return word_vector1, word_vector2


def cos_dist(vec1, vec2):
    """
    :param vec1: 向量1
    :param vec2: 向量2
    :return: 返回两个向量的余弦相似度
    """
    dist1 = float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
    return dist1


def filter_html(html):
    """
    :param html: html
    :return: 返回去掉html的纯净文本
    """
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', html).strip()
    return dd


if __name__ == '__main__':
    s2 = "送到阿斯蒂芬撒地方"
    s1 = "我们都有的发送到阿斯蒂芬撒地一骑红尘妃子笑"
    vec1, vec2 = get_word_vector(s1, s2)
    dist1 = cos_dist(vec1, vec2)
    print(dist1)



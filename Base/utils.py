# !/usr/bin/python
# -*- coding: UTF-8 -*-
from run import PATH
from PIL import Image
import math
import operator
from functools import reduce

import cv2
import numpy as np


# 均值哈希算法
def aHash(img):
    # 缩放为8*8
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    # 遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s = s + gray[i, j]
    # 求平均灰度
    avg = s / 64
    # 灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# 差值感知算法
def dHash(img):
    # 缩放8*8
    img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
    # 转换灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j + 1]:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# Hash值对比
def cmpHash(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n


def getusedCarBanner():
    exp1 = PATH("./tmp/usedCar_screenshot/exp_topBanner_1.png")
    exp2 = PATH("./tmp/usedCar_screenshot/exp_topBanner_2.png")
    exp5 = PATH("./tmp/usedCar_screenshot/exp_topBanner_5.png")
    exp6 = PATH("./tmp/usedCar_screenshot/exp_topBanner_6.png")

    img1 = cv2.imread(exp1)
    img2 = cv2.imread(exp2)
    img5 = cv2.imread(exp5)
    img6 = cv2.imread(exp6)

    hash1 = aHash(img1)
    hash2 = aHash(img2)
    hash5 = aHash(img5)
    hash6 = aHash(img6)

    result=[hash1, hash2, hash5, hash6]
    result.sort()

    return result


def getElementImgHashById(driver, imgPath, elementId):

    element = driver.find_element_by_id(elementId)
    location = element.location
    size = element.size
    box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])
    driver.get_screenshot_as_file(imgPath)
    # 截取图片
    image = Image.open(imgPath)
    newImage = image.crop(box)
    newImage.save(imgPath)

    targetImg = cv2.imread(imgPath)
    hashValue = aHash(targetImg)
    print(hashValue)
    return hashValue


def getElementImgHashByXpath(driver, imgPath, elementId):

    element = driver.find_element_by_xpath(elementId)
    location = element.location
    size = element.size
    box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])
    driver.get_screenshot_as_file(imgPath)
    # 截取图片
    image = Image.open(imgPath)
    newImage = image.crop(box)
    newImage.save(imgPath)

    targetImg = cv2.imread(imgPath)
    hashValue = aHash(targetImg)
    print(hashValue)
    return hashValue



if __name__ == '__main__':
    # targetImage1 = PATH("./tmp/usedCar_screenshot/temp_screen9.png")
    # targetImage2 = PATH("./tmp/usedCar_screenshot/temp_screen8.png")
    #
    # img1 = cv2.imread(targetImage1)
    # img2 = cv2.imread(targetImage2)
    # hash1 = aHash(img1)
    # hash2 = aHash(img2)
    # print(hash1)
    # print(hash2)
    # n = cmpHash(hash1, hash2)
    # print('均值哈希算法相似度：' + str(n))
    #
    # hash1 = dHash(img1)
    # hash2 = dHash(img2)
    # print(hash1)
    # print(hash2)
    # n = cmpHash(hash1, hash2)
    # print(type(n))
    # print('差值哈希算法相似度：' + str(n))

    print(getusedCarBanner())

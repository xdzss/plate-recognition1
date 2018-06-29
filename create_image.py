# coding=gbk
import numpy as np
from genplate_advanced import *
import os

index = {"��": 0, "��": 1, "��": 2, "��": 3, "��": 4, "��": 5, "��": 6, "��": 7, "��": 8, "��": 9, "��": 10, "��": 11, "��": 12,
         "��": 13, "��": 14, "³": 15, "ԥ": 16, "��": 17, "��": 18, "��": 19, "��": 20, "��": 21, "��": 22, "��": 23, "��": 24,
         "��": 25, "��": 26, "��": 27, "��": 28, "��": 29, "��": 30, "0": 31, "1": 32, "2": 33, "3": 34, "4": 35, "5": 36,
         "6": 37, "7": 38, "8": 39, "9": 40, "A": 41, "B": 42, "C": 43, "D": 44, "E": 45, "F": 46, "G": 47, "H": 48,
         "J": 49, "K": 50, "L": 51, "M": 52, "N": 53, "P": 54, "Q": 55, "R": 56, "S": 57, "T": 58, "U": 59, "V": 60,
         "W": 61, "X": 62, "Y": 63, "Z": 64,"ѧ":65}

chars = ["��", "��", "��", "��", "��", "��", "��", "��", "��", "��", "��", "��", "��", "��", "��", "³", "ԥ", "��", "��", "��", "��",
             "��", "��", "��", "��", "��", "��", "��", "��", "��", "��", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A",
             "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
             "Y", "Z","ѧ"]


def rand_range(lo, hi):
    return lo + r(hi - lo)


def r(val):
    return int(np.random.random() * val)


def gen_rand():
    name = ""
    label = []
    label.append(19)
    label.append(rand_range(41, 65))
    for i in range(4):
        label.append(rand_range(31, 40))
    label.append(65)    

    name += chars[label[0]]
    name += chars[label[1]]
    for i in range(4):
        name += chars[label[i + 2]]
    name += chars[label[6]]
    print(name,label)
    return name, label


def gen_sample(genplate_advanced, width, height):
    name, label = gen_rand()
    img = genplate_advanced.generate(name)
    img = cv2.resize(img, (width, height))
    # img = np.multiply(img, 1 / 255.0)
    # img = img.transpose(2, 0, 1)
    return label, img, name


def genBatch(batchSize, outputPath):
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
    label_store = []
    for i in range(batchSize):
        print('create num:' + str(i))
        label, img, name = gen_sample(genplate_advanced, 120, 30)
        label_store.append(label)
        # filename = os.path.join(outputPath, str(i).zfill(4) + '.' + plateStr + ".jpg")
        filename = os.path.join(outputPath, str(i).zfill(5) + ".jpg")
        filename1 = str(i).zfill(5) + ".jpg"
        with open('train_labels.txt','a') as f:
            f.write(filename1 + ":" + name + "\n")
            #f.write(":")
            #f.write(name)
            #f.write("\n")
        img = cv2.resize(img,(250,40))
        cv2.imwrite(filename, img)
    label_store = np.array(label_store)
    np.savetxt('label.txt', label_store)


batchSize = 50000
path = './data/train_data'
font_ch = './font/platech.ttf'
font_en = './font/platechar.ttf'
bg_dir = './NoPlates'
genplate_advanced = G = GenPlate(font_ch, font_en, bg_dir)
genBatch(batchSize=batchSize, outputPath=path)

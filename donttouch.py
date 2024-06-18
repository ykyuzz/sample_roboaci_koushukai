import csv
import os
import random
import time



def mkdata():
    HinshuList = ['ShinanoGold', 'Tsugaru', 'Toki', 'Fuji', 'Ourin', 'JonaGold', 'Kougyoku']
    PrefectureList = ['Aomori', 'Nagano', 'Iwate', 'Yamagata', 'Fukushima', 'Akita', 'Gunma', 'Hokkaido', 'Miyagi', 'Gifu']

    os.remove('sumple_data.csv')

    with open('sumple_data.csv', mode='w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['品種', '産地', '数量(kg)', '農薬使用の有無', '買付金額'])
        for i in range(1000):
            if random.random() > 0.5:
                sig = True
            else:
                sig = False
            a = [HinshuList[random.randrange(7)], PrefectureList[random.randrange(10)], random.randrange(1, 10) * 100000, sig, random.randrange(1, 10) * 100000]
            writer.writerow(a)

def getData():
    k = 0
    if time.time() % 3 == 0:
        with open('sumple_data.csv') as f:
            reader = csv.reader(f)
            ind = random.randrange(100)
            cur_ind = 0
            for row in reader:
                cur_ind = cur_ind+1
                if (cur_ind == ind):
                    return [True] + row
    else:
        return [False]
    
def getRequirement():
    HinshuList = ['シナノゴールド', 'つがる', 'とき', 'ふじ', '王林', 'ジョナゴールド', '紅玉']
    PrefectureList = ['青森県', '長野県', '岩手県', '山形県', '福島県', '秋田県', '群馬県', '北海道', '宮城県', '岐阜県', 'なんでもよい']
    hinshu = HinshuList[random.randrange(7)]
    prefecture = PrefectureList[random.randrange(11)]
    ryou = random.randrange(1, 10) * 100000
    kakaku = random.randrange(1, 10) * 100000
    if random.random() > 0.5:
        sig = 'あり'
    else:
        sig = 'なし'
    return '品種は{}で産地は{}、数量は{}kgで価格は￥{}くらいがいいなあ、あと農薬使用{}でいいよ'.format(hinshu, prefecture,ryou, kakaku, sig)


def getRequirementAsList():
    HinshuList = ['シナノゴールド', 'つがる', 'とき', 'ふじ', '王林', 'ジョナゴールド', '紅玉']
    PrefectureList = ['青森県', '長野県', '岩手県', '山形県', '福島県', '秋田県', '群馬県', '北海道', '宮城県', '岐阜県', 'なんでもよい']
    hinshu = HinshuList[random.randrange(7)]
    prefecture = PrefectureList[random.randrange(11)]
    ryou = random.randrange(1, 10) * 100000
    kakaku = random.randrange(1, 10) * 100000
    if random.random() > 0.5:
        sig = 'あり'
    else:
        sig = 'なし'
    return [hinshu, prefecture, ryou, kakaku, sig]


import difflib

text1='甄子丹 Donnie Yen|徐峥 Zheng Xu|袁泉 Quan Yuan|周冬雨 Dongyu Zhou|陶慧 Hui Tao|岳小军 Xiaojun Yue|张俪 Li Zhang|马苏 Su Ma|刘美含 Mikan|焦俊艳 Junyan Jiao|郭涛 Tao Guo|李晨 Chen Li|夏雨 Yu Xia|刘仪伟 Yiwei Liu|雷佳音 Jiayin Lei|宁浩 Hao Ning|沈腾 Teng Shen|熊乃瑾 Naijin Xiong'
text2='甄子丹 Donnie Yen|周润发 Yun-Fat Chow|郭富城 Aaron Kwok|夏梓桐 Xia Zi Tong|陈乔恩 Joe Chan|张梓琳 Zilin Zhang|何润东 Peter Ho|梁咏琪 Gigi Leung|陈慧琳 Kelly Chen|张兆辉 Siu-fai Cheung|郑家星 Jiaxing Zheng|樊少皇 Siu-Wong Fan|汪圆圆 Irene Wong|李菁 Jing Li|海一天 Yitian Hai|刘桦 Hua Liu|罗仲谦 Chung Him Law|梁雨恩 Cathy Leung|刘双宁 Shuangning Liu'

t1=text1.split('|')
t2=text2.split('|')

# 数组类型:
def compareShuzu( a,b):
    r1=a
    r2=b
    if len(r1)>len(r2) :
        r1=b
        r2=a
    same=0
    for r in r1:
       for rr in r2:
           if r==rr:
               same+=1
               break
    if same*len(r1)/( len(r2)*len(r2) )>1:
        print(same*len(r1)/( len(r2)*len(r2) ))
        print("数组")
    return same*len(r1)/( len(r2)*len(r2) )
# 数字类型： 两数之差，但伸缩到0~1范围
def compareint(r1, r2, max , mix):
    try:
        int(r2)
    except:
        r2=max
    if (abs(int(r1)-int(r2))-mix)/(max-mix)>1:
        print((abs(int(r1)-int(r2))-mix)/(max-mix))
        print("数字")
    return (abs(int(r1)-int(r2))-mix)/(max-mix)


# 字符类型：字符的相同个数/两者之中最大字符数
def compareStr(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

# 上映时间：输入为三个元素的数组年月日，差值伸缩
def compareUpdate(s1,s2):
    d=0
    d+=abs(int(s1[0])-int(s2[0]))/10*0.25
    try:
        d+=abs(int(s1[1])-int(s2[1]))/12*0.70
    except:
        if d > 1:
            print(d)
            print("时间")
        return d
    try:
        d+=abs(int(s1[2])-int(s2[2]))/30*0.05
    except:
        if d > 1:
            print("时间")
            print(d)
        return d
    if d > 1:
        print("时间")
        print(d)
    return d

def compareMov(m1,m2):
    all=0
    # 每行代码后面的*N，N就是相似度的权值
    all+=compareStr(m1['名'],m2['名'])*0.05
    all+=compareShuzu(m1['类型'],m2['类型'])*0.025
    all+=compareint(m1['时长'],m2['时长'],150,0)*0.05
    all+=compareUpdate(m1['上映时间'],m2['上映时间'])*0.1
    all+=compareStr(m1['制式'],m2['制式'])*0.025
    all+=compareShuzu(m1['地区'],m2['地区'])*0.05
    all+=compareShuzu(m1['导演'],m2['导演'])*0.2
    all+=compareShuzu(m1['演员'],m2['演员'])*0.2
    all+=compareShuzu(m1['制作公司'],m2['制作公司'])*0.1
    all+=compareShuzu(m1['发行公司'],m2['发行公司'])*0.2
    return all

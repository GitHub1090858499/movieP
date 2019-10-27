from _票房预测配置 import compareMov
from _快速输入模块 import opeee
# import os
# print(os.getcwd())

f = open("dataM.txt",encoding='UTF-8-sig',mode='r+')
f.seek(0)
alltext=f.readlines()
f.close()


# 设置输入
# themo={
#     '名':'变形金刚4：绝迹重生',
#     '类型':['科幻','动作','冒险'],
#     '时长':'166',
#     '上映时间':['2014','6','27'],
#     '制式':'3D/IMAX',
#     '地区':['美国','中国'],
#     '导演':['迈克尔·贝 Michael Bay'],
#     '演员':['马克·沃尔伯格 Mark Wahlberg'],
#     '制作公司' : ['派拉蒙影业公司','美国迪·博纳文图拉影片公司','一九零五（北京）网络科技有限公司','美国汤姆·迪桑托/唐·墨菲影片公司','家赋（北京）文化传媒有限公司'],
#     '发行公司' : ['中国电影集团公司','华夏电影发行有限责任公司'],
#     '内地票房' : '197,752'
# }
# 设置输入,themo将在下面的票房预测程序作为输入
themo={
    '名':'终结者：黑暗命运',
    '类型':['动作','科幻','冒险'],
    '时长':'128',
    '上映时间':['2019','11','1'],
    '制式':'2D/IMAX',
    '地区':['美国'],
    '导演':['蒂姆·米勒 Tim Miller'],
    '演员':['麦肯兹·戴维斯 Mackenzie Davis',"琳达·汉密尔顿 Linda Hamilton","阿诺·施瓦辛格 Arnold Schwarzenegger","加布里埃尔·鲁纳 Gabriel Luna","娜塔利娅·雷耶斯 Natalia Reyes","迭戈·博内塔 Diego Boneta"
          ,"爱德华·福隆 Edward Furlong","特里斯坦·乌罗阿 Trist&#225;n Ulloa","史蒂文·克瑞 Steven Cree","汤姆·霍珀 Tom Hopper"],
    '制作公司' : ['Lightstorm Entertainment','天空之舞制片公司','二十世纪福斯电影公司','腾讯影业文化传播有限公司','派拉蒙影业公司'],
    '发行公司' : ['二十世纪福斯公司','华纳兄弟公司',"腾讯影业文化传播有限公司","20世纪福斯公司"],
    '内地票房' : '0'
}
# # 或者用快速输入
# themo=opeee( id='694522')
# themo=opeee( id='573968')
# themo=opeee( id='588865')
themo=opeee( id='662685')
# for ii in themo.values():
#     print(ii)




# 遍历本地txt文件的行索引
seek=0
# 读取本地txt文件后的格式化电影信息
moves={}
# 匹配集的最小值
mixbig=0
# 匹配集最小值得索引
mixindex=0
# 匹配集容量
N=4
# 匹配集
pipeis=[]
# 当前要替换的电影信息
pipei={}

# 从pipeis数组中预测themo票房
def yuche(themo,pipeis2):
    pipeis=pipeis2.copy()
    piaofans=[]
    i=0
    leng=len(pipeis)
    while i<leng:
        max=0
        for pipei in pipeis:
            if compareMov(themo, pipei)>max:
                max=compareMov(themo, pipei)
                maxt=pipei
        pipeis.remove(maxt)
        piaofans.append(float(maxt["内地票房"].replace(",",".")))
        # print(piaofans[i])
        i+=1
    #
    return  piaofans[0]*0.7+piaofans[1]*0.2+piaofans[2]*0.07+piaofans[3]*0.03

# 在pipeis数组元素中选择与themo最小相似度的索引
def findmin(themo,pipeis):
    i=0
    min=2
    minindex=0
    # print("ha")
    while i<len(pipeis):
        if compareMov(themo, pipeis[i])<=min:
            minindex=i
            min=compareMov(themo, pipeis[i])
        i+=1
    return minindex


while seek < len(alltext):
    moves['名']=alltext[seek].strip()
    seek+=1
    moves['类型']=alltext[seek].strip().split('|')
    seek += 1
    moves['时长']=alltext[seek].strip()
    seek += 1
    moves['上映时间']=alltext[seek].strip().split('|')
    seek += 1
    moves['制式']=alltext[seek].strip()
    seek += 1
    moves['地区']=alltext[seek].strip().split('|')
    seek += 1
    moves['导演']=alltext[seek].strip().split('|')
    seek += 1
    moves['演员']=alltext[seek].strip().split('|')
    seek += 1
    moves['制作公司']=alltext[seek].strip().split('|')
    seek += 1
    moves['发行公司']=alltext[seek].strip().split('|')
    seek += 1
    moves['内地票房']=alltext[seek].strip()
    seek += 2
    if len(pipeis)<N:
        newMove=moves.copy()
        pipeis.append(newMove)
        mixindex=findmin(themo, pipeis)
        mixbig=compareMov(themo, pipeis[mixindex])
    else :
        thisd=compareMov(themo, moves)
        if thisd>mixbig:
            newMove = moves.copy()
            # moves替换pipeis的最小值
            pipeis[mixindex]=newMove
            # 获取pipeis中最小值的索引
            mixindex = findmin(themo, pipeis)
            # 获取pipeis中最小相似度
            mixbig = compareMov(themo, pipeis[mixindex])

for pipei in pipeis:
    print("【"+pipei['名']+"】\t相似度：【"+str(compareMov(themo, pipei))+"】\t\t内地票房【"+pipei["内地票房"]+"】")
# print(themo['名']+"|"+)
print("\n【"+themo['名']+"】票房预测： 【"+str(yuche(themo, pipeis))+"】  单位 千万元")





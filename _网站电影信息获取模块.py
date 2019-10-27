
import requests
from lxml import  html




# 消息头
head={
    'Host': 'www.cbooo.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'http://www.cbooo.cn/movies',
    'Cookie': 'Hm_lvt_daabace29afa1e8193c0e3000d391562=1568855276; Hm_lpvt_daabace29afa1e8193c0e3000d391562=1568869628; hibext_instdsigdipv2=1; bdshare_firstime=1568855313232',
}

# 开始年份
beginyear=2017
# 结束年份
maxyear=2019


with open('dataM.txt',encoding='utf8', mode='a+') as file:
    # 开始年份
    year = beginyear
    # 按年份遍历
    while year<=maxyear:
        # 本年份最大页，用于每年的遍历的操作最终标志
        lpage=1
        # 开始页，用于每年的遍历
        index=1
        # 每年中的电影中，按页遍历
        while index<=lpage :
            # 发送的数据
            data={
                'area':'50',
                'type':'0',
                'year':str(year),
                'initial':'全部',
                'pIndex':str(index),
            }
            # 目的网站
            url='http://www.cbooo.cn/Mdata/getMdata_movie?area=50&type=0&year='+str(year)+'&initial=%E5%85%A8%E9%83%A8&pIndex='+str(index)

            # 上传数据和消息头到url
            response = requests.get(url, headers=head, data=data)
            # 获得响应，转换成字典
            dict1=response.json()
            # 本年份最大页，这是个赘余的动作
            lpage=dict1['tPage']
            # print(lpage)
            # 所有电影，用数组来存储，在目前的设计阶段，这个结构是多余的
            moveAll=[]

            # print(len(dict1['pData']))

            # 遍历一页中的所有电影信息
            for i in range(len(dict1['pData'])):
                # print('http://www.cbooo.cn/m/'+dict1['pData'][i]['ID'])
                # 获得电影链接
                ssrc='http://www.cbooo.cn/m/'+dict1['pData'][i]['ID']
                # 电影链接异常处理
                if dict1['pData'][i]['BoxOffice']=='' or int(dict1['pData'][i]['BoxOffice'])<=0:
                    continue
                try :
                    # 获得电影信息网站的html
                    elements=html.fromstring(requests.get(ssrc).text)
                except :
                    continue
                # 一个电影信息，用字典来存储{电影名，（属性）}
                oneMove={}

                # 字符串类型
                try :
                    mName=elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/h2/text()')[0]
                except :
                    continue
                oneMove['名']=mName
                print(mName)
                # 数组类型
                mType=elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[3]/text()')[0].split('：')[1].split('/')
                oneMove['类型']=mType
                # 数字类型
                try:
                    mTimeLong = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[4]/text()')[0].split('：')[1].strip().strip('min').strip('分钟')
                    if(mTimeLong==''):
                        mTimeLong=str(100)
                except :
                    mTimeLong=str(100)
                oneMove['时长']=mTimeLong
                # 数组类型
                mTimeUp = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[5]/text()')[0].split('：')[1].split('（')[0].split('-')
                oneMove['上映时间']=mTimeUp
                # 字符类型
                m3d = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[6]/text()')[0].split('：')[1]
                oneMove['制式']=m3d
                # 数组类型
                mlocoal = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[7]/text()')[0].split('：')[1].split('/')
                oneMove['地区']=mlocoal
                # 数组类型
                mDritor = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/dl/dd[1]/p/a/text()')
                oneMove['导演']=mDritor
                # 数组类型
                mActors = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/dl/dd[2]/p/a/@title')
                oneMove['演员']=mActors
                # 数组类型
                mMaker = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/dl/dd[3]/p/a/@title')
                oneMove['制作公司']=mMaker
                # 数组类型
                mSendOut = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/dl/dd[4]/p/a/@title')
                oneMove['发行公司']=mSendOut
                # 字符类型
                try:
                    mMoney = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[2]/h4[1]/a/text()')[0].split('：')[1].strip('万')
                except :
                    try:
                        mMoney = elements.xpath('//span[@class="m-span"]/text()')[1].strip('万')
                    except:
                        continue
                oneMove['内地票房']=mMoney
                # 将字典格式的电影信息添加到数组格式的电影集
                moveAll.append(oneMove)
                # 写入字符串格式到本地文件
                text=oneMove['名']+'\n'+'|'.join(oneMove['类型'])+'\n'+str(oneMove['时长'])+'\n'+'|'.join(oneMove['上映时间'])+'\n'+oneMove['制式']+'\n'+'|'.join(oneMove['地区']) + '\n'+'|'.join(oneMove['导演']) + '\n'+'|'.join(oneMove['演员']) + '\n'+'|'.join(oneMove['制作公司']) + '\n'+'|'.join(oneMove['发行公司']) + '\n'+oneMove['内地票房']+'\n\n'
                file.write(text)
                # text = oneMove['名'] + '/n' + oneMove['类型'] + '/n' + oneMove['时长'] + '/n' + oneMove['上映时间'] + '/n' + oneMove[
                #     '制式'] + '/n' + oneMove['地区'] + '/n' + oneMove['导演'] + '/n' + oneMove['演员'] + '/n' + oneMove[
                #            '制作公司'] + '/n' + oneMove['发行公司'] + '/n' + oneMove['内地票房']
                # file.write(text)
            index+=1
        year+=1
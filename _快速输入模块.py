from lxml import  html
import requests

def opeee(id):
    ssrc = 'http://www.cbooo.cn/m/' +id
    elements = html.fromstring(requests.get(ssrc).text)
    oneMove = {}
    # 字符串类型
    mName = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/h2/text()')[0]
    oneMove['名'] = mName
    # 数组类型
    mType = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[3]/text()')[0].split('：')[1].split('/')
    oneMove['类型'] = mType
    # 数字类型
    try:
        mTimeLong = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[4]/text()')[0].split('：')[
            1].strip().strip('min').strip('分钟')
        if (mTimeLong == ''):
            mTimeLong = str(100)
    except:
        mTimeLong = str(100)
    oneMove['时长'] = mTimeLong
    # 数组类型
    mTimeUp = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[5]/text()')[0].split('：')[1].split('（')[
        0].split('-')
    oneMove['上映时间'] = mTimeUp
    # 字符类型
    m3d = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[6]/text()')[0].split('：')[1]
    oneMove['制式'] = m3d
    # 数组类型
    mlocoal = elements.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[1]/p[7]/text()')[0].split('：')[1].split('/')
    oneMove['地区'] = mlocoal
    # 数组类型
    mDritor = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/dl/dd[1]/p/a/text()')
    oneMove['导演'] = mDritor
    # 数组类型
    mActors = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/dl/dd[2]/p/a/@title')
    oneMove['演员'] = mActors
    # 数组类型
    mMaker = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/dl/dd[3]/p/a/@title')
    oneMove['制作公司'] = mMaker
    # 数组类型
    mSendOut = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/dl/dd[4]/p/a/@title')
    oneMove['发行公司'] = mSendOut
    # 字符类型
    try:
        mMoney = elements.xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[2]/h4[1]/a/text()')[0].split('：')[1].strip('万')
    except:
        try:
            mMoney = elements.xpath('//span[@class="m-span"]/text()')[1].strip('万')
        except:
            mMoney=0
    oneMove['内地票房'] = mMoney
    return oneMove
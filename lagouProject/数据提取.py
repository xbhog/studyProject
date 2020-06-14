import requests
import  pymysql
from lxml import  etree
import  json,time

# 工作年限，薪水，城市职位，学历要求

# 基础页
def textInformation(post_url, data, cookies):
    response = requests.post(post_url, headers=headers, data=data, cookies=cookies,timeout=5).text
    div1 = json.loads(response)
    # 拿到该页的职位信息
    position_data = div1["content"]["positionResult"]["result"]
    db = pymysql.connect('192.168.75.135', 'root', 'root', 'lagouMysql', charset='utf8mb4')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = '''insert into  stable(id,positionName,companyFullName,city,salary,Education,work_year) values (%s,%s,%s,%s,%s,%s,%s)'''
    n = 1
    for list in position_data:

        value_data = (list['positionId'], list['positionName'], list['companyFullName'], list['city'], list['salary'],list['education'],list['workYear'])
        # mysqlData(value_data)

        print(value_data)
        cursor.execute(sql,value_data)
        db.commit()
        time.sleep(5)
        print('----------写入%s次-------' %n)
        n +=1
    db.close()
    # return value_data




# 获取职位页面数量
def getPageNumber(start_url, cookies):
    response = requests.get(start_url, headers=headers, cookies=cookies,timeout=3).text
    html = etree.HTML(response)
    # 获取到该职位页面数量
    sums = html.xpath("//span[@class='span totalNum']/text()")[0]
    return sums


def cookieRequest(start_url):
    r = requests.Session()
    r.get(url=start_url, headers=headers, timeout=3)
    return r.cookies

if __name__ == '__main__':
    start_url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    post_url = "https://www.lagou.com/jobs/positionAjax.json?"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    }
    # 动态cookies
    cookies = cookieRequest(start_url)
    # 页面数量
    number = getPageNumber(start_url, cookies)
    print("该职位的总页数：", number)
    time.sleep(1)
    try:
        s = 1
        for num in range(1, int(number)):
            data = {
                "first": "true",
                "pn": str(num),  # 1
                "kd": "python",
            }
            textInformation(post_url, data, cookies)
            time.sleep(7)
            print('------------第%s页爬取成功，正在进行下一页--------------' % s)
            s += 1
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"

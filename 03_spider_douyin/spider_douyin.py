# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 0:48
# @Author  : Nixin
# @Email   : nixin@foxmail.com
# @File    : spider_douyin.py
# @Software: PyCharm


import requests, re, sys, os, time, random, socket
import http.client
from bs4 import BeautifulSoup


def get_html(url, data=None):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    timeout = random.choice(range(80, 100))
    while True:
        try:
            response = requests.get(url, headers=header, timeout=timeout)
            response.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print(e)
            time.sleep(random.choice(range(20, 60)))
        except socket.error as e:
            print(e)
            time.sleep(random.choice(range(20, 60)))
        except http.client.BadStatusLine as e:
            print(e)
            time.sleep(random.choice(range(30, 60)))
        except http.client.IncompleteRead as e:
            print(e)
            time.sleep(random.choice(range(20, 60)))
    # print(response.text)
    return response.text


def download_douyin(num, url):
    rsp = get_html(url)
    patt = 'playAddr: "(.*?)",'
    play = re.compile(patt).findall(rsp)[0].replace("playwm", "play")
    print(play)
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'identity;q=1, *;q=0',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    res = requests.get(play, stream=True, headers=header)

    path = 'E:/nixin/douyin/video/20200416/'
    if not os.path.exists(path):
        os.makedirs(path)
    pathinfo = 'E:/nixin/douyin/video/20200416/%d.mp4' % num  # %d 用于整数输出   %s用于字符串输出
    total_size = int(res.headers['Content-Length'])
    print('这是视频的总大小：', total_size)

    temp_size = 0
    if res.status_code == 200:
        with open(pathinfo, 'wb') as file:
            # file.write(res.content)
            # print(pathinfo + '下载完成啦啦啦啦啦')

            # 当流下载时，下面是优先推荐的获取内容方式，iter_content()函数就是得到文件的内容，指定chunk_size=1024，大小可以自己设置哟，设置的意思就是下载一点流写一点流到磁盘中
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    temp_size += len(chunk)
                    file.write(chunk)
                    file.flush()  # 刷新缓存

                    # 下载进度条部分start
                    done = int(50 * temp_size / total_size)
                    # print('百分比:',done)
                    # 调用标准输出刷新命令行，看到\r回车符了吧
                    # 相当于把每一行重新刷新一遍
                    sys.stdout.write("\r[%s%s] %d%%" % (
                    '█' * done, ' ' * (50 - done), 100 * temp_size / total_size) + " 文件：" + pathinfo + " 下载完成")
                    sys.stdout.flush()  # 刷新缓存
                    # 下载进度条部分end

            print('\n')  # 每一条打印在屏幕上换行输出
    pass


def batch_download_douyin(start, pathtxt):
    with open(pathtxt) as f:
        f_url_list = f.readlines()  # 得到的是一个list类型
        for a in f_url_list:
            print(a.strip())
            download_douyin(start, a.strip())
            start += 1
            time.sleep(random.choice(range(3, 6)))

    pass


if __name__ == '__main__':
    # download_douyin(23, "https://v.douyin.com/cPXLbt")
    batch_download_douyin(75, "E:/nixin/douyin/video/20200416/1.txt")
    pass

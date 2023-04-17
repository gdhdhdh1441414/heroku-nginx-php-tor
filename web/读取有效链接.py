import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# 代理
proxy = {'http': 'http://127.0.0.1:1086', 'https': 'http://127.0.0.1:1086'}

# 需要尝试的链接列表


urls = [
    "https://ellie056.onrender.com",
]    



'''
#奇数
urls = [
    "https://github.c/qodnh/?这是无效链接，让这个代码能无限循环", 
    "https://vimeo362227-1.onrender.com",
    "https://vimeo362227-3.onrender.com",
    "https://vimeo362227-5.onrender.com",
    "https://vimeo362227-7.onrender.com",
    "https://vimeo362227-9.onrender.com",
    "https://vimeo362227-11.onrender.com",
    "https://vimeo362227-13.onrender.com",
    "https://vimeo362227-15.onrender.com",
    "https://vimeo362227-17.onrender.com",
    "https://vimeo362227-19.onrender.com",
    "https://vimeo362227-21.onrender.com",
    "https://vimeo362227-23.onrender.com",
    "https://vimeo362227-25.onrender.com",
    "https://vimeo362227-27.onrender.com",
    "https://vimeo362227-29.onrender.com",
    "https://vimeo362227-31.onrender.com",
    "https://vimeo362227-33.onrender.com",
    "https://vimeo362227-35.onrender.com",
    "https://vimeo362227-37.onrender.com",
    "https://vimeo362227-39.onrender.com",
    "https://vimeo362227-41.onrender.com",
    "https://vimeo362227-43.onrender.com",
    "https://vimeo362227-45.onrender.com",
    "https://vimeo362227-47.onrender.com",
    "https://vimeo362227-49.onrender.com",
    "https://vimeo362227-51.onrender.com",
    "https://vimeo362227-53.onrender.com",
    "https://vimeo362227-55.onrender.com",
    "https://vimeo362227-57.onrender.com",
    "https://vimeo362227-59.onrender.com",
    "https://vimeo362227-61.onrender.com",
    "https://vimeo362227-63.onrender.com",
    "https://vimeo362227-65.onrender.com",
    "https://vimeo362227-67.onrender.com",
    "https://vimeo362227-69.onrender.com",
    "https://vimeo362227-71.onrender.com",
    "https://vimeo10362227-1.onrender.com",
    "https://vimeo10362227-3.onrender.com",
    "https://vimeo10362227-5.onrender.com",
    "https://vimeo10362227-7.onrender.com",
    "https://vimeo10362227-9.onrender.com",
    "https://vimeo10362227-11.onrender.com",
    "https://vimeo10362227-13.onrender.com",
    "https://vimeo10362227-15.onrender.com",
    "https://vimeo10362227-17.onrender.com",
    "https://vimeo10362227-19.onrender.com",
    "https://vimeo10362227-21.onrender.com",
    "https://vimeo10362227-23.onrender.com",
    "https://vimeo10362227-25.onrender.com",
    "https://vimeo10362227-27.onrender.com",
    "https://vimeo10362227-29.onrender.com",
    "https://vimeo10362227-31.onrender.com",
    "https://vimeo10362227-33.onrender.com",
    "https://vimeo10362227-35.onrender.com",
    "https://vimeo10362227-37.onrender.com",
    "https://vimeo10362227-39.onrender.com",
    "https://vimeo10362227-41.onrender.com",
    "https://vimeo10362227-43.onrender.com",
    "https://vimeo10362227-45.onrender.com",
    "https://vimeo10362227-47.onrender.com",
    "https://vimeo10362227-49.onrender.com",
    "https://vimeo10362227-51.onrender.com",
    "https://vimeo10362227-53.onrender.com",
    "https://vimeo10362227-55.onrender.com",
    "https://vimeo10362227-57.onrender.com",
    "https://vimeo10362227-59.onrender.com",
    "https://vimeo10362227-61.onrender.com",
    "https://vimeo10362227-63.onrender.com",
    "https://vimeo10362227-65.onrender.com",
    "https://vimeo10362227-67.onrender.com",
    "https://vimeo10362227-69.onrender.com",
    "https://vimeo10362227-71.onrender.com",
    "https://vimeo10362227-73.onrender.com",

    
    "https://ellie001.onrender.com",
    "https://ellie003.onrender.com",
    "https://ellie005.onrender.com",
    "https://ellie007.onrender.com",
    "https://ellie009.onrender.com",
    "https://ellie011.onrender.com",
    "https://ellie013.onrender.com",
    "https://ellie015.onrender.com",
    "https://ellie017.onrender.com",
    "https://ellie019.onrender.com",
    "https://ellie021.onrender.com",
    "https://ellie023.onrender.com",
    "https://ellie025.onrender.com",
    "https://ellie027.onrender.com",
    "https://ellie029.onrender.com",
    "https://ellie031.onrender.com",
    "https://ellie033.onrender.com",
    "https://ellie035.onrender.com",
    "https://ellie037.onrender.com",
    "https://ellie039.onrender.com",
    "https://ellie041.onrender.com",
    "https://ellie043.onrender.com",
    "https://ellie045.onrender.com",
    "https://ellie047.onrender.com",
    "https://ellie049.onrender.com",
    "https://ellie051.onrender.com",
    "https://ellie053.onrender.com",
    "https://ellie055.onrender.com",
    "https://ellie057.onrender.com",
    "https://ellie059.onrender.com",
    "https://ellie061.onrender.com",
    "https://ellie063.onrender.com",
    "https://ellie065.onrender.com",
    "https://ellie067.onrender.com",
    "https://ellie069.onrender.com",
    "https://ellie071.onrender.com",
    "https://ellie073.onrender.com",
    "https://ellie075.onrender.com",
    "https://ellie077.onrender.com",
    "https://ellie079.onrender.com",
    "https://ellie081.onrender.com",
    "https://ellie083.onrender.com",
    "https://ellie085.onrender.com",
    "https://ellie087.onrender.com",
    "https://ellie089.onrender.com",
    "https://ellie091.onrender.com",
    "https://ellie093.onrender.com",
    "https://ellie095.onrender.com",
    "https://ellie097.onrender.com",
    "https://ellie099.onrender.com",
    "https://ellie101.onrender.com",
    "https://ellie103.onrender.com",
    "https://kai005.onrender.com",
]
'''

'''
#偶数
urls = [
    "https://github.c/qodnh/?这是无效链接，让这个代码能无限循环", 
    "https://vimeo362227-2.onrender.com",
    "https://vimeo362227-4.onrender.com",
    "https://vimeo362227-6.onrender.com",
    "https://vimeo362227-8.onrender.com",
    "https://vimeo362227-10.onrender.com",
    "https://vimeo362227-12.onrender.com",
    "https://vimeo362227-14.onrender.com",
    "https://vimeo362227-16.onrender.com",
    "https://vimeo362227-18.onrender.com",
    "https://vimeo362227-20.onrender.com",
    "https://vimeo362227-22.onrender.com",
    "https://vimeo362227-24.onrender.com",
    "https://vimeo362227-26.onrender.com",
    "https://vimeo362227-28.onrender.com",
    "https://vimeo362227-30.onrender.com",
    "https://vimeo362227-32.onrender.com",
    "https://vimeo362227-34.onrender.com",
    "https://vimeo362227-36.onrender.com",
    "https://vimeo362227-38.onrender.com",
    "https://vimeo362227-40.onrender.com",
    "https://vimeo362227-42.onrender.com",
    "https://vimeo362227-44.onrender.com",
    "https://vimeo362227-46.onrender.com",
    "https://vimeo362227-48.onrender.com",
    "https://vimeo362227-50.onrender.com",
    "https://vimeo362227-52.onrender.com",
    "https://vimeo362227-54.onrender.com",
    "https://vimeo362227-56.onrender.com",
    "https://vimeo362227-58.onrender.com",
    "https://vimeo362227-60.onrender.com",
    "https://vimeo362227-62.onrender.com",
    "https://vimeo362227-64.onrender.com",
    "https://vimeo362227-66.onrender.com",
    "https://vimeo362227-68.onrender.com",
    "https://vimeo362227-70.onrender.com",
    "https://vimeo362227-72.onrender.com",
    "https://vimeo10362227-2.onrender.com",  
    "https://vimeo10362227-4.onrender.com",  
    "https://vimeo10362227-6.onrender.com",  
    "https://vimeo10362227-8.onrender.com",
    "https://vimeo10362227-10.onrender.com",  
    "https://vimeo10362227-12.onrender.com", 
    "https://vimeo10362227-14.onrender.com",  
    "https://vimeo10362227-16.onrender.com",  
    "https://vimeo10362227-18.onrender.com",  
    "https://vimeo10362227-20.onrender.com",  
    "https://vimeo10362227-22.onrender.com", 
    "https://vimeo10362227-24.onrender.com",  
    "https://vimeo10362227-26.onrender.com",  
    "https://vimeo10362227-28.onrender.com",  
    "https://vimeo10362227-30.onrender.com",  
    "https://vimeo10362227-32.onrender.com", 
    "https://vimeo10362227-34.onrender.com",  
    "https://vimeo10362227-36.onrender.com",  
    "https://vimeo10362227-38.onrender.com",  
    "https://vimeo10362227-40.onrender.com",  
    "https://vimeo10362227-42.onrender.com", 
    "https://vimeo10362227-44.onrender.com",  
    "https://vimeo10362227-46.onrender.com",  
    "https://vimeo10362227-48.onrender.com",  
    "https://vimeo10362227-50.onrender.com",  
    "https://vimeo10362227-52.onrender.com", 
    "https://vimeo10362227-54.onrender.com",  
    "https://vimeo10362227-56.onrender.com",  
    "https://vimeo10362227-58.onrender.com",  
    "https://vimeo10362227-60.onrender.com",  
    "https://vimeo10362227-62.onrender.com",  
    "https://vimeo10362227-64.onrender.com",  
    "https://vimeo10362227-66.onrender.com",  
    "https://vimeo10362227-68.onrender.com",  
    "https://vimeo10362227-70.onrender.com",
    "https://vimeo10362227-72.onrender.com",
    "https://vimeo10362227-74.onrender.com",

    
    "https://ellie002.onrender.com",
    "https://ellie004.onrender.com",
    "https://ellie006.onrender.com",
    "https://ellie008.onrender.com",
    "https://ellie010.onrender.com",
    "https://ellie012.onrender.com",
    "https://ellie014.onrender.com",
    "https://ellie016.onrender.com",
    "https://ellie018.onrender.com",
    "https://ellie020.onrender.com",
    "https://ellie022.onrender.com",
    "https://ellie024.onrender.com",
    "https://ellie026.onrender.com",
    "https://ellie028.onrender.com",
    "https://ellie030.onrender.com",
    "https://ellie032.onrender.com",
    "https://ellie034.onrender.com",
    "https://ellie036.onrender.com",
    "https://ellie038.onrender.com",
    "https://ellie040.onrender.com",
    "https://ellie042.onrender.com",
    "https://ellie044.onrender.com",
    "https://ellie046.onrender.com",
    "https://ellie048.onrender.com",
    "https://ellie050.onrender.com",
    "https://ellie052.onrender.com",
    "https://ellie054.onrender.com",
    "https://ellie056.onrender.com",
    "https://ellie058.onrender.com",
    "https://ellie060.onrender.com",
    "https://ellie062.onrender.com",
    "https://ellie064.onrender.com",
    "https://ellie066.onrender.com",
    "https://ellie068.onrender.com",
    "https://ellie070.onrender.com",
    "https://ellie072.onrender.com",
    "https://ellie074.onrender.com",
    "https://ellie076.onrender.com",  
    "https://ellie078.onrender.com",  
    "https://ellie080.onrender.com",  
    "https://ellie082.onrender.com",  
    "https://ellie084.onrender.com",  
    "https://ellie086.onrender.com",  
    "https://ellie088.onrender.com",  
    "https://ellie090.onrender.com",  
    "https://ellie092.onrender.com",  
    "https://ellie094.onrender.com",  
    "https://ellie096.onrender.com",  
    "https://ellie098.onrender.com",  
    "https://ellie100.onrender.com",  
    "https://ellie102.onrender.com",
    "https://ellie104.onrender.com",
    "https://kai006.onrender.com",
]
'''


'''
urls = [
        "https://vimeo362227.onrender.com",
    "https://vimeo362227-1.onrender.com",
    "https://vimeo362227-2.onrender.com",
    "https://vimeo362227-3.onrender.com",
    "https://vimeo362227-4.onrender.com",
    "https://vimeo362227-5.onrender.com",
    "https://vimeo362227-6.onrender.com",
    "https://vimeo362227-7.onrender.com",
    "https://vimeo362227-8.onrender.com",
    "https://vimeo362227-9.onrender.com",
    "https://vimeo362227-10.onrender.com",
    "https://vimeo362227-11.onrender.com",
    "https://vimeo362227-12.onrender.com",
    "https://vimeo362227-13.onrender.com",
    "https://vimeo362227-14.onrender.com",
    "https://vimeo362227-15.onrender.com",
    "https://vimeo362227-16.onrender.com",
    "https://vimeo362227-17.onrender.com",
    "https://vimeo362227-18.onrender.com",
    "https://vimeo362227-19-7hgu.onrender.com",
    "https://vimeo362227-20.onrender.com",
    "https://vimeo362227-21.onrender.com",
    "https://vimeo362227-22.onrender.com",
    "https://vimeo362227-23.onrender.com",
    "https://vimeo362227-24.onrender.com",
    "https://vimeo362227-25.onrender.com",
    "https://vimeo362227-26.onrender.com",
    "https://vimeo362227-27.onrender.com",
    "https://vimeo362227-28.onrender.com",
    "https://vimeo362227-29.onrender.com",
    "https://vimeo362227-30.onrender.com",
    "https://vimeo362227-31.onrender.com",
    "https://vimeo362227-32.onrender.com",
    "https://vimeo362227-33.onrender.com",
    "https://vimeo362227-34.onrender.com",
    "https://vimeo362227-35.onrender.com",
    "https://vimeo362227-36.onrender.com",
    "https://vimeo362227-37.onrender.com",
    "https://vimeo362227-38.onrender.com",
    "https://vimeo362227-39.onrender.com",
    "https://vimeo362227-40.onrender.com",
    "https://vimeo362227-41.onrender.com",
    "https://vimeo362227-42.onrender.com",
    "https://vimeo362227-43.onrender.com",
    "https://vimeo362227-44.onrender.com",
    "https://vimeo362227-45.onrender.com",
    "https://vimeo362227-46.onrender.com",
    "https://vimeo362227-47.onrender.com",
    "https://vimeo362227-48.onrender.com",
    "https://vimeo362227-49.onrender.com",
    "https://vimeo362227-50.onrender.com",
    "https://vimeo362227-51.onrender.com",
    "https://vimeo362227-52.onrender.com",
    "https://vimeo362227-53.onrender.com"
    "https://ellie001.onrender.com",
    "https://ellie002.onrender.com",
    "https://ellie003.onrender.com",
    "https://ellie004.onrender.com",
    "https://ellie006.onrender.com",
    "https://ellie005.onrender.com",
    "https://ellie010.onrender.com",
    "https://ellie007.onrender.com",
    "https://ellie008.onrender.com",
    "https://ellie009.onrender.com",
    "https://kai005.onrender.com",
    "https://kai006.onrender.com"
    
    "https://bcxdxrdqx-manyapps-001.onrender.com",
    "https://bcxdxrdqx-manyapps-002.onrender.com",
    "https://bcxdxrdqx-manyapps-003.onrender.com",
    "https://bcxdxrdqx-manyapps-004.onrender.com",
    "https://bcxdxrdqx-manyapps-005.onrender.com",
    "https://bcxdxrdqx-manyapps-006.onrender.com",
    "https://bcxdxrdqx-manyapps-007.onrender.com",
    "https://bcxdxrdqx-manyapps-008.onrender.com",
    "https://bcxdxrdqx-manyapps-009.onrender.com",
    "https://bcxdxrdqx-manyapps-010.onrender.com",
    "https://bcxdxrdqx-manyapps-011.onrender.com",
    "https://bcxdxrdqx-manyapps-012.onrender.com",
    "https://bcxdxrdqx-manyapps-013.onrender.com",
    "https://bcxdxrdqx-manyapps-014.onrender.com",
    "https://bcxdxrdqx-manyapps-015.onrender.com",
    "https://bcxdxrdqx-manyapps-016.onrender.com",
    "https://bcxdxrdqx-manyapps-017.onrender.com",
    "https://bcxdxrdqx-manyapps-018.onrender.com",
    "https://bcxdxrdqx-manyapps-019.onrender.com",
    "https://bcxdxrdqx-manyapps-020.onrender.com",  
    
    "https://uflulnjoaurhdhk-manyapps-001.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-002.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-003.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-004.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-005.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-006.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-007.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-008.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-009.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-010.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-011.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-012.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-013.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-014.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-015.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-016.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-017.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-018.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-019.onrender.com",
    "https://uflulnjoaurhdhk-manyapps-020.onrender.com",  
    
    "https://kobpiwpwprfnj-manyapps-001.onrender.com",
    "https://kobpiwpwprfnj-manyapps-002.onrender.com",
    "https://kobpiwpwprfnj-manyapps-003.onrender.com",
    "https://kobpiwpwprfnj-manyapps-004.onrender.com",
    "https://kobpiwpwprfnj-manyapps-005.onrender.com",
    "https://kobpiwpwprfnj-manyapps-006.onrender.com",
    "https://kobpiwpwprfnj-manyapps-007.onrender.com",
    "https://kobpiwpwprfnj-manyapps-008.onrender.com",
    "https://kobpiwpwprfnj-manyapps-009.onrender.com",
    
    "https://resignation1-manyapps-001.onrender.com",
    "https://resignation1-manyapps-002.onrender.com",
    "https://resignation1-manyapps-003.onrender.com",
    "https://resignation1-manyapps-004.onrender.com",
    "https://resignation1-manyapps-005.onrender.com",
    "https://resignation1-manyapps-006.onrender.com",
    "https://resignation1-manyapps-007.onrender.com",
    "https://resignation1-manyapps-008.onrender.com",
    "https://resignation1-manyapps-009.onrender.com",
    "https://resignation1-manyapps-010.onrender.com",
    "https://resignation1-manyapps-011.onrender.com",
    "https://resignation1-manyapps-012.onrender.com",
    "https://resignation1-manyapps-013.onrender.com",
    "https://resignation1-manyapps-014.onrender.com",
    "https://resignation1-manyapps-015.onrender.com",
    "https://resignation1-manyapps-016.onrender.com",
    "https://resignation1-manyapps-017.onrender.com",
    "https://resignation1-manyapps-018.onrender.com",
    "https://resignation1-manyapps-019.onrender.com",
    "https://resignation1-manyapps-020.onrender.com",
]
'''

while True:
    # 记录成功的链接
    successful_urls = []

    def request_url(url):
        retry = 0
        while True:
            try:
                response = requests.get(url, timeout=15)
                if response.status_code == 200:
                    print(f'{url} returned 200')
                    successful_urls.append(url)
                    return None  # 返回None表示成功
                else:
                    print(f'{url} returned {response.status_code}')
                    if retry < 5:
                        retry += 1
                        print(f'{url} retrying {retry}/5')
                    else:
                        break
            except requests.exceptions.RequestException as e:
                print(f'{url} failed: {e}')
                if retry < 6:
                    retry += 1
                    print(f'{url} retrying {retry}/6')
                else:
                    break
            time.sleep(1)  # 等待1秒后重试

    # 使用线程池并发请求
    with ThreadPoolExecutor(max_workers=80) as executor:
        futures = [executor.submit(request_url, url) for url in urls]
        # 等待所有请求完成
        for _ in as_completed(futures):
            pass

    # 将成功的链接写入文件
    if len(successful_urls) >= 90:
        with open('/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/urls.txt', 'w') as f:
            for url in successful_urls:
                f.write(url + '\n')
    else:
        print('Successful URLs less than 40, skipped writing to file.')

    # 如果所有链接都成功，则退出循环
    if set(successful_urls) == set(urls):
        print("All URLs succeeded!")
        break

    # 休眠一段时间后再次尝试
    print("一轮结束")
    print(len(successful_urls))
    time.sleep(5)
    os.system('clear')

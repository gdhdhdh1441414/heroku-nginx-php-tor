import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# 代理
proxy = {'http': 'http://127.0.0.1:1086', 'https': 'http://127.0.0.1:1086'}

# 需要尝试的链接列表


urls = [
    "https://kacey1--doyathing9.无效2023-05-18.co",
    "https://myphp-1.vercel.app/api",
    "https://myphp-2.vercel.app/api",
    "https://myphp-3.vercel.app/api",
    "https://myphp-4.vercel.app/api",
    "https://myphp-5.vercel.app/api",
    "https://myphp-6.vercel.app/api",
    "https://myphp-7.vercel.app/api",
    "https://myphp-8.vercel.app/api",
    "https://myphp-9.vercel.app/api",
    "https://myphp-10.vercel.app/api",
    "https://myphp-11.vercel.app/api",
    "https://myphp-12.vercel.app/api",
    "https://myphp-13.vercel.app/api",
    "https://myphp-14.vercel.app/api",
    "https://myphp-15.vercel.app/api",
    "https://myphp-16.vercel.app/api",
    "https://myphp-17.vercel.app/api",
    "https://myphp-18.vercel.app/api",
    "https://myphp-19.vercel.app/api",
    "https://myphp-20.vercel.app/api",
    "https://myphp-21.vercel.app/api",
    "https://myphp-22.vercel.app/api",
    "https://myphp-23.vercel.app/api",
    "https://myphp-24.vercel.app/api",
    "https://myphp-25.vercel.app/api",
    "https://myphp-26.vercel.app/api",
    "https://myphp-27.vercel.app/api",
    "https://myphp-28.vercel.app/api",
    "https://myphp-29.vercel.app/api",
    "https://myphp-30.vercel.app/api",
    "https://myphp-31.vercel.app/api",
    "https://myphp-32.vercel.app/api",
    "https://myphp-33.vercel.app/api",
    "https://myphp-34.vercel.app/api",
    "https://myphp-35.vercel.app/api",
    "https://myphp-36.vercel.app/api",
    "https://myphp-37.vercel.app/api",
    "https://myphp-38.vercel.app/api",
    "https://myphp-39.vercel.app/api",
    "https://myphp-40.vercel.app/api",
    "https://myphp-41.vercel.app/api",
    "https://myphp-42.vercel.app/api",
    "https://myphp-43.vercel.app/api",
    "https://myphp-44.vercel.app/api",
    "https://myphp-45.vercel.app/api",
    "https://myphp-46.vercel.app/api",
    "https://myphp-47.vercel.app/api",
    "https://myphp-48.vercel.app/api",
    "https://myphp-49.vercel.app/api",
    "https://myphp-50.vercel.app/api",
    "https://myphp-51.vercel.app/api",
    "https://myphp-52.vercel.app/api",
    "https://myphp-53.vercel.app/api",
    "https://myphp-54.vercel.app/api",
    "https://myphp-55.vercel.app/api",
    "https://myphp-56.vercel.app/api",
    "https://myphp-57.vercel.app/api",
    "https://myphp-58.vercel.app/api",
    "https://myphp-59.vercel.app/api",
    "https://myphp-60.vercel.app/api",
] 




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
                response = requests.get(url, timeout=10)
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
                if retry < 3:
                    retry += 1
                    print(f'{url} retrying {retry}/3')
                else:
                    break
            time.sleep(1)  # 等待1秒后重试

    # 使用线程池并发请求
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(request_url, url) for url in urls]
        # 等待所有请求完成
        for _ in as_completed(futures):
            pass

    # 将成功的链接写入文件
    if len(successful_urls) >= 50:
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

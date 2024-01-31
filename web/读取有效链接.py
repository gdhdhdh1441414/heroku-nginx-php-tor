import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# 代理
proxy = {'http': 'http://127.0.0.1:1086', 'https': 'http://127.0.0.1:1086'}

# 需要尝试的链接列表


urls = [
    "https://github.c/qodnh/?这是无效链接，让这个代码能无限循环", 
    "https://dc328d28-ef61-4e36-9b6d-040bb1384e09-00-3bjxvzmdvu0yu.sisko.replit.dev",
    "https://0c92fe09-72ff-45c1-9fa4-e5b4e51ad53c-00-11vqtgma08u4p.pike.replit.dev",
    "https://109ef66c-c2f0-4345-8d15-47333a179e2e-00-1q1wc7w4fmtnq.sisko.replit.dev",
    "https://1616325f-23ff-469e-ba6a-1227e6bc9155-00-14uiu4b8ug72l.sisko.replit.dev",
    "https://b2a7c1ca-37cc-4f02-9656-8bd00e662f3f-00-39r5sxr4czym3.pike.replit.dev",
    "https://b9dc0bd1-a377-4b49-b51f-0ee53c458d30-00-3cko837imdl1x.pike.replit.dev", #006
    "https://418d13b4-66ab-447d-bc84-2f55955eb0a0-00-1ansofx0xaop3.pike.replit.dev",
    "https://0cd68126-a42c-4462-98f0-0772bdf5a633-00-3evk3tcly5ul6.pike.replit.dev",
    "https://690a829d-6ec1-4398-9135-74d6a47797fb-00-erbdketagsxu.sisko.replit.dev",
    "https://08dfa419-1e33-4304-8090-34b45898e918-00-2o5pwozmgmibl.sisko.replit.dev",
    "https://00b71873-f31d-4ff3-a533-b970877f66bd-00-20msvcz8kwyrm.sisko.replit.dev",
    "https://38aa1ced-6fc4-4ccd-9697-449adc179fb4-00-2p9u0tpa20m71.pike.replit.dev",
    "https://e8319eba-7220-46ed-81d7-313ccc7d23fe-00-39xx0i6na1qko.sisko.replit.dev",#013
    "https://b496a42e-7303-4bc9-a41c-f9c3a0f0913d-00-36q04rcb2dpkd.pike.replit.dev",
    "https://4b54585b-93ce-40b8-8ed8-8409e6149bc1-00-3j3qa2bkxrh4j.sisko.replit.dev",
    "https://b55c4990-91b9-4bb6-9ccc-bd6acf8f53f7-00-vtxwj8iqzz0q.sisko.replit.dev",
    "https://8d842128-c9db-4034-8b6d-8a8bdc676b24-00-13vvnzhxh71ud.sisko.replit.dev",
    "https://231e043d-ccc3-4745-844a-6733c2eccc6d-00-1su3n6wokv5ak.pike.replit.dev",#018
    "https://afa0dbe6-1f87-4ced-97c0-31b27b86a0b2-00-1z8q9znnltnxt.sisko.replit.dev",
    "https://1693b230-6c1c-4abb-873b-681269e2e5e0-00-y9eg92ccex2f.pike.replit.dev",
    "https://07e19ba9-4e6d-40d5-b647-0f391428a575-00-ercu3jo9g8f1.pike.replit.dev",
    "https://f106af53-2531-49b6-8c90-521bf1a18853-00-26wmhdpq6zt0i.sisko.replit.dev",
    "https://1c436fd2-3624-4525-a509-49a89ce4a9c4-00-3nrfmwzoxfmrq.pike.replit.dev",#023
    "https://cf03483d-d2b1-4ebf-986c-2767b0c3c7eb-00-14ctda071g6ad.sisko.replit.dev",
    "https://255a6db3-a8a4-4dd0-a953-312169949915-00-jmjpzqdv28nd.pike.replit.dev",
    "https://d43a954d-fd50-457a-8473-e423ba3d4c2c-00-zyqdwth8kk6.pike.replit.dev",
    "https://43e20eae-ab31-41ab-991e-c1106f24b54d-00-ynmabhl3gjo.pike.replit.dev",
    "https://77eb5890-9946-48c3-806c-46e1e27dfaab-00-1zpl3age3m5sp.pike.replit.dev",
    "https://ad6c04b6-1479-4b5f-963a-f60253ef3980-00-2f0g7gw5k3gwi.sisko.replit.dev",
    "https://74262e29-cc16-4ca5-b5bc-5e1afbb9c8b9-00-japykm2itjzc.sisko.replit.dev",#030
    "https://82ddcbd3-ca03-4574-918e-834b79c19127-00-38mj9ak3ufhom.sisko.replit.dev",
    "https://74bc2e10-bdbe-4ef5-baec-51d41de85b02-00-o2l87ogck6u3.pike.replit.dev",
    "https://94493377-bf60-4eae-bb81-18c662a6c66e-00-ovuwf0ynm6x0.sisko.replit.dev",
    "https://f0116cf2-57a6-4cbb-bca5-fcb161df1f07-00-12gn9j5l4vhjg.sisko.replit.dev",
    "https://9e1ada2e-1c89-471e-b2f3-44d700f76eae-00-3gkkwlcxqi2wi.sisko.replit.dev",
    "https://7f257882-c08d-46d0-8c65-59e48b271c2a-00-sxkjvtx0ldpg.sisko.replit.dev",
    "https://886342c9-809a-44f4-b627-5b44744c5774-00-s6rxlwg1co7l.pike.replit.dev",
    "https://fd12ff2d-911c-4dd8-b0b7-264a7dc06137-00-1hh6ian5f4qb0.sisko.replit.dev",#038
    "https://4be13f6b-1923-4ca7-aef8-bbd4d5717a71-00-99hxh2b30yne.pike.replit.dev",
    "https://92b77251-e799-46bf-8438-fd3a9b8eb7c8-00-37sr0bqh54c40.sisko.replit.dev",
    "https://c5ebb141-8e53-477a-80b5-46012df5979b-00-2ulvmp1cyz8u2.pike.replit.dev",
    "https://8c1a8276-6915-444b-a223-086c46d845fe-00-kquanb6x6pz2.pike.replit.dev",
    "https://fbd75ad1-19ab-4877-938c-3fe37fe77991-00-1ntg9fb4g776r.pike.replit.dev",#043
    "https://7a470919-70e9-410a-8a0d-009b9817629e-00-2q5b4ls9jbs2.sisko.replit.dev",
    "https://e73222d9-fe37-441c-8a2a-93f14e667728-00-86bpv28xqlp2.sisko.replit.dev",
    "https://ac92980d-c108-4c15-a57f-975cb735d561-00-2skxdgfg02wwc.pike.replit.dev",
    "https://52e33c71-b6e1-4333-85e3-bc3613a5ae71-00-2u8vt4874b5tp.pike.replit.dev",
    "https://d4bdb13d-7c0f-42a3-8a76-8e21c37fca77-00-2xo7j1dl3t00i.sisko.replit.dev",
    "https://47e2c0e3-d67d-4fc7-9276-452dfdbdcdc0-00-2jpr4qzyapfch.sisko.replit.dev",
    "https://a0210401-a79c-43eb-8b96-973cb8264393-00-n6tr9w4b4imv.sisko.replit.dev",
    "https://84090fe1-db7c-4a13-8f5c-9064e7f37d98-00-1n0ic1yhtuamw.pike.replit.dev",
    "https://df700d70-2873-45ea-a5a2-43b141a5fbef-00-2qvx347i6sqgb.sisko.replit.dev",
    "https://ad9de448-2c00-48c9-9d18-801951026f74-00-3h4uffaizpbj7.pike.replit.dev",
    "https://5fcc8131-aa62-4fe9-8ea8-427bf886ee9b-00-13k28kaqc4wbm.pike.replit.dev",
    "https://ffb4ee7d-4ccf-4551-ab55-9beeace4ae18-00-14xz8nzizagjs.sisko.replit.dev",
    "https://02395bbf-2ec0-4663-bcac-21371bbbde4e-00-33agsp9xk0ki2.sisko.replit.dev",
    "https://3aeaeacd-75a5-41d4-b284-2a6ce9532258-00-3a3dpmi3nz8gm.pike.replit.dev",
    "https://970b7467-0034-4c12-b4ef-3a80cc17def1-00-ppst0nwxdkvg.sisko.replit.dev",
    "https://b85a4b15-bd26-4871-a0fe-17fd45749c3b-00-1h4tapl0ly681.sisko.replit.dev",
    "https://2ebb2256-09aa-4ade-b34f-00f7da59651a-00-1vx9xpjp4v0fc.sisko.replit.dev",
    "https://bf0e4cfe-1412-4246-a15f-ed2dd05ed6ef-00-3rwath7ly5rec.pike.replit.dev",
    "https://494c2801-4c96-4b69-bf3a-44f09a6bd92a-00-229gfxo49bm49.pike.replit.dev",
    "https://2cfac56c-b1b6-49e9-bf01-df12d00a5c65-00-9jr52li7jj76.sisko.replit.dev",
   
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

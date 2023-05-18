import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


# 代理
proxy = {'http': 'http://127.0.0.1:1083', 'https': 'http://127.0.0.1:1083'}

urls = [
    "https://kacey1--doyathing9.repl.co",
    "https://kacey2--doyathing9.repl.co",
    "https://kacey3--doyathing9.repl.co",
    "https://kacey4--doyathing9.repl.co",
    "https://kacey5--doyathing9.repl.co",
    "https://kacey6--doyathing9.repl.co",
    "https://gulley1--doyathing10.repl.co",
    "https://gulley2--doyathing10.repl.co",
    "https://gulley3--doyathing10.repl.co",
    "https://gulley4--doyathing10.repl.co",
    "https://gulley5--doyathing10.repl.co",
    "https://gulley5--doyathing10.repl.co",
    "https://gulley6--doyathing10.repl.co",
    "https://gyh1--doyathing20.repl.co",
    "https://gyh2--doyathing20.repl.co",
    "https://gyh3--doyathing20.repl.co",
    "https://gyh4--doyathing20.repl.co",
    "https://ghy5--doyathing20.repl.co",
    "https://gyh5--doyathing20.repl.co",
    "https://gyh6--doyathing20.repl.co",
    "https://webb1--doyathing22.repl.co",
    "https://webb2--doyathing22.repl.co",
    "https://webb3--doyathing22.repl.co",
    "https://webb4--doyathing22.repl.co",
    "https://webb5--doyathing22.repl.co",
    "https://webb6--doyathing22.repl.co",
    "https://sgst1--doyathing23.repl.co",
    "https://sgst2--doyathing23.repl.co",
    "https://sgst3--doyathing23.repl.co",
    "https://sgst4--doyathing23.repl.co",
    "https://sgst5--doyathing23.repl.co",
    "https://sgst6--doyathing23.repl.co",
    "https://guy1--goodya75.repl.co",
    "https://guy2--goodya75.repl.co",
    "https://guy3--goodya75.repl.co",
    "https://guy4--goodya75.repl.co",
    "https://guy5--goodya75.repl.co",
    "https://guy6--goodya75.repl.co",
    "https://crisp1--doyathing33.repl.co",
    "https://crisp2--doyathing33.repl.co",
    "https://crisp3--doyathing33.repl.co",
    "https://crisp4--doyathing33.repl.co",
    "https://crisp5--doyathing33.repl.co",
    "https://crisp6--doyathing33.repl.co",
    "https://crisp7--doyathing33.repl.co",
    "https://crisp8--doyathing33.repl.co",
    "https://crisp9--doyathing33.repl.co",
    "https://crisp10--doyathing33.repl.co",
    "https://phps1--doyathing44.repl.co",
    "https://phps2--doyathing44.repl.co",
    "https://phps3--doyathing44.repl.co",
    "https://phps4--doyathing44.repl.co",
    "https://phps5--doyathing44.repl.co",
    "https://phps6--doyathing44.repl.co",
    "https://phps7--doyathing44.repl.co",
    "https://phps8--doyathing44.repl.co",
    "https://phps9--doyathing44.repl.co",
    "https://phps10--doyathing44.repl.co",
    "https://phps1--doyathing44.repl.co",
    "https://phps2--doyathing44.repl.co",
    "https://phps3--doyathing44.repl.co",
    "https://phps4--doyathing44.repl.co",
    "https://phps5--doyathing44.repl.co",
    "https://phps6--doyathing44.repl.co",
    "https://phps7--doyathing44.repl.co",
    "https://phps8--doyathing44.repl.co",
    "https://phps9--doyathing44.repl.co",
    "https://phps10--doyathing44.repl.co",
    "https://crisp1--doyathing33.repl.co",
    "https://crisp2--doyathing33.repl.co",
    "https://crisp3--doyathing33.repl.co",
    "https://crisp4--doyathing33.repl.co",
    "https://crisp5--doyathing33.repl.co",
    "https://crisp6--doyathing33.repl.co",
    "https://crisp7--doyathing33.repl.co",
    "https://crisp8--doyathing33.repl.co",
    "https://crisp9--doyathing33.repl.co",
    "https://crisp10--doyathing33.repl.co",
    
    
    "https://txfzubvpwz-1--txfzubvpwz.repl.co",
    "https://txfzubvpwz-2--txfzubvpwz.repl.co",
    "https://txfzubvpwz-3--txfzubvpwz.repl.co",
    "https://txfzubvpwz-4--txfzubvpwz.repl.co",
    "https://txfzubvpwz-5--txfzubvpwz.repl.co",
    "https://txfzubvpwz-6--txfzubvpwz.repl.co",  
    "https://txfzubvpwz-7--txfzubvpwz.repl.co",
    "https://txfzubvpwz-8--txfzubvpwz.repl.co",
    "https://txfzubvpwz-9--txfzubvpwz.repl.co",
    "https://txfzubvpwz-10--txfzubvpwz.repl.co",  
    "https://wvqxkfyg-1--wvqxkfyg.repl.co",
    "https://wvqxkfyg-2--wvqxkfyg.repl.co",
    "https://wvqxkfyg-3--wvqxkfyg.repl.co",
    "https://wvqxkfyg-4--wvqxkfyg.repl.co",
    "https://wvqxkfyg-5--wvqxkfyg.repl.co",
    "https://wvqxkfyg-6--wvqxkfyg.repl.co",  
    "https://wvqxkfyg-7--wvqxkfyg.repl.co",
    "https://wvqxkfyg-8--wvqxkfyg.repl.co",
    "https://wvqxkfyg-9--wvqxkfyg.repl.co",
    "https://wvqxkfyg-10--wvqxkfyg.repl.co",  
    "https://tsvkmwzpgcn-1--tsvkmwzpgcn.repl.co",
    "https://tsvkmwzpgcn-2--tsvkmwzpgcn.repl.co",
    "https://tsvkmwzpgcn-3--tsvkmwzpgcn.repl.co",
    "https://tsvkmwzpgcn-4--tsvkmwzpgcn.repl.co",
    "https://tsvkmwzpgcn-5--tsvkmwzpgcn.repl.co",
    "https://tsvkmwzpgcn-6--tsvkmwzpgcn.repl.co",  
    "https://tsvkmwzpgcn-7--tsvkmwzpgcn.repl.co",
    "https://tsvkmwzpgcn-8--tsvkmwzpgcn.repl.co",
    "https://tsvkmwzpgcn-9--tsvkmwzpgcn.repl.co",
    "https://tsvkmwzpgcn-10--tsvkmwzpgcn.repl.co", 
    "https://sezuipdjrcjq-1--sezuipdjrcjq.repl.co",
    "https://sezuipdjrcjq-2--sezuipdjrcjq.repl.co",
    "https://sezuipdjrcjq-3--sezuipdjrcjq.repl.co",
    "https://sezuipdjrcjq-4--sezuipdjrcjq.repl.co",
    "https://sezuipdjrcjq-5--sezuipdjrcjq.repl.co",
    "https://sezuipdjrcjq-6--sezuipdjrcjq.repl.co",  
    "https://sezuipdjrcjq-7--sezuipdjrcjq.repl.co",
    "https://sezuipdjrcjq-8--sezuipdjrcjq.repl.co",
    "https://sezuipdjrcjq-9--sezuipdjrcjq.repl.co",
    "https://sezuipdjrcjq-10--sezuipdjrcjq.repl.co",  
    "https://voscmor-1--voscmor.repl.co",
    "https://voscmor-2--voscmor.repl.co",
    "https://voscmor-3--voscmor.repl.co",
    "https://voscmor-4--voscmor.repl.co",
    "https://voscmor-5--voscmor.repl.co",
    "https://voscmor-6--voscmor.repl.co",  
    "https://voscmor-7--voscmor.repl.co",
    "https://voscmor-8--voscmor.repl.co",
    "https://voscmor-9--voscmor.repl.co",
    "https://voscmor-10--voscmor.repl.co",
    "https://eegznavcufl-1--eegznavcufl.repl.co",
    "https://eegznavcufl-2--eegznavcufl.repl.co",
    "https://eegznavcufl-3--eegznavcufl.repl.co",
    "https://eegznavcufl-4--eegznavcufl.repl.co",
    "https://eegznavcufl-5--eegznavcufl.repl.co",
    "https://eegznavcufl-6--eegznavcufl.repl.co",  
    "https://eegznavcufl-7--eegznavcufl.repl.co",
    "https://eegznavcufl-8--eegznavcufl.repl.co",
    "https://eegznavcufl-9--eegznavcufl.repl.co",
    "https://eegznavcufl-10--eegznavcufl.repl.co",  
    "https://pzgttatm-1--pzgttatm.repl.co",
    "https://pzgttatm-2--pzgttatm.repl.co",
    "https://pzgttatm-3--pzgttatm.repl.co",
    "https://pzgttatm-4--pzgttatm.repl.co",
    "https://pzgttatm-5--pzgttatm.repl.co",
    "https://pzgttatm-6--pzgttatm.repl.co",  
    "https://pzgttatm-7--pzgttatm.repl.co",
    "https://pzgttatm-8--pzgttatm.repl.co",
    "https://pzgttatm-9--pzgttatm.repl.co",
    "https://pzgttatm-10--pzgttatm.repl.co",  
    "https://sawshqfud-1--sawshqfud.repl.co",
    "https://sawshqfud-2--sawshqfud.repl.co",
    "https://sawshqfud-3--sawshqfud.repl.co",
    "https://sawshqfud-4--sawshqfud.repl.co",
    "https://sawshqfud-5--sawshqfud.repl.co",
    "https://sawshqfud-6--sawshqfud.repl.co",  
    "https://sawshqfud-7--sawshqfud.repl.co",
    "https://sawshqfud-8--sawshqfud.repl.co",
    "https://sawshqfud-9--sawshqfud.repl.co",
    "https://sawshqfud-10--sawshqfud.repl.co",  
    "https://ffwzod-1--ffwzod.repl.co",
    "https://ffwzod-2--ffwzod.repl.co",
    "https://ffwzod-3--ffwzod.repl.co",
    "https://ffwzod-4--ffwzod.repl.co",
    "https://ffwzod-5--ffwzod.repl.co",
    "https://ffwzod-6--ffwzod.repl.co",  
    "https://ffwzod-7--ffwzod.repl.co",
    "https://ffwzod-8--ffwzod.repl.co",
    "https://ffwzod-9--ffwzod.repl.co",
    "https://ffwzod-10--ffwzod.repl.co", 
    "https://kobpiwpwprfnj-1--kobpiwpwprfnj.repl.co",
    "https://kobpiwpwprfnj-2--kobpiwpwprfnj.repl.co",
    "https://kobpiwpwprfnj-3--kobpiwpwprfnj.repl.co",
    "https://kobpiwpwprfnj-4--kobpiwpwprfnj.repl.co",
    "https://kobpiwpwprfnj-5--kobpiwpwprfnj.repl.co",
    "https://kobpiwpwprfnj-6--kobpiwpwprfnj.repl.co",  
    "https://kobpiwpwprfnj-7--kobpiwpwprfnj.repl.co",
    "https://kobpiwpwprfnj-8--kobpiwpwprfnj.repl.co",
    "https://kobpiwpwprfnj-9--kobpiwpwprfnj.repl.co",
    "https://kobpiwpwprfnj-10--kobpiwpwprfnj.repl.co",  
    "https://bcxdxrdqx-1--bcxdxrdqx.repl.co",
    "https://bcxdxrdqx-2--bcxdxrdqx.repl.co",
    "https://bcxdxrdqx-3--bcxdxrdqx.repl.co",
    "https://bcxdxrdqx-4--bcxdxrdqx.repl.co",
    "https://bcxdxrdqx-5--bcxdxrdqx.repl.co",
    "https://bcxdxrdqx-6--bcxdxrdqx.repl.co",  
    "https://bcxdxrdqx-7--bcxdxrdqx.repl.co",
    "https://bcxdxrdqx-8--bcxdxrdqx.repl.co",
    "https://bcxdxrdqx-9--bcxdxrdqx.repl.co",
    "https://bcxdxrdqx-10--bcxdxrdqx.repl.co",  
    "https://bnmiwztvf-1--bnmiwztvf.repl.co",
    "https://bnmiwztvf-2--bnmiwztvf.repl.co",
    "https://bnmiwztvf-3--bnmiwztvf.repl.co",
    "https://bnmiwztvf-4--bnmiwztvf.repl.co",
    "https://bnmiwztvf-5--bnmiwztvf.repl.co",
    "https://bnmiwztvf-6--bnmiwztvf.repl.co",  
    "https://bnmiwztvf-7--bnmiwztvf.repl.co",
    "https://bnmiwztvf-8--bnmiwztvf.repl.co",
    "https://bnmiwztvf-9--bnmiwztvf.repl.co",
    "https://bnmiwztvf-10--bnmiwztvf.repl.co", 
    "https://wlztanuig-1--wlztanuig.repl.co",
    "https://wlztanuig-2--wlztanuig.repl.co",
    "https://wlztanuig-3--wlztanuig.repl.co",
    "https://wlztanuig-4--wlztanuig.repl.co",
    "https://wlztanuig-5--wlztanuig.repl.co",
    "https://wlztanuig-6--wlztanuig.repl.co",  
    "https://wlztanuig-7--wlztanuig.repl.co",
    "https://wlztanuig-8--wlztanuig.repl.co",
    "https://wlztanuig-9--wlztanuig.repl.co",
    "https://wlztanuig-10--wlztanuig.repl.co", 
    "https://xidysgipbjx-1--xidysgipbjx.repl.co",
    "https://xidysgipbjx-2--xidysgipbjx.repl.co",
    "https://xidysgipbjx-3--xidysgipbjx.repl.co",
    "https://xidysgipbjx-4--xidysgipbjx.repl.co",
    "https://xidysgipbjx-5--xidysgipbjx.repl.co",
    "https://xidysgipbjx-6--xidysgipbjx.repl.co",  
    "https://xidysgipbjx-7--xidysgipbjx.repl.co",
    "https://xidysgipbjx-8--xidysgipbjx.repl.co",
    "https://xidysgipbjx-9--xidysgipbjx.repl.co",
    "https://xidysgipbjx-10--xidysgipbjx.repl.co",  
    "https://nngoku-1--nngoku.repl.co",
    "https://nngoku-2--nngoku.repl.co",
    "https://nngoku-3--nngoku.repl.co",
    "https://nngoku-4--nngoku.repl.co",
    "https://nngoku-5--nngoku.repl.co",
    "https://nngoku-6--nngoku.repl.co",  
    "https://nngoku-7--nngoku.repl.co",
    "https://nngoku-8--nngoku.repl.co",
    "https://nngoku-9--nngoku.repl.co",
    "https://nngoku-10--nngoku.repl.co",  
    "https://kkdrff-1--kkdrff.repl.co",
    "https://kkdrff-2--kkdrff.repl.co",
    "https://kkdrff-3--kkdrff.repl.co",
    "https://kkdrff-4--kkdrff.repl.co",
    "https://kkdrff-5--kkdrff.repl.co",
    "https://kkdrff-6--kkdrff.repl.co",  
    "https://rruwseukn-1--rruwseukn.repl.co",
    "https://rruwseukn-2--rruwseukn.repl.co",
    "https://rruwseukn-3--rruwseukn.repl.co",
    "https://rruwseukn-4--rruwseukn.repl.co",
    "https://rruwseukn-5--rruwseukn.repl.co",
    "https://rruwseukn-6--rruwseukn.repl.co",  
    "https://rruwseukn-7--rruwseukn.repl.co",
    "https://rruwseukn-8--rruwseukn.repl.co",
    "https://rruwseukn-9--rruwseukn.repl.co",
    "https://rruwseukn-10--rruwseukn.repl.co",  
    "https://aaabic-1--aaabic.repl.co",
    "https://aaabic-2--aaabic.repl.co",
    "https://aaabic-3--aaabic.repl.co",
    "https://aaabic-4--aaabic.repl.co",
    "https://aaabic-5--aaabic.repl.co",
    "https://aaabic-6--aaabic.repl.co",  
    "https://aaabic-7--aaabic.repl.co",
    "https://aaabic-8--aaabic.repl.co",
    "https://aaabic-9--aaabic.repl.co",
    "https://aaabic-10--aaabic.repl.co",
    "https://cqqnst-1--cqqnst.repl.co",
    "https://cqqnst-2--cqqnst.repl.co",
    "https://cqqnst-3--cqqnst.repl.co",
    "https://cqqnst-4--cqqnst.repl.co",
    "https://cqqnst-5--cqqnst.repl.co",
    "https://cqqnst-6--cqqnst.repl.co",  
    "https://cqqnst-7--cqqnst.repl.co",
    "https://cqqnst-8--cqqnst.repl.co",
    "https://cqqnst-9--cqqnst.repl.co",
    "https://cqqnst-10--cqqnst.repl.co", 
    "https://davbpjefsvwd-1--davbpjefsvwd.repl.co",
    "https://davbpjefsvwd-2--davbpjefsvwd.repl.co",
    "https://davbpjefsvwd-3--davbpjefsvwd.repl.co",
    "https://davbpjefsvwd-4--davbpjefsvwd.repl.co",
    "https://davbpjefsvwd-5--davbpjefsvwd.repl.co",
    "https://davbpjefsvwd-6--davbpjefsvwd.repl.co", 
    "https://davbpjefsvwd-7--davbpjefsvwd.repl.co",
    "https://davbpjefsvwd-8--davbpjefsvwd.repl.co",
    "https://davbpjefsvwd-9--davbpjefsvwd.repl.co",
    "https://davbpjefsvwd-10--davbpjefsvwd.repl.co", 
    "https://kiycea-1--kiycea.repl.co",
    "https://kiycea-2--kiycea.repl.co",
    "https://kiycea-3--kiycea.repl.co",
    "https://kiycea-4--kiycea.repl.co",
    "https://kiycea-5--kiycea.repl.co",
    "https://kiycea-6--kiycea.repl.co", 
    "https://kiycea-7--kiycea.repl.co",
    "https://kiycea-8--kiycea.repl.co",
    "https://kiycea-9--kiycea.repl.co",
    "https://kiycea-10--kiycea.repl.co", 
    "https://uajesopxvupgu-1--uajesopxvupgu.repl.co",
    "https://uajesopxvupgu-2--uajesopxvupgu.repl.co",
    "https://uajesopxvupgu-3--uajesopxvupgu.repl.co",
    "https://uajesopxvupgu-4--uajesopxvupgu.repl.co",
    "https://uajesopxvupgu-5--uajesopxvupgu.repl.co",
    "https://uajesopxvupgu-6--uajesopxvupgu.repl.co", 
    "https://uajesopxvupgu-7--uajesopxvupgu.repl.co",
    "https://uajesopxvupgu-8--uajesopxvupgu.repl.co",
    "https://uajesopxvupgu-9--uajesopxvupgu.repl.co",
    "https://uajesopxvupgu-10--uajesopxvupgu.repl.co", 
    "https://ihowwkwqztb-1--ihowwkwqztb.repl.co",
    "https://ihowwkwqztb-2--ihowwkwqztb.repl.co",
    "https://ihowwkwqztb-3--ihowwkwqztb.repl.co",
    "https://ihowwkwqztb-4--ihowwkwqztb.repl.co",
    "https://ihowwkwqztb-5--ihowwkwqztb.repl.co",
    "https://ihowwkwqztb-6--ihowwkwqztb.repl.co", 
    "https://envvcjqwbpat-1--envvcjqwbpat.repl.co",
    "https://envvcjqwbpat-2--envvcjqwbpat.repl.co",
    "https://envvcjqwbpat-3--envvcjqwbpat.repl.co",
    "https://envvcjqwbpat-4--envvcjqwbpat.repl.co",
    "https://envvcjqwbpat-5--envvcjqwbpat.repl.co",
    "https://envvcjqwbpat-6--envvcjqwbpat.repl.co", 

#分割线
    "https://replitt1.15651618096.无效.co",
    "https://replitt1.15651618096.repl.co",
    "https://replitt2.15651618096.repl.co",
    "https://replitt3.15651618096.repl.co",
    "https://replitt4.15651618096.repl.co",
    "https://replitt5.15651618096.repl.co",
    "https://replitt6.15651618096.repl.co",
    "https://hoola1.hellyahoola.repl.co",
    "https://hoola2.hellyahoola.repl.co",
    "https://hoola3.hellyahoola.repl.co",
    "https://hoola4.hellyahoola.repl.co",
    "https://hoola5.hellyahoola.repl.co",
    "https://hoola6.hellyahoola.repl.co",
    "https://kevin1.hoolahellya.repl.co",
    "https://kevin2.hoolahellya.repl.co",
    "https://kevin3.hoolahellya.repl.co",
    "https://kevin4.hoolahellya.repl.co",
    "https://kevin5.hoolahellya.repl.co",
    "https://kevin6.hoolahellya.repl.co",
    "https://killer1.hellyakiller.repl.co",
    "https://killer2.hellyakiller.repl.co",
    "https://killer3.hellyakiller.repl.co",
    "https://killer4.hellyakiller.repl.co",
    "https://killer5.hellyakiller.repl.co",
    "https://killer6.hellyakiller.repl.co",
    "https://hooray1.hoorayhuh.repl.co",
    "https://hooray2.hoorayhuh.repl.co",
    "https://hooray3.hoorayhuh.repl.co",
    "https://hooray4.hoorayhuh.repl.co",
    "https://hooray5.hoorayhuh.repl.co",
    "https://hooray6.hoorayhuh.repl.co",
    "https://rendeer1.yagoodyahell.repl.co",
    "https://rendeer2.yagoodyahell.repl.co",
    "https://rendeer3.yagoodyahell.repl.co",
    "https://rendeer4.yagoodyahell.repl.co",
    "https://rendeer5.yagoodyahell.repl.co",
    "https://rendeer6.yagoodyahell.repl.co",
    "https://amazoon1.goodyahellya.repl.co",
    "https://amazoon2.goodyahellya.repl.co",
    "https://amazoon3.goodyahellya.repl.co",
    "https://amazoon4.goodyahellya.repl.co",
    "https://amazoon5.goodyahellya.repl.co",
    "https://amazoon6.goodyahellya.repl.co",
    "https://yaheyyahey1.doyathing3.repl.co",
    "https://yaheyyahey2.doyathing3.repl.co",
    "https://yaheyyahey3.doyathing3.repl.co",
    "https://yaheyyahey4.doyathing3.repl.co",
    "https://yaheyyahey5.doyathing3.repl.co",
    "https://yaheyyahey6.doyathing3.repl.co",
    "https://felly1.goodya5678.repl.co",
    "https://felly2.goodya5678.repl.co",
    "https://felly3.goodya5678.repl.co",
    "https://felly4.goodya5678.repl.co",
    "https://felly5.goodya5678.repl.co",
    "https://felly6.goodya5678.repl.co",
    "https://jelly1.goodya3.repl.co",
    "https://jelly2.goodya3.repl.co",
    "https://jelly3.goodya3.repl.co",
    "https://jelly4.goodya3.repl.co",
    "https://jelly5.goodya3.repl.co",
    "https://jelly6.goodya3.repl.co",
    "https://helly1.doyathing2.repl.co",
    "https://helly2.doyathing2.repl.co",
    "https://helly3.doyathing2.repl.co",
    "https://helly4.doyathing2.repl.co",
    "https://helly5.doyathing2.repl.co",
    "https://helly6.doyathing2.repl.co",
    "https://ulley1.pistolwayne.repl.co",
    "https://ulley2.pistolwayne.repl.co",
    "https://ulley3.pistolwayne.repl.co",
    "https://ulley4.pistolwayne.repl.co",
    "https://ulley5.pistolwayne.repl.co",
    "https://ulley6.pistolwayne.repl.co",
    "https://wulley1.goodya1234.repl.co",
    "https://wulley2.goodya1234.repl.co",
    "https://wulley3.goodya1234.repl.co",
    "https://wulley4.goodya1234.repl.co",
    "https://wulley5.goodya1234.repl.co",
    "https://wulley6.goodya1234.repl.co",
    "https://shelly1.goodya4.repl.co",
    "https://shelly2.goodya4.repl.co",
    "https://shelly3.goodya4.repl.co",
    "https://shelly4.goodya4.repl.co",
    "https://shelly5.goodya4.repl.co",
    "https://shelly6.goodya4.repl.co",
    "https://kelly1.doyathing7.repl.co",
    "https://kelly2.doyathing7.repl.co",
    "https://kelly3.doyathing7.repl.co",
    "https://kelly4.doyathing7.repl.co",
    "https://kelly5.doyathing7.repl.co",
    "https://kelly6.doyathing7.repl.co",
    "https://hikitiki1.doyathing6.repl.co",
    "https://hikitiki2.doyathing6.repl.co",
    "https://hikitiki3.doyathing6.repl.co",
    "https://hikitiki4.doyathing6.repl.co",
    "https://hikitiki5.doyathing6.repl.co",
    "https://hikitiki6.doyathing6.repl.co",
    "https://felley1.doyathing7890.repl.co",
    "https://felley2.doyathing7890.repl.co",
    "https://felley3.doyathing7890.repl.co",
    "https://felley4.doyathing7890.repl.co",
    "https://felley5.doyathing7890.repl.co",
    "https://felley6.doyathing7890.repl.co",

    
    "https://google1.iyiyi.repl.co",
    "https://google2.iyiyi.repl.co",
    "https://google3.iyiyi.repl.co",
    "https://google4.iyiyi.repl.co",
    "https://google5.iyiyi.repl.co",
    "https://google6.iyiyi.repl.co",
    "https://google7.iyiyi.repl.co",
    "https://google8.iyiyi.repl.co",
    "https://google9.iyiyi.repl.co",
    "https://google10.iyiyi.repl.co",
    "https://362227github1.362227.repl.co",
    "https://362227github2.362227.repl.co",
    "https://362227github3.362227.repl.co",
    "https://362227github4.362227.repl.co",
    "https://362227github5.362227.repl.co",
    "https://362227github6.362227.repl.co",
    "https://362227github7.362227.repl.co",
    "https://362227github8.362227.repl.co",
    "https://362227github9.362227.repl.co",
    "https://362227github10.362227.repl.co",
    "https://10362227github1.10362227.repl.co",
    "https://10362227github2.10362227.repl.co",
    "https://10362227github3.10362227.repl.co",
    "https://10362227github4.10362227.repl.co",
    "https://10362227github5.10362227.repl.co",
    "https://10362227github6.10362227.repl.co",
    "https://10362227github7--10362227.repl.co",
    "https://10362227github8--10362227.repl.co",
    "https://10362227github9--10362227.repl.co",
    "https://10362227github10--10362227.repl.co",
    "https://gdhdhdh1441414github1.gdhdhdh1441414.repl.co",
    "https://gdhdhdh1441414github2.gdhdhdh1441414.repl.co",
    "https://gdhdhdh1441414github3.gdhdhdh1441414.repl.co",
    "https://gdhdhdh1441414github4.gdhdhdh1441414.repl.co",
    "https://gdhdhdh1441414github5.gdhdhdh1441414.repl.co",
    "https://gdhdhdh1441414github6.gdhdhdh1441414.repl.co",
    "https://gdhdhdh1441414github7--gdhdhdh1441414.repl.co",
    "https://gdhdhdh1441414github8--gdhdhdh1441414.repl.co",
    "https://gdhdhdh1441414github9--gdhdhdh1441414.repl.co",
    "https://gdhdhdh1441414github10--gdhdhdh1441414.repl.co",
    "https://tdlguwwlnj-1.tdlguwwlnj.repl.co",
    "https://tdlguwwlnj-2.tdlguwwlnj.repl.co",
    "https://tdlguwwlnj-3.tdlguwwlnj.repl.co",
    "https://tdlguwwlnj-4.tdlguwwlnj.repl.co",
    "https://tdlguwwlnj-5.tdlguwwlnj.repl.co",
    "https://tdlguwwlnj-6.tdlguwwlnj.repl.co",
    "https://tdlguwwlnj-7--tdlguwwlnj.repl.co",
    "https://tdlguwwlnj-8--tdlguwwlnj.repl.co",
    "https://tdlguwwlnj-9--tdlguwwlnj.repl.co",
    "https://tdlguwwlnj-10--tdlguwwlnj.repl.co",
    "https://ksmggouvixkmp-1.ksmggouvixkmp.repl.co",
    "https://ksmggouvixkmp-2.ksmggouvixkmp.repl.co",
    "https://ksmggouvixkmp-3.ksmggouvixkmp.repl.co",
    "https://ksmggouvixkmp-4.ksmggouvixkmp.repl.co",
    "https://ksmggouvixkmp-5.ksmggouvixkmp.repl.co",
    "https://ksmggouvixkmp-6.ksmggouvixkmp.repl.co",
    "https://ksmggouvixkmp-7--ksmggouvixkmp.repl.co",
    "https://ksmggouvixkmp-8--ksmggouvixkmp.repl.co",
    "https://ksmggouvixkmp-9--ksmggouvixkmp.repl.co",
    "https://ksmggouvixkmp-10--ksmggouvixkmp.repl.co",
    "https://ldgukyzubqress-1.ldgukyzubqress.repl.co",
    "https://ldgukyzubqress-2.ldgukyzubqress.repl.co",
    "https://ldgukyzubqress-3.ldgukyzubqress.repl.co",
    "https://ldgukyzubqress-4.ldgukyzubqress.repl.co",
    "https://ldgukyzubqress-5.ldgukyzubqress.repl.co",
    "https://ldgukyzubqress-6.ldgukyzubqress.repl.co",
    "https://ldgukyzubqress-7--ldgukyzubqress.repl.co",
    "https://ldgukyzubqress-8--ldgukyzubqress.repl.co",
    "https://ldgukyzubqress-9--ldgukyzubqress.repl.co",
    "https://ldgukyzubqress-10--ldgukyzubqress.repl.co",
    "https://vfjfhw-1.vfjfhw.repl.co",
    "https://vfjfhw-2.vfjfhw.repl.co",
    "https://vfjfhw-3.vfjfhw.repl.co",
    "https://vfjfhw-4.vfjfhw.repl.co",
    "https://vfjfhw-5.vfjfhw.repl.co",
    "https://vfjfhw-6.vfjfhw.repl.co",
    "https://vfjfhw-7--vfjfhw.repl.co",
    "https://vfjfhw-8--vfjfhw.repl.co",
    "https://vfjfhw-9--vfjfhw.repl.co",
    "https://vfjfhw-10--vfjfhw.repl.co",
    "https://zywfttnabp-1.zywfttnabp.repl.co",
    "https://zywfttnabp-2.zywfttnabp.repl.co",
    "https://zywfttnabp-3.zywfttnabp.repl.co",
    "https://zywfttnabp-4.zywfttnabp.repl.co",
    "https://zywfttnabp-5.zywfttnabp.repl.co",
    "https://zywfttnabp-6.zywfttnabp.repl.co",
    "https://zywfttnabp-7--zywfttnabp.repl.co",
    "https://zywfttnabp-8--zywfttnabp.repl.co",
    "https://zywfttnabp-9--zywfttnabp.repl.co",
    "https://zywfttnabp-10--zywfttnabp.repl.co",
    "https://bruqtp-1.bruqtp.repl.co",
    "https://bruqtp-2.bruqtp.repl.co",
    "https://bruqtp-3.bruqtp.repl.co",
    "https://bruqtp-4.bruqtp.repl.co",
    "https://bruqtp-5.bruqtp.repl.co",
    "https://bruqtp-6.bruqtp.repl.co",
    "https://bruqtp-7--bruqtp.repl.co",
    "https://bruqtp-8--bruqtp.repl.co",
    "https://bruqtp-9--bruqtp.repl.co",
    "https://bruqtp-10--bruqtp.repl.co",
    "https://nsgnipqrwke-1.nsgnipqrwke.repl.co",
    "https://nsgnipqrwke-2.nsgnipqrwke.repl.co",
    "https://nsgnipqrwke-3.nsgnipqrwke.repl.co",
    "https://nsgnipqrwke-4.nsgnipqrwke.repl.co",
    "https://nsgnipqrwke-5.nsgnipqrwke.repl.co",
    "https://nsgnipqrwke-6.nsgnipqrwke.repl.co",
    "https://nsgnipqrwke-7--nsgnipqrwke.repl.co",
    "https://nsgnipqrwke-8--nsgnipqrwke.repl.co",
    "https://nsgnipqrwke-9--nsgnipqrwke.repl.co",
    "https://nsgnipqrwke-10--nsgnipqrwke.repl.co",
    "https://sovj2weiosjke-1.sovj2weiosjke.repl.co",
    "https://sovj2weiosjke-2.sovj2weiosjke.repl.co",
    "https://sovj2weiosjke-3.sovj2weiosjke.repl.co",
    "https://sovj2weiosjke-4.sovj2weiosjke.repl.co",
    "https://sovj2weiosjke-5.sovj2weiosjke.repl.co",
    "https://sovj2weiosjke-6.sovj2weiosjke.repl.co",
    "https://sovj2weiosjke-7--sovj2weiosjke.repl.co",
    "https://sovj2weiosjke-8--sovj2weiosjke.repl.co",
    "https://sovj2weiosjke-9--sovj2weiosjke.repl.co",
    "https://sovj2weiosjke-10--sovj2weiosjke.repl.co",
    "https://sdllguovhw-1.sdllguovhw.repl.co",
    "https://sdllguovhw-2.sdllguovhw.repl.co",
    "https://sdllguovhw-3.sdllguovhw.repl.co",
    "https://sdllguovhw-4.sdllguovhw.repl.co",
    "https://sdllguovhw-5.sdllguovhw.repl.co",
    "https://sdllguovhw-6.sdllguovhw.repl.co",
    "https://sdllguovhw-7--sdllguovhw.repl.co",
    "https://sdllguovhw-8--sdllguovhw.repl.co",
    "https://sdllguovhw-9--sdllguovhw.repl.co",
    "https://sdllguovhw-10--sdllguovhw.repl.co",
    "https://otbdylgngzhwxyl-1.otbdylgngzhwxyl.repl.co",
    "https://otbdylgngzhwxyl-2.otbdylgngzhwxyl.repl.co",
    "https://otbdylgngzhwxyl-3.otbdylgngzhwxyl.repl.co",
    "https://otbdylgngzhwxyl-4.otbdylgngzhwxyl.repl.co",
    "https://otbdylgngzhwxyl-5.otbdylgngzhwxyl.repl.co",
    "https://otbdylgngzhwxyl-6.otbdylgngzhwxyl.repl.co",
    "https://otbdylgngzhwxyl-7--otbdylgngzhwxyl.repl.co",
    "https://otbdylgngzhwxyl-8--otbdylgngzhwxyl.repl.co",
    "https://otbdylgngzhwxyl-9--otbdylgngzhwxyl.repl.co",
    "https://otbdylgngzhwxyl-10--otbdylgngzhwxyl.repl.co",
    "https://kfmbpjpjesgu-1.kfmbpjpjesgu.repl.co",
    "https://kfmbpjpjesgu-2.kfmbpjpjesgu.repl.co",
    "https://kfmbpjpjesgu-3.kfmbpjpjesgu.repl.co",
    "https://kfmbpjpjesgu-4.kfmbpjpjesgu.repl.co",
    "https://kfmbpjpjesgu-5.kfmbpjpjesgu.repl.co",
    "https://kfmbpjpjesgu-6.kfmbpjpjesgu.repl.co",
    "https://mxsfgnoixer-1.mxsfgnoixer.repl.co",
    "https://mxsfgnoixer-2.mxsfgnoixer.repl.co",
    "https://mxsfgnoixer-3.mxsfgnoixer.repl.co",
    "https://mxsfgnoixer-4.mxsfgnoixer.repl.co",
    "https://mxsfgnoixer-5.mxsfgnoixer.repl.co",
    "https://mxsfgnoixer-6.mxsfgnoixer.repl.co",
    "https://tocviuwifjiaie-1.tocviuwifjiaie.repl.co",
    "https://tocviuwifjiaie-2.tocviuwifjiaie.repl.co",
    "https://tocviuwifjiaie-3.tocviuwifjiaie.repl.co",
    "https://tocviuwifjiaie-4.tocviuwifjiaie.repl.co",
    "https://tocviuwifjiaie-5.tocviuwifjiaie.repl.co",
    "https://tocviuwifjiaie-6.tocviuwifjiaie.repl.co",
    "https://uqefmnntxyleey-1.uqefmnntxyleey.repl.co",
    "https://uqefmnntxyleey-2.uqefmnntxyleey.repl.co",
    "https://uqefmnntxyleey-3.uqefmnntxyleey.repl.co",
    "https://uqefmnntxyleey-4.uqefmnntxyleey.repl.co",
    "https://uqefmnntxyleey-5.uqefmnntxyleey.repl.co",
    "https://uqefmnntxyleey-6.uqefmnntxyleey.repl.co",
    "https://znxcrawynkg-1.znxcrawynkg.repl.co",
    "https://znxcrawynkg-2.znxcrawynkg.repl.co",
    "https://znxcrawynkg-3.znxcrawynkg.repl.co",
    "https://znxcrawynkg-4.znxcrawynkg.repl.co",
    "https://znxcrawynkg-5.znxcrawynkg.repl.co",
    "https://znxcrawynkg-6.znxcrawynkg.repl.co",
    "https://dvipdrxrifxqq-1.dvipdrxrifxqq.repl.co",
    "https://dvipdrxrifxqq-2.dvipdrxrifxqq.repl.co",
    "https://dvipdrxrifxqq-3.dvipdrxrifxqq.repl.co",
    "https://dvipdrxrifxqq-4.dvipdrxrifxqq.repl.co",
    "https://dvipdrxrifxqq-5.dvipdrxrifxqq.repl.co",
    "https://dvipdrxrifxqq-6.dvipdrxrifxqq.repl.co",
    
] 


while True:
    # 记录成功的链接
    successful_urls = []

    def request_url(url):
        retry = 0
        while True:
            try:
                new_url = f"{url}/vimeo.php?link=https://player.vimeo.com/video/211"
                response = requests.get(new_url, timeout=15)
                if response.status_code == 200 and 'gutierrez' in response.text:
                    print(f'{new_url} returned 200')
                    successful_urls.append(url)
                    return None  # 返回None表示成功
                else:
                    print(f'{new_url} returned {response.status_code}')
                    if retry < 2:
                        retry += 1
                        print(f'{new_url} retrying {retry}/2')
                    else:
                        break
            except requests.exceptions.RequestException as e:
                print(f'{new_url} failed: {e}')
                if retry < 2:
                    retry += 1
                    print(f'{new_url} retrying {retry}/2')
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
    if len(successful_urls) >= 140:
        with open('/mnt/d/常用/vimeo/传统方法刷-下载后再处理数据/urls.txt', 'w') as f:
            for url in successful_urls:
                f.write(url + '\n')
        print("以下链接未成功写入urls.txt:")
        print(set(urls) - set(successful_urls))
    else:
        print('Successful URLs less than 40, skipped writing to file.')

    # 如果所有链接都成功，则退出循环
    if set(successful_urls) == set(urls):
        print("All URLs succeeded!")
        break

    # 休眠一段时间后再次尝试
    print("一轮结束")
    print(len(successful_urls))
    time.sleep(4)
    os.system('clear')

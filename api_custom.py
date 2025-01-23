from playwright.sync_api import sync_playwright
import requests
import like_post_ttc
import time
import random
import logging
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def parse_cookies(cookie_str):
    cookies = []
    for cookie in cookie_str.split("; "):  # Tách từng cookie tại dấu "; "
        if "=" in cookie:  # Chỉ xử lý nếu có định dạng name=value
            name, value = cookie.split("=", 1)
            cookies.append({
                "name": name.strip(),
                "value": value.strip(),
                "domain": ".facebook.com",
                "path": "/",
                "secure": True,
                "httpOnly": False,
                "sameSite": "None",
            })
    return cookies

def parse_proxy(data):
    proxy={
        "server":f"http://{data['ip']}:{data['port']}",
        "username":data['username'],
        "password":data['password']
    }
    return proxy

def open_web_proxy(url,data,timeout):
    
    context_config=data["context"]
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            proxy=parse_proxy(data["proxy"])
        )

        context = browser.new_context(
            user_agent=context_config["user_agent"],
            viewport=context_config["viewport"],
            locale=context_config["locale"],
            timezone_id=context_config["timezone_id"],
            geolocation=context_config["geolocation"]
            # permissions=["geolocation"]  # Cấp quyền nếu cần
        )

        # Mở trang web trong context
        page = context.new_page()
        page.goto(url,timeout=200000)  # Kiểm tra IP

        page.wait_for_timeout(timeout)

        # Đóng trình duyệt
        browser.close()

def open_web_facebook(url,data,timeout):
    
    context_config=data["context"]
    # cookie = data[]
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            proxy=parse_proxy(data["proxy"])
        )

        context = browser.new_context(
            user_agent=context_config["user_agent"],
            viewport=context_config["viewport"],
            locale=context_config["locale"],
            timezone_id=context_config["timezone_id"],
            geolocation=context_config["geolocation"]
            # permissions=["geolocation"]  # Cấp quyền nếu cần
        )

        # Mở trang web trong context
        page = context.new_page()
        page.goto(url,timeout=200000)  # Kiểm tra IP

        page.wait_for_timeout(timeout)

        # Đóng trình duyệt
        browser.close()

# def live_facebook(index):
#     url="https://facebook.com/"
#     timeout= 100000000
#     open_web_proxy(url,fb_configs[index],timeout)

def live_proxy(data):
    url="https://checkip.com.vn/"
    timeout= 100000000
    open_web_proxy(url,data,timeout)

# def task_like_ttc(ttc_index, proxy_index, fb_index, reload_cookie_ttc_times, time_wait_error_ttc, number_task_in_times, timeout_link, timeout_like, timeout_unlike, time_close_browser, time_for_every_task, logging):
#     ttc_account = ttc_accounts[ttc_index]
#     proxy = get_proxy(proxy_index)
#     cookie_ttc = like_post_ttc.login(ttc_account['access_token'], proxy, logging)
#     fb_config = fb_configs[fb_index]
#     reload_cookie_ttc = 0
#     facebook_status=True
    
#     while True:
#         if facebook_status == False:
#             break
#         try:
            
#             if reload_cookie_ttc == reload_cookie_ttc_times:
#                 reload_cookie_ttc = 0
#                 cookie_ttc = like_post_ttc.login(ttc_account['access_token'], proxy, logging)
#                 if cookie_ttc==None:
#                     # print(f"Chương trình sẽ thử lại sau do lỗi cookie ttc {time_wait_error_ttc} giây.")
#                     logging.error(f"Error cookie ttc {time_wait_error_ttc} seconds.")
#                     time.sleep(time_wait_error_ttc)
#             reload_cookie_ttc += 1
#             count_task = 0
#             data = like_post_ttc.get_likepost(cookie_ttc, proxy)
#             for item in data:
#                 count_task +=1
#                 idpost = item.get("idpost")
#                 link = item.get("link")
#                 # print(f"idpost: {idpost}, link: {link}")
#                 logging.info(f"idpost: {idpost}, link: {link}")
#                 status = {
#                     'award':False,
#                     'facebook':True
#                 }

#                 if random.choice([True, False]):
#                     logging.info(f"like post - unlike post")
#                     status = like_post_ttc.like_post(fb_config, link, idpost, cookie_ttc, proxy, timeout_link, timeout_like, timeout_unlike, time_close_browser,logging)
#                 else:
#                     logging.info(f"like post")
#                     status = like_post_ttc.like_post_v2(fb_config, link, idpost, cookie_ttc, proxy, timeout_link, timeout_like, timeout_unlike, time_close_browser,logging)
                
#                 facebook_status = status['facebook']
#                 if status['award'] == False:
#                     reload_cookie_ttc=reload_cookie_ttc_times-1
#                     break
#                 if count_task == number_task_in_times:
#                     break

#             # print(f"Đợi task tiếp theo {time_for_every_task} giây.")
#             logging.info(f"Wait next task {time_for_every_task} seconds.")
#             time.sleep(time_for_every_task)

#         except Exception as e:
#             cookie_ttc = like_post_ttc.login(ttc_account['access_token'], proxy, logging)
#             if cookie_ttc==None:
#                 # print(f"Chương trình sẽ thử lại sau {time_wait_error_ttc} giây.")
#                 logging.warning(f"Restart after {time_wait_error_ttc} seconds.")
#                 time.sleep(time_wait_error_ttc)
#             # print(f"Đã xảy ra lỗi: {e}. Chương trình sẽ thử lại sau {time_for_every_task} giây.")
#             logging.error(f"occur error: {e}. Restart after {time_for_every_task} seconds.")
#             time.sleep(time_for_every_task)
            
#         # facebook_status = False
        
    

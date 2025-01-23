from playwright.sync_api import sync_playwright
import requests
import json
import logging
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def login(access_token, proxy_config, logging):
    url = "https://tuongtaccheo.com/logintoken.php"
    headers = {
        "Content-type": "application/x-www-form-urlencoded"
    }
    data = {
        "access_token": access_token
    }
    proxy_url = f"http://{proxy_config['username']}:{proxy_config['password']}@{proxy_config['server'].replace('http://', '').replace('https://', '')}"
        
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    response = requests.post(url, headers=headers, data=data, proxies=proxies)

    if response.status_code == 200:
        logging.info("login success!")
        
        cookies = response.cookies
        logging.info(response.text)
        
        for cookie in cookies:
            logging.info(f"{cookie.name}: {cookie.value}")
            return cookie.value
    else:
        logging.error(f"error {response.status_code}: {response.text}")
        return None
    
#cookie ttc
def get_likepost(cookie_ttc, proxy_config):

    url = "https://tuongtaccheo.com/kiemtien/likepostvipcheo/getpost.php"

    headers = {
        "Cookie": f"PHPSESSID={cookie_ttc}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://tuongtaccheo.com/kiemtien/likepostvipcheo/"
    }
    proxy_url = f"http://{proxy_config['username']}:{proxy_config['password']}@{proxy_config['server'].replace('http://', '').replace('https://', '')}"
        
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }

    try:
        # Gửi yêu cầu GET
        response = requests.get(url, headers=headers, proxies=proxies)
        
        if response.status_code == 200:
            try:
                data = json.loads(response.text)
                if isinstance(data, list): 
                    return data
                else:
                    print("Dữ liệu không phải dạng danh sách JSON.")
                    return None
            except json.JSONDecodeError as e:
                print(f"Không thể giải mã JSON: {e}")
                return None
        else:
            print(f"require fail: {response.status_code}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"occur when send request: {e}")
        return None

def like_post(fb_config, link, idpost, cookie_ttc, proxy, timeout_link, timeout_like, timeout_unlike, time_close_browser,logging):
    status = {
        'award':False,
        'facebook':True
    }
    context_config=fb_config["context_config"]
    cookie_fb=fb_config["cookie"]

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            proxy=fb_config["proxy"]
        )
        context = browser.new_context(
            user_agent=context_config["user_agent"],
            viewport=context_config["viewport"],
            locale=context_config["locale"],
            timezone_id=context_config["timezone_id"],
            geolocation=context_config["geolocation"]
            # permissions=["geolocation"]  # Cấp quyền nếu cần
        )
        if cookie_fb is not None:
            context.add_cookies(cookie_fb)

        page = context.new_page()
        page.goto(link,timeout=timeout_link)

        page.wait_for_timeout(2000)
        page.evaluate("document.body.style.zoom = '50%'")

        # print(f"Wait like {timeout_like} ms.")
        logging.info(f"Wait like {timeout_like} ms.")
        page.wait_for_timeout(timeout_like)
        try:
            like_button_selector = "div[aria-hidden='false'] div[aria-label='Like'][tabindex='0']" 
            try:
                page.wait_for_timeout(2000)
                page.click(like_button_selector, timeout=2000)
                # print("Liked post.")
                logging.info(f"Liked post.")
                page.wait_for_timeout(2000)
                status['award'] = award_coin(cookie_ttc, idpost, proxy, logging)
                
                # Hủy like
                # print(f"Wait unlike {timeout_unlike} ms.")
                logging.info(f"Wait unlike {timeout_unlike} ms.")
                page.wait_for_timeout(timeout_unlike)
                like_button_selector = "div[aria-hidden='false'] div[aria-label='Remove Like'][tabindex='0']"
                try:
                    page.click(like_button_selector, timeout=2000)
                    # print("Unlike post.")
                    logging.info("Unlike post.")
                except Exception as e:
                    page.wait_for_timeout(timeout_unlike)
                    like_button_selector = "div[aria-hidden='false'] div[aria-label='Active Like'][tabindex='0']" #Nút Thích đang hoạt động
                    try:
                        page.click(like_button_selector, timeout=2000)
                        # print("Unlike post.") 
                        logging.info("Unlike post.") 
                    except Exception as e:
                        # print(f"Not unlike post: {e}")
                        logging.warning(f"Not unlike post: {e}")
                        status['facebook']=False
                page.wait_for_timeout(2000)

            except Exception as e:
                like_button_selector = "div[aria-label='Like'][tabindex='0']"
                try:
                    page.wait_for_timeout(2000)
                    page.click(like_button_selector, timeout=2000)
                    # print("Liked post.")
                    logging.info("Liked post.")
                    page.wait_for_timeout(2000)

                    status['award'] = award_coin(cookie_ttc, idpost, proxy, logging)
                   
                    # Hủy like
                    # print(f"Wait unlike {timeout_unlike} ms.")
                    logging.info(f"Wait unlike {timeout_unlike} ms.")
                    page.wait_for_timeout(timeout_unlike)
                    like_button_selector = "div[aria-label='Remove Like'][tabindex='0']" #Gỡ Thích
                    try:
                        page.click(like_button_selector, timeout=2000)
                        # print("Unlike post.")
                        logging.info("Unlike post.")
                    except Exception as e:
                        page.wait_for_timeout(timeout_unlike)
                        like_button_selector = "div[aria-label='Active Like'][tabindex='0']"
                        try:
                            page.click(like_button_selector, timeout=2000)
                            # print("Unlike post.") 
                            logging.info("Unlike post.") 
                        except Exception as e:
                            # print(f"Not unlike post: {e}")
                            logging.warning(f"Not unlike post: {e}")
                    # Wait trang tải xong
                    page.wait_for_timeout(2000)

                except Exception as e:
                    # print(f"Not like post: {e}")
                    logging.warning(f"Not like post: {e}")
                    status['facebook']=False

        except Exception as e:
            # print(f"error action: {e}")
            logging.warning(f"error action: {e}")
        # close browser
        # print(f"Wait close browser {time_close_browser} ms.")
        logging.error(f"Wait close browser {time_close_browser} ms.")
        page.wait_for_timeout(time_close_browser)
        browser.close()
        
    # print(f"close browser")
    logging.info(f"close browser")
    return status

def award_coin(cookie_ttc, idpost, proxy_config, logging):
    url = "https://tuongtaccheo.com/kiemtien/likepostvipcheo/nhantien.php"
    # Thiết lập headers với cookie và thông tin khác cookie ttc
    headers = {
        "Cookie": f"PHPSESSID={cookie_ttc}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://tuongtaccheo.com/kiemtien/likepostvipcheo/"
    }
    proxy_url = f"http://{proxy_config['username']}:{proxy_config['password']}@{proxy_config['server'].replace('http://', '').replace('https://', '')}"
        
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }

    # Dữ liệu cần gửi trong POST request
    payload = {
        "id": idpost  # Thay đổi theo id bạn muốn gửi
    }

    try:
        # Gửi yêu cầu POST
        response = requests.post(url, headers=headers, data=payload, proxies=proxies)
        
        # Kiểm tra mã trạng thái HTTP
        if response.status_code == 200:
            logging.info("require ttc get xu success:")
            # logging.info(response.text)  # In ra nội dung trả về từ server
            print(response.text)
            if "error" in response.text:
                logging.info("Fail")
            else:
                logging.info("Successfully")
            return True
        else:
            logging.info(f"require fail: {response.status_code}")
            return False
    
    except requests.exceptions.RequestException as e:
        logging.info(f"occur when send request: {e}")
        return False
    

def like_post_v2(fb_config, link, idpost, cookie_ttc, proxy, timeout_link, timeout_like, timeout_unlike, time_close_browser, logging):
    status = {
        'award':False,
        'facebook':True
    }
    context_config=fb_config["context_config"]
    cookie_fb=fb_config["cookie"]

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            proxy=fb_config["proxy"]
        )
        context = browser.new_context(
            user_agent=context_config["user_agent"],
            viewport=context_config["viewport"],
            locale=context_config["locale"],
            timezone_id=context_config["timezone_id"],
            geolocation=context_config["geolocation"]
            # permissions=["geolocation"]  # Cấp quyền nếu cần
        )
        if cookie_fb is not None:
            context.add_cookies(cookie_fb)

        page = context.new_page()
        page.goto(link,timeout=timeout_link)

        page.wait_for_timeout(2000)
        page.evaluate("document.body.style.zoom = '50%'")
        logging.info(f"Wait like {timeout_like} ms.")
        page.wait_for_timeout(timeout_like)
        try:
            like_button_selector = "div[aria-hidden='false'] div[aria-label='Like'][tabindex='0']" 
            try:
                page.wait_for_timeout(2000)
                page.click(like_button_selector, timeout=2000)
                logging.info("Liked post.")
                page.wait_for_timeout(2000)
                status['award'] = award_coin(cookie_ttc, idpost, proxy, logging)
                
                
                page.wait_for_timeout(2000)

            except Exception as e:
                like_button_selector = "div[aria-label='Like'][tabindex='0']"
                try:
                    page.wait_for_timeout(2000)
                    page.click(like_button_selector, timeout=2000)
                    logging.info("Liked post.")
                    page.wait_for_timeout(2000)

                    status['award'] = award_coin(cookie_ttc, idpost, proxy, logging)
                   
                    
                    # Wait trang tải xong
                    page.wait_for_timeout(2000)

                except Exception as e:
                    logging.warning(f"Not like post: {e}")
                    status['facebook']=False

        except Exception as e:
            logging.error(f"error action: {e}")
        # close browser
        logging.info(f"Wait close browser {time_close_browser} ms.")
        page.wait_for_timeout(time_close_browser)
        browser.close()
        
    logging.info(f"close browser")
    return status
import requests

def get_geolocation(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data.get("loc", "")
        if location:
            latitude, longitude = map(float, location.split(","))
            return {"latitude": latitude, "longitude": longitude}
    return None

# Ví dụ: Lấy vị trí của một địa chỉ IP
ip = "14.181.153.172"  # Thay bằng IP của bạn
geolocation = get_geolocation(ip)
print(geolocation)

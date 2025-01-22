
data={
    "proxies":[
        {"ip":"123", "port":"123", "username":"123", "password":"123"},
        {"ip":"234", "port":"234", "username":"234", "password":"234"}
    ],
    "user_agents":[
        {"user_agent":"123"},
    ]
}
// {"ip":"123", "port":"123", "username":"123", "password":"123"}

user_agents user_agent_id user_agent
viewports viewport_id width height
geolocations geolocation_id longitude latitude
contexts context_id user_agent_id viewport_id locale timezone_id geolocation_id

ttc_accounts ttc_account_id username password access_token

fb_accounts fb_account_id uid otp_2fa mail password_mail cookie

fb_proxy_couples fb_proxy_id fb_account_id proxy_id 
ttc_fb_couples ttc_fb_id ttc_account_id fb_account_id
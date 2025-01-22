from database import show_table_data
from action import (
     get_action,search_action, delete_action, insert_action, update_action
)

def ls(var=['-h']):
    match var[0]:
        case '-p':
            show_table_data("proxies")
        case '-u':
            show_table_data("user_agents")
        case '-v':
            show_table_data("viewports")
        case '-g':
            show_table_data("geolocations")
        case '-c':
            show_table_data("contexts")
        
        case '-ttc':
            show_table_data("ttc_accounts")
        case '-fa':
            show_table_data("fb_accounts")
        case '-fp':
            show_table_data("fb_proxy_couples")
        case '-ttcf':
            show_table_data("ttc_fb_couples")

        case '-h':
            print("ls help")
        case _:
            print("command not found!")

def insert(var=['-h']):
    match var[0]:
        case '-h':
            print("insert help")
        case '-p':
            var.pop(0)
            insert_action("proxies",var)
        case '-u':
            var.pop(0)
            insert_action("user_agents",var)
        case '-v':
            var.pop(0)
            insert_action("viewports",var)
        case '-g':
            var.pop(0)
            insert_action("geolocations",var)
        case '-c':
            var.pop(0)
            insert_action("contexts",var)
            
        case '-ttc':
            var.pop(0)
            insert_action("ttc_accounts",var)
        case '-fa':
            var.pop(0)
            insert_action("fb_accounts",var)
        case '-fp':
            var.pop(0)
            insert_action("fb_proxy_couples",var)
        case '-ttcf':
            var.pop(0)
            insert_action("ttc_fb_couples",var)


        case _:
            print("command not found!")

def delete(var=['-h']):
    match var[0]:
        case '-h':
            print("delete help")
        case '-p':
            var.pop(0)
            delete_action("proxies",var)
        case '-u':
            var.pop(0)
            delete_action("user_agents",var)
        case '-v':
            var.pop(0)
            delete_action("viewports",var)
        case '-g':
            var.pop(0)
            delete_action("geolocations",var)
        case '-c':
            var.pop(0)
            delete_action("contexts",var)
            
        case '-ttc':
            var.pop(0)
            delete_action("ttc_accounts",var)
        case '-fa':
            var.pop(0)
            delete_action("fb_accounts",var)
        case '-fp':
            var.pop(0)
            delete_action("fb_proxy_couples",var)
        case '-ttcf':
            var.pop(0)
            delete_action("ttc_fb_couples",var)
        

        case _:
            print("command not found!")

def search(var=['-h']):
    match var[0]:
        case '-h':
            print("search help")
        case '-p':
            var.pop(0)
            search_action("proxies",var)
        case '-u':
            var.pop(0)
            search_action("user_agents",var)
        case '-v':
            var.pop(0)
            search_action("viewports",var)
        case '-g':
            var.pop(0)
            search_action("geolocations",var)
        case '-c':
            var.pop(0)
            search_action("contexts",var)
            
        case '-ttc':
            var.pop(0)
            search_action("ttc_accounts",var)
        case '-fa':
            var.pop(0)
            search_action("fb_accounts",var)
        case '-fp':
            var.pop(0)
            search_action("fb_proxy_couples",var)
        case '-ttcf':
            var.pop(0)
            search_action("ttc_fb_couples",var)
        
        case _:
            print("command not found!")

def update(var=['-h']):
    match var[0]:
        case '-h':
            print("update help")
        case '-p':
            var.pop(0)
            update_action("proxies",var)
        case '-u':
            var.pop(0)
            update_action("user_agents",var)
        case '-v':
            var.pop(0)
            update_action("viewports",var)
        case '-g':
            var.pop(0)
            update_action("geolocations",var)
        case '-c':
            var.pop(0)
            update_action("contexts",var)
            
        case '-ttc':
            var.pop(0)
            update_action("ttc_accounts",var)
        case '-fa':
            var.pop(0)
            update_action("fb_accounts",var)
        case '-fp':
            var.pop(0)
            update_action("fb_proxy_couples",var)
        case '-ttcf':
            var.pop(0)
            update_action("ttc_fb_couples",var)
        
        case _:
            print("command not found!")

def get(var=['-h']):
    match var[0]:
        case '-h':
            print("get help")
        case '-p':
            var.pop(0)
            get_action("proxies",var)
        case '-u':
            var.pop(0)
            get_action("user_agents",var)
        case '-v':
            var.pop(0)
            get_action("viewports",var)
        case '-g':
            var.pop(0)
            get_action("geolocations",var)
        case '-c':
            var.pop(0)
            get_action("contexts",var)
            
        case '-ttc':
            var.pop(0)
            get_action("ttc_accounts",var)
        case '-fa':
            var.pop(0)
            get_action("fb_accounts",var)
        case '-fp':
            var.pop(0)
            get_action("fb_proxy_couples",var)
        case '-ttcf':
            var.pop(0)
            get_action("ttc_fb_couples",var)
        
        case _:
            print("command not found!")

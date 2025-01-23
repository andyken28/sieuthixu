import json
import os
import api_custom
import threading
import time
import random
import logging

from database import (
    get_data,search_data, get_type, get_variable, get_null, delete_data, insert_data, update_data,
    get_primary_keys, get_foreign_keys,
    create_tables
    
)

def check_proxy(data):
  api_custom.live_proxy(data)

def input_action(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        print(f"data in {file_path}:")
        # print(data)
        delete_path = "sieuthixu.db"
        if os.path.exists(delete_path):
            os.remove(delete_path)
            print(f"File '{delete_path}' đã được xóa.")
            create_tables()
        else:
            print(f"File '{delete_path}' không tồn tại.")
        for key in data:
            for item in data[key]:
                insert_data(key,item)
                # print(item)

    except ValueError:
        print(f"==> data error {file_path}")

def check_action(table_name,var):
    variables=get_variable(table_name)
    if len(var)==0:
        print(f"\nplease choice id in {table_name}")
        data = get_data(table_name)
        for item in data:
            print(item)
        var=[input(f"\ninput {variables[0]}: ")]
    try:
        var[0]=int(var[0])
        print(f"\nget {variables[0]}: {var[0]}")
        data = get_data(table_name,var[0])
        
    except ValueError:
        print("id not int!")
        return

    match table_name:
        case "proxies":
            if data:
                proxy_context = search_data("proxy_context_couples",1,data[0][variables[0]])[0]
                proxy_context = get_data("proxy_context_couples",proxy_context["proxy_context_id"])[0]
                print(proxy_context)
                thread1 = threading.Thread(target=check_proxy, args=(proxy_context,))
                thread1.start()
                # thread1.join()
        case "fb_accounts":
            if data:
                fb_proxy = search_data("fb_proxy_couples",1,data[0][variables[0]])[0]
                print(fb_proxy)
                proxy_context = search_data("proxy_context_couples",1,fb_proxy["proxy_id"])[0]
                # proxy_context = get_data("proxy_context_couples",proxy_context["proxy_context_id"])[0]
                print(proxy_context)
                # thread1 = threading.Thread(target=check_proxy, args=(proxy_context,))
                # thread1.start()
                # thread1.join()

def insert_action(table_name,var):
    if len(var)==0:
        command = input(f"are you insert {table_name}? y/n: ")
        var.append(command)
    match var[0]:
        case 'y':
            variables=get_variable(table_name)
            foreign_keys=get_foreign_keys()
            primary_keys=get_primary_keys()
            index=0
            data={}
            check=False
            for item in variables:
                if(index==0):
                    print()
                    index+=1
                    continue
                type_var=get_type(table_name,index)
                null_var=get_null(table_name,index)
                type_var_str=""
                null_var_str="null"
                match type_var:
                    case 0:
                        type_var_str="int"
                    case 1:
                        type_var_str="string"
                    case 2:
                        type_var_str="float"
                    case 3:
                        type_var_str="date"
                if null_var==1:
                    null_var_str="not null"
                data[item] = input(f"input {item}({type_var_str}, {null_var_str}): ")
                while True:
                    if data[item]=="" and null_var==1:
                        data[item] = input(f"input {item}({type_var_str}, {null_var_str}) again (enter=exit): ")
                        if data[item]=="":
                            check = True
                            break
                    try:
                        match type_var:
                            case 0:
                                data[item]=int(data[item])
                            case 1:
                                data[item]=str(data[item])
                            case 2:
                                data[item]=float(data[item])
                    except ValueError:
                        data[item] = input(f"input {item}({type_var_str}, {null_var_str}) again (enter=exit): ")
                        if data[item]=="":
                            check = True
                            break
                        continue
                    if item in foreign_keys:
                        foreign_table=primary_keys[item]
                        foreign_data=get_data(foreign_table,data[item])
                        if foreign_data:
                            print(foreign_data[0])
                            break
                        data[item] = input(f"input {item}({type_var_str}, {null_var_str}) again (enter=exit): ")
                        if data[item]=="":
                            check = True
                            break
                    else:
                        break
                index+=1
                if check:
                    break            
            if check == False:
                print(f"\n{data}")
                command = input(f"\nare you insert? y/n: ")
                match command:
                    case 'y':
                        insert_data(table_name,data)
            
        case _:
            print("command not found!")

def delete_action(table_name,var):
    if len(var)==0 or len(var)==2:
        if len(var)==0:
            index=0
            variables=get_variable(table_name)
            print(f"\nPlease choice option:")
            for item in variables:
                type_var=get_type(table_name,index)
                type_var_str=""
                match type_var:
                    case 0:
                        type_var_str="int"
                    case 1:
                        type_var_str="string"
                    case 2:
                        type_var_str="float"
                    case 3:
                        type_var_str="date"
                print(f"{index} : {item}(type:{type_var_str})")
                index+=1
            key = input("\ninput key: ")
            value = input("input value: ")
        elif len(var)==2:
            variables=get_variable(table_name)
            key = var[0]
            value = var[1]
        try:
            if not key or not value:
                print("variable not none!")
            else:
                key = int(key)
                if key < len(variables):
                    type_var=get_type(table_name,key)
                    try:
                        match type_var:
                            case 0:
                                value=int(value)
                            case 1:
                                value=str(value)
                            case 2:
                                value=float(value)
                        print(f"\nsearch {table_name} {variables[key]}={value}")
                        data = search_data(table_name,key,value)
                        check = False
                        for item in data or []:
                            check = True
                            print(item)
                        if check:
                            command = input("are you delete? y/n: ")
                            match command:
                                case 'y':
                                    delete_data(table_name,key,value)
                    except ValueError:
                        print("value valid!")
                else:
                    print("key valid!")
        except ValueError:
            print("key not int!")
    else:
        print("command not found!")
        return


def update_action(table_name,var):
    if len(var)==0 or len(var)==2:
        if len(var)==0:
            index=0
            variables=get_variable(table_name)
            print(f"\nPlease choice option:")
            for item in variables:
                type_var=get_type(table_name,index)
                type_var_str=""
                match type_var:
                    case 0:
                        type_var_str="int"
                    case 1:
                        type_var_str="string"
                    case 2:
                        type_var_str="float"
                    case 3:
                        type_var_str="date"
                print(f"{index} : {item}(type:{type_var_str})")
                index+=1
            key = input("\ninput key: ")
            value = input("input value: ")
        elif len(var)==2:
            variables=get_variable(table_name)
            key = var[0]
            value = var[1]
        try:
            if not key or not value:
                print("variable not none!")
            else:
                key = int(key)
                if key < len(variables):
                    type_var=get_type(table_name,key)
                    try:
                        match type_var:
                            case 0:
                                value=int(value)
                            case 1:
                                value=str(value)
                            case 2:
                                value=float(value)
                        print(f"\nsearch {table_name} {variables[key]}={value}")
                        data = search_data(table_name,key,value)
                        check = False
                        for item in data or []:
                            check = True
                            print(item)
                        if check:
                            command = input("are you update? y/n: ")
                            match command:
                                case 'y':
                                    update_core(table_name,key,value)
                    except ValueError:
                        print("value valid!")
                else:
                    print("key valid!")
        except ValueError:
            print("key not int!")
    else:
        print("command not found!")
        return


def update_core(table_name,key,value):
    variables=get_variable(table_name)
    foreign_keys=get_foreign_keys()
    primary_keys=get_primary_keys()
    index=0
    data={}
    check=False
    print(f"\n==> input enter = not change")
    for item in variables:
        if(index==0):
            index+=1
            continue
        type_var=get_type(table_name,index)
        null_var=get_null(table_name,index)
        type_var_str=""
        null_var_str="null"
        match type_var:
            case 0:
                type_var_str="int"
            case 1:
                type_var_str="string"
            case 2:
                type_var_str="float"
            case 3:
                type_var_str="date"
        if null_var==1:
            null_var_str="not null"
        temp = input(f"input {item}({type_var_str}): ")
        if temp == "":
            continue
        data[item] = temp
        while True:
            try:
                match type_var:
                    case 0:
                        data[item]=int(data[item])
                    case 1:
                        data[item]=str(data[item])
                    case 2:
                        data[item]=float(data[item])
            except ValueError:
                data[item] = input(f"input {item}({type_var_str}) again (enter=exit): ")
                if data[item]=="":
                    check = True
                    break
                continue
            if item in foreign_keys:
                foreign_table=primary_keys[item]
                foreign_data=get_data(foreign_table,data[item])
                if foreign_data:
                    print(foreign_data[0])
                    break
                data[item] = input(f"input {item}({type_var_str}) again (enter=exit): ")
                if data[item]=="":
                    check = True
                    break
            else:
                break
        index+=1
        if check:
            break            
    if check == False:
        if data:
            print(f"\n{data}")
            command = input(f"\nare you update? y/n: ")
            match command:
                case 'y':
                    update_data(table_name,data,key,value)
        else:
            print(f"\n==> no data for update!")
                    
def get_action(table_name,var):
    if len(var)==0:
        var=["all"]
    match var[0]:
        case 'all':
            print(f"\nget all {table_name}")
            data = get_data(table_name)
            for item in data:
                print(item) 
        case _:
            try:
                var[0]=int(var[0])
                print(f"\nget {table_name} id: {var[0]}")
                data = get_data(table_name,var[0])
                for item in data:
                    print(item)
            except ValueError:
                print("id not int!")

def search_action(table_name,var):
    if len(var)==0 or len(var)==2:
        if len(var)==0:
            index=0
            variables=get_variable(table_name)
            print(f"\nPlease choice option:")
            for item in variables:
                type_var=get_type(table_name,index)
                type_var_str=""
                match type_var:
                    case 0:
                        type_var_str="int"
                    case 1:
                        type_var_str="string"
                    case 2:
                        type_var_str="float"
                    case 3:
                        type_var_str="date"
                print(f"{index} : {item}(type:{type_var_str})")
                index+=1
            key = input("\ninput key: ")
            value = input("input value: ")
        elif len(var)==2:
            variables=get_variable(table_name)
            key = var[0]
            value = var[1]
        try:
            if not key or not value:
                print("variable not none!")
            else:
                key = int(key)
                if key < len(variables):
                    type_var=get_type(table_name,key)
                    try:
                        match type_var:
                            case 0:
                                value=int(value)
                            case 1:
                                value=str(value)
                            case 2:
                                value=float(value)
                        print(f"\nsearch {table_name} {variables[key]}={value}")
                        data = search_data(table_name,key,value)
                        for item in data or []:
                            print(item)
                    except ValueError:
                        print("value valid!")
                else:
                    print("key valid!")
        except ValueError:
            print("key not int!")
    else:
        print("command not found!")
        return
    
###############


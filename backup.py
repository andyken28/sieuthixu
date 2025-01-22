
def search_proxy_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nsearch proxy id: {var[0]}")
                rows = search_proxy(var[0],None)
                if rows == 0:
                    print(f"==> no data")
            case '-ip':
                var.pop(0)
                print(f"\nsearch proxy ip: {var[0]}")
                rows = search_proxy(None, var[0])
                if rows == 0:
                    print(f"==> no data")
            case _:
                print("command not found!")


def get_proxy_action(var):
    if len(var)==0:
        print("command not found!")
    else:
        match var[0]:
            case 'all':
                print(f"\nget all proxy")
                data = get_data("proxies")
                for item in data:
                    print(item) 
            case _:
                print(f"\nget proxy id: {var[0]}")
                data = get_data("proxies",var[0])
                print(data[0])


def search_user_agent_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nsearch user agent id: {var[0]}")
                rows = search_user_agent(var[0])
                if rows == 0:
                    print(f"==> no data")
            case _:
                print("command not found!")



def get_user_agent_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nget user agent id: {var[0]}")
                data = get_user_agent(var[0])
                print(data) 
            case _:
                print("command not found!")


def search_viewport_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nsearch viewport id: {var[0]}")
                rows = search_viewport(var[0])
                if rows == 0:
                    print(f"==> no data")
            case _:
                print("command not found!")


def get_viewport_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nget viewport id: {var[0]}")
                data = get_viewport(var[0])
                print(data)
            case _:
                print("command not found!")


def search_geolocation_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nsearch geolocation id: {var[0]}")
                rows = search_geolocation(var[0])
                if rows == 0:
                    print(f"==> no data")
            case _:
                print("command not found!")
                

def get_geolocation_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nget geolocation id: {var[0]}")
                data = get_geolocation(var[0])
                print(data) 
            case _:
                print("command not found!")



def search_context_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nsearch context id: {var[0]}")
                rows = search_context(var[0])
                if rows == 0:
                    print(f"==> no data")
            case _:
                print("command not found!")



def get_context_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nget context id: {var[0]}")
                data = get_data("contexts",var[0])
                print(data) 
            case _:
                print("command not found!")
                

def search_ttc_account_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nsearch geolocation id: {var[0]}")
                rows = search_geolocation(var[0])
                if rows == 0:
                    print(f"==> no data")
            case _:
                print("command not found!")



def get_ttc_account_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nget geolocation id: {var[0]}")
                data = get_geolocation(var[0])
                print(data) 
            case _:
                print("command not found!")


def search_proxy(proxy_id=None, ip=None):
    conn = connect_db()
    cursor = conn.cursor()

    if proxy_id != None:
        cursor.execute('''
        SELECT * FROM proxies WHERE proxy_id = ?
        ''', (proxy_id,))
    elif ip != None:
        cursor.execute('''
        SELECT * FROM proxies WHERE ip = ?
        ''', (ip,))
    else:
        cursor.execute('''
        SELECT * FROM proxies
        ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)    
    conn.commit()
    conn.close()
    return len(rows)


def get_proxy(proxy_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if proxy_id != None:
        cursor.execute('''
        SELECT * FROM proxies WHERE proxy_id = ?
        ''', (proxy_id,))

    rows = cursor.fetchall()
    data = {"ip":None, "port":None, "username":None, "password":None}
    for row in rows:
        data={"ip":row[1], "port":row[2], "username":row[3], "password":row[4]}
    conn.commit()
    conn.close()
    return data


def search_user_agent(user_agent_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if user_agent_id != None:
        cursor.execute('''
        SELECT * FROM user_agents WHERE user_agent_id = ?
        ''', (user_agent_id,))
    else:
        cursor.execute('''
        SELECT * FROM user_agents
        ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)    
    conn.commit()
    conn.close()
    return len(rows)


def get_user_agent(user_agent_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if user_agent_id != None:
        cursor.execute('''
        SELECT * FROM user_agents WHERE user_agent_id = ?
        ''', (user_agent_id,))

    rows = cursor.fetchall()
    data = {"user_agent":None}
    for row in rows:
        data={"user_agent":row[1]}
    conn.commit()
    conn.close()
    return data


def search_viewport(viewport_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if viewport_id != None:
        cursor.execute('''
        SELECT * FROM viewports WHERE viewport_id = ?
        ''', (viewport_id,))
    else:
        cursor.execute('''
        SELECT * FROM viewports
        ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)    
    conn.commit()
    conn.close()
    return len(rows)


def get_viewport(viewport_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if viewport_id != None:
        cursor.execute('''
        SELECT * FROM viewports WHERE viewport_id = ?
        ''', (viewport_id,))
    rows = cursor.fetchall()
    data = {"width":None, "height":None}
    for row in rows:
        data = {"width":row[1], "height":row[2]}
    conn.commit()
    conn.close()
    return data



def search_geolocation(geolocation_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if geolocation_id != None:
        cursor.execute('''
        SELECT * FROM geolocations WHERE geolocation_id = ?
        ''', (geolocation_id,))
    else:
        cursor.execute('''
        SELECT * FROM geolocations
        ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)    
    conn.commit()
    conn.close()
    return len(rows)


def get_geolocation(geolocation_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if geolocation_id != None:
        cursor.execute('''
        SELECT * FROM geolocations WHERE geolocation_id = ?
        ''', (geolocation_id,))
    rows = cursor.fetchall()
    data = {"longitude":None, "latitude":None}
    for row in rows:
        data = {"longitude":row[1], "latitude":row[2]}
    conn.commit()
    conn.close()
    return data


def search_context(context_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if context_id != None:
        cursor.execute('''
        SELECT * FROM contexts WHERE context_id = ?
        ''', (context_id,))
    else:
        cursor.execute('''
        SELECT * FROM contexts
        ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)    
    conn.commit()
    conn.close()
    return len(rows)



def get_context(context_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if context_id != None:
        cursor.execute('''
        SELECT * FROM contexts WHERE context_id = ?
        ''', (context_id,))
    else:
        cursor.execute('''
        SELECT * FROM contexts
        ''')
    rows = cursor.fetchall()
    data=[]

    for row in rows:
        print(row)
        user_agent_id = row[1]
        user_agent = get_user_agent(user_agent_id)['user_agent']
        viewport_id = row[2]
        viewport = get_viewport(viewport_id)
        locale = row[3]
        timezone_id = row[4]
        geolocation_id = row[5]
        geolocation = get_geolocation(geolocation_id)
        data.append(
            {
                "user_agent": user_agent,
                "viewport": viewport,
                "locale": locale,
                "timezone_id": timezone_id,
                "geolocation": geolocation
            }
        )        
    conn.commit()
    conn.close()
    return data


def search_ttc_account(ttc_account_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if ttc_account_id != None:
        cursor.execute('''
        SELECT * FROM ttc_accounts WHERE ttc_account_id = ?
        ''', (ttc_account_id,))
    else:
        cursor.execute('''
        SELECT * FROM ttc_accounts
        ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)    
    conn.commit()
    conn.close()
    return len(rows)



def get_ttc_account(ttc_account_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if ttc_account_id != None:
        cursor.execute('''
        SELECT * FROM ttc_accounts WHERE ttc_account_id = ?
        ''', (ttc_account_id,))

    rows = cursor.fetchall()
    data = {"username":None, "password":None, "access_token":None}
    for row in rows:
        data={"username":row[1], "password":row[2], "access_token":row[3]}
    conn.commit()
    conn.close()
    return data


def delete_proxy_action(var):
    if len(var)<2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\ndelete proxy id: {var[0]}")
                rows = search_proxy(var[0],)
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("y/n: ")
                    match command:
                        case 'y':
                            delete_proxy(var[0],None)
            case '-ip':
                var.pop(0)
                print(f"\ndelete proxy ip: {var[0]}")
                rows = search_proxy(None, var[0])
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("y/n: ")
                    match command:
                        case 'y':
                            delete_proxy(None,var[0])
            case _:
                print("command not found!")


def delete_user_agent_action(var):
    if len(var)<2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\ndelete user agent id: {var[0]}")
                rows = search_user_agent(var[0],)
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("y/n: ")
                    match command:
                        case 'y':
                            delete_user_agent(var[0])
            case _:
                print("command not found!")


def delete_viewport_action(var):
    if len(var)<2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\ndelete viewport id: {var[0]}")
                rows = search_viewport(var[0],)
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("y/n: ")
                    match command:
                        case 'y':
                            delete_viewport(var[0])
            case _:
                print("command not found!")


def delete_geolocation_action(var):
    if len(var)<2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\ndelete geolocation id: {var[0]}")
                rows = search_geolocation(var[0])
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("y/n: ")
                    match command:
                        case 'y':
                            delete_geolocation(var[0])
            case _:
                print("command not found!")


def delete_context_action(var):
    if len(var)<2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\ndelete context id: {var[0]}")
                rows = search_context(var[0],)
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("y/n: ")
                    match command:
                        case 'y':
                            delete_context(var[0])
            case _:
                print("command not found!")


def delete_ttc_account_action(var):
    if len(var)<2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\ndelete geolocation id: {var[0]}")
                rows = search_geolocation(var[0])
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("y/n: ")
                    match command:
                        case 'y':
                            delete_geolocation(var[0])
            case _:
                print("command not found!")


def delete_proxy(proxy_id=None, ip=None):
    conn = connect_db()
    cursor = conn.cursor()

    if proxy_id != None:
        cursor.execute('''
        DELETE FROM proxies WHERE proxy_id = ?
        ''', (proxy_id,))
        print("==> delete proxy success!")
    elif ip != None:
        cursor.execute('''
        DELETE FROM proxies WHERE ip = ?
        ''', (ip,))
        print("==> delete proxy success!")
    else:
        print("==> delete error!")
    
    conn.commit()
    conn.close()


def delete_user_agent(user_agent_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if user_agent_id != None:
        cursor.execute('''
        DELETE FROM user_agents WHERE user_agent_id = ?
        ''', (user_agent_id,))
        print("==> delete proxy success!")
    else:
        print("==> delete error!")
    
    conn.commit()
    conn.close()



def delete_viewport(viewport_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if viewport_id != None:
        cursor.execute('''
        DELETE FROM viewports WHERE viewport_id = ?
        ''', (viewport_id,))
        print("==> delete viewport success!")
    else:
        print("==> delete error!")
    
    conn.commit()
    conn.close()


def delete_geolocation(geolocation_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if geolocation_id != None:
        cursor.execute('''
        DELETE FROM geolocations WHERE geolocation_id = ?
        ''', (geolocation_id,))
        print("==> delete geolocation success!")
    else:
        print("==> delete error!")
    
    conn.commit()
    conn.close()



def delete_context(context_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if context_id != None:
        cursor.execute('''
        DELETE FROM contexts WHERE context_id = ?
        ''', (context_id,))
        print("==> delete context success!")
    else:
        print("==> delete error!")
    
    conn.commit()
    conn.close()

def delete_ttc_account(ttc_account_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if ttc_account_id != None:
        cursor.execute('''
        DELETE FROM ttc_accounts WHERE ttc_account_id = ?
        ''', (ttc_account_id,))
        print("==> delete ttc_account success!")
    else:
        print("==> delete error!")
    
    conn.commit()
    conn.close()


def insert_proxy_action(var):
    if len(var) == 2:
        print(f"\ninsert proxy {var[0]}:{var[1]}")
        command = input("y/n: ")
        match command:
            case 'y':
                insert_proxy(var[0],var[1])
    elif len(var) == 4:
        print(f"\ninsert proxy {var[0]}:{var[1]}:{var[2]}:{var[3]}")
        command = input("y/n: ")
        match command:
            case 'y':
                insert_proxy(var[0],var[1],var[2],var[3])
    else:
        print("command not found!")


def insert_user_agent_action(var):
    if len(var)==0:
        command = input("are you insert user agent? y/n: ")
        var.append(command)
    match var[0]:
        case 'y':
            user_agent = input("\ninput user agent: ")
            command = input(f"\nuser_agent={user_agent}\nare you insert? y/n: ")
            match command:
                case 'y':
                    insert_user_agent(user_agent)
        case _:
            print("command not found!")


def insert_viewport_action(var):
    if len(var)==0:
        command = input("are you insert viewport? y/n: ")
        var.append(command)
    match var[0]:
        case 'y':
            width = input("\ninput width: ")
            height = input("input height: ")
            if width=="" or height=="":
                print("variable not none!")
            else: 
                command = input(f"\nviewport={width}.{height}\nare you insert? y/n: ")
                match command:
                    case 'y':
                        insert_viewport(width, height)
        case _:
            print("command not found!")


def insert_geolocation_action(var):
    if len(var)==0:
        command = input("are you insert geolocation? y/n: ")
        var.append(command)
    match var[0]:
        case 'y':
            longitude = input("\ninput longitude: ")
            latitude = input("input latitude: ")
            if longitude=="" or latitude=="":
                print("variable not none!")
            else: 
                command = input(f"\ngeolocation={longitude}.{latitude}\nare you insert? y/n: ")
                match command:
                    case 'y':
                        insert_geolocation(longitude, latitude)
        case _:
            print("command not found!")


def insert_context_action(var):
    if len(var)==0:
        command = input("are you insert context? y/n: ")
        var.append(command)
    match var[0]:
        case 'y':
            user_agent_id = input("\ninput user_agent_id: ")
            viewport_id = input("input viewport_id: ")
            locale = input("input locale: ")
            timezone_id = input("input timezone_id: ")
            geolocation_id = input("input geolocation_id: ")
            check = True
            print("\nuser agent:")
            rows=search_user_agent(user_agent_id)
            if rows == 0:
                check = False
                print(f"==> user agent no data")
            print("\nviewport:")
            rows=search_viewport(viewport_id)
            if rows == 0:
                check = False
                print(f"==> viewport no data")
            print(f"\nlocale: {locale}")
            print(f"\ntimezone_id: {timezone_id}")
            print("\ngeolocation:")
            rows=search_geolocation(geolocation_id)
            if rows == 0:
                check = False
                print(f"==> geolocation no data")
            if check:
                command = input(f"\nnare you insert? y/n: ")
                match command:
                    case 'y':
                        insert_context(user_agent_id, viewport_id, locale, timezone_id, geolocation_id)
        case _:
            print("command not found!")


def insert_ttc_account_action(var):
    if len(var)==0:
        command = input("are you insert ttc_account? y/n: ")
        var.append(command)
    match var[0]:
        case 'y':
            username = input("\ninput username: ")
            password = input("input password: ")
            access_token = input("input access_token: ")
            command = input(f"are you insert? y/n: ")
            if username=="" or password=="":
                print("variable not none!")
            else:
                match command:
                    case 'y':
                        insert_ttc_account(username, password, access_token)
            
        case _:
            print("command not found!")


def insert_proxy(ip, port, username=None, password=None):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO proxies (ip, port, username, password)
    VALUES (?, ?, ?, ?)
    ''', (ip, port, username, password))

    conn.commit()
    conn.close()
    print("==> insert proxy success!")


def insert_user_agent(user_agent):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO user_agents (user_agent)
    VALUES (?)
    ''', (user_agent,))

    conn.commit()
    conn.close()
    print("==> insert user agent success!")



def insert_viewport(width, height):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO viewports (width, height)
    VALUES (?,?)
    ''', (width, height,))

    conn.commit()
    conn.close()
    print("==> insert viewport success!")


def insert_geolocation(longitude, latitude):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO geolocations (longitude, latitude)
    VALUES (?,?)
    ''', (longitude, latitude,))

    conn.commit()
    conn.close()
    print("==> insert geolocation success!")


def insert_context(user_agent_id, viewport_id, locale, timezone_id, geolocation_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO contexts (user_agent_id, viewport_id, locale, timezone_id, geolocation_id)
    VALUES (?,?,?,?,?)
    ''', (user_agent_id, viewport_id, locale, timezone_id, geolocation_id,))

    conn.commit()
    conn.close()
    print("==> insert context success!")


def insert_ttc_account(username, password, access_token=None):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO ttc_accounts (username, password, access_token)
    VALUES (?, ?, ?)
    ''', (username, password, access_token))

    conn.commit()
    conn.close()
    print("==> insert ttc_account success!")


def delete_data(table_name, key=None, value=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        if key != None:
            if type(value)==str:
                cursor.execute(f"DELETE FROM {table_name} WHERE {tables[table_name][key]} = '{value}'")
            else:
                cursor.execute(f"DELETE FROM {table_name} WHERE {tables[table_name][key]} = {value}")
        else:
            cursor.execute(f"DELETE FROM {table_name}")
        print(f"==> delete {table_name} success!")
        conn.commit()
    except sqlite3.Error as e:
        print(f"==> error '{table_name}': {e}")
    finally:
        conn.close()

def search_data(table_name, key=None, value=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        if key != None:
            if type(value)==str:
                cursor.execute(f"SELECT * FROM {table_name} WHERE {tables[table_name][key]} = '{value}'")
            else:
                cursor.execute(f"SELECT * FROM {table_name} WHERE {tables[table_name][key]} = {value}")
        else:
            cursor.execute(f"SELECT * FROM {table_name}")
            
        rows = cursor.fetchall()
        if rows:
            data=[]
            for row in rows:
                index = 0
                d={}
                for item in tables[table_name]:
                    d[item]=row[index]
                    index+=1
                data.append(d)
            return data
        else:
            print(f"\n==> table '{table_name}' no data.")

    except sqlite3.Error as e:
        print(f"==> error '{table_name}': {e}")
    finally:
        conn.close()

def update_data(table_name, data, key=None, value=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        values = tuple(data.values())
        sql = f"UPDATE {table_name} SET ({columns}) VALUES ({placeholders}) WHERE {tables[table_name][0]} = {id}"
        if key != None:
            if type(value)==str:
                sql = f"UPDATE {table_name} SET ({columns}) VALUES ({placeholders}) WHERE {tables[table_name][key]} = '{value}'"
            else:
                sql = f"UPDATE {table_name} SET ({columns}) VALUES ({placeholders}) WHERE {tables[table_name][key]} = {value}"
            cursor.execute(sql, values)
        else:
            sql = f"UPDATE {table_name} SET ({columns}) VALUES ({placeholders})"
            cursor.execute(sql)
        conn.commit()
        print(f"==> updade {table_name} success!")
    except sqlite3.Error as e:
        print(f"==> updade error: {e}")
    finally:
        conn.close()


def update_proxy_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nupdate proxy id: {var[0]}")
                rows = search_proxy(var[0],)
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("are you update? y/n: ")
                    match command:
                        case 'y':
                            ip = input("input ip (enter=none): ")
                            port = input("input port (enter=none): ")
                            username = input("input username (enter=none): ")
                            password = input("input password (enter=none): ")
                            if ip=="":
                                ip = None
                            if port=="":
                                port = None
                            if username=="":
                                username = None
                            if password=="":
                                password = None
                            command = input(f"\nproxy={ip}:{port}:{username}:{password}\nare you update? y/n: ")
                            match command:
                                case 'y':
                                    update_proxy(var[0],ip,port,username,password)
            case _:
                print("command not found!")

###################

def update_user_agent_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nupdate user agent id: {var[0]}")
                rows = search_user_agent(var[0])
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("are you update? y/n: ")
                    match command:
                        case 'y':
                            user_agent = input("input user agent: ")
                            command = input(f"\nuser_agent={user_agent}\nare you update? y/n: ")
                            match command:
                                case 'y':
                                    update_user_agent(var[0],user_agent)
            case _:
                print("command not found!")


###################

def update_viewport_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nupdate viewport id: {var[0]}")
                rows = search_viewport(var[0])
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("are you update? y/n: ")
                    match command:
                        case 'y':
                            width = input("\ninput width: ")
                            height = input("input height: ")
                            if width=="":
                                width = None
                            if height=="":
                                height = None
                            command = input(f"\nviewport={width}.{height}\nare you update? y/n: ")
                            match command:
                                case 'y':
                                    update_viewport(var[0],width, height)
            case _:
                print("command not found!")


###################

def update_geolocation_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nupdate geolocation id: {var[0]}")
                rows = search_geolocation(var[0])
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("are you update? y/n: ")
                    match command:
                        case 'y':
                            longitude = input("\ninput longitude: ")
                            latitude = input("input latitude: ")
                            if longitude=="":
                                longitude = None
                            if latitude=="":
                                latitude = None
                            command = input(f"\ngeolocation={longitude}x{latitude}\nare you update? y/n: ")
                            match command:
                                case 'y':
                                    update_geolocation(var[0],longitude, latitude)
            case _:
                print("command not found!")

###################

def update_context_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nupdate context id: {var[0]}")
                rows = search_context(var[0])
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("are you update? y/n: ")
                    match command:
                        case 'y':
                            user_agent_id = input("\ninput user_agent_id: ")
                            viewport_id = input("input viewport_id: ")
                            locale = input("input locale: ")
                            timezone_id = input("input timezone_id: ")
                            geolocation_id = input("input geolocation_id: ")
                            
                            if user_agent_id=="":
                                user_agent_id = None
                            if viewport_id=="":
                                viewport_id = None
                            if locale=="":
                                locale = None
                            if timezone_id=="":
                                timezone_id = None
                            if geolocation_id=="":
                                geolocation_id = None
                            
                            check = True
                            if user_agent_id:
                                print("\nuser agent:")
                                rows=search_user_agent(user_agent_id)
                                if rows == 0:
                                    check = False
                                    print(f"==> user agent no data")
                            if viewport_id:
                                print("\nviewport:")
                                rows=search_viewport(viewport_id)
                                if rows == 0:
                                    check = False
                                    print(f"==> viewport no data")
                            if locale:
                                print(f"\nlocale: {locale}")
                            if timezone_id:
                                print(f"\ntimezone_id: {timezone_id}")
                            if geolocation_id:
                                print("\ngeolocation_id:")
                                rows=search_geolocation(geolocation_id)
                                if rows == 0:
                                    check = False
                                    print(f"==> geolocation no data")

                            if check:
                                command = input(f"\nare you update? y/n: ")
                                match command:
                                    case 'y':
                                        update_context(var[0],user_agent_id, viewport_id, locale, timezone_id, geolocation_id)
            case _:
                print("command not found!")

############

def update_ttc_account_action(var):
    if len(var)!=2:
        print("command not found!")
    else:
        match var[0]:
            case '-id':
                var.pop(0)
                print(f"\nupdate geolocation id: {var[0]}")
                rows = search_geolocation(var[0])
                if rows == 0:
                    print(f"==> no data")
                else:
                    command = input("are you update? y/n: ")
                    match command:
                        case 'y':
                            longitude = input("\ninput longitude: ")
                            latitude = input("input latitude: ")
                            if longitude=="":
                                longitude = None
                            if latitude=="":
                                latitude = None
                            command = input(f"\ngeolocation={longitude}x{latitude}\nare you update? y/n: ")
                            match command:
                                case 'y':
                                    update_geolocation(var[0],longitude, latitude)
            case _:
                print("command not found!")


def update_proxy(proxy_id, ip=None, port=None, username=None, password=None):
    conn = connect_db()
    cursor = conn.cursor()

    updates = []
    params = []

    if ip is not None:
        updates.append("ip = ?")
        params.append(ip)
    if port is not None:
        updates.append("port = ?")
        params.append(port)
    if username is not None:
        updates.append("username = ?")
        params.append(username)
    if password is not None:
        updates.append("password = ?")
        params.append(password)
    
    if not updates:
        print("==> no data.")
        conn.close()
        return

    sql = f"UPDATE proxies SET {', '.join(updates)} WHERE proxy_id = ?"
    params.append(proxy_id)

    # Thực thi câu lệnh SQL
    cursor.execute(sql, params)
    
    conn.commit()
    conn.close()
    print("==> update proxy success!")


##################

def update_user_agent(user_agent_id, user_agent):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE user_agents SET user_agent = ? WHERE user_agent_id = ?
        ''', (user_agent, user_agent_id,))
    
    conn.commit()
    conn.close()
    print("==> update user agent success!")


##################


def update_viewport(viewport_id, width=None, height=None):
    conn = connect_db()
    cursor = conn.cursor()

    updates = []
    params = []

    if width is not None:
        updates.append("width = ?")
        params.append(width)
    if height is not None:
        updates.append("height = ?")
        params.append(height)
    
    if not updates:
        print("==> no data.")
        conn.close()
        return

    sql = f"UPDATE viewports SET {', '.join(updates)} WHERE viewport_id = ?"
    params.append(viewport_id)

    cursor.execute(sql, params)
    
    conn.commit()
    conn.close()
    print("==> update viewport success!")

##################


def update_geolocation(geolocation_id, longitude=None, latitude=None):
    conn = connect_db()
    cursor = conn.cursor()

    updates = []
    params = []

    if longitude is not None:
        updates.append("longitude = ?")
        params.append(longitude)
    if latitude is not None:
        updates.append("latitude = ?")
        params.append(latitude)
    
    if not updates:
        print("==> no data.")
        conn.close()
        return

    sql = f"UPDATE geolocations SET {', '.join(updates)} WHERE geolocation_id = ?"
    params.append(geolocation_id)

    cursor.execute(sql, params)
    
    conn.commit()
    conn.close()
    print("==> update geolocation success!")

##################

def update_context(context_id, user_agent_id=None, viewport_id=None, locale=None, timezone_id=None, geolocation_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    updates = []
    params = []

    if user_agent_id is not None:
        updates.append("user_agent_id = ?")
        params.append(user_agent_id)
    if viewport_id is not None:
        updates.append("viewport_id = ?")
        params.append(viewport_id)
    if locale is not None:
        updates.append("locale = ?")
        params.append(locale)
    if timezone_id is not None:
        updates.append("timezone_id = ?")
        params.append(timezone_id)
    if geolocation_id is not None:
        updates.append("geolocation_id = ?")
        params.append(geolocation_id)
    
    if not updates:
        print("==> no data.")
        conn.close()
        return

    sql = f"UPDATE contexts SET {', '.join(updates)} WHERE context_id = ?"
    params.append(context_id)

    cursor.execute(sql, params)
    
    conn.commit()
    conn.close()
    print("==> update context success!")


####################

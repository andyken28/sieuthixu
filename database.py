import sqlite3

def connect_db():
    return sqlite3.connect('sieuthixu.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS proxies (
        proxy_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT NOT NULL,
        port TEXT NOT NULL,
        username TEXT,
        password TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_agents (
        user_agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_agent TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS viewports (
        viewport_id INTEGER PRIMARY KEY AUTOINCREMENT,
        width INTEGER NOT NULL,
        height INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS geolocations (
        geolocation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        longitude FLOAT NOT NULL,
        latitude FLOAT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contexts (
        context_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_agent_id INTEGER NOT NULL,
        viewport_id INTEGER NOT NULL,
        locale TEXT NOT NULL,
        timezone_id TEXT NOT NULL,
        geolocation_id INTEGER NOT NULL
    )
    ''')

########################

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ttc_accounts (
        ttc_account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        access_token TEXT NOT NULL
    )
    ''')

########################

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fb_accounts (
        fb_account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT NOT NULL,
        password TEXT NOT NULL,
        otp_2fa TEXT NULL,
        mail TEXT NULL,
        password_mail TEXT NULL,
        cookie TEXT NULL
    )
    ''')

########################

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fb_proxy_couples (
        fb_proxy_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fb_account_id INTEGER NOT NULL,
        proxy_id INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ttc_fb_couples (
        ttc_fb_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ttc_account_id INTEGER NOT NULL,
        fb_account_id INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS proxy_context_couples (
        proxy_context_id INTEGER PRIMARY KEY AUTOINCREMENT,
        proxy_id INTEGER NOT NULL,
        context_id INTEGER NOT NULL
    )
    ''')

########################
    conn.commit()
    conn.close()

tables={
    "proxies":["proxy_id","ip", "port", "username", "password"],
    "user_agents":["user_agent_id", "user_agent"],
    "viewports":["viewport_id", "width", "height"],
    "geolocations":["geolocation_id", "longitude", "latitude"],
    "contexts":["context_id", "user_agent_id", "viewport_id", "locale", "timezone_id", "geolocation_id"],

    "ttc_accounts":["ttc_account_id", "username", "password", "access_token"],
    "fb_accounts":["fb_account_id", "uid", "password", "otp_2fa", "mail", "password_mail", "cookie"],

    "fb_proxy_couples":["fb_proxy_id", "fb_account_id", "proxy_id"],
    "ttc_fb_couples":["ttc_fb_id", "ttc_account_id", "fb_account_id"],
    "proxy_context_couples":["proxy_context_id", "proxy_id", "context_id"]
}
# 0:int, 1:string, 2:float, 3: date
types={
    "proxies":[0,1,1,1,1],
    "user_agents":[0,1],
    "viewports":[0,0,0],
    "geolocations":[0,2,2],
    "contexts":[0,0,0,1,1,0],

    "ttc_accounts":[0, 1, 1, 1],
    "fb_accounts":[0, 1, 1, 1, 1, 1],

    "fb_proxy_couples":[0, 0, 0],
    "ttc_fb_couples":[0, 0, 0],
    "proxy_context_couples":[0, 0, 0]
}
# 0:null 1:not null
not_nulls={
    "proxies":[1,1,1,0,0],
    "user_agents":[1,1],
    "viewports":[1,1,1],
    "geolocations":[1,1,1],
    "contexts":[1,1,1,1,1,1],

    "ttc_accounts":[1, 1, 1, 0],
    "fb_accounts":[1, 1, 0, 0, 0, 0],

    "fb_proxy_couples":[1, 1, 1],
    "ttc_fb_couples":[1, 1, 1],
    "proxy_context_couples":[1, 1, 1]
}
primary_keys={
    "proxy_id":"proxies",
    "user_agent_id":"user_agents",
    "viewport_id":"viewports",
    "geolocation_id":"geolocations",
    "context_id":"contexts",

    "ttc_account_id":"ttc_accounts",
    "fb_account_id":"fb_accounts",

    "fb_proxy_id":"fb_proxy_couples",
    "ttc_fb_id":"ttc_fb_couples",
    "proxy_context_id":"proxy_context_couples"
}
foreign_keys={
    "user_agent_id":"user_agent",
    "viewport_id":"viewport",
    "geolocation_id":"geolocation",

    "fb_account_id":"fb_account",
    "proxy_id":"proxy",
    "ttc_account_id":"ttc_account",
    "context_id":"context"
}
def get_foreign_keys():
    return foreign_keys

def get_primary_keys():
    return primary_keys

def get_type(table_name, index):
    return types[table_name][index]

def get_null(table_name, index):
    return not_nulls[table_name][index]

def get_variable(table_name):
    return tables[table_name]

def insert_data(table_name, data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        values = tuple(data.values())

        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        cursor.execute(sql, values)
        conn.commit()
        
        print(f"==> insert {table_name} success!")
    except sqlite3.Error as e:
        print(f"==> insert rror: {e}")
    finally:
        conn.close()

def delete_data(table_name, key=None, value=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        if key is not None:
            sql = f"DELETE FROM {table_name} WHERE {tables[table_name][key]} = ?"
            cursor.execute(sql, (value,))
        else:
            sql = f"DELETE FROM {table_name}"
            cursor.execute(sql)

        # Thực thi và xác nhận
        conn.commit()
        print(f"==> delete {table_name} success!")
    except sqlite3.Error as e:
        print(f"==> error '{table_name}': {e}")
    finally:
        conn.close()

def update_data(table_name, data, key=None, value=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        set_clause = ', '.join([f"{col} = ?" for col in data.keys()])
        values = tuple(data.values())

        if key is not None and value is not None:
            sql = f"UPDATE {table_name} SET {set_clause} WHERE {tables[table_name][key]} = ?"
            values += (value,)
        else:
            sql = f"UPDATE {table_name} SET {set_clause}"

        cursor.execute(sql, values)
        conn.commit()

        print(f"==> update {table_name} success!")
    except sqlite3.Error as e:
        print(f"==> update error: {e}")
    finally:
        conn.close()


def get_data(table_name, id=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        data=[]
        if id:
            cursor.execute(f"SELECT * FROM {table_name} WHERE {tables[table_name][0]} = {id}")
        else:
            cursor.execute(f"SELECT * FROM {table_name}")
        
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                index = 0
                d={}
                for item in tables[table_name]:
                    if index != 0 and item in foreign_keys:
                        foreign_table=primary_keys[item]
                        foreign_data=get_data(foreign_table,row[index])[0]

                        del foreign_data[tables[foreign_table][0]]
                        if len(tables[primary_keys[item]])==2:
                            d[foreign_keys[item]]=foreign_data[tables[foreign_table][1]]
                        else:
                            d[foreign_keys[item]]=foreign_data
                    else:
                        d[item]=row[index]
                    index+=1
                data.append(d)
        else:
            print(f"\n==> table '{table_name}' no data.")
            
    except sqlite3.Error as e:
        print(f"==> error '{table_name}': {e}")
        return []
    finally:
        conn.close()
        return data

def search_data(table_name, key=None, value=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        if key != None:
            sql = f"SELECT * FROM {table_name} WHERE {tables[table_name][key]} = ?"
            cursor.execute(sql, (value,))
        else:
            sql = f"SELECT * FROM {table_name}"
            cursor.execute(sql)
            
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

def show_table_data(table_name):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if rows:
            print(f"\n==> datas in table '{table_name}':")
            for row in rows:
                index = 0
                d={}
                for item in tables[table_name]:
                    d[item]=row[index]
                    index+=1
                print(d)
        else:
            print(f"\n==> table '{table_name}' no data.")

    except sqlite3.Error as e:
        print(f"==> error '{table_name}': {e}")
    finally:
        conn.close()

###########

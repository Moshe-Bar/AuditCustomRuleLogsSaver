import sqlite3

from audit_log import ALog, log_0
table_columns = '(time_stamp, utf, log_index, event_type, full_log, log_key, user, dir)'
def db_preparation(cur, table_name):
    sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (
	id integer PRIMARY KEY AUTOINCREMENT,
	time_stamp text NOT NULL,
    utf real,
    log_index integer,
    event_type text NOT NULL,
    full_log text NOT NULL UNIQUE,
    log_key text,
    user text,
    dir text
	);'''
    res = cur.execute(sql)
    res.fetchall()


def open_db_connection(sql_connection_string):
    '''
    returns db connection aand cursor
    '''
    try:
        con = sqlite3.connect(sql_connection_string)
        cur = con.cursor()
        return cur, con
    except Exception:
        pass

def save_new_data(logs:[], db_cur, db):
    '''
    Gets list of serialized logs and insert them into the DB
    '''
    # todo sql injection
    
    if not logs:
        print('got empty list to save')
        return
    sql = f"INSERT INTO Logs {table_columns} VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
    log_tuples = list(map(lambda log:log.fields(),logs))
    try:
        db_cur.executemany(sql, log_tuples)
        db.commit()
    except sqlite3.IntegrityError as error:
        print(f'error while trying to add rows, log row should be unique.\n{error}')    

def close_db_connection(db):
    '''
    close connection of DB
    '''
    db.close()

def latest_log(db_cur) -> []:
    '''
    returns newest log utf in db
    '''
    sql = '''SELECT t.time_stamp, [Max(utf)], MAX(t.log_index), t.event_type, t.full_log, t.log_key, t.user, dir
                FROM 
                (SELECT time_stamp, MAX(utf), log_index, event_type, full_log, log_key, user, dir 
                    FROM Logs) t;'''
    db_cur.execute(sql)
    last_log_time = db_cur.fetchone()
    # in case the db is empty log_0 is used (definition in audit_log.py file)
    if last_log_time:
        return ALog(*last_log_time)
    else:
        return log_0

from db_utility import close_db_connection, db_preparation, latest_log, open_db_connection, save_new_data
from files_utility import CONFIG, read_audit_log



def main():
    # open new connection to local sqlite db
    cur, db = open_db_connection(CONFIG['sql_con'])
    # create table if not exists for first use
    db_preparation(cur, CONFIG['main_table_name'])
    # get id of last log inserted to db in order to filter new logs
    last_log = latest_log(cur)
    # read logs from local files
    new_logs = read_audit_log(CONFIG, last_log)
    # save new logs to db
    print(f'{len(new_logs)} New logs are inserted')
    save_new_data(new_logs, cur, db)
    # end and close the db
    close_db_connection(db)


if __name__ == '__main__':
    main()

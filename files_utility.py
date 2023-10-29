from datetime import datetime
import re
import yaml
import os

from audit_log import ALog

def first_and_last_logs(data):
    '''
    return last and first logs
    '''
    logs = list(re.finditer(CONFIG['log_regex'],data))
    
    first_log = ALog(regex_match=logs[0])
    last_log = ALog(regex_match=logs[-1])
    return first_log, last_log

def read_and_serialize(data,filter_log:ALog):
    '''
    filter by ALog object method
    '''
    serialized_logs = list(filter(lambda new_log:new_log > filter_log,map(lambda match: ALog(regex_match=match),re.finditer(CONFIG['log_regex'], data))))
    return serialized_logs

def read_audit_log(config, latest_log_in_db:ALog) -> [str]:
    '''
    Reads auditd logs file 
    return list of maped log as a tuple
    '''
    audit_log_dir = config['audit_log_dir']
    audit_log_file_regex = config['audit_log_file']
    
    # for reading all auditd log files iused regex
    log_files_path = ''.join(sorted(list(map(lambda file:audit_log_dir+'/'+file,os.listdir(audit_log_dir)))))
    proper_log_files = list(map(lambda match:match.group(0),re.finditer(audit_log_dir+'/'+audit_log_file_regex, log_files_path)))
    # appends all relevant log files data 
    all_files_data = ''

    # the order of log files is from newest to the oldest
    # in the process if log file not relevant becuase it contains older logs than DB logs
    # there us a 'break' and the the other log files are not going to be proccessed
    for log_file in proper_log_files:
        try:
            with open(log_file, 'r') as f:
                file_data = f.read()    
                print(f'file opend: {log_file}')
                first_log, last_log = first_and_last_logs(file_data)
                
                # not relevant file
                if last_log < latest_log_in_db:
                    break
                
                # relevant file and the oldestmayby also
                elif latest_log_in_db < first_log:
                    print('in if 2')
                    all_files_data+=file_data

                # first_log < latest_db_log < last_log
                # relevant file but the remaining files not
                else:
                    all_files_data+=file_data
                    break
               
        except IOError as error:
            print(f"couldn't read audit logs file, make sure the file exists and path in config file correct: {error}")
    serialized_log_list = read_and_serialize(all_files_data,latest_log_in_db)        
    return serialized_log_list



# For configuration file i used yaml format in order to achieve less complexity for regex string
def read_config():
    '''
    Reads config yaml file
    return al values as dict
    '''
    try:
        with open('config.yaml', 'r') as conf:
            return yaml.safe_load(conf)
    except IOError as error:
        print(f"couldn't read configuration file: {error}")

CONFIG = read_config()
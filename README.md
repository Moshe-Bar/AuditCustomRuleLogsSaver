# Audit deamon custom rule logs saver
This tool reads logs of Audit deamon service and savig them in local sqlite-db.


The tool is intended for those who want to monitor system logs that were written due to system actions that were activated and that had to be detected according to Auditd rules


## Acknowledgements
 - [Auditd overview](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/chap-system_auditing)
 - [Auditd logs explanation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-understanding_audit_log_files)
 - [Auditd rules overview](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-defining_audit_rules_and_controls)



## Authors


- [@https://github.com/Moshe-Bar]()



## Run Locally

Using Ubuntu 22 as OS

Install dependencies

```bash
apt -y update
apt install python3
```
```bash
git clone  https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver.git
cd AuditCustomRuleLogsSaver
```

## Usage/Examples

Start the script


```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt  
```
```bash
python3 main.py
```


## Screenshots

Important notes!
- Those are non persistent rules which means that after the Auditd service restarts they will be deleted. more info on: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sec-defining_audit_rules_and_controls_in_the_audit.rules_file

- For executing SQL queries i used Ubuntu tool called: "DB Browser for SQLite",
the tool can be found and downloaded from Ubuntu store app.




-----

[Adding rule 1 to Auditd:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/adding%20rule%201.png)

command: 
```bash
auditctl -a always,exit -F arch=b64 -S rename,unlink,unlinkat,renameat -F key=file_dir_delete 
```

In this example we see no custom rules exist yet and after adding the first rule it shows up in the list of rules.
this rule should tell audit service to watch after all actions of type "rename", "renameat" "unlink" and "unlinkat" meaning all deletion of directory or file in all system and create logs for all those actions.

![Adding rule 1 to Auditd](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/adding%20rule%201.png)

-----

[New logs created for the first custom rule:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/rule%201%20logs.png)

command:
```bash
ausearch -k file_dir_delete
```

![Rule 1 logs](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/rule%201%20logs.png)

-----

[Adding rule 2 to Auditd:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/adding%20rule%202.png)

command:
```bash
auditctl -w /home/mo/file_changes.txt -p wa -k write_file_watch
```
 
Adding the second rule to Auditd.
this rule will make audit to watch after a specific file called file_changes.txt whether the file content is changed or its attributes changes: 

![Adding rule 2 to Auditd](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/adding%20rule%202.png)

-----

[New logs created for the second custom rule:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/rule%202%20logs.png)

command:
```bash
ausearch -k write_file_watch
```

![Rule 2 logs](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/rule%202%20logs.png)

-----

[After the script run's for the first time those records where added to the db:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/logs%20in%20db.png)

command:
```sql
SELECT *
FROM Logs;
```

![Logs in DB](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/logs%20in%20db.png)

-----

[After first run there is query for new records from 1698322018 date and on (Thu Oct 26 2023 15:06:58), there are no new records so the query returns 0.
utf stands for unix-time-format although the popular name is UTS (Unix-time-stamp):](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/before%20second%20run.png)

command:
```sql
SELECT COUNT(*) 
FROM Logs
WHERE utf>16983220180.542;
```

![Query for new records](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/before%20second%20run.png)

-----

[After the second run there are more records in db so the same query as before results new records:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/after%20second%20run.png)

command:
```sql
SELECT COUNT(*) 
FROM Logs
WHERE utf>16983220180.542;

```

![Query for new records after second run](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/after%20second%20run.png)

-----

[Query for search the number of different types of rules in db:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/types%20of%20rules.png)

command:
```sql
SELECT COUNT(DISTINCT log_key)
FROM Logs;
```

![Query for number of rules](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/types%20of%20rules.png)

-----

[Query for search the most frequent rule type of logs:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/rule%201.png)


command:
```SQL
SELECT log_key
FROM Logs
GROUP BY log_key
LIMIT 1;
```

![Most frequent rule logs](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/rule%201.png)

-----

[Query for all logs of rule 1:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/filter%20by%20rule%201%20in%20db.png)

command:
```SQL
SELECT * 
FROM Logs 
WHERE log_key = 'file_dir_delete' 
LIMIT 10;
```

![Rule 1 logs](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/filter%20by%20rule%201%20in%20db.png)

-----

[Query for all logs of rule 2:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/filter%20by%20rule2%20in%20db.png)

command:
```SQL
SELECT * 
FROM Logs 
WHERE log_key = 'write_file_watch' 
LIMIT 10;
```

![Rule 2 logs](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/filter%20by%20rule2%20in%20db.png)

-----

[Query for least frequent rule:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/least%20frequent%20rule.png)

command:
```SQL
SELECT log_key AS Least_frequent_rule 
FROM Logs 
GROUP BY log_key
ORDER BY log_key DESC
LIMIT 1;
```

![Least frequent rule](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/least%20frequent%20rule.png)

-----

[Query for most frequent dir of files caused the logs event:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/most%20frequent%20dir.png)

command:
```SQL
SELECT dir AS Most_frequent_directory 
FROM Logs 
GROUP BY dir
LIMIT 1;
```

![Most frequent dir](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/most%20frequent%20dir.png)

-----

[Query for most frequent rule caused the logs event:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/most%20frequent%20rule.png)

command:
```SQL
SELECT log_key AS Most_frequent_rule
FROM Logs 
GROUP BY log_key
LIMIT 1;
```

![Most frequent rule](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/most%20frequent%20rule.png)

-----

[Query for most frequent user responsible of the logs event:](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/most%20frequent%20user.png)

command:
```SQL
SELECT user AS Most_frequent_user
FROM Logs 
GROUP BY user
LIMIT 1;
```

![Most frequent user](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/most%20frequent%20user.png)

-----
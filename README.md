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
Those are non persistent rules which means that after the Auditd service restarts they will be deleted.
more info on: (https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sec-defining_audit_rules_and_controls_in_the_audit.rules_file)

Adding rule 1 to Auditd:
command: auditctl -a always,exit -F arch=b64 -S rename,unlink,unlinkat,renameat -F key=file_dir_delete 
in this example we see no custom rules exist yet and after adding the first rule it shows up in the list of rules.
this rule should tell audit service to watch after all actions of type "rename", "renameat" "unlink" and "unlinkat" meaning all deletion of directory or file in all system and create logs for all those actions.
![Adding rule 1 to Auditd](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/adding%20rule%201.png)


Adding rule 2 to Auditd: 
command: auditctl -w /home/mo/file_changes.txt -p wa -k write_file_watch
adding the second rule to Auditd.
this rule will make audit to watch after a specific file called file_changes.txt whether the file content is changed or its attributes changes. 
![Adding rule 1 to Auditd](https://github.com/Moshe-Bar/AuditCustomRuleLogsSaver/blob/develop/screenshots/adding%20rule%202.png)
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

![Adding rule 1 to Auditd](\screenshots\adding rule 1.png)



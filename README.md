
# Audit deamon custom rule logs saver
This tool reads logs of Audit deamon service and savig them in local sqlite-db.


The tool is intended for those who want to monitor system logs that were written due to system actions that were activated and that had to be detected according to Auditd rules


## Acknowledgements
 - [Audit overview](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/chap-system_auditing)
 - [Audit logs explanation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-understanding_audit_log_files)
 - [Audt rules overview](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-defining_audit_rules_and_controls)



## Authors


- [@https://github.com/Moshe-Bar]()



## Run Locally

Using Ubuntu 22 as OS
Go to the project directory

Install dependencies

```bash
  apt -y update
  apt install python3
```

Start the script


```bash
  python3 -m venv venv
```
```
  pip install -r requirements.txt  
```


## Usage/Examples

```
python3 main.py
```
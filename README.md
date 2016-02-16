Overview
--------
Gerrit hooks. 
 - update JIRA issue

Installation Steps
-------------------
 - copy dist/grrit-jira-hook.tar to Gerrit instance server
 - install dependencies and copy hooks to gerrit install path

 ```
    mkdir install
    tar -xvf grrit-jira-hook.tar -C install
    cd install
    chmod +x install.sh
    GERRIT_PATH=<gerrit_install_path> ./install.sh
 ```
 - config file. Edit config file at hooks/jira-hook.config.
 - check gerrit permission.
 
```
ssh -p 29418 admin@localhost gerrit
```
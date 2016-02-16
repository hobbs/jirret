Overview
--------
Gerrit hooks. 
 - update JIRA issue

Installation Steps
-------------------
 - copy dist/grrit-jira-hook.tar to Gerrit instance server
 
 ```
 wget https://github.com/defrur/jirret/releases/download/v0.1/gerrit-jira-hook.tar.gz
 ```
 
 - install dependencies and copy hooks to gerrit install path

 ```
    mkdir install
    tar -xzvf gerrit-jira-hook.tar.gz -C install
    cd install
    chmod +x install.sh
    GERRIT_PATH=<gerrit_install_path> ./install.sh
 ```
 - config file. Edit config file at hooks/jira-hook.config.
 - check gerrit permission.
 
```
ssh -p 29418 admin@localhost gerrit
```

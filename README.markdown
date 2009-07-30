mytopg - A naive mysql to postgresql dump converter
================

Kinda like money laundering... reads in a dirty mysql dump and outputs clean
postgres statements

Installation
------------

    curl http://github.com/jzellman/mytopg/raw/master/mytopg.py > mytopg &&
    chmod 755 mytopg && 
    sudo mv mytopg /usr/local/bin/mytopg

Use
---
    mysqldump db_name | mytopg | psql db_name
    or
    mysqldump db_name > mysql.dump
    mytopg < mysql.dump > pg.dump


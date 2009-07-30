#!/usr/bin/env python

import re
import sys

# create table conversions
converters = (("`", ""),
              ("int(11) NOT NULL auto_increment", "serial"),
              ("mediumint(9) NOT NULL auto_increment", "serial"),
              ("mediumint(9)", "integer"),
              ("default '0'", ""),
              ("int(11)", "integer"),
              ("tinyint(4)", "integer"),
              ("default CURRENT_TIMESTAMP", ""),
              ("on update CURRENT_TIMESTAMP", ""),
              ("NOT NULL default ''", ""),
              ("User ", "Users "),
              (re.compile("^KEY.*"), ""))


lines = [line.strip() for line in sys.stdin.readlines()]

# Handle printing of table statements
printing = False
sql = []
for line in lines:
    if line.startswith("CREATE TABLE"):
        printing = True
    elif line.startswith(") ENGINE="):
        if sql:
            sql[-1] = re.compile(",$").sub("", sql[-1])
        sys.stdout.writelines(sql)
        sys.stdout.write(");\n")
        sql = []
        printing = False
    if printing:
        for pattern, replacement in converters:
            if type(pattern) is str:
                line = line.replace(pattern, replacement)
            else:
                line = pattern.sub(replacement, line)
        if line.strip(): sql.append(line)

# Handle printing of converted insert statements
for line in lines:
    if line.startswith("INSERT INTO"):
       sys.stdout.write(line.replace("`", "").replace("User", "Users") + "\n")

import pymysql

from pymysql.utils import


conn = pymysql.Connection(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    database='WinJay'
)


import json

import time
import inspect

#CONTANTS

URL = "https://demo.actitime.com/login.do"
UserName = "admin"
PassWord = "manager"



def whoami():
    return inspect.stack()[1][3]

from Python_SQL_Connectivity_module import mycon, cur

def register_user():
    # Registration of new users.
    try:
        username = input('Enter new username: ')
        password = input('Enter new password: ')
        cur.execute("INSERT INTO account VALUES('{}','{}')".format(username, password))
        mycon.commit()
        print('ACCOUNT ADDED SUCCESSFULLY!')
    except:
        print("Username already exists. Please try a different one.")

def login_user():
    # Login of existing users.
    username = input('Enter username: ')
    password = input('Enter password: ')
    cur.execute("SELECT * FROM account WHERE uname = '{}'  AND paswrd = '{}'".format(username, password))
    data = cur.fetchone()
    if data is None:
        print('INVALID USERNAME OR PASSWORD')
        return False
    else:
        print('LOGIN SUCCESSFUL!')
        return True
        
        
        
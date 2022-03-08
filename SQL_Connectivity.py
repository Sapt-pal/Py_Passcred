# ___ RDBMS MODULE ____

# __Data Storage and retrieval module below__

import mysql.connector as sql_conn

conn_obj = sql_conn.connect(host="localhost", user="root", passwd="")

if conn_obj.is_connected():
    print("Connection established...")
    sql_cursor = conn_obj.cursor()
    sql_cursor.execute("CREATE DATABASE IF NOT EXISTS Py_PassCred")
    sql_cursor.execute("USE Py_PassCred")
    print("Py_Pass database created")
    table = "CREATE TABLE IF NOT EXISTS passwords_data (SNo INTEGER AUTO_INCREMENT PRIMARY KEY,site_name VARCHAR(20),site_URL VARCHAR(50),username VARCHAR(20), password VARCHAR(20), password_nature VARCHAR(20) DEFAULT 'Random')"
    sql_cursor.execute(table)


def data_entry(site_name, site_URL, username, password, password_nature="Custom"):
    """
    Actual insertion of data into RDBMS.

    To be called inside "usr_input()" after taking all credentials from user.

    If custom password was set, no value for password_nature to be passed.
    Else if random password was set, pass password_nature as "Random"

    Parameters
    ----------
    site_name : STRING
        .
    site_URL : STRING
        .
    username : STRING
        .
    password : STRING
        .
    password_nature : STRING, optional
        DESCRIPTION. The default is "Custom".

    Returns
    -------
    None.

    """
    cmd = f"INSERT INTO passwords_data (site_name, site_url, username, password, password_nature) VALUES ('{site_name}', '{site_URL}', '{username}', '{password}', '{password_nature}')"
    print(cmd)
    data_entry = cmd
    print("Storing your credentials...")
    try:
        sql_cursor.execute(data_entry)
        conn_obj.commit()
        print("Your data was entered.")
    except:
        err = "Only one password per URL is allowed for data integrity\n Please try again with a unique URL"
        print(err)


def usr_input(pswd="y"):
    """
    Take credentials from user to be input in the DB.

    If random password to be generated, pass pswd = "n" in function call.
    Else if custom password input by user, no value required to be passed.

    Parameters
    ----------
    pswd : STRING, optional
        DESCRIPTION. The default is "y".

    Returns
    -------
    None.

    """
    sName = input("Enter Site Name: ")
    sURL = input("Enter Site URL: ")
    uName = input("Enter Username: ")
    if pswd == "y":
        pswd = input("Enter password: ")
        pswd_nat = "Custom"
    else:
        # pswd = '''Call the password generator func here'''
        pswd_nat = "Random"
    data_entry(sName, sURL, uName, pswd, pswd_nat)
	
	def update_sName(old_sName, new_sName):
    """


    Parameters
    ----------
    old_sName : STRING
        CURRENT SITE NAME.
    new_sName : STRING
        NEW SITE NAME.

    Returns
    -------
    None.

    """
    exc = f"UPDATE TABLE table_temp set site_name = '{new_sName}' where site_name = '{old_sName}'"
    sql_cursor.execute(exc)
    conn_obj.commit()


def update_sURL(sName, new_sURL):
    """


    Parameters
    ----------
    sName : STRING
        CURRENT SITE NAME.
    new_sURL : STRING
        NEW SITE URL.

    Returns
    -------
    None.

    """
    exc = f"UPDATE TABLE table_temp set site_URL = '{new_sURL}' where site_name = '{sName}'"
    sql_cursor.execute(exc)
    conn_obj.commit()


def update_uName(sName, new_uName):
    """


    Parameters
    ----------
    sName : STRING
        CURRENT SITE NAME.
    new_uName : STRING
        NEW USER NAME.

    Returns
    -------
    None.

    """
    exc = f"UPDATE TABLE table_temp set username = '{new_uName}' where site_name = '{sName}'"
    sql_cursor.execute(exc)
    conn_obj.commit()


def update_pswd(uName, new_pswd):
    """


    Parameters
    ----------
    uName : STRING
        USER NAME.
    new_pswd : STRING
        NEW PASSWORD.

    Returns
    -------
    None.

    """
    exc = f"UPDATE TABLE table_temp set password = '{new_pswd}' where username = '{uName}'"
    sql_cursor.execute(exc)
    conn_obj.commit()


def update_cred(choice):
    """


    Parameters
    ----------
    choice : STRING
        INDICATES WHICH DATA IS TO BE MODIFIED.

    Returns
    -------
    None.

    """
    if choice == "1":
        o_sName = input(" Enter old site name: ")
        n_sName = input(" Enter new site name: ")
        update_sName(o_sName, n_sName)
        print(f" Current site name changed to '{n_sName}'")
    elif choice == "2":
        sName = input(" Enter current site name: ")
        n_sURL = input(" Enter new site URL: ")
        update_sURL(sName, n_sURL)
        print(f" Current site URL changed to '{n_sURL}'")
    elif choice == "3":
        sName = input(" Enter current site name: ")
        n_uName = input(" Enter new user name: ")
        update_uName(sName, n_uName)
        print(f" Current user name changed to '{n_uName}'")
    elif choice == "4":
        uName = input(" Enter user name: ")
        n_pswd = input(" Enter new password: ")
        update_pswd(uName, n_pswd)
        print(f" Current password changed to '{n_pswd}'")
    else:
        print(" Invalid input. Please try again.")


# ___ Modifying credentials ___

ans = "y"
while ans == "y":
    print(" You are about to modify your credentials. \n")
    print(" Please note that none of the modifications can be reverted! \n")

    print(" Input '1' for modifying site name. \n")
    print(" Input '2' for modifying site URL. \n")
    print(" Input '3' for modifying user name. \n")
    print(" Input '4' for modifying password. \n")

    choice = input(" Enter your choice: ")
    update_cred(choice)

    ans = input(" More changes? (y/n): ")

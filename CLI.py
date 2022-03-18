# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 18:29:04 2021.

@author: Saptarshi Pal
@Project: Py PassCred PGaMA (Password Generator and Management Application)
"""

import string
import random

LowStr = string.ascii_lowercase  # String of all lowercase letters
uppStr = string.ascii_uppercase  # String of all uppercase letters
intStr = "01234565789"  # String of all numerals
speLst = [
    "~",
    "`",
    "@",
    "#",
    "$",
    "%",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "{",
    "}",
    "|",
    "?",
    "<",
    ">",
    ",",
    ".",
    "/",
    ":",
    ";",
]
# List of some commonly found special characters in a standard keyboard: "~`!@#$%^&*()_-+={[}]|\ : ;"'<,>.?/"  #Note: "\" has been ommitted for in-compatibility issues with Python syntax


def spexc(speLst):
    """Exculde certain special characters from the password to be generated to avoid interference with softwares' code."""
    print("Some systems don't allow certain special characters in passwords")
    ans = input(
        "Do you want some special characters to be excluded from your passwords? (y/n) : "
    )
    while ans == "y":
        try:
            exc = input("Please enter the character to be removed: ")
            speLst.remove(exc)
            print(f"New list of special characters after exculding {exc} is {speLst}")
            ans = input("More characters to be excluded?(y/n): ")
        except ValueError:
            print(f"No such character {exc} found. Please try again")
            ans = input("Try again?(y/n): ")


# Inserts random strings
def strinsert(s):
    """


    Parameters.
    ----------
    s : STRING
        Insert random string (min. 1;max. 3).

    Returns
    -------
    s : STRING
        Password with random string added at end.

    """
    x = random.randint(1, 2)
    for i in range(x):
        x2 = random.randint(1, 2)
        if x2 == 1:
            s += random.choice(LowStr)
        else:
            s += random.choice(uppStr)
    return s


# Inserts random numbers
def intinsert(s):
    """


    Parameters.
    ----------
    s : INTEGER
        Insert random integer (min. 1;max. 3).

    Returns
    -------
    s : INTEGER
        Password with random integer added at end.

    """
    x = random.randint(1, 2)
    for i in range(x):
        s += random.choice(intStr)
    return s


# Inserts random symbols
def syminsert(s):
    """


    Parameters.
    ----------
    s : SYMBOL
        Insert random symbol (min. 1;max. 3).

    Returns
    -------
    s : SYMBOL
        Password with random symbol added at end.

    """
    s += random.choice(speLst)
    return s


# Generates complex passwords
def complexpass(s, n):
    """


    Parameters
    ----------
    n : INTEGER
        appx. number of triplet random characters inserted.

    Returns
    -------
    s : STRING
        Password with a 'n' triplets of random characters added at end.

    """
    while len(s) <= n:
        s = strinsert(s)
        s = intinsert(s)
        s = syminsert(s)
    else:
        return s


# Generates passwords
def wordspass():
    """


    Returns
    -------
    s : STRING
        THE PASSWORD.
    nat : STRING
        Password nature (custom or random).

    """
    s = ""
    opt = input("Custom or random password? (cust/rand): ")
    if opt == "cust":
        nat = "Custom"
        ans = "n"
        s = input("Enter password: ")
    else:
        nat = "Random"
        ans = "y"
        Ln = int(input("Enter desired length of password: "))
    s = complexpass(s, Ln)
    print(f"Your password has been generated!\n {s} \n Please preserve this carefully.")
    return s, nat


# User Credentials
def cred():
    sName = input("Enter Site Name: ")
    sURL = input("Enter Site URL: ")
    uName = input("Enter Username: ")
    return sName, sURL, uName


def menu():
    print("Enter:")
    print("'1' to simply generate a password.")
    print("'2' to record a row of credentials.")
    print("'3' to modify a row of credentials.")
    print("'exit' to exit the application.")
    return input("Enter your choice: ")


# UI / UX (a.k.a ThE M@$teRMa!nd)
def UI():
    print("Welcome to Py_PassCred!\n")
    input("Please log in to your SQL interface apriori...\nEnter to continue...\n")
    choice = menu()
    while choice != "exit":
        if choice == "1":
            pswd = complexpass(int(input("Enter desired length of password")))
            print(f"{pswd}is your password.")
            choice = menu()
        elif choice == "2":
            sName, sURL, uName = cred()
            pswd, nat = wordspass()
            print(
                "Please note RDBMS database 'Py_PassCred' table 'passwords_data' will be used.\n"
            )
            print("Switching to RDBMS module SQL database...\n")
            data_entry(sName, sURL, uName, pswd, nat)
            choice = menu()
        elif choice == "3":
            mod()
            choice = menu()
    else:
        print("Exiting application.\nBye!")


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
else:
    print("MySQL connection failed.")
    print("Please restart app after logging in to your MySQL interface.")


def data_entry(site_name, site_URL, username, password, password_nature="random"):
    """
    Actual insertion of data into RDBMS.

    To be called inside "UI()" after taking all credentials from user.

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
        DESCRIPTION. default "random".

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
    except (sql_conn.ProgrammingError, sql_conn.IntegrityError):
        err = "Only one password per URL is allowed for data integrity\n Please try again with a unique URL"
        print(err)


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


def mod():
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


# __main__

UI()

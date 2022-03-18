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
    """This function exculdes certain special characters from the password to be generated to avoid interference with softwares' code."""
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
    x = random.randint(1, 3)
    for i in range(x):
        x2 = random.randint(1, 2)
        if x2 == 1:
            s += random.choice(LowStr)
        else:
            s += random.choice(uppStr)
    return s


# Inserts random numbers
def intinsert(s):
    x = random.randint(1, 3)
    for i in range(x):
        s += random.choice(intStr)
    return s

# Inserts random symbols
def syminsert(s):
    x = random.randint(1, 3)
    for i in range(x):
        s += random.choice(speLst)
    return s

# Generates complex passwords
def complexpass(n):
    s = ""
    for i in range(n):
        s = strinsert(s)
        s = intinsert(s)
        s = syminsert(s)
    return s

# Generates passwords
def wordspass():
    s = ""
    opt = input("Custom or default password? (cust/defa): ")
    if opt == "cust":
        nat = "Custom"
        ans = "n"
        s = input("Enter password: ")
    else:
        nat = "Random"
        ans = "y"
        Ln = int(input("Enter desired length of password: "))
    while ans == "y":
        while len(s) < Ln:
            s = strinsert(s)
            s = intinsert(s)
            s = syminsert(s)
        print(
            f"Your password has been generated!\n {s} \n Please preserve this carefully."
        )
    return s,nat

# User Credentials
def cred():
    sName = input("Enter Site Name: ")
    sURL = input("Enter Site URL: ")
    uName = input("Enter Username: ")
    return sName,sURL,uName


# UI / UX
def UI():
    flag = "y"
    while flag == "y":
        print("Welcome to Py_PassCred!\n")
        input("Please log in to your SQL interface apriori...\nEnter to continue...\n")
        sName,sURL,uName = cred()
        pswd,nat = wordspass()
        print("Please note RDBMS database 'Py_PassCred' table 'passwords_data' will be used.\n")
        print("Switching to RDBMS module SQL database...\n")
        data_entry(sName, sURL, uName, pswd, nat)
        flag = input("Want to generate more such passwords? (y/n): ")
        print("Exiting application.\nBye!")
    return "Exit"




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
        DESCRIPTION. default "Custom".

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


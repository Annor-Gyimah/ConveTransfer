import sqlite3
import os
def Database():
    global conn, cursor
    #global db
    #db = 'file_transfer.db'
    
    conn = sqlite3.connect('file_transfer.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS member (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sent  TEXT,
                date TEXT,
                size TEXT,
                received TEXT,
                sent_location TEXT,
                received_location TEXT
                    )
                ''')
    conn.commit()
    conn.close()
    

def insert_sent_file(filename, datetime, size, sent_location):
    
    conn = sqlite3.connect('file_transfer.db')
    cursor = conn.cursor()
    cursor.execute(''' 
                   INSERT INTO member (sent,date,size,received,sent_location)
                   VALUES (?, ?, ?, ?, ?)
                   
                ''', (filename, datetime,size, "", sent_location))
    conn.commit()
    conn.close()


def insert_received_file(filename, datetime, size, received_location):
    
    conn = sqlite3.connect('file_transfer.db')
    cursor = conn.cursor()
    cursor.execute(''' 
                   INSERT INTO member (sent,date,size,received,received_location)
                   VALUES (?, ?, ?, ?, ?)
                   
                ''', ("", datetime, size, filename, received_location))
    conn.commit()
    conn.close()


def get_transferred_files():
    
    conn = sqlite3.connect('file_transfer.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM member')
    fetch = cursor.fetchall()
    conn.commit()
    conn.close()

    return fetch

def get_files():
    conn = sqlite3.connect('file_transfer.db')
    cursor = conn.cursor()
    cursor.execute('SELECT sent, date, size, received, sent_location, received_location FROM member')
    fetch = cursor.fetchall()
    conn.commit()
    conn.close()
    return fetch



def delete_item(filename, datetime, size):
    try:
        conn = sqlite3.connect('file_transfer.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM member WHERE sent=? AND date=? AND size=? AND received=?", (filename, datetime, size, ""))
        #cursor.execute("DELETE FROM member WHERE sent=? AND date=? AND size=? AND received=?", ("", datetime, size, filename))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print("Error deleting item from the database:", str(e))
        conn.rollback()
        return False


def delete_item_rec(filename, datetime, size):
    try:
        conn = sqlite3.connect('file_transfer.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM member WHERE sent=? AND date=? AND size=? AND received=?", ("", datetime, size, filename))
        #cursor.execute("DELETE FROM member WHERE sent=? AND date=? AND size=? AND received=?", ("", datetime, size, filename))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print("Error deleting item from the database:", str(e))
        conn.rollback()
        return False


def get_sent_received_counts():
    conn = sqlite3.connect('file_transfer.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM member WHERE sent != ''")
    sent_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM member WHERE received != ''")
    received_count = cursor.fetchone()[0]

    conn.close()

    return sent_count, received_count
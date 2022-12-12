import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()


# Table
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS jobstable(name TEXT, address TEXT, title TEXT, email TEXT, jobtype TEXT, salary INTEGER, status TEXT)")


# Add Data
def add_data(name, address, email, title, salary, status, jobtype):
    c.execute("INSERT INTO jobstable(name, address, email, title, salary, status, jobtype) VALUES (?,?,?,?,?,?,?)", (name, address, email, title, salary, status, jobtype))
    conn.commit()


# View all Data
def show_all_jobs():
    c.execute("SELECT * FROM jobstable")
    data = c.fetchall()
    return data


# Search/View
def get_job_by(text, field):
    c.execute(f"SELECT * FROM jobstable WHERE {field} = '{text}'")
    data = c.fetchall()
    return data


#  Edit Job
def edit_job_by(new_text, old_text, field):
    c.execute(f'UPDATE jobstable SET {field}="{new_text}" WHERE {field}="{old_text}"')
    conn.commit()
    data = c.fetchall()
    return data


# Delete Job
def delete_job(title):
    c.execute(f'DELETE FROM jobstable WHERE title="{title}"')
    conn.commit()



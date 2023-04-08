from pathlib import Path
from zipfile import ZipFile
import csv



# path = Path('ecommerce')

# paths = [ p for p in path.iterdir()]

# print(paths)   


# with ZipFile('files.zip', 'w') as zip:
#     for path in Path('ecommerce').rglob('*.*'):
#         zip.write(path)


# with ZipFile('files.zip') as zip:
#     print(zip.namelist())
#     info = zip.getinfo('ecommerce/__init__.py')
#     print('file size : ', info.file_size)
#     print(info.compress_size)
#     zip.extractall('extract')



# How to write to a csv file 
# with open('data.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['transaction_id', 'product_id', 'quantity'])
#     writer.writerow([1000,1,5])
#     writer.writerow([10010,2,13])


# How to read a file
# with open('data.csv') as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)


# HOw to write data to json
import json

movies = [
    {
        'id': 1, 
        'title': 'Doctor',
        'year':2020
    },
    {
        'id': 2, 
        'title': 'Software Engineer',
        'year':2023
    },
]

# data = json.dumps(movies)
# Path('movies.json').write_text(data)


# How to read a json file 
# data = Path('movies.json').read_text()
# movies = json.loads(data)
# print(movies)

'''
# Working with sqlite3
import sqlite3

movies = json.loads(Path('movies.json').read_text())

with sqlite3.connect('db.sqlite3') as db:
    # command = 'INSERT INTO movies VALUES(?, ?, ?)'
    # for movie in movies:
    #     db.execute(command,tuple(movie.values()))
    # db.commit()    

    command = 'SELECT * FROM movies'

    cursor = db.execute(command)
    movies = cursor.fetchall()
   
'''

# DATETIME OBJECT 
from datetime import datetime, timedelta
import time

dt1 = datetime(2023,5,25)
dt2 = datetime.now()
dt = datetime.strptime('2023/02/25', '%Y/%m/%d') # string to datetime object
dt = datetime.fromtimestamp(time.time())


# TIME DURATION
duration = dt2- dt1
print(duration)
print(dt.strftime('%Y-%m/%d'))
print(dt)


import random
import string

# print(random.random())
# print(random.randint(1,10))
# print(random.choice([1,2,3,4,5,6,7]))
# print(random.choices([1,2,3,4,5,6,7], k=2))
# print(''.join(random.choices(string.ascii_letters + string.digits, k=2)))
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)


# OPENING BROWSER 
# import webbrowser

# print('Delopment Completed')

# webbrowser.open('http://google.com')

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# import smtplib

# message = MIMEMultipart()
# message['from'] = 'Akorede F.'
# message['to'] = 'syllabus28@gmail.com'
# message['subject'] = 'This is a testing email message'
# message.attach(MIMEText('Body', 'plain'))
# message.attach(MIMEImage(Path('mosh.png').read_bytes()))


# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('f.owolabi81@gmail.com', 'password')
#     smtp.send_message(message)
#     print('Sent.......')


# COMMAND LINE ARGUMENTS
# 0108032450

# import sys
# if len(sys.argv) == 1:
#     print('USAGE: python3 009_library.py <password>')
# else:
#     password = sys.argv[1]
#     print('PASSWORD: ', password)   
# 
#  RUNNING EXTERNAL PROGRAMS

import subprocess

completed = subprocess.run(['ls', '-l' ], capture_output=True, text=True)

print('args', completed.args)
print('returncode', completed.returncode)
print('stderr', completed.stderr)
print('stdout', completed.stdout)
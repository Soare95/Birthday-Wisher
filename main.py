import datetime as d
import smtplib
import random
import pandas as pd


MY_EMAIL = "YOUR_EMAIL"
PASSWORD = "EMAIL_PASSWORD"

data = pd.read_csv("birthdays.csv")
birthday_dict = {(value["month"], value["day"]): value for (key, value) in data.iterrows()}

date_now = dt.datetime.now()
today_birthday = (date_now.month, date_now.day)

if today_birthday in birthday_dict:
    birthday_person = birthday_dict[today_birthday]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        random_letter = file.read()
        random_letter = random_letter.replace("[NAME]", birthday_person["name"])

        connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=data["email"], msg=f"Subject: Happy Birthday\n\n{random_letter}")
        connection.close()
        print('Email sended')

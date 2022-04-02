
import pandas as pd
import datetime as dt
import smtplib
import random
    
birthdays = pd.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict('index')

now = dt.datetime.now()
month = now.month
day = now.day

my_email = mail_id
password = p_assword


for k,v in birthdays_dict.items():
    if month == v['month'] and day == v["day"]:
        
        letters_list= ['letter_1','letter_2','letter_3']   
        content = random.choice(letters_list)
        
        with open(f"./letter_templates/{content}.txt") as file:
            letter=file.read()
            message=letter.replace('[NAME]',v["name"])
            
        print(message)       
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= my_email,password= password)
            connection.sendmail(from_addr = my_email, to_addrs =v["email"] , msg=f'Subject:HAPPY BIRTHDAY!\n\n{message}')



import smtplib
import datetime as dt
import random
from secret import username,password,agent_email
MY_EMAIL = username
MY_PASSWORD = password


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        # get a list of all of the lines in the file
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password= MY_PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs= agent_email,
                            msg= f"Subject: Happy new week\n\n {quote}")

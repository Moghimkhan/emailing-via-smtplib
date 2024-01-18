import smtplib
import datetime as dt
import random
from secret import username, password, agent_email

MY_EMAIL = username
MY_PASSWORD = password

def get_random_quote(file_path):
    """
    Get a random quote from a file.

    :param file_path: The path to the file containing quotes.
    :return: A randomly selected quote from the file.
    """
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        return random.choice(all_quotes)

def send_email(subject, message, to_email):
    """
    Send an email using SMTP.

    :param subject: The subject of the email.
    :param message: The body of the email.
    :param to_email: The recipient's email address.
    """
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject: {subject}\n\n{message}")

def main():
    # Get the current date and weekday
    now = dt.datetime.now()
    weekday = now.weekday()

    # Check if it's Friday (weekday == 4)
    if weekday == 1:
        # Get a random quote
        quote = get_random_quote("quotes.txt")
        print(quote)

        # Prepare and send the email
        subject = "Happy new Week"
        send_email(subject, quote, agent_email)
    elif weekday == 3:
        # Get a random quote
        quote = get_random_quote("quotes.txt")
        print(quote)

        # Prepare and send the email
        subject = "Quotes of the Week"
        send_email(subject, quote, agent_email)
if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
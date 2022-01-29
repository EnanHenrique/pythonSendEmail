import smtplib
from email.message import EmailMessage

from private import EMAIL_ADRESS as email
from private import EMAIL_PASSWORD as password

EMAIL_ADRESS = email #Your e-mail
EMAIL_PASSWORD = password #Your e-mail password

message = EmailMessage()

message['Subject'] = 'Mapa X X X foi terminado!' #Tittle
message['From'] = email #Your e-mail here
message['To'] = 'email.destination@example.com' #ENTER DESTINATION E-MAIL HERE
message.set_content('Favor olhar o telegram para conferir o envio do mapa X X X')

def send_email():
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: #port 465
            smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
            smtp.send_message(message)
            print('E-mail sucessfully sent!')
    except Exception as error:
        print('An error ocurred when trying to send the e-mail: ', error)

send_email()

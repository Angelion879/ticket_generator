import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from credentials import sender_email, password


def email_sender(email):
    msg = MIMEMultipart()
    msg['from'] = 'Suricato'
    msg['to'] = email
    msg['subject'] = 'Ingresso do Suricato!'

    email_body = MIMEText("Aqui está seu ingresso para a nossa festa! Nos vemos na toca!")
    msg.attach(email_body)

    with open('suricatoFinal.png', 'rb') as img:
        img_data = img.read()
        image = MIMEImage(img_data, name="Suringresso")
        msg.attach(image)

    with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
        smtp.ehlo()
        smtp.login(sender_email, password)
        smtp.send_message(msg)

        print('Mail Delivered!')
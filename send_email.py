import smtplib
from email import message

def email_alert(body, to_addr):
    from_addr = 'sesi.alert@gmail.com'
    subject = 'Vagas Sesi'

    msg = message.Message()
    msg.add_header('from', from_addr)
    #msg.add_header('to', to_addr[0])
    msg.add_header('subject', subject)
    msg.set_payload(body)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_addr, 'dthk yraj yhfs kpsm')
    server.send_message(msg,from_addr=from_addr, to_addrs=to_addr)
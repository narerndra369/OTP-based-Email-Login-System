import smtplib
import main
recv = 'malapulanarendrayadav@gmail.com'
send = 'usemeon1@gmial.com'
msg = 'Hello'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(send, main.password)
print("login")
server.sendmail(send, recv, msg)
print("Message sent ")


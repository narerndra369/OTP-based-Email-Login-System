from tkinter import *
import smtplib
import ssl, random
import tkinter.messagebox

recivemail = "12345689" # Default value for recipient email (will be updated later)
n = '123456'
t = Entry


def gett1():
    inp1 = t.get()  # Get input from Entry widget
    # Compare entered OTP with generated OTP
    if otp == inp1:
        tkinter.messagebox.showinfo('Login/Status', 'Login succesfull')
        root.withdraw() # Hide login window
        r1 = Tk()   # Create a new window for successful login
        l3 = Label(r1, text = "Welcome", font = ("Courier", 100), fg = '#0000FF', bg = "yellow")
        l3.pack()
        r1.mainloop()
    else:
        tkinter.messagebox.showerror('Login/Status', "Login Failed")

# Function to get recipient email and send OTP
def gett():
    inp = T1.get()
    global recivemail
    recivemail = inp

    try:
        # Send email with OTP
        server.sendmail(sender_email,recivemail,msg)
        l2 = Label(root, text="otp")
        l2.pack(side=TOP)
        b.destroy()
        global t
        t = Entry(root)
        t.pack(side=TOP)
        b2 = Button(root, text="check otp", activebackground="pink", activeforeground="blue", command=gett1)
        b2.pack(side=TOP)
    except Exception:
        tkinter.messagebox.showerror("Mail check", "Please enter valid email")
    finally:
        server.quit()

sender_email = '******' #add your sending email
password = '******' #add your pawword to here
otp = random.randint(100000, 999999)
otp = str(otp)
context = ssl.create_default_context()

msg = 'OTP to login is ' + otp
# Establish connection with SMTP server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
except Exception as e:
    print(e)

# GUI

root = Tk()
root.title("nare tech solutions")
l1 = Label(root, text="Username")
l1.pack(side=TOP)
T1 = Entry(root)
T1.pack(side=TOP)
b = Button(root, text="submit", activebackground="pink", activeforeground="blue", command=gett)
b.pack(side=TOP)
root.geometry('400x400')
root.mainloop()

import smtplib
x = input("Your Gmail Address : ")
y = input("Your Gmail Password : ")
z = input("Your Message : ")
#################################################################################################################
def send_mail(email,password,message):                                                                          #
    email_server = smtplib.SMTP("smtp.gmail.com",587) ## Server Address, Port.                                  #
    email_server.starttls() ## Connect server.                                                                  #
    email_server.login(email,password) ## Login with 1 par , 2 par.                                             #
    email_server.sendmail(email,email,message) ## Sender, Target of sender. => Mail message.                    #
    email_server.quit() ## Quit the server.                                                                     #
#################################################################################################################
## <-------------------- Coded By SBDH-cosmin (Owl-planet) https://github.com/Owl-planet --------------------> ##
#################################################################################################################
send_mail("{}" , "{}" , "{}".format(x,y,z))

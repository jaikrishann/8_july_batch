import smtplib
try:
    #connecting to gmail server
    server = smtplib.SMTP(host= "smtp.gmail.com",port  = 587)
    server.starttls()


    #ask receiver mail:
    receiver_email = input("enter your mail ")

    #put your mail credentials
    sender_email = "jaikrishan2001@gmail.com"
    password = "ztxu lpdu lmfm xqxc"

    #server login
    server.login(sender_email,password=password)

    ###subject and body of the mail
    subject  = input("what is your problem 😒😒")
    body = input("thoda detail me batao 😂")

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(sender_email,receiver_email,message)
    print("successfully sent 👍👍")

    server.quit()

except Exception as e:
    print(" mail nahi gyi 😮😮")
import smtplib
toaddr = ''
cc = []
bcc = []
message_subject = "Testing"

with open('message.txt', 'r') as myfile:
    message_text = myfile.read()

emails = open('email list.txt','r')
senders = open('senders.txt','r')
counter = 0

for sender in senders:
    a = sender.split(":")
    fromaddr,password = a[0],a[1]
    print("[Sender] ", fromaddr)
    print("[password] ", password)
    for line in emails:
        bcc.append(line)
        counter+=1
        if counter%100 == 0:
            print("[BCC] ",bcc)
            print(" ")
            server = smtplib.SMTP('smtp.mail.yahoo.com',587)
            server.ehlo()
            server.starttls()
            server.login(str(fromaddr), str(password))
            message = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddr + "CC: %s\r\n" % ",".join(cc) + "Subject: %s\r\n" %message_subject + "\r\n" + message_text
            toaddrs = [toaddr] + cc + bcc

            server.sendmail(fromaddr, toaddrs, message)
            server.quit()
            print("100 EMAILS SENT !")
            bcc = []
            break

print(" ")
print("----------------------------------------")
print("Emails Successfully Sent !")

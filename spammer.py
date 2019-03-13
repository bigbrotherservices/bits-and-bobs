import smtplib
import time
i=0

GMAIL_USER = 'spammer.kindness.bot@gmail.com'
GMAIL_PASS = 'NOCode4YoULolxD'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

time.sleep(2)
rec = input('\nWho would you like to send this to?')
time.sleep(2)
msg=input('\nWhat would you like to say?(In Quotes)')
time.sleep(2)
rep = input('\nHow many times would you like it to repeat?')
time.sleep(2)
smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(GMAIL_USER, GMAIL_PASS)
check = input('\nAre you sure if you want to send this? Y for yes, and N for no.(In quotes)')
time.sleep(2)
rep=int(rep)
if (check == 'Y' or check == 'y'):

    while (i<=rep):
        i=i+1
        smtpserver.sendmail(GMAIL_USER, rec,msg)
        print('SENT '+str(i))
smtpserver.close()
print('DONE')

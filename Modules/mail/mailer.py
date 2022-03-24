import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def keypassmail (clientmail,keypass):
   fromaddr = "noreplay.isecure@gmail.com"
   password = "mari@isecure"
   toaddr = clientmail


   # instance of MIMEMultipart
   msg = MIMEMultipart()

   # storing the senders email address
   msg['From'] = fromaddr
   msg['To'] = toaddr

   msg['Subject'] = "Registration Success - Keypass Generated"
   
   html = """\
<html>
  <head></head>
  <body>
    <p><b>Thank You For Regestering !!!</b><br>
       Your Key Pass generated Successfully.<br>
       Find The Keypass Attached below.
    </p>
  </body>
</html>
"""
   
   # string to store the body of the mail
   #body = "  F" 
   body = html
   
   # attach the body with the msg instance
   msg.attach(MIMEText(html, 'html'))
   
   # create file
   f = open("keypass.json", "a")
   f.write(keypass)
   f.close()
   
   # open the file to be sent
   filename = "keypass.json"
   attachment = open(filename, "rb")
   
   # instance of MIMEBase and named as p
   p = MIMEBase('application', 'octet-stream')
   
   # To change the payload into encoded form
   p.set_payload((attachment).read())
   
   
   # encode into base64
   encoders.encode_base64(p)
   
   p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
   
   # attach the instance 'p' to instance 'msg'
   msg.attach(p)
   
   # creates SMTP session
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(fromaddr,password)
   
   # Converts the Multipart msg into a string
   text = msg.as_string()
   
   server.send_message(msg)
   
   server.quit()
      

    
def otpmail(clientmail,otps):
    
   fromaddr = "noreplay.isecure@gmail.com"
   password = "mari@isecure"
   toaddr = clientmail
   otp=otps


   # instance of MIMEMultipart
   msg = MIMEMultipart()

   # storing the senders email address
   msg['From'] = fromaddr
   msg['To'] = toaddr

   msg['Subject'] = "iSecure - OTP"
   
   # string to store the body of the mail
   body = "OTP Number : "+str(otp)+". Please use this OTP."
   
   # attach the body with the msg instance
   msg.attach(MIMEText(body, 'plain'))
   
   # creates SMTP session
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(fromaddr,password)
   
   # Converts the Multipart msg into a string
   text = msg.as_string()
   
   server.send_message(msg)
      
   server.quit()
   
   
  

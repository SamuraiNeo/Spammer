import smtplib

fromaddress = "fromaddress@gmail.com"
toaddress = "toaddress@gmail.com"
username = "yourgmail username"
password = "yourgmail password"
message = """From:Neo 
...text here...
"""

server =smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

for i in range (0,10):
  server.sendmail(fromaddress,toaddress,message)
  print("Mail sent")

server.quit()

import os

#function for sending email
def email_sent():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    fromaddr = "senderaddress123@gmail.com"
    toaddr = "reciveraddress123@gmail.com"
   
    # instance of MIMEMultipart
    msg = MIMEMultipart()
  
    # storing the senders email address  
    msg['From'] = fromaddr
  
    # storing the receivers email address 
    msg['To'] = toaddr
  
    # storing the subject 
    msg['Subject'] = "Sending Shrishti Photo from tanushree"
  
    # string to store the body of the mail
    body = "this is the face of Shrishti"
  
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
  
    # open the file to be sent 
    filename = "Shrishti_photo.jpg"
    attachment = open("./Shrishti_photo.jpg", "rb")
  
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
    s = smtplib.SMTP('smtp.gmail.com', 587)
  
    # start TLS for security
    s.starttls()
  
    # Authentication
    s.login(fromaddr, "password-of-sender-id")
  
    # Converts the Multipart msg into a string
    text = msg.as_string()
  
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
  
    # terminating the session
    s.quit()

    
# Function for sending whatsapp message
def whatsapp_msg_sent():
    import pywhatkit
    pywhatkit.sendwhatmsg_instantly(
        phone_no="+91**********", 
        message="Hello Shrishti , Your Face Detected.....!!!"
)
    
# Function for launching ec2 instance
def ec2_launch():
    # Creating an ec2 instance on aws cloud
    os.system("aws ec2 run-instances  --image-id ami-0ad704c126371a549 --instance-type t2.micro  --subnet-id subnet-dcc2d6b4  --count 1 --security-group-ids  sg-01dfc9b7e00273e76  --key-name myaccountAWS > ec2_out.txt")
    print("Instance Launched")
  
# Function for launching ebs volume
def ebs_launch():
    os.system("aws ec2 create-volume --availability-zone ap-south-1a --size 5 --volume-type gp2 --tag-specification  ResourceType=volume,Tags=[{Key=aws,Value=key}]")    
    print("EBS volume Launched")

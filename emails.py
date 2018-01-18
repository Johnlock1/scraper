import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(day, email):
    # setting up email
    fromaddr = "email@email.com"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Νέες Αγγελίες car.gr {}".format(day)

    # add body
    body = "Νέες αγγελίες αυτοκινήτων από ιδιώτες, στην Μακεδονία, για αυτοκίνητα με ζημία."
    msg.attach(MIMEText(body, "plain"))

    #attachment
    filename = "cargr {}.xlsx".format(day)
    attachment = open("/home/ubuntu/workspace/scraper/cargr {}.xlsx".format(day), "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    # setup server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # login to server
    password = "woehztaqpaieukaj"  # for gmail, get password from https://myaccount.google.com/lesssecureapps
    server.login(fromaddr, password)

    # send message
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    server.quit()
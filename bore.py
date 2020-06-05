import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "ramapriya3105@gmail.com"
rec_list =  ['ramamaha827@gmail.com', 'ramapriyamanickam3105@gmail.com','mithunramesh300905@gmail.com','78mahee@gmail.com','pandi.ganesh2000m@hmail.com','priyadharsi31@gmail.com','953615104027@ritrjpm.ac.in']
rec =  ', '.join(rec_list)


password = "dharshini05@"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, rec_list, message)

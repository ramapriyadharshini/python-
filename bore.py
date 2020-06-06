import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "example@gmail.com"
rec_list =  ['example1@gmail.com', 'example2@gmail.com','example3@gmail.com']
rec =  ', '.join(rec_list)


password = "enter your password"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, rec_list, message)

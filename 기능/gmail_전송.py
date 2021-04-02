import smtplib
from email.mime.text import MIMEText
from email.header import Header

# MIMEText 객체로 메일을 생성합니다.
msg = MIMEText('메일 본문입니다.')  

# 제목에 한글이 포함될 경우 Header 객체를 사용합니다.
msg['Subject'] = Header('메일 제목입니다.', 'utf-8') 
msg['From'] = 'me@example.com'
msg['To'] = 'you@example.com'

# SMTP()의 첫 번째 매개변수에 SMTP 서버의 호스트 이름을 지정합니다.
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    # 메일을 전송합니다.
    smtp.starttls()
    smtp.login('gmail 이메일', '2단계 인증 암호')
    smtp.send_message(msg)

from email.mime.text import MIMEText
import smtplib

__author__ = "zzh"


class Mail(object):
    def __init__(self):
        cipher = Cipher()
        self._MAIL_CONFIG = {
            'SERVER': 'smtp.exmail.qq.com',
            'PORT': 0,
            'USER': 'zhihe.zhang@wwwarehouse.com',
            'PASSWORD': cipher.decrypt(),
        }
        self._subject = "UI自动化测试结果"
        self._from = "UI自动化"
        self._to = []
        self._sender = self._MAIL_CONFIG["USER"]

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        self._subject = subject

    @property
    def mail_from(self):
        return self._from

    @mail_from.setter
    def mail_from(self, mail_from):
        self._from = mail_from

    @property
    def mail_to(self):
        return self._to

    @mail_to.setter
    def mail_to(self, mail_to):
        self._to = mail_to

    def send_mail(self, content):
        msg = MIMEText(content)
        msg["Subject"] = self.subject
        msg["From"] = self._from
        msg["To"] = ";".join(self._to)
        msg["Sender"] = self._sender
        s = smtplib.SMTP(host=self._MAIL_CONFIG["SERVER"], port=self._MAIL_CONFIG["PORT"])
        s.login(self._MAIL_CONFIG["USER"], self._MAIL_CONFIG["PASSWORD"])
        s.send_message(msg)
        s.quit()


class Cipher(object):
    def __init__(self):
        self._original_code = "0x5a0x7a0x680x310x360x300x320x300x34"

    # def encrypt(self):
    #     target_code = ""
    #     for code in self._original_code:
    #         target_code += hex(ord(code))
    #     return target_code

    def decrypt(self):
        hex_split = self._original_code.split("0x")
        hex_split.pop(0)
        target_code = ""
        for code in hex_split:
            code = "0x" + code
            target_code += chr(int(code, 16))
        return target_code


if __name__ == '__main__':
    mail = Mail()
    mail.subject = "UI自动化测试结果"
    mail.mail_to = ["zhihe.zhang@wwwarehouse.com"]
    mail.send_mail("https://www.baidu.com")



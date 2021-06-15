import paramiko
import time
import turtle
import tkinter

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
target_host = 'xxx.xxx.xxx.xxx'
target_port = 22
target_port = 22
pwd = 'xxxxxxxxxxxx'
un = 'xxxxx'
ssh.connect( hostname = target_host , username = un, password = pwd )
stdin, stdout, stderr = ssh.exec_command('sudo python robotics/main.py')
print ("STDOUT:\n%s\n\nSTDERR:\n%s\n" %( stdout.read(), stderr.read() ))

stdin, stdout, stderr = ssh.exec_command('cat text1.txt')
so=stdout.readlines()
print ("STDOUT:\n%s\n\nSTDERR:\n%s\n" %( stdout.read(), stderr.read() ))
print (so)

for i in so:
    exec(i)
tkinter.mainloop()

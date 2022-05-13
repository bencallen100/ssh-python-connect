#!/usr/bin/python3

#written by: Benjamin Allen

import paramiko  #this library is used when connecting to servers with ssh. 

import subprocess #use this code to create new system processes that run applications

def ssh_connection(ip,user,passwd, command):
    client=paramiko.SSHClient()
    #you can uncomment the line below if you wanted to use ssh keys instead. Modify the known_hosts file to your needs.
    #client.load_host_keys('/home/user/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return

ssh_connection('x.x.x.x', 'username', 'password','pwd') #replace the I.P, username and password with the right credentials for the server you want to connect to.

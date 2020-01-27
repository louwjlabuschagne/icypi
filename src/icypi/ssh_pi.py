import paramiko

ip= input("Ip: ")
username= input("username: ")
password= input("Password: ")



ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,username,password)

stdin,stdout,stderr=ssh.exec_command('cd Documents/')
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

stdin,stdout,stderr=ssh.exec_command('python3 Pisense.py')
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

close()

from paramiko.client import SSHClient

get_temp_cmd = 'bash /home/pi/Documents/gitProjects/src/mcp9808/get_temp_mcp9808.sh'

client = SSHClient()
client.load_system_host_keys()
client.connect('192.168.101.109', username='pi')
stdin, stdout, stderr = client.exec_command(get_temp_cmd)

lines = stdout.readlines()
temp = float(lines[0].strip())

print(temp)

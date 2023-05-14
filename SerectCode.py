import socket
import ssl
import os
import paramiko

def check_remote_ip(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        ssl_sock = ssl.wrap_socket(sock)
        ssl_sock.connect((ip, 443))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        ssl_sock.close()

def sync_files(ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username='jack8168', password='8168')

    sftp = ssh.open_sftp()
    remote_path = '/home/data/'
    local_path = 'd:/data/'

    remote_files = sftp.listdir(remote_path)
    local_files = os.listdir(local_path)

    for file in remote_files:
        if file not in local_files:
            remote_file = os.path.join(remote_path, file)
            local_file = os.path.join(local_path, file)
            sftp.get(remote_file, local_file)

    sftp.close()
    ssh.close()

ip = '61.219.126.136'
if check_remote_ip(ip):
    print("IP is online.")
    sync_files(ip)
else:
    print("IP is offline.")
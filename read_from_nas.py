import io
import pandas as pd   
from ftplib import FTP


ftp_server_ip = 'YourFTPServerIP'
username = 'YourUsername'
password = 'YourPassword'
directory = 'YourFTPDirectory'


def read_from_ftp(ftp_connection, filename):   
    download_file = io.BytesIO()
    ftp_connection.retrbinary(f'RETR {filename}', download_file.write)
    download_file.seek(0)
    return pd.read_csv(download_file)


ftp = FTP(ftp_server_ip, user=username, passwd=password)
ftp.cwd(directory)

df = read_from_ftp(ftp, 'file.txt')

ftp.quit()

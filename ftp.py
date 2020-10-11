from ftplib import FTP
import os
import re

class Ftp_connection():
    def __init__(self, server_ip):
        self.server_ip = server_ip
        self.ftp = FTP(self.server_ip)
        self.ftp.login() #anonymous login
        self.ftp.encoding = "utf-8"
        self.ftp.cwd('images') #change dir

    def upload_file(self, path_to_file, filename):
        """ using the ftp connection to upload a file, we give it the 
        path to the file and the name it will be saved as on the ftp server """
        self.path_to_file = path_to_file
        self.filename = filename
        with open(self.path_to_file, "rb") as file:
            # use FTP's STOR command to upload the file
            self.ftp.storbinary(f"STOR {self.filename}", file)
        # We opened the file with "rb" mode, which means we're reading the local file in binary mode.

    def download_file(self, download_folder_path, filename):
        """using the ftp connection to download a file to the dir we choose
        as the download folder for the images"""
        self.download_folder_path = download_folder_path
        self.filename = filename
        with open(os.path.join(self.download_folder_path,self.filename), "wb") as file:
            # use FTP's RETR command to download the file
            self.ftp.retrbinary(f"RETR {self.filename}", file.write)
        # This time, we're opening the local file in "wb" mode, 
        # as we're gonna write the file from the server to the local machine.

    def list_files(self):
        """this simply returns a list of all the files in the dir"""
        return self.ftp.nlst()

# 代码生成时间: 2025-09-22 07:30:19
import os
import zipfile
from scrapy.exceptions import NotConfigured

"""
UnzipTool is a utility class for extracting files from zip archives"""
class UnzipTool:
    def __init__(self, archive_path):
        """
        Initialize the UnzipTool with the path to the archive file.
        :param archive_path: The path to the archive file.
        """
        self.archive_path = archive_path
        if not os.path.exists(self.archive_path):
            raise NotConfigured("Archive file does not exist.")

    def extract_all(self, extract_path):
        """
        Extract all the files from the archive to the specified directory.
        :param extract_path: The directory where files will be extracted.
        """
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)

        try:
            with zipfile.ZipFile(self.archive_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
                print(f"Files extracted successfully to {extract_path}.")
        except zipfile.BadZipFile:
            print("Error: The file is not a zip file or it is corrupted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def extract(self, extract_path, file_name):
        """
        Extract a specific file from the archive to the specified directory.
        :param extract_path: The directory where the file will be extracted.
        :param file_name: The name of the file to extract.
        """
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)

        try:
            with zipfile.ZipFile(self.archive_path, 'r') as zip_ref:
                if file_name in zip_ref.namelist():
                    zip_ref.extract(file_name, extract_path)
                    print(f"{file_name} extracted successfully to {extract_path}.")
                else:
                    print(f"{file_name} does not exist in the archive.")
        except zipfile.BadZipFile:
            print("Error: The file is not a zip file or it is corrupted.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage:
if __name__ == '__main__':
    archive = 'path/to/your/archive.zip'
    extract_path = 'path/to/extract/to'
    unzipper = UnzipTool(archive)
    unzipper.extract_all(extract_path)  # Extract all files
    # or
    # unzipper.extract(extract_path, 'specific_file.txt')  # Extract a specific file
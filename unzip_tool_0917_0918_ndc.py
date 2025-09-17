# 代码生成时间: 2025-09-17 09:18:29
import zipfile
import os
from scrapy.exceptions import NotConfigured

"""
Unzip Tool: A utility for decompressing files using Python and Scrapy framework.

This tool is designed to be easily understandable, with clear code structure,
error handling, and necessary comments for maintainability and scalability.
"""

class UnzipTool:
    def __init__(self, input_dir, output_dir):
        """
        Initialize the UnzipTool with input and output directories.

        :param input_dir: The directory containing the compressed files.
        :param output_dir: The directory where the decompressed files will be stored.
        """
        self.input_dir = input_dir
        self.output_dir = output_dir

    def unzip(self, file_path):
        """
        Unzip a single file to the output directory.

        :param file_path: The path to the file to be unzipped.
        """
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(self.output_dir)
                print(f"Successfully unzipped {file_path} to {self.output_dir}")
        except zipfile.BadZipFile:
            print(f"Error: {file_path} is not a valid zip file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def unzip_all(self):
        """
        Unzip all files in the input directory.
        """
        try:
            for root, dirs, files in os.walk(self.input_dir):
                for file in files:
                    if file.endswith('.zip'):
                        file_path = os.path.join(root, file)
                        self.unzip(file_path)
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_directory = "path/to/input"
    output_directory = "path/to/output"
    unzipper = UnzipTool(input_directory, output_directory)
    unzipper.unzip_all()

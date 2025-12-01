import gdown
import os
import re
import sys
import requests
from bs4 import BeautifulSoup


def extract_file_id(url):
    """Extract file ID from Google Drive URL"""
    patterns = [
        r'/file/d/([a-zA-Z0-9_-]+)',
        r'id=([a-zA-Z0-9_-]+)',
        r'^([a-zA-Z0-9_-]+)$'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def extract_folder_id(url):
    """Extract folder ID from Google Drive URL"""
    patterns = [
        r'/folders/([a-zA-Z0-9_-]+)',
        r'id=([a-zA-Z0-9_-]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def is_folder_url(url):
    """Check if URL is a folder URL"""
    return '/folders/' in url


def get_folder_name(folder_id):
    """Get folder name from Google Drive"""
    try:
        url = f"https://drive.google.com/drive/folders/{folder_id}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.text
                # Remove " - Google Drive" suffix
                if " - Google Drive" in title:
                    folder_name = title.replace(" - Google Drive", "").strip()
                    if folder_name:
                        return folder_name
                return title.strip()
    except Exception as e:
        print(f"Could not get folder name: {e}")
    
    return f"folder_{folder_id[:8]}"  # Return short folder ID as fallback


def download_folder(url, output_folder):
    """Download all files from a Google Drive folder with folder name preserved"""
    folder_id = extract_folder_id(url)
    
    if not folder_id:
        print(f"Error: Could not extract folder ID from URL: {url}")
        return False
    
    # Get the folder name from Google Drive
    folder_name = get_folder_name(folder_id)
    print(f"Folder name: {folder_name}")
    
    # Create output path with folder name (e.g., downloads/Testing/)
    final_output = os.path.join(output_folder, folder_name)
    
    # Create output folder if it doesn't exist
    if not os.path.exists(final_output):
        os.makedirs(final_output)
        print(f"Created folder: {final_output}")
    
    try:
        print(f"Downloading folder ID: {folder_id}")
        folder_url = f"https://drive.google.com/drive/folders/{folder_id}"
        gdown.download_folder(folder_url, output=final_output, quiet=False)
        print(f"Successfully downloaded folder to: {final_output}")
        return True
            
    except Exception as e:
        print(f"Error downloading folder: {e}")
        return False


def download_file(url, output_folder):
    """Download a file from Google Drive"""
    file_id = extract_file_id(url)
    
    if not file_id:
        print(f"Error: Could not extract file ID from URL: {url}")
        return False
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")
    
    # Construct download URL
    download_url = f"https://drive.google.com/uc?id={file_id}"
    
    try:
        print(f"Downloading file ID: {file_id}")
        output_path = gdown.download(download_url, output=output_folder + os.sep, fuzzy=True)
        
        if output_path:
            print(f"Successfully downloaded: {output_path}")
            return True
        else:
            print("Download failed!")
            return False
            
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False


def download(url, output_folder):
    """Download file or folder based on URL type"""
    if is_folder_url(url):
        return download_folder(url, output_folder)
    else:
        return download_file(url, output_folder)


def main():
    print("=" * 50)
    print("Google Drive File/Folder Downloader")
    print("=" * 50)
    
    # Get output folder
    output_folder = input("\nEnter output folder path (or press Enter for 'downloads'): ").strip()
    if not output_folder:
        output_folder = "downloads"
    
    while True:
        print("\nOptions:")
        print("1. Download a file or folder")
        print("2. Download multiple files/folders")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == "1":
            url = input("Enter Google Drive URL (file or folder): ").strip()
            if url:
                download(url, output_folder)
            else:
                print("No URL provided!")
                
        elif choice == "2":
            print("Enter Google Drive URLs (one per line, empty line to finish):")
            urls = []
            while True:
                url = input().strip()
                if not url:
                    break
                urls.append(url)
            
            if urls:
                print(f"\nDownloading {len(urls)} items...")
                for i, url in enumerate(urls, 1):
                    print(f"\n[{i}/{len(urls)}]")
                    download(url, output_folder)
            else:
                print("No URLs provided!")
                
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

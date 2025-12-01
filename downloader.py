import gdown
import os
import re
import sys


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


def download_folder(url, output_folder):
    """Download all files from a Google Drive folder"""
    folder_id = extract_folder_id(url)
    
    if not folder_id:
        print(f"Error: Could not extract folder ID from URL: {url}")
        return False
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")
    
    try:
        print(f"Downloading folder ID: {folder_id}")
        folder_url = f"https://drive.google.com/drive/folders/{folder_id}"
        gdown.download_folder(folder_url, output=output_folder, quiet=False)
        print(f"Successfully downloaded folder to: {output_folder}")
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

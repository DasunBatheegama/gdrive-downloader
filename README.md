# Google Drive Downloader

A Python terminal application to download files and folders from Google Drive.

## Features

- ✅ Download files/folders from ONE Google Drive link
- ✅ Download files/folders from MULTIPLE Google Drive links
- ✅ Download entire folders with all contents preserved
- ✅ Preserves folder names and structure
- ✅ Handles duplicate names automatically (adds `(1)`, `(2)`, etc.)
- ✅ Detects private/inaccessible links with helpful error messages
- ✅ Progress bar for downloads
- ✅ Download summary (total, success, failed counts)
- ✅ Supports Sinhala and other Unicode filenames

## Requirements

- Python 3.7+
- Windows/Linux/macOS

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DasunBatheegama/gdrive-downloader.git
   cd gdrive-downloader
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   
   Windows:
   ```powershell
   .\venv\Scripts\activate
   ```
   
   Linux/macOS:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   ```bash
   python downloader.py
   ```

2. **Choose output folder** (or press Enter for default `downloads` folder)

3. **Select an option:**
   ```
   ==================================================
   OPTIONS:
   ==================================================
   1. Download files/folders from ONE Google Drive link
   2. Download files/folders from MULTIPLE Google Drive links
   3. Exit
   ==================================================
   ```

### Supported URL Formats

| Type | URL Format |
|------|------------|
| File | `https://drive.google.com/file/d/FILE_ID/view` |
| File | `https://drive.google.com/open?id=FILE_ID` |
| Folder | `https://drive.google.com/drive/folders/FOLDER_ID` |

## Examples

### Option 1: Download from ONE link
```
Enter choice (1-3): 1

[Single Link Download]
------------------------------
Enter Google Drive URL (file or folder): https://drive.google.com/drive/folders/1XYZ789abc
Detected: FOLDER URL
Folder name: Physics Notes
Downloading...
Successfully downloaded folder to: downloads\Physics Notes
```

### Option 2: Download from MULTIPLE links
```
Enter choice (1-3): 2

[Multiple Links Download]
------------------------------
Enter Google Drive URLs (one per line)
Press Enter on empty line when finished:

  Link 1: https://drive.google.com/drive/folders/abc123
  Link 2: https://drive.google.com/file/d/xyz789/view
  Link 3: https://drive.google.com/drive/folders/def456
  Link 4: 

==================================================
Starting download of 3 items...
==================================================

[1/3] Downloading...
...

==================================================
DOWNLOAD SUMMARY
==================================================
  Total: 3
  Success: 2
  Failed: 1
==================================================
```

## Output Structure

```
downloads/
├── Physics Notes/
│   ├── English.pdf
│   ├── Sinhala.pdf
│   └── subfolder/
│       └── extra.docx
├── Physics Notes (1)/       # Duplicate folder (auto-renamed)
│   └── ...
├── Chemistry Notes/
│   └── ...
└── single_file.pdf
```

## Error Handling

### Private/Inaccessible Links
```
==================================================
ERROR: Cannot access this folder!
==================================================
Possible reasons:
  1. The folder is PRIVATE (not shared)
  2. The folder requires sign-in
  3. The folder doesn't exist
  4. The link is invalid

Solution:
  - Ask the owner to share the folder
  - Set folder to 'Anyone with the link' can view
==================================================
```

### Permission Denied
```
==================================================
ERROR: Permission denied!
==================================================
The folder exists but you don't have access.
Ask the owner to change sharing settings to:
  'Anyone with the link' can view
==================================================
```

## Important Notes

⚠️ **Only public files/folders can be downloaded**

To download a file or folder, the owner must:
1. Right-click the file/folder in Google Drive
2. Click "Share"
3. Change "General access" to "Anyone with the link"
4. Click "Done"

## Dependencies

- `gdown` - Google Drive downloader
- `requests` - HTTP library
- `beautifulsoup4` - HTML parser

## License

MIT License

## Author

[DasunBatheegama](https://github.com/DasunBatheegama)

# Google Drive Downloader

A Python terminal application to download files and folders from Google Drive.

## Features

- ✅ Download single files from Google Drive
- ✅ Download entire folders with all contents
- ✅ Download multiple files/folders at once
- ✅ Preserves folder names and structure
- ✅ Handles duplicate names automatically (adds `(1)`, `(2)`, etc.)
- ✅ Detects private/inaccessible links with helpful error messages
- ✅ Progress bar for downloads
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
   - `1` - Download a single file or folder
   - `2` - Download multiple files/folders
   - `3` - Exit

### Supported URL Formats

| Type | URL Format |
|------|------------|
| File | `https://drive.google.com/file/d/FILE_ID/view` |
| File | `https://drive.google.com/open?id=FILE_ID` |
| Folder | `https://drive.google.com/drive/folders/FOLDER_ID` |

## Examples

### Download a single file
```
Enter choice (1-3): 1
Enter Google Drive URL: https://drive.google.com/file/d/1ABC123xyz/view
```

### Download a folder
```
Enter choice (1-3): 1
Enter Google Drive URL: https://drive.google.com/drive/folders/1XYZ789abc
```

### Download multiple items
```
Enter choice (1-3): 2
Enter Google Drive URLs (one per line, empty line to finish):
https://drive.google.com/file/d/1ABC123xyz/view
https://drive.google.com/drive/folders/1XYZ789abc

```

## Output Structure

```
downloads/
├── FolderName/
│   ├── file1.pdf
│   ├── file2.jpg
│   └── subfolder/
│       └── file3.docx
├── FolderName (1)/          # Duplicate folder
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

Solution:
  - Ask the owner to share the folder
  - Set folder to 'Anyone with the link' can view
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

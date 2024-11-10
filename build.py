import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'gui.py',
    '--onefile',
    '--windowed',
    '--name=NSE-Underlyings-Scraper',
    # '--add-data=underylings_20241110.csv;.',  # Include your data file
    # '--icon=app.ico',  # Optional: You can add this later with your own icon
])

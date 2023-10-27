from flask import Flask, render_template, request
from WallpaperDownloader import wallpaper_search_function

app = Flask(__name__)

@app.get('/')
def wallHome():
  return render_template('index.html')

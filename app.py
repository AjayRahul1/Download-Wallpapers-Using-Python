from flask import Flask, render_template, request
from WallpaperDownloader import wallpaper_search_function

app = Flask(__name__)

@app.get('/')
def wallHome():
  return render_template('index.html')

@app.get("/get_wps")
def return_wallpapers():
  wallpaper_search = request.args.get('wallpaper_search')
  urls = wallpaper_search_function(wallpaper_search)
  return render_template("images_htmx.html", urls=urls)
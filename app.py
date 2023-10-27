from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from WallpaperDownloader import wallpaper_search_function

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
def wallHome(request: Request):
  return templates.TemplateResponse('index.html', {"request": request})

@app.get("/get_wps")
def return_wallpapers(request: Request):
  wallpaper_search = request.query_params['wallpaper_search']
  urls = wallpaper_search_function(wallpaper_search)
  return templates.TemplateResponse("images_htmx.html", {"request": request, "urls": urls})
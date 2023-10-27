import requests
import os
import random
import string

def wallpaper_search_function(search_query):
    search_query = search_query.replace(" ", "+")
    wallpaper_search_url = f"https://wallhaven.cc/api/v1/search?q={search_query}"
    print("Searching for URL: ", wallpaper_search_url)
    wp_resources = requests.get(wallpaper_search_url)
    json_data_of_wallpapers = wp_resources.json()
    download_links =[]
    for wallpaper in json_data_of_wallpapers["data"]:
        download_links.append(wallpaper["path"])
    return download_links

def generate_id():
    return ''.join(random.choices(string.ascii_lowercase+string.digits, k=6))

def download_wallpapers(url, folder_to_be_created_for_wallpapers):
    print(f"Downloading... {url}")
    res = requests.get(url)
    wallpaper_name = generate_id() # Generate a random name for the wallpaper
    ext = os.path.splitext(url)[1]
    download_link_path = f"{folder_to_be_created_for_wallpapers}/{wallpaper_name}{ext}"
    # open(download_link_path,'wb').write(res.content)
    os.chdir(folder_to_be_created_for_wallpapers)
    os.system(f"wget {url}")

# wallpaper_search_name_input = input("Enter the name to download it's wallpapers: ").replace(" ", "%20")
# wallpaper_dl_url = wallpaper_search_function(wallpaper_search_name_input)
# parent_path = f"{os.path.expanduser('~')}/Downloads"
# folder_to_be_created_for_wallpapers = os.path.join(parent_path,wallpaper_search_name_input.replace("%20"," ")+" Wallpapers")
# os.mkdir(folder_to_be_created_for_wallpapers)
# # print(folder_to_be_created_for_wallpapers)
# for url in wallpaper_dl_url:
#     download_wallpapers(url,folder_to_be_created_for_wallpapers)

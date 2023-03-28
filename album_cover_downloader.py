import os
import requests

def download_album_cover(album_id):
    # Fetch album data from Deezer API
    url = f'https://api.deezer.com/album/{album_id}'
    response = requests.get(url)
    album_data = response.json()

    # Download album cover image
    cover_url = album_data['cover_big']
    image_data = requests.get(cover_url).content

    # Create output folder on the desktop if it doesn't exist
    desktop_path = os.path.expanduser("~/Desktop")
    output_folder = os.path.join(desktop_path, "album covers")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save album cover to a file with the album name
    album_name = album_data['title']
    output_file = f"{album_name}.jpg"
    output_path = os.path.join(output_folder, output_file)
    with open(output_path, 'wb') as f:
        f.write(image_data)

if __name__ == '__main__':
    album_id = input("Enter the album ID: ")
    download_album_cover(album_id)
    print("Album cover downloaded successfully.")
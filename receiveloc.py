import os
def receive_loc():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
    videos_path = os.path.join(os.path.expanduser('~'), 'Videos')
    music_path = os.path.join(os.path.expanduser('~'), 'Music')
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    pictures_path = os.path.join(os.path.expanduser('~'), 'Pictures')

    return desktop_path, documents_path, videos_path, music_path, downloads_path, pictures_path

desktop, documents, videos, music, downloads, pictures = receive_loc()
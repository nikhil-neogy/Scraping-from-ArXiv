import os
import urllib3

http = urllib3.PoolManager()


def download(url, file_path=None, chunk_size=65536):

    print("Downloading", file_path, "...")

    optional_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'
    }

    response = http.request('GET', url, preload_content=False, headers=optional_headers)

    if not file_path:
        file_path = os.path.join(os.getcwd(), 'downloads', 'filename.jpg')
    else:
        file_path = os.path.join(os.getcwd(), 'downloads', file_path)

    with open(file_path, 'wb') as out:
        while True:
            data = response.read(chunk_size)
            if not data:
                break
            out.write(data)

    response.release_conn()

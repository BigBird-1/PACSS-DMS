from tqdm import tqdm
import requests
import time
import os


path = os.path.split(os.path.realpath(__file__))[0]
current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
file_path = os.path.join(path, 'flow_file')


def download_file():
    url = "https://oe-upload.dms.t.hxqcgf.com/uploads/Fee/22061011/9f9259c9499c09d8b3740b81ed6f179a.zip"
    res = requests.get(url, stream=True)
    total = int(res.headers.get('Content-Length', 0))
    # print(total)
    txt_name = "5555.zip"
    txt_path = os.path.join(file_path, txt_name)

    with open(txt_path, 'wb') as f, tqdm(
            desc=txt_name,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            ncols=65
    ) as bar:
        for chunk in res.iter_content(chunk_size=1024):
            size = f.write(chunk)
            bar.update(size)


download_file()




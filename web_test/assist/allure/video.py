import time

import requests


def get_selenoid_video(video_url):
    response = None
    try:
        for i in range(10):
            try:
                response = requests.get(video_url, stream=True)
                if response.status_code == 200:
                    break
                else:
                    time.sleep(1)
            except requests.exceptions.RequestException:
                time.sleep(1)
        return response.content
    except Exception:
        pass
    return None

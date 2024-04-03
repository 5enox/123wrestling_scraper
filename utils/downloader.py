import os
import requests


def download_videos(data):
    # Replace with the actual path to your videos directory
    videos_dir = "/path/to/videos/directory"

    for entry in data:
        link = entry.get("link")
        if link:
            retry_count = 3  # Number of times to retry in case of network errors or failed downloads
            while retry_count > 0:
                try:
                    response = requests.get(link)
                    if response.status_code == 200:
                        # Assuming each entry has an 'id' key
                        video_path = os.path.join(
                            videos_dir, f"{entry['id']}.mp4")
                        with open(video_path, "wb") as f:
                            f.write(response.content)
                        entry["video_path"] = video_path
                        break  # Break out of the retry loop if download is successful
                except (requests.exceptions.RequestException, IOError):
                    retry_count -= 1
            else:
                # Set video_path to None if download fails after retries
                entry["video_path"] = None

    return data

from asyncio import streams
from pytube import YouTube
from app.download_file.schema import DownloadRequest
from typing import Any

    
async def download(data: DownloadRequest) -> DownloadRequest | str:
    url = YouTube(str(data.link))

    try:
        if data.output == 'audio': 
            audio = url.streams.get_audio_only()
            save_response = await __savePath(data=audio, directory_save=data.directory_save+ "/audio", filename=url.title + ".mp3")
        else:
            video = url.streams.get_highest_resolution()
            save_response = await __savePath(data=video, directory_save=data.directory_save + "/video", filename=url.title + ".mp4")

        return save_response
    except Exception as exception:
        return("Pytube unstable for repeated file downloads: ", exception)

async def __savePath(data:streams, directory_save: str, filename: str) -> Any | str:
    try:
        data.download(directory_save, filename=filename)
        return "file downloaded in current directory"

    except Exception as exception:
        return("Error!", exception)
    
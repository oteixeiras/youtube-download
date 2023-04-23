from asyncio import streams
from pytube import YouTube
from app.download_file.schema import DownloadRequest
from typing import Any

async def fetch_file(data: DownloadRequest) -> DownloadRequest | Any:
    try:
        url = YouTube(str(data.link))
        return await __download(url=url, optional_save=data.output, directory_save=data.directory_save)
    
    except Exception as exception:
        return("Pytube unstable for repeated file downloads: ", exception)
    
async def __download(url: str, optional_save: str, directory_save: str) -> Any:
    title = url.title

    try:
        if optional_save == 'audio': 
            audio = url.streams.get_audio_only()
            save_response = await __save(data=audio, directory_save=directory_save + "/audio", filename=title + ".mp3")
        else:
            video = url.streams.get_highest_resolution()
            save_response = await __save(data=video, directory_save=directory_save + "/video", filename=title + ".mp4")

        return save_response
    except Exception as exception:
        return("Error: ", exception)

async def __save(data:streams, directory_save: str, filename: str) -> Any:
    data.download(directory_save, filename=filename)
    return "file downloaded in current directory"

# if __name__ == "__main__":
#     main()
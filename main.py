from fastapi import FastAPI

from app.download_file import service
from app.download_file.schema import DowloadResponse, DownloadRequest

app = FastAPI()

@app.post("/download", status_code=200, response_model=DowloadResponse, tags=["youtube_download"], summary="Download a video or audio from youtube")
async def file_download(data: DownloadRequest):
    downloaded = await service.download(data)

    return DowloadResponse(message=downloaded, code=200)
 
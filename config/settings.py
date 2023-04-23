from starlette.config import Config

config = Config(".env")

PATH_SYTEM = config("PATH_SYTEM", default="/home/youtubeDownload/")
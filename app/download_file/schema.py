from pydantic import BaseModel, Field
from config.settings import PATH_SYTEM

class DownloadRequest(BaseModel):
    link: str = Field(default = "https://www.youtube.com/watch?v=9bZkp7q19f0")
    output: str = Field(default = "audio")
    directory_save: str = Field(default = PATH_SYTEM)

    class config:
        schema_extra = {
            "example": {
                "link": "https://www.youtube.com/watch?v=9bZkp7q19f0",
                "output": "audio",
                "directory_save": "C:/Users/Usuario/Downloads"
            }
        }

class DowloadResponse(BaseModel):
    message: str
    code: int

    class config:
        schema_extra = {
            "example": {
                "message": "file downloaded in current directory",
                "code": 200
            }
        }
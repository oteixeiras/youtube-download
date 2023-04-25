# API documentation - **Youtube Download**

  API to download files from youtube in audio or video format (Python - FastAPI)

# Version control

| Date       | Version | Description          | Author                    |
|------------|---------|----------------------|---------------------------|
| 22/04/2023 | 0.1.0   | Project creation     | **Fernando Teixeira** |

# Summary
1. [Endpoint Overview](#1-Endpoint-Overview)

2. [Environment Preparation](#2-Environment-Preparation)

3. [Contacts](#3-Contacts)

# 1. Endpoint-Overview 

    URL: http:/DOMAIN/youtube_download/file_download_post
    exemple DOMAIN: http://localhost:8000/

  <details>
    <summary> Default values for request</summary>

  ```json

    {
      "link": "https://www.youtube.com/watch?v=9bZkp7q19f0",
      "output": "audio",
      "directory_save": "/home/youtubeDownload/"
    }

  ```
  </details>  
  <details>
    <summary> Validate schema</summary>

  ```json

    {
      "link": string,
      "output": string,
      "directory_save": string,
    }

  ```
  </details>
  
# 2. Environment Preparation
### Via Local 
1. Clone the api repository:
    ```shell
    git clone git@github.com:oteixeiras/youtube-download.git
    ```
    
3. install the dependencies:
    ```shell
    make install
    ```

4. Configure environment variables:
    > **_NOTE:_** optional to change default download directory.
    ```shell
    PATH_SYTEM= <directory path>
    ```

5. Run the application:
     ```shell
     make run
     ```

6. For running unit tests locally:
   > **_NOTE:_** tests under construction.

     ```shell
     make test
     ```

# 3 Contacts
1. [Linkedin](https://www.linkedin.com/in/fernandodesouzateixeira)

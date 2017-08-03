This is a RESTful web service based on Python language with Flask API. This service performs four opereations on the data.csv file located at /opt/bitflow/data-collector/:
- size: fetches the data.csv file size in bytes
- lines: fetches total number of lines in data.csv file
- head: fetches starting x lines from the data.csv. By default, it is 1; however, if you speciy parameters ?num=10, it will fetch 10 lines from the start
- tail: fetches ending x lines from the data.csv. By default, it is 1; however, if you speciy parameters ?num=10, it will fetch 10 lines from the end

The service uses port 8000 for its operations.

Note: Before using this service, please change permissions on the data.csv file by entering the following command:
    sudo chmod 6444 file-path
However, this command is included in the shell scrip available on ~/scripts/ folder.

Systemd service code is located in /etc/systemd/system.
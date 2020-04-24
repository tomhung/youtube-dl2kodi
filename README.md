# youtube-dl2kodi

# options
youtube-dl2 -f <video.info.json>
 -f file path of the youtube-dl video.info.json file

# example
~~~~
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' \
--continue --ignore-errors --write-info-json --write-thumbnail --write-sub \ 
--output './Season 1/%(title)s-e%(playlist_index)s.%(ext)s' \ 
--exec 'youtube-dl2kodi.py -f {}' \
https://www.youtube.com/playlist?list=PLKocZwBnFDxNAoxyxZ0w7mum35YY4v0nb 
~~~~

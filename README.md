# VPD
VPD - Video Playlist Downloader.

# Usage
this script could help you for downloading blob videos 
<br>
you could use network tools in your browser, search for .m3u8 extension and download it
<br>
then copy url path of one those videos (which loaded in that page, you can find on developer tools too) and 
download videos using this script :)

- first clone repo (of course)
- then run ./main.py with following arguments:
1. m3u8 file: the playlist file you wanted to download its videos
2. uri path: such as https://statics.example.com/videos. where videos are located.
```bash
python main.py playlist.m3u8 https://static.example.com/videos
```

# How to combine files into one?
follow [this question](https://superuser.com/questions/692990/use-ffmpeg-copy-codec-to-combine-ts-files-into-a-single-mp4/693009) for .ts files. it's not hard

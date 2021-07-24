#!/usr/bin/env python3
"""
VideoPlaylistDownloader - VPD
download m3u8 playlists with given base uri

usage: main.py Playlist.m3u8 https://statics.example.com
"""
import requests
import sys
import os
from dataclasses import dataclass
from logger import Logger

@dataclass
class ReadFile:
    file_name: str
    lines = []
    videos = []

    def read_file(self) -> None:
        self.file_cursor = open(self.file_name, "r")

    def read_lines(self) -> None:
        for line in self.file_cursor.readlines():
            self.lines.append(line)
        self.file_cursor.close()

    def render_lines(self) -> None:
        global logger
        for l in self.lines:
            l = l.replace("\n", "")
            if l.startswith("#"):
                logger.log(f"`{l}`. continue...", "render_lines")
            else:
                logger.warning(f"Found {l}. adding to the queue...", "render_lines")
                self.videos.append(l)

    def get_videos(self) -> list:
        global logger
        functions = ["self.read_file()", "self.read_lines()", "self.render_lines()"]
        for func in functions:
            try:
                exec(func)
            except Exception as e:
                logger.error(e, func)
        return self.videos



@dataclass
class DownloadVideos:
    videos_list: list
    uri: str

    def make_dir(self) -> None:
        global file, logger
        try:
            self.dir_name = os.path.splitext(file)[0]
            os.mkdir(self.dir_name)
        except FileExistsError:
            logger.warning(f"cannot make directory `{self.dir_name}` because it eists. passing...", "make_dir")

    def download(self, file) -> bytes:
        try:
            logger.log(f"downloading {file}...", "download")
            file_binary = requests.get(self.uri + "/" + file).content
            logger.log("done.", "download")
            return file_binary 
        except Exception as e:
            logger.error(e, "download")

    def save(self, name, binary) -> None:
        try:
            logger.log(f"saving {name}...", "save")
            with open(self.dir_name + "/" + name, "wb") as file:
                file.write(binary)
            logger.log("saved.", "save")
        except Exception as e:
            logger.error(e, "save")
    
    def download_videos(self):
        self.make_dir()
        try:
            for video in self.videos_list:
                self.save(
                        video,
                        self.download(video)
                )
        except Exception as e:
            logger.error(e, "download_videos")
    

if __name__ == "__main__":
    logger: object = Logger()  # making a logger object
    
    # parsing arguments
    try:
        file: str = sys.argv[1]
        uri : str = sys.argv[2]
        logger.log(f"FILE: {file}", "__main__")
        logger.log(f"URI: {uri}", "__main__")

    except IndexError as e:
        logger.error("`file` or `uri` not specified", "__main__")
    
    # parsing list and finding videos
    readfile = ReadFile(file_name=file)

    # downloading the videos
    downloadvideos = DownloadVideos(videos_list=readfile.get_videos(), uri=uri)
    downloadvideos.download_videos()


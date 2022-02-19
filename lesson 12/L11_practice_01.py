# -*- coding: utf-8 -*-
# L11_practice_01.py
"""
1. Создайте 3 любых класса, у которых будут 3 атрибута и 1 метод
"""

class Song:
    def __init__(self, singer, song_name, play_time):
        self.singer = singer
        self.song_name = song_name
        self.play_time = play_time
    def get_info(self):
        print(f'{self.singer} - {self.song_name} ({self.play_time})')

song = Song('竹内まりや', '夢の続き', '4:50')
song.get_info()
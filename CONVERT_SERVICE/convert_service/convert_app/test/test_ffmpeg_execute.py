#
# @test_ffmpeg_execute.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from unittest import TestCase
from ..model.ffmpeg.ffmpeg_execute import ffmpegexecute
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent


class Test(TestCase):
    def test_ffmpegexecute(self):
        filepath = str(BASE_DIR) + '/resources_test/video_test/testvideo.mp4'
        print(filepath)
        current = ffmpegexecute(filepath)
        expected = f'ffmpeg -i "{filepath}"  -r 1/1  "images/%04d.jpg"'
        self.assertEqual(current, expected)

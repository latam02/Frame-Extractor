#
# @ffmpeg_execute.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from .frame_extractor import FrameExtractor
from .python_parameters import PythonParameters
from .folder_check import FolderCheck
from .frameExtractor_execute import Execute
import os


def ffmpegexecute(videopath):
    folderCheck = FolderCheck
    folderCheck.execute()
    pythonParameters = PythonParameters(videopath, 'images/%04d.jpg')  # Video input, Frames Output
    frameExtractor = FrameExtractor()
    command = frameExtractor.build(pythonParameters)

    # Execute class fmex_execute
    execute = Execute(command)
    execute.run()

    return command


# In our output of images %04d = 4 zeros equals 2,70 hrs, %05d = 5 zeros equals 27 hrs

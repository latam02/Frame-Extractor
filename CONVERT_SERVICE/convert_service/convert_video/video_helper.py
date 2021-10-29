#
# @video_helper.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
import os
from django.core.files.storage import FileSystemStorage
from exception import video_exception
from util.utilities import Utilities


class VideoHelper:
    """ Methods that validate inputs and outputs """

    def __init__(self, session_key, base_dir):
        self.session_id = session_key
        self.directory = base_dir

    # Method that validates if at least one video is uploaded
    def validatefiles(self, total_files, vs_horizontally: str, vs_vertically: str):

        if int(total_files) == 0:
            raise video_exception.VideoException("Error", "At least one video must be uploaded")

        if ((str(vs_horizontally) == "1") | (str(vs_vertically) == "1")) & int(total_files) == 1:
            raise video_exception.VideoException("Error", "For this option, two videos are required")

    # Method that saves the files
    def savefile(self, uploaded_file):

        filename = self.session_id + "_" + uploaded_file.name
        full_filename = str(self.directory) + "/media/" + filename

        fs = FileSystemStorage()
        fs.save(full_filename, uploaded_file)
        return full_filename

    # Executing the commands obtained
    def excutecommands(self, commands):

        for cmd in commands:
            if cmd.startswith("rename"):
                # KB: https://pynative.com/python-rename-file/
                os.rename(cmd.split('|')[1], cmd.split('|')[2])
            else:
                os.system(cmd)

        # Deleting extra files - KB: https://pynative.com/python-delete-files-and-directories/
        pattern = str(self.directory) + "/media/" + self.session_id + "_*"
        Utilities.DeleteFilesPattern(pattern)

    def buildresult(self, request, vs_horizontally, vs_vertically, vs_remove_audio, vs_rotate, vs_percentage,
                    vs_reduce_video):

        # Setting up the route to the final result - KB: https://try2explore.com/questions/10019689
        relative_file = Utilities.GenerateFinalUrl(request, self.session_id + ".mp4")

        result = {
            "id": self.session_id,
            "status": "OK",
            "videoOutput": str(relative_file),
            "params": {
                "horizontally": vs_horizontally,
                "vertically": vs_vertically,
                "remove_audio": vs_remove_audio,
                "rotate": vs_rotate,
                "percentage": vs_percentage,
                "reduce_video": vs_reduce_video
            }
        }
        return result

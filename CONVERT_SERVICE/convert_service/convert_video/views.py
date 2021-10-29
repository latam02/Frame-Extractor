#
# @views.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
import uuid
import json
from django.views import View
from django.http import HttpResponse
from pathlib import Path
from .model.VideoConverterModel import VideoConverterModel
from .video_helper import VideoHelper
from util.utilities import Utilities
from exception.video_exception import VideoException


class VideoConverter(View):
    """ Video converter endpoint, call video converter model module with the parameters
        selected  and returns a new video according to the selection made. """

    # Method running the video converter
    def post(self, request):

        # Generating a unique identifier as a session key
        session_key = str(uuid.uuid4().hex)

        # Get base directory for the file
        base_dir = Path(__file__).resolve().parent.parent

        result_type = 'application/json'

        try:
            # Upload files and parameters
            vs_horizontally = request.POST.get('horizontally', "0")
            vs_vertically = request.POST.get('vertically', "0")
            vs_remove_audio = request.POST.get('remove_audio', "0")
            vs_rotate = request.POST.get('rotate', "0")
            vs_percentage = request.POST.get('percentage', "0")
            vs_reduce_video = request.POST.get('reduce_video', "0")

            helper = VideoHelper(session_key, base_dir)

            # Validate inputs
            total_files = len(request.FILES)
            helper.validatefiles(total_files, vs_horizontally, vs_vertically)

            # Save videos
            full_filename1 = helper.savefile(request.FILES['file'])
            full_filename2 = ''
            if (str(vs_horizontally) == "1") | (str(vs_vertically) == "1"):
                full_filename2 = helper.savefile(request.FILES['file2'])

            # Video treatment
            video = VideoConverterModel()
            commands = video.GetCommandsForVideo(str(base_dir), session_key, vs_horizontally == "1",
                                                 vs_vertically == "1", vs_remove_audio == "1", vs_rotate == "1",
                                                 vs_percentage, vs_reduce_video == "1", full_filename1,
                                                 full_filename2)

            # Execute commands
            helper.excutecommands(commands)

            # format response
            result = helper.buildresult(request, vs_horizontally, vs_vertically, vs_remove_audio, vs_rotate,
                                        vs_percentage, vs_reduce_video)
            return HttpResponse(json.dumps(result), result_type)

        except VideoException as e_video:
            # Delete extra files - KB: https://pynative.com/python-delete-files-and-directories/
            pattern = str(base_dir) + "/media/" + session_key + "_*"
            Utilities.DeleteFilesPattern(pattern)

            result_error = {
                "id": session_key,
                "code": e_video.code,
                "status": e_video.status,
                "message": str(e_video.message)
            }
            # Result in json
            return HttpResponse(json.dumps(result_error), result_type)

        except Exception as e:
            # Delete extra files - KB: https://pynative.com/python-delete-files-and-directories/
            pattern = str(base_dir) + "/media/" + session_key + "_*"
            Utilities.DeleteFilesPattern(pattern)

            result_error = {
                "id": session_key,
                "status": "error",
                "message": str(e)
            }
            # Result in json
            return HttpResponse(json.dumps(result_error), result_type)

#
# @tests.py Copyright (c) 2021 Jalasoft.
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
from unittest import TestCase
from convert_video.model.VideoConverterModel import VideoConverterModel
from convert_video.video_helper import VideoHelper
from exception.video_exception import VideoException


class TestVideoConverterModel(TestCase):
    """ Create your tests here. """

    # Positive unit test: Rotate the image clockwise and vertical flip
    def test_GetCommandsForVideo1(self):
        BASE_DIR = 'D:\GITHUB\ATLatam2\CONVERT_SERVICE\convert_service'
        sessionkey = str(uuid.uuid4().hex)
        vt_horizontally = False
        vt_vertically = False
        vt_remove_audio = False
        vt_rotate = 1
        vt_percentage = 3
        vt_reduce_video = False
        input1 = str(BASE_DIR) + "/media/" + sessionkey + "_" + 'input1.mp4'
        output = str(BASE_DIR) + "/media/" + sessionkey + '_output'

        call_method = VideoConverterModel()
        execute_method = call_method.GetCommandsForVideo(BASE_DIR, sessionkey, vt_horizontally, vt_vertically,
                                                         vt_remove_audio, vt_rotate, vt_percentage, vt_reduce_video,
                                                         input1)

        current = execute_method[0]
        expected = 'ffmpeg -i ' + input1 + ' -vf "transpose=' + str(vt_percentage) + '" ' + output + '.mp4'
        self.assertEqual(current, expected)

    # Positive unit test: Place two videos horizontally in parallel, remove video and rotate the video clockwise
    def test_GetCommandsForVideo2(self):
        BASE_DIR = 'D:\GITHUB\ATLatam2\CONVERT_SERVICE\convert_service'
        sessionkey = str(uuid.uuid4().hex)
        vt_horizontally = True
        vt_vertically = False
        vt_remove_audio = True
        vt_rotate = True
        vt_percentage = 1
        vt_reduce_video = False
        input1 = str(BASE_DIR) + "/media/" + sessionkey + "_" + 'input1.mp4'
        input2 = str(BASE_DIR) + "/media/" + sessionkey + "_" + 'input2.mp4'
        output = str(BASE_DIR) + "/media/" + sessionkey + '_output'

        call_method = VideoConverterModel()
        execute_method = call_method.GetCommandsForVideo(BASE_DIR, sessionkey, vt_horizontally, vt_vertically,
                                                         vt_remove_audio, vt_rotate, vt_percentage, vt_reduce_video,
                                                         input1, input2)

        current = execute_method[0] + execute_method[1] + execute_method[2]
        expected = 'ffmpeg -i ' + input1 + ' -i ' + input2 + ' -filter_complex hstack=inputs=2 ' + output + '.mp4' + \
                   'ffmpeg -i ' + output + '.mp4' + ' -c:v copy -an ' + output + '1.mp4' + \
                   'ffmpeg -i ' + output + '1.mp4 -vf "transpose=' + str(vt_percentage) + '" ' + output + '13.mp4'
        self.assertEqual(current, expected)

    # Positive unit test: Place two videos vertically in parallel and reduce video size
    def test_GetCommandsForVideo3(self):
        BASE_DIR = 'D:\GITHUB\ATLatam2\CONVERT_SERVICE\convert_service'
        sessionkey = str(uuid.uuid4().hex)
        vt_horizontally = False
        vt_vertically = True
        vt_remove_audio = False
        vt_rotate = False
        vt_percentage = 0
        vt_reduce_video = True
        input1 = str(BASE_DIR) + "/media/" + sessionkey + "_" + 'input1.mp4'
        input2 = str(BASE_DIR) + "/media/" + sessionkey + "_" + 'input2.mp4'
        output = str(BASE_DIR) + "/media/" + sessionkey + '_output'

        call_method = VideoConverterModel()
        execute_method = call_method.GetCommandsForVideo(BASE_DIR, sessionkey, vt_horizontally, vt_vertically,
                                                         vt_remove_audio, vt_rotate, vt_percentage, vt_reduce_video,
                                                         input1, input2)

        current = execute_method[0] + execute_method[1]
        expected = 'ffmpeg -i ' + input1 + ' -i ' + input2 + ' -filter_complex vstack=inputs=2 ' + output + '.mp4' + \
                   'ffmpeg -i ' + output + '.mp4' + ' -vf scale=220:240 -preset slow -crf 18 ' + output + '2.mp4'
        self.assertEqual(current, expected)

    # Negative unit test: Place two videos vertically in parallel and reduce video size
    def test_validatefiles(self):
        vs_horizontally = "1"
        vs_vertically = "0"
        base_dir = 'D:\GITHUB\ATLatam2\CONVERT_SERVICE\convert_service'
        session_key = str(uuid.uuid4().hex)
        total_files = 0

        try:
            helper = VideoHelper(session_key, base_dir)
            helper.validatefiles(total_files, vs_horizontally, vs_vertically)

        except VideoException as err_video:
            current = err_video.message
            expected = 'At least one video must be uploaded'
            self.assertEqual(current, expected)

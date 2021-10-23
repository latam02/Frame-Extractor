#
# @video_exception.py Copyright (c) 2021 Jalasoft
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


class VideoException(Exception):
    """ Class of the controlled exceptions """
    def __init__(self, vf_status, vf_message):
        self.code = "Latam-video-03"
        self.status = vf_status
        self.message = vf_message
        super().__init__(self.message)

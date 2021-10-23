#
# @python_parameters.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

class PythonParameters:
    # Estos son nuestros parametros de la ubicacion del video y de las imagenes
    def __init__(self, video_path, img_output_path):
        self.video_path = video_path
        self.img_output_path = img_output_path

    def get_video_path(self):
        return self.video_path

    def get_img_output_path(self):
        return self.img_output_path

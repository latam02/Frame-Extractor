#
# @frame_extractor.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

class FrameExtractor:
    def build(self, parameter):
        video_input = parameter.get_video_path()                 # Ubicacion de nuestro video
        images_output = parameter.get_img_output_path()          # Ubicacion de nuestros fotrogramas

        #  -i Separador de frames | -r = fottogramas x segundo | -s 200x200 resolucion |
        command = f'ffmpeg -i "{video_input}"  -r 1/1  "{images_output}"'

        return command

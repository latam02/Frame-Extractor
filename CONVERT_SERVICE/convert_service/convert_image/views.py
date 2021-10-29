#
# @views.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .model.convert_image import ConvertImage
from .model.convert_image_params import ConvertImageParams
from .model.file import File


class ImageConverter(View):
    """ Image converter endpoint """
    def post(self, request):

        file: File = File(request)
        param: ConvertImageParams = ConvertImageParams(file.get_file_image(), request)

        new_image: ConvertImage = ConvertImage(request)
        new_image.convert(param)
        return new_image.get_result()

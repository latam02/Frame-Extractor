#
# @convert_image_params.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

class ConvertImageParams:
    """Class to manage the params to convert image"""

    def __init__(self, filename, request):
        self.filename = filename
        self.grayscale = self.except_request(request, 'grayscale')
        self.blur = self.except_request(request, 'blur')
        self.adaptive_sharpen = self.except_request(request, 'adaptive_sharpen')
        self.resize = self.except_request(request, 'resize')
        self.flip = self.except_request(request, 'flip')
        self.flop = self.except_request(request, 'flop')
        self.rotate = self.except_request(request, 'rotate')
        self.noise = self.except_request(request, 'noise')
        self.charcoal = self.except_request(request, 'charcoal')
        self.matrix = self.except_request(request, 'matrix')
        self.implode = self.except_request(request, 'implode')
        self.vignette = self.except_request(request, 'vignette')

    def get_filename(self):
        return self.filename

    def get_grayscale(self):
        return self.grayscale

    def get_blur(self):
        return self.blur

    def get_adaptive_sharpen(self):
        return self.adaptive_sharpen

    def get_resize(self):
        return self.resize

    def get_flip(self):
        return self.flip

    def get_flop(self):
        return self.flop

    def get_rotate(self):
        return self.rotate

    def get_noise(self):
        return self.noise

    def get_charcoal(self):
        return self.charcoal

    def get_matrix(self):
        return self.matrix

    def get_implode(self):
        return self.implode

    def get_vignette(self):
        return self.vignette

    # Function to validate requests to convert images
    @staticmethod
    def except_request(request, value):
        try:
            return request.POST[value]
        except:
            return False

#
# @file.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from django.http import HttpResponse
import json


class File:
    """Class to upload image"""

    def __init__(self, request):
        self.uploaded_file = self.except_request_file_image(request)
        fs = FileSystemStorage()
        # Save the file
        try:
            fs.save(self.uploaded_file.name, self.uploaded_file)
            file = self.uploaded_file.name
        except:
            return None
        # Set the path to the requested file
        filename = file
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.filepath = str(BASE_DIR) + "/media/" + filename

    def get_file_image(self):
        return self.filepath

    @staticmethod
    def except_request_file_image(request):
        try:
            return request.FILES['file']
        except:
            result_error = {
                "status": "ERROR",
                "imageOutput": "NOT IMAGE"
            }
            return HttpResponse(json.dumps(result_error), 'application/json')
        return HttpResponse("Please, used method POST")

#
# @utilities.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
import glob
import os
from django.contrib.sites.shortcuts import get_current_site


class Utilities:
    """Utilities to generate the url of the final file and delete extra files """

    # Method that generates the url to visualize the result video
    @staticmethod
    def GenerateFinalUrl(request, namefile: str):
        relative_file = "http://" + str(get_current_site(request).domain) + "/media/" + namefile
        return relative_file

    @staticmethod
    # Method that deletes extra files - KB: https://pynative.com/python-delete-files-and-directories/
    def DeleteFilesPattern(pattern: str):
        files = glob.glob(pattern)
        # deleting the files with pattern
        for file in files:
            os.remove(file)

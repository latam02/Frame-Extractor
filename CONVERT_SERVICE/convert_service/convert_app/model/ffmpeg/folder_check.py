#
# @folder_check.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import os
import shutil


class FolderCheck:
    # Verifica si la carpeta images existe y la crea, o borra el contenido
    @staticmethod
    def execute():
        if os.path.exists("images"):
            shutil.rmtree("images")
            os.mkdir("images")
        else:
            os.mkdir("images")

#
# @frameExtractor_execute.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import subprocess


# Ejecutable para iniciar el frame extractor
class Execute:
    def __init__(self, cmd):
        self._cmd = cmd

    def run(self):
        result = subprocess.check_output(self._cmd, shell=True)
        return result

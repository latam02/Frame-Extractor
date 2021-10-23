#
# @convert_exception.py Copyright (c) 2021 Jalasoft
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


class ConvertException(Exception):
    """ Class of the controlled exceptions """
    def __init__(self, message):
        self.code = "Latam-convert-01"
        self.status = ""
        self.message = ""
        super().__init__(self.message)

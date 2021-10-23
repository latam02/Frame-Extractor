#
# @urls.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from django.conf.urls.static import static
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

urlpatterns = [
    path('', csrf_exempt(views.Converter.as_view()))
]

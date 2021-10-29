#
# @test_convert_image.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from pathlib import Path
from unittest import TestCase
from wand.image import Image

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent


class TestImageConverter(TestCase):
    """Class to test functions of the library to convert images, using some effects or dimensions changes"""
    def test_convert_blur(self):
        filepath = str(BASE_DIR) + '/resources_test/image_test/google.jpg'
        with Image(filename=filepath) as img:
            blur_radius = 10
            blur_sigma = 10
            img.blur(radius=blur_radius, sigma=blur_sigma)
            current = str(img)
            expected = "<wand.image.Image: c165216 'JPEG' (2400x1600)>"
            self.assertEqual(current, expected)

    def test_convert_grayscale(self):
        filepath = str(BASE_DIR) + '/resources_test/image_test/google.jpg'
        with Image(filename=filepath) as img:
            img.type = 'grayscale'
            current = str(img)
            expected = "<wand.image.Image: 1c9a025 'JPEG' (2400x1600)>"
            self.assertEqual(current, expected)

    def test_convert_resize(self):
        filepath = str(BASE_DIR) + '/resources_test/image_test/google.jpg'
        with Image(filename=filepath) as img:
            width = 1000
            height = 500
            img.resize(width, height)
            current = str(img)
            expected = "<wand.image.Image: 1885189 'JPEG' (1000x500)>"
            self.assertEqual(current, expected)

    def test_convert_blur_grayscale_resize(self):
        filepath = str(BASE_DIR) + '/resources_test/image_test/google.jpg'
        with Image(filename=filepath) as img:
            blur_radius = 10
            blur_sigma = 10
            img.blur(radius=blur_radius, sigma=blur_sigma)
            img.type = 'grayscale'
            width = 1000
            height = 500
            img.resize(width, height)
            current = str(img)
            expected = "<wand.image.Image: 1b2a8e8 'JPEG' (1000x500)>"
            self.assertEqual(current, expected)

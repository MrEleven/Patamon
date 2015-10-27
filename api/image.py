#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-27
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
import module.image_ctrl as image_ctrl

class UploadHandler(tornado.web.RequestHandler):
    """上传图片"""
    def post(self):
        """上传图片"""
        image = self.request.files.get("image", [])
        if not image:
            return ""
        image_url = image_ctrl.upload_pic(image)
        return self.write(image_url)
        

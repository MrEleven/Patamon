#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-27
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
import os

from tornado.options import define, options
define("port", default=8088, help="run on the given port", type=int)

from api.image import UploadHandler, TestHandler

if __name__ == "__main__":
    tornado.options.parse_command_line()
    handlers = [(r"/image/upload", UploadHandler), (r"/test", TestHandler)]
    app = tornado.web.Application(
        handlers=handlers,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

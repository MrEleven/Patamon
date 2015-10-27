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

from tornado.options import define, options
define("port", default=8088, help="run on the given port", type=int)

from api.image import UploadHandler

if __name__ == "__main__":
    tornado.options.parse_command_line()
    handlers = [(r"/image/upload", UploadHandler)]
    app = tornado.web.Application(
        handlers=handlers,
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

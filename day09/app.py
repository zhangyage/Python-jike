#!/usr/bin/env python
# -*- coding:utf-8 -*-
from dominate.tags import header


#wsgi app first

# 1、environ参数是个字典对象，包含CGI风格的环境变量
# 2、start_response参数是一个接受两个固定参数和一个可选参数的可调用者

#定义这两参数，参数名称名并不是一定要这个名字
def application(environ, start_response):
    response_body = "<h1>Hello World</h1>"
    
    header = [('Content-Type','text/html')]
    status = "200 OK"
    
    start_response(status, header)
    
    print "environ http request method:"+environ['REQUEST_METHOD']
    
    return [response_body]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    #导入标准的wsgi库  使用wsgiserverer运行
    httpd = make_server("0.0.0.0", 8080, application)
    print "httpd run on :" + str(httpd.server_port)
    httpd.serve_forever()
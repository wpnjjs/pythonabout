# coding:utf-8

'''
@author: monster
@file: serverwebpy.py.py
@time: 2018/1/23 下午3:46
'''

import web

render = web.template.render('templates/')

urls = ('/', 'hello',
        '/hello', 'hi')

app = web.application(urls, globals())


class hello:
    def GET(self):
        # if not name:
        #     name = 'world'
        # return 'hi' + name
        i = web.input(name=None)
        return render.index(i.name)


class hi:
    def GET(self): return "hello"


if __name__ == '__main__':
    pass
    # app.run()
    # print app.request('/hi').data

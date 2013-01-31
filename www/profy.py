#!/usr/bin/python

import os
import re
import web

LOGDIR='../log'
STATICDIR='static'

templates = web.template.render('templates')


class Log(object):
	def GET(self, log):
		log = re.sub(r'[^A-Za-z.-]', '', log)
		return open(os.path.join(LOGDIR, log)).read()


class Static(object):
	def GET(self, fn):
		fn = re.sub(r'[^A-Za-z.-]', '', fn)
		return open(os.path.join(STATICDIR, log)).read()


class Index(object):
	def GET(self):
		web.header('Content-Type', 'text/html; charset=UTF-8')
		return templates.index(os.listdir(LOGDIR))


def main():
	urls = (
		r'/log/(.*)', 'Log',
		r'/static/(.*)', 'Static',
		r'/', 'Index',
	)
	app = web.application(urls, globals())

	app.run()

if __name__ == '__main__':
	main()

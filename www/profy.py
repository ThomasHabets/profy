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


class Cmd(object):
	CMDS = {
		'ifconfig': '/sbin/ifconfig',
		'ip_addr': '/sbin/ip a l',
		'ip_route': '/sbin/ip r l',
		'iptables': '../bin/iptables-list',
	}
	def GET(self, cmd):
		return os.popen(self.CMDS[cmd]).read()


class Static(object):
	def GET(self, fn):
		fn = re.sub(r'[^A-Za-z.-]', '', fn)
		return open(os.path.join(STATICDIR, log)).read()


class Index(object):
	def GET(self):
		web.header('Content-Type', 'text/html; charset=UTF-8')
		return templates.index(os.listdir(LOGDIR),
				       Cmd.CMDS)


def main():
	urls = (
		r'/log/(.*)', 'Log',
		r'/cmd/(.*)', 'Cmd',
		r'/static/(.*)', 'Static',
		r'/', 'Index',
	)
	app = web.application(urls, globals())
	app.run()

if __name__ == '__main__':
	main()

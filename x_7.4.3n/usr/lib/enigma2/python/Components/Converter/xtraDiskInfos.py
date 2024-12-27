# -*- coding: utf-8 -*-
# by digiteng...04.2022
# <widget source="session.CurrentService" render="Label" position="1265,900" size="600,40" zPosition="1" font="Console; 24" transparent="1" foregroundColor="fc" backgroundColor="black">
	# <convert type="xtraDiskInfos">flash_info:short</convert>
# </widget>
from Components.Converter.Converter import Converter
from Components.Element import cached
from Components.Converter.Poll import Poll
import os
try:
	paths = ('/media/hdd', '/media/usb', '/media/sda1', '/media/sda2')
	for path in paths:
		if os.path.ismount(path):
			path = path
			break
except:
	path = "/"


class xtraDiskInfos(Poll, Converter, object):

	def __init__(self, type):
		Converter.__init__(self, type)
		Poll.__init__(self)
		self.type = type
		self.poll_interval = 1000
		self.poll_enabled = True

	@cached
	def getText(self):

		if "flashInfo" in self.type:
			st = os.statvfs("/")	# flash...
			free = self.inf(st)[0]
			total = self.inf(st)[4]
			if "short" in self.type:
				return "FLASH {:.1f} {szf} / {:.1f} {szt}".format(self.sizename(free)[1], self.sizename(total)[1], 
						szf=self.sizename(free)[0], szt=self.sizename(total)[0])
			return"\c0000????FLASH \c00eeeeeeTotal:\c00bbbbbb{:.1f} {szt}, \c00eeeeeeFree:\c00bbbbbb{:.1f} {szf} ({}%) ".format(
					self.sizename(total)[1], self.sizename(free)[1], self.inf(st)[1], 
					szf=self.sizename(free)[0], szt=self.sizename(total)[0])
		if "diskInfo" in self.type:
			st = os.statvfs(path) # hdd or usb
			free = self.inf(st)[0]
			total = self.inf(st)[4]
			if "short" in self.type:
				return "DISK {:.1f} {szf} / {:.1f} {szt}".format(self.sizename(free)[1], self.sizename(total)[1], 
						szf=self.sizename(free)[0], szt=self.sizename(total)[0])
			return "\c0000????{} \c00eeeeeeTotal:\c00bbbbbb{:.1f} {szt}, \c00eeeeeeFree:\c00bbbbbb{:.1f} {szf} ({}%) ".format(path, 
					self.sizename(total)[1], self.sizename(free)[1], self.inf(st)[1], 
					szf=self.sizename(free)[0], szt=self.sizename(total)[0])

		if "ramInfo" in self.type:
			mem = self.meminfo()
			for i in mem:
				mem = i.split()
				if mem[0] == "MemFree:":
					mf = int(mem[1]) // 1000
				if mem[0] == "MemTotal:":
					mt = int(mem[1]) // 1000
			if mt != 0:
				p = 100 - int(float(mf) / float(mt) * 100)
			else:
				p = 0
			return "\c0000????RAM \c00eeeeeeFree:\c00bbbbbb{} {szf} \c00eeeeeeTotal:\c00bbbbbb{} {szt} \c00eeeeeeUsed:{}%".format(mf, mt, p, szf=self.sizename(mf)[0], szt=self.sizename(mt)[0])
		if "swapInfo" in self.type:
			mem = self.meminfo()
			for i in mem:
				mem = i.split()
				if mem[0] == "SwapFree:":
					sf = int(mem[1]) // 1000
				if mem[0] == "SwapTotal:":
					st = int(mem[1]) // 1000
			if st != 0:
				p = 100 - int(float(sf) / float(st) * 100)
			else:
				return 0
			return "\c0000????SWAP \c00eeeeeeFree:\c00bbbbbb{} {szf} \c00eeeeeeTotal:\c00bbbbbb{} {szt} \c00eeeeeeUsed:\c00bbbbbb{}%".format(sf, st, p, szf=self.sizename(sf)[0], szt=self.sizename(st)[0])

	text = property(getText)

	@cached
	def getValue(self):

		if "flashProgress" in self.type:
			st = os.statvfs("/")
			return self.inf(st)[3]
		if "diskProgress" in self.type:
			st = os.statvfs(path)
			return self.inf(st)[3]
		if "ramProgress" in self.type:
			mem = self.meminfo()
			for i in mem:
				mem = i.split()
				if mem[0] == "MemFree:":
					mf = int(mem[1]) // 1000
				if mem[0] == "MemTotal:":
					mt = int(mem[1]) // 1000
			if mt != 0:
				return 100 - int(float(mf) / float(mt) * 100)
			else:
				return 0
		if "swapProgress" in self.type:
			mem = self.meminfo()
			for i in mem:
				mem = i.split()
				if mem[0] == "SwapFree:":
					sf = int(mem[1]) // 1000
				if mem[0] == "SwapTotal:":
					st = int(mem[1]) // 1000
			if st != 0:
				return 100 - int(float(sf) / float(st) * 100)
			else:
				return 0

	value = property(getValue)
	range = 100
	
	def inf(self, st):
		try:
			free = 0.0
			used = 0.0
			total = 0.0
			percent_free = 0.0
			percent_used = 0.0
			free = st.f_bavail * st.f_frsize / 1024000
			used = (st.f_blocks - st.f_bfree) * st.f_frsize / 1024000
			total = st.f_blocks * st.f_frsize / 1024000
			percent_free = (100 * st.f_bavail) // st.f_blocks
			percent_used = (100 * (st.f_blocks - st.f_bfree )) // st.f_blocks
			return free, percent_free, used, percent_used, total
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
				
	def meminfo(self):
		mem = ""
		try:
			with open("/proc/meminfo", "r") as f:
				mem = f.readlines()
		except:
			with open("/proc/meminfo", "rb") as f:
				mem = f.read()		
		return mem
		
	def sizename(self, value):
		sz = ["MB", "GB"]
		if value <= 1000:
			szs = sz[0]
			value = float(value)
		else:
			szs = sz[1]
			value = value / 1000
		return szs, value
		
	def changed(self, what):
		if what[0] == self.CHANGED_POLL:
			Converter.changed(self, what)
			
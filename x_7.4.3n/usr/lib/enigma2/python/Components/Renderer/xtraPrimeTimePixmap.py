# -*- coding: utf-8 -*-
# by digiteng, 03.10.2024
# for ch
# <widget render="xtraPrimeTimePixmap" source="ServiceEvent" mode="backdrop" position="90,700" size="300,170" zPosition="2" transparent="1" cornerRadius="20" />
# <widget render="xtraPrimeTimePixmap" source="ServiceEvent" mode="poster" position="900,700" size="185,278" zPosition="2" transparent="1" cornerRadius="20" />

from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import eLabel, eEPGCache, eServiceReference, eWidget, ePixmap, eTimer
from time import localtime, mktime, time
from datetime import datetime
from Components.config import config
import os
from skin import parseColor
from Tools.xtraTool import REGEX, pathLoc

class xtraPrimeTimePixmap(Renderer):

	def __init__(self):
		Renderer.__init__(self)
		self.epgcache = eEPGCache.getInstance()

	def applySkin(self, desktop, screen):
		attribs = self.skinAttributes[:]
		for attrib, value in self.skinAttributes:
			if attrib == 'position':
				self.px = int(value.split(',')[0])
				self.py = int(value.split(',')[1])
			elif attrib == 'size':
				self.szX = int(value.split(',')[0])
				self.szY = int(value.split(',')[1])
			elif attrib == 'backgroundColor':
				self.backgroundColor = value
			elif attrib == 'mode':
				self.mod = value
			elif attrib == 'fontSize':
				self.fontSize = int(value)
			
		self.skinAttributes = attribs
		return Renderer.applySkin(self, desktop, screen)

	GUI_WIDGET = ePixmap
	def changed(self, what):
		if not self.instance:
			return

		if what[0] != self.CHANGED_CLEAR:
			try:
				event = self.source.event
				if event is None:
					self.instance.hide()
					return
				try:
					service = self.source.service
				except:
					import NavigationInstance
					service = NavigationInstance.instance.getCurrentlyPlayingServiceReference()
				primetime = "N/A"
				try:
					prime_hour = config.epgselection.graph_primetimehour.value
					prime_minute = config.epgselection.graph_primetimemins.value
				except:
					prime_hour = 20
					prime_minute = 15
				bt = None
				now = localtime(time())
				dt = datetime(now.tm_year, now.tm_mon, now.tm_mday, prime_hour, prime_minute)
				pt = int(mktime(dt.timetuple()))
				self.epgcache.startTimeQuery(eServiceReference(service), pt)
				evn = self.epgcache.getNextTimeEntry()
				eNm = evn.getEventName()
				evntNm = REGEX.sub('', eNm).strip()
				bcdrpNm = "{}xtraEvent/backdrop/{}.jpg".format(pathLoc, evntNm)
				pstrNm = "{}xtraEvent/poster/{}.jpg".format(pathLoc, evntNm)
				if evn and (now.tm_hour <= prime_hour):
					bt = localtime(evn.getBeginTime())
					duration = round(evn.getDuration() // 60)
					primetime = "\c0000????Prime Time\n\c00aaaaaa%02d:%02d \n%smin\c00??????\n%s"%(bt[3], bt[4], duration, evntNm)
					if self.mod == "backdrop":
						self.instance.setPixmapFromFile(bcdrpNm)
						self.instance.setScale(1)
						self.instance.show()
					elif self.mod == "poster":
						self.instance.setPixmapFromFile(pstrNm)
						self.instance.setScale(1)
						self.instance.show()
					else:
						self.instance.hide()
				else:
					self.instance.hide()
			except Exception as err:
				from Tools.xtraTool import errorlog
				errorlog(err, __file__)

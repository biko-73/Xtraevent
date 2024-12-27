# -*- coding: utf-8 -*-
# by digiteng, 03.10.2024
# for ch
# <widget render="xtraPrimeTimeLabel" source="ServiceEvent" position="90,800" size="300,70" font="Regular;14" backgroundColor="#50000000" noWrap="1" zPosition="9" transparent="1" cornerRadius="20" />

from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import eLabel, eEPGCache, eServiceReference, eWidget, ePixmap, loadJPG, eTimer
from time import localtime, mktime, time
from datetime import datetime
from Components.config import config
import os
from skin import parseColor
from Tools.xtraTool import pathLoc

class xtraPrimeTimeLabel(Renderer):

	def __init__(self):
		Renderer.__init__(self)
		self.epgcache = eEPGCache.getInstance()

	GUI_WIDGET = eLabel
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
				if evn and (now.tm_hour <= prime_hour):
					bt = localtime(evn.getBeginTime())
					duration = round(evn.getDuration() // 60)
					primetime = "\c0000????Prime Time\n\c00aaaaaa%02d:%02d \n%smin\c00??????\n%s"%(bt[3], bt[4], duration, eNm)
					self.instance.setText(str(primetime))
					self.instance.show()
				else:
					self.instance.hide()
			except Exception as err:
				from Tools.xtraTool import errorlog
				errorlog(err, __file__)

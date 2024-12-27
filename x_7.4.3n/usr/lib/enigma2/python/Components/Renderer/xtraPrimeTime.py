# -*- coding: utf-8 -*-
# by digiteng, 03.10.2024
# for ch
#<widget render="xtraPrimeTime" source="ServiceEvent" position="0,0" size="600,170" font="Regular; 30" noWrap="1" zPosition="2" transparent="1" />

from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import eLabel, eEPGCache, eServiceReference, eWidget, ePixmap, loadJPG, eTimer
from time import localtime, mktime, time
from datetime import datetime
from Components.config import config

class xtraPrimeTime(Renderer):

	def __init__(self):
		Renderer.__init__(self)
		self.epgcache = eEPGCache.getInstance()
		self.timer = eTimer()
		self.timer.callback.append(self.ptw)
		
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
				self.mode = value
			elif attrib == 'font':
				self.fontType = str(value.split(";")[0]).sprit()
				self.fontSize = int(str(value.split(";")[1]).sprit())
			
		self.skinAttributes = attribs
		return Renderer.applySkin(self, desktop, screen)


	GUI_WIDGET = eWidget
	def changed(self, what):
		if not self.instance:
			return
		else:
			if what[0] != self.CHANGED_CLEAR:
				self.timer.start(200, True)


	def ptw(self):
		try:
			event = self.source.event
			if event is None:
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
			bcdrpNm = "{}xtraEvent/backdrop/{}.jpg".format(pathLoc, eNm)
			if evn and (now.tm_hour <= prime_hour):
				bt = localtime(evn.getBeginTime())
				duration = round(evn.getDuration() // 60)
				primetime = "\c0000????Prime Time\n\c00aaaaaa%02d:%02d \n%smin\c00??????\n%s"%(bt[3], bt[4], duration, eNm)
				self.ptNm.setText(str(primetime))
				self.ptNm.setBackgroundColor(parseColor(self.backgroundColor))
				if self.mode == "vertical":
					self.ptNm.setBackgroundColor(parseColor(self.backgroundColor))
					self.ptNm.resize(eSize(self.szX // 2, self.szY))
					self.ptNm.move(ePoint(self.szX // 2 + 10, 0))
					self.ptNm.setFont(gFont(self.fontType, self.fontSize))
					self.ptNm.setHAlign(eLabel.alignLeft)
					self.ptNm.setTransparent(1)
					self.ptNm.setZPosition(99)
					self.ptNm.show()
				elif self.mode == "horizontal":
					self.ptNm.setBackgroundColor(parseColor(self.backgroundColor))
					self.ptNm.resize(eSize(self.szX, self.fontSize + 5))
					self.ptNm.move(ePoint(10, self.szY // 5 * 4))
					self.ptNm.setFont(gFont(self.fontType, self.fontSize))
					self.ptNm.setHAlign(eLabel.alignLeft)
					self.ptNm.setTransparent(0)
					self.ptNm.setZPosition(99)
					self.ptNm.show()
				else:
					self.ptNm.setBackgroundColor(parseColor(self.backgroundColor))
					self.ptNm.resize(eSize(self.szX // 2, self.szY))
					self.ptNm.move(ePoint(self.szX // 2 + 10, 0))
					self.ptNm.setFont(gFont(self.fontType, self.fontSize))
					self.ptNm.setHAlign(eLabel.alignLeft)
					self.ptNm.setTransparent(1)
					self.ptNm.setZPosition(99)
					self.ptNm.show()
				
				if os.path.exists(bcdrpNm):
					self.ptPic.setPixmap(loadJPG(bcdrpNm))
					self.ptPic.resize(eSize(self.szX // 2, self.szY))
					self.ptPic.move(ePoint(0,0))
					self.ptPic.setTransparent(0)
					self.ptPic.setZPosition(9)
					self.ptPic.setScale(1)
					self.ptPic.show()

			else:
				self.ptPic.hide()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)


	def GUIcreate(self, parent):
		self.instance = eWidget(parent)
		self.ptNm = eLabel(self.instance)
		self.ptPic = ePixmap(self.instance)













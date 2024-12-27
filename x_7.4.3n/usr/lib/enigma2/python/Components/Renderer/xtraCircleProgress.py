# by digiteng...11.2020, 04.2022, 08.2024
# <widget render="NachtCircleProgress" source="global.CurrentTime" mode="rtng" scale="2" pixmapCircle="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150orange.png" pixmapCircleBack="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150back.png"position="1500,140" size="60,60" backgroundColor="black" zPosition="3" transparent="1" />

from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, ePoint, eWidget, eLabel, eSize, loadPNG, gFont, eDVBVolumecontrol, eTimer, eEPGCache
from skin import parseColor
import os
import re
import json
from Components.Converter.Poll import Poll
from Components.config import config
import NavigationInstance
from Tools.xtraTool import REGEX, pathLoc
epgcache = eEPGCache.getInstance()

class xtraCircleProgress(Renderer):
	def __init__(self):
		Renderer.__init__(self)
		# Poll.__init__(self)
		self.scale = 0
		self.timer = eTimer()
		self.timer.callback.append(self.cPrgrss)
		
	GUI_WIDGET = eWidget

	def applySkin(self, desktop, screen):
		attribs = self.skinAttributes[:]
		for (attrib, value) in self.skinAttributes:
			if attrib == 'size':
				self.szX = int(value.split(',')[0])
				self.szY = int(value.split(',')[1])
			elif attrib == 'backgroundColor':
				self.backgroundColor = value
			elif attrib == 'mode':
				self.mode = value
			elif attrib == 'scale':
				self.scale = int(value)
			elif attrib == 'pixmapCircle':
				self.pixmapCirclex = value
			elif attrib == 'pixmapCircleBack':
				self.pixmapCircleBack = value
		self.skinAttributes = attribs
		
		self.prgrsPxmp.setBackgroundColor(parseColor(self.backgroundColor))
		self.prgrsPxmp.resize(eSize(self.szX, self.szY))
		self.prgrsPxmp.setZPosition(2)
		self.prgrsPxmp.setTransparent(1)
		self.prgrsPxmp.setAlphatest(2)
		
		self.prgrsPxmpBack.setBackgroundColor(parseColor(self.backgroundColor))
		self.prgrsPxmpBack.resize(eSize(self.szX, self.szY))
		self.prgrsPxmpBack.setTransparent(1)
		self.prgrsPxmpBack.setAlphatest(2)
		self.prgrsPxmpBack.setZPosition(5)
		
		self.prgrsBack.setBackgroundColor(parseColor(self.backgroundColor))
		self.prgrsBack.resize(eSize(self.szX, self.szY))
		self.prgrsBack.move(ePoint(0, 0))
		self.prgrsBack.setTransparent(0)
		self.prgrsBack.setZPosition(0)
		ret = Renderer.applySkin(self, desktop, screen)
		return ret

	def changed(self, what):
		if not self.instance:
			return
		if what[0] == self.CHANGED_CLEAR:
			return
		self.timer.start(200, True)	
		
	def cPrgrss(self):
		try:
			if self.pixmapCirclex.endswith(".png"):
				self.prgrsPxmp.setPixmap(loadPNG("{}".format(self.pixmapCirclex)))
				self.prgrsPxmp.setScale(self.scale)
		
				self.prgrsPxmpBack.setPixmap(loadPNG("{}".format(self.pixmapCircleBack)))
				self.prgrsPxmpBack.setScale(self.scale)

			val = None
			try:
				eventName="n/a"
				if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
					ref=None
					event = None
					title = ""
					read_json = {}
					ref = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
					event = epgcache.lookupEvent(['IBDCTSERN', (ref, 1, -1, 1)])
					event_name = event[0][4]
					title = REGEX.sub('', event_name).strip()
					# open("/tmp/title", "w").write(str(title))
					rating_json = "{}xtraEvent/infos/{}.json".format(pathLoc, title)
					# open("/tmp/titleread_json", "w").write(str(rating_json))
					if os.path.exists(rating_json):
						with open(rating_json) as f:
							read_json = json.load(f)
							
						if self.mode == "rating":
							val = int(read_json["tmdbRating"]) * 10
							# open("/tmp/titleval", "w").write(str(val))
			except Exception as err:
				from Tools.xtraTool import errorlog
				errorlog(err, __file__)
			# val = "60"
			if val is not None :
				val = int(val)
				x, y = 0, 0
				if val >= 0 and val <= 50:
					x = 0
					y = (float(50) / float(self.szY) ) * 100
					y = ((float(val) / float(self.szY)) * float(self.szY)) / y * 100
					y = int(-y)
					
					p = (self.szY / 2 - self.szY / 4) + (self.szY / 20)
					s = (self.szY / 4) + (self.szY / 10)
					f = (self.szY / 3)

					self.prgrsText.setText(str(val))
					self.prgrsText.setBackgroundColor(parseColor(self.backgroundColor))
					self.prgrsText.resize(eSize(self.szX, int(s)))
					self.prgrsText.move(ePoint(0, int(p)))
					self.prgrsText.setFont(gFont("Regular", int(f)))
					self.prgrsText.setHAlign(eLabel.alignCenter)
					self.prgrsText.setTransparent(1)
					self.prgrsText.setZPosition(99)
					self.prgrsText.show()
					
					self.prgrsVal.setBackgroundColor(parseColor(self.backgroundColor))
					self.prgrsVal.resize(eSize(int(self.szX / 2), self.szY))
					self.prgrsVal.move(ePoint(x, y))
					self.prgrsVal.setTransparent(0)
					self.prgrsVal.setZPosition(3)
					self.prgrsVal.show()
					
					self.prgrsValR.setBackgroundColor(parseColor(self.backgroundColor))
					self.prgrsValR.resize(eSize(int(self.szX / 2), self.szY))
					self.prgrsValR.move(ePoint(int(self.szX / 2), 0))
					self.prgrsValR.setTransparent(0)
					self.prgrsValR.setZPosition(3)
					self.prgrsValR.show()
				elif val >= 51 and val <= 100:
					x = self.szX // 2
					y = (float(50) / float(self.szY) ) * 100
					y = (float(val) / float(self.szY) * float(self.szY)) / y * 100
					y = y - self.szY + self.szY / 10
					y = int(y)

					p = (self.szY / 2-self.szY / 4)+(self.szY / 20)
					s = (self.szY / 4)+(self.szY / 10)
					f = (self.szY / 3)

					self.prgrsText.setText(str(val))
					self.prgrsText.setBackgroundColor(parseColor(self.backgroundColor))
					self.prgrsText.resize(eSize(self.szX, int(s)))
					self.prgrsText.move(ePoint(0, int(p)))
					self.prgrsText.setFont(gFont("Regular", int(f)))
					self.prgrsText.setHAlign(eLabel.alignCenter)
					self.prgrsText.setTransparent(1)
					self.prgrsText.setZPosition(99)
					self.prgrsText.show()
					
					self.prgrsValR.clearBackgroundColor()
					self.prgrsValR.hide()
					self.prgrsVal.clearBackgroundColor()
					self.prgrsVal.setBackgroundColor(parseColor(self.backgroundColor))
					self.prgrsVal.resize(eSize(x, self.szY))
					self.prgrsVal.move(ePoint(x, y))
					self.prgrsVal.setTransparent(0)
					self.prgrsVal.setZPosition(3)
					self.prgrsVal.show()
				else:
					return
			else:
				self.prgrsText.hide()
				self.prgrsVal.hide()
				self.prgrsVal.resize(eSize(self.szX, self.szY))
				self.prgrsVal.move(ePoint(0,0))
				self.prgrsVal.setTransparent(0)
				self.prgrsVal.setZPosition(3)
				self.prgrsVal.show()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def GUIcreate(self, parent):
		self.instance = eWidget(parent)
		self.prgrsVal = eLabel(self.instance)
		self.prgrsValR = eLabel(self.instance)
		self.prgrsText = eLabel(self.instance)
		self.prgrsBack = eLabel(self.instance)
		self.prgrsPxmp = ePixmap(self.instance)
		self.prgrsPxmpBack = ePixmap(self.instance)

	def GUIdelete(self):
		self.prgrsVal = None
		self.prgrsValR = None
		self.prgrsText = None
		self.prgrsBack = None
		self.prgrsPxmp = None
		self.prgrsPxmpBack = None

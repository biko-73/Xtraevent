# -*- coding: utf-8 -*-
# by digiteng...06.2020 - 08.2020 - 11.2021
# <widget source="session.Event_Now" render="xtraBanner" position="0,0" size="762,141" zPosition="1" />
from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, ePicLoad, eEPGCache
from Components.AVSwitch import AVSwitch
from Components.Pixmap import Pixmap
from Components.config import config
import os
import re
from Tools.xtraTool import REGEX, pathLoc

class xtraBanner(Renderer):

	def __init__(self):
		Renderer.__init__(self)

	GUI_WIDGET = ePixmap
	def changed(self, what):
		if not self.instance:
			return
		else:
			if what[0] != self.CHANGED_CLEAR:
				evnt = ''
				pstrNm = ''
				evntNm = ''
				try:
					event = self.source.event
					if event:
						evnt = event.getEventName()
						evntNm = REGEX.sub('', evnt).strip()
						pstrNm = "{}xtraEvent/banner/{}.jpg".format(pathLoc, evntNm)
						if os.path.exists(pstrNm):
							size = self.instance.size()
							self.picload = ePicLoad()
							sc = AVSwitch().getFramebufferScale()
							if self.picload:
								self.picload.setPara((size.width(), size.height(),	sc[0], sc[1], False, 1, '#00000000'))
							result = self.picload.startDecode(pstrNm, 0, 0, False)
							if result == 0:
								ptr = self.picload.getData()
								if ptr != None:
									self.instance.setPixmap(ptr)
									self.instance.show()
							del self.picload
						else:
							self.instance.hide()
					else:
						self.instance.hide()
				except:
					pass
			else:
				self.instance.hide()
				return

# -*- coding: utf-8 -*-
# by digiteng...08.2020 - 11.2021
# <widget source="session.Event_Now" render="xtraPoster" position="0,0" size="185,278" zPosition="1" />
from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, eEPGCache, loadJPG
from Components.config import config
import re
import os
from Tools.xtraTool import REGEX, pathLoc
		
class xtraPoster(Renderer):

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
						pstrNm = "{}xtraEvent/poster/{}.jpg".format(pathLoc, evntNm)
						if os.path.exists(pstrNm):
							self.instance.setPixmap(loadJPG(pstrNm))
							self.instance.setScale(1)
							self.instance.show()
						else:
							self.instance.hide()
					else:
						self.instance.hide()
					return
				except:
					self.instance.hide()
					return				
			else:
				self.instance.hide()
				return

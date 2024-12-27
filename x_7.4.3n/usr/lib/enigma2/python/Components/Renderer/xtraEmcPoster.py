# -*- coding: utf-8 -*-
# by digiteng...07.2020 - 08.2020 - 10.2021
# <widget source="Service" render="xtraEmcPoster" delayPic="500" position="0,0" size="185,278" zPosition="0"
from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, loadJPG
import os
from Components.Sources.ServiceEvent import ServiceEvent
from Components.Sources.CurrentService import CurrentService
from Components.config import config
import re
from Tools.xtraTool import REGEX, pathLoc
		
class xtraEmcPoster(Renderer):

	def __init__(self):
		Renderer.__init__(self)
		self.piconsize = (0,0)

	GUI_WIDGET = ePixmap
	def changed(self, what):
		if not self.instance:
			return
		else:
			if what[0] != self.CHANGED_CLEAR:
				
				movieNm = ""
				try:
					service = self.source.getCurrentService()
					if service:
						evnt = service.getPath()
						movieNm = evnt.split('-')[-1].split(".")[0].strip()
						movieNm = REGEX.sub('', movieNm).strip()
						pstrNm = "{}xtraEvent/EMC/{}-poster.jpg".format(pathLoc, movieNm.strip())
						if os.path.exists(pstrNm):
							self.instance.setScale(1)
							self.instance.setPixmap(loadJPG(pstrNm))
							self.instance.show()
						else:
							self.instance.hide()
					else:
						self.instance.hide()
				except:
					pass
			else:
				self.instance.hide()
				return
					
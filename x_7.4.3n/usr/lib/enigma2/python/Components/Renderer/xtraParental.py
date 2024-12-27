# -*- coding: utf-8 -*-
# by digiteng...
# 07.2020, 11.2020, 11.2021, 10.2024
# <widget render="xtraParental" source="session.Event_Now" position="0,0" size="60,60" alphatest="blend" zPosition="2" transparent="1" />
from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, loadPNG
from Components.config import config
import re
import json
import os
from Tools.xtraTool import REGEX, pRating, pathLoc
pratePath = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/parental/"

class xtraParental(Renderer):

	def __init__(self):
		Renderer.__init__(self)

	GUI_WIDGET = ePixmap
	def changed(self, what):
		if not self.instance:
			return
		else:
			rate = None
			parentName = ""
			event = self.source.event
			if event:
				evnt = event.getEventName()
				ShortDescription = event.getShortDescription()
				ExtendedDescription = event.getExtendedDescription()
				fd = "{}\n{}".format(ShortDescription, ExtendedDescription)
				evntNm = REGEX.sub('', evnt).strip()
				rating_json = "{}xtraEvent/infos/{}.json".format(pathLoc, evntNm)
				if os.path.exists(rating_json):
					with open(rating_json) as f:
						read_json = json.load(f)
					try:
						rate = read_json["rated"]
					except:
						pass
					if rate is None:
						try:
							rate = read_json["parentalRating"]
						except:
							pass
				if rate is None or rate == "":
					parentName = ''
					prs = ['[aA]b ((\d+))', '[+]((\d+))', 'Od lat: ((\d+))', '(\d+)[+]', '(TP)', '[-](\d+)']
					for i in prs:
						prr = re.search(i, fd)
						if prr:
							parentName = prr.group(1)
							rate = parentName.replace('7', '6').replace('10', '12').replace('TP', '0')
							break
					if not rate:
						try:
							age = ''
							rating = event.getParentalData()
							if rating:
								rate = rating.getRating()
						except:
							pass

				rate = str(rate).strip()
				getRate = pRating(rate)
				if rate is not None:
					rateNm = "{}FSK_{}.png".format(pratePath, getRate)
					self.instance.setPixmapFromFile(rateNm)
					self.instance.setScale(1)
					self.instance.show()
				else:
					self.instance.setPixmapFromFile("{}FSK_NA.png".format(pratePath))
					self.instance.setScale(1)
					self.instance.show()				
			else:
				self.instance.setPixmapFromFile("{}FSK_NA.png".format(pratePath))
				self.instance.setScale(1)
				self.instance.show()

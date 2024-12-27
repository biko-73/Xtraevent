# -*- coding: utf-8 -*-
# by digiteng...05.2024, 10.2024
# <widget source="session.CurrentService" render="xtraCast" noWrap="1" 
# castNum="0" castNameColor="#ffffff" castCaracterColor="#999999" castNameFont="Console; 14" castCaracterFont="Regular; 12" 
# position="80,455" size="154,462" zPosition="1" backgroundColor="background" transparent="1" />

from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from enigma import ePoint, eWidget, eSize, eLabel, gFont, ePixmap, eEPGCache, loadJPG
from skin import parseColor
from Components.config import config
from Tools.xtraTool import REGEX, pathLoc
import re
import os

class xtraCast(Renderer):
	def __init__(self):
		Renderer.__init__(self)
		# self.epgcache = eEPGCache.getInstance()
		self.castNamefontType = "Regular"
		self.castNamefontSize = 12
		self.castCaracterfontType = "Regular"
		self.castCaracterfontSize = 10
		self.csx, self.csy = 200,30
		self.cpx, self.cpy = 0,0
		self.foregroundColor = "#ffffff"
		self.backgroundColor = "#000000"
		self.castNameColor = "#ffffff"
		self.castCaracterColor = "#cccccc"
		self.castNamenumber = 0
		
	def applySkin(self, desktop, screen):
		attribs = self.skinAttributes[:]
		for attrib, value in self.skinAttributes:
			if attrib == 'backgroundColor':
				self.backgroundColor = value
			if attrib == 'castNameColor':
				self.castNameColor = value
			if attrib == 'castCaracterColor':
				self.castCaracterColor = value
			if attrib == 'castNum':
				self.castNamenumber = int(value)
			if attrib == 'castNameFont':
				self.castNamefontType = value.split(";")[0]
				self.castNamefontSize = value.split(";")[1]
			if attrib == 'castCaracterFont':
				self.castCaracterfontType = value.split(";")[0]
				self.castCaracterfontSize = value.split(";")[1]
			if attrib == 'size':
				self.csx = int(value.split(",")[0])
				self.csy = int(value.split(",")[1])
			if attrib == 'position':
				self.cpx = int(value.split(",")[0])
				self.cpy = int(value.split(",")[1])
				
		self.skinAttributes = attribs
		return Renderer.applySkin(self, desktop, screen)

	GUI_WIDGET = eWidget
	def changed(self, what):
		if not self.instance:
			return
		if what[0] == self.CHANGED_CLEAR:
			return
		self.castName.hide()
		self.castNamePic.hide()
		ref=""
		evnt=""
		events=None
		event = self.source.event
		if event:
			try:
				evnt = event.getEventName()
				evntNm = REGEX.sub('', evnt).strip()
				cf=""
				cNm=""
				castsFolder = "{}xtraEvent/casts/{}".format(pathLoc, evntNm)
				if os.path.isdir(castsFolder):
					castFiles = sorted(os.listdir(castsFolder))
					if castFiles:
						try:
							cf = castFiles[self.castNamenumber]
						except:
							return
						self.castNamePic.setPixmapFromFile("{}/{}".format(castsFolder, cf))
						self.castNamePic.resize(eSize(self.csx, self.csy // 2))
						self.castNamePic.move(ePoint(0,0))
						self.castNamePic.setTransparent(1)
						self.castNamePic.setZPosition(3)
						self.castNamePic.setScale(1)
						self.castNamePic.setAlphatest(2)
						self.castNamePic.show()
						
						cName = cf[:-4][3:].split("(")[0]
						cCrctr = cf[:-4][3:].split("(")[1].replace(")", "")

						self.castName.setText(cName)
						self.castName.setBackgroundColor(parseColor(self.backgroundColor))
						self.castName.setForegroundColor(parseColor(self.castNameColor))
						self.castName.resize(eSize(self.csx, int(self.castNamefontSize) + 4))
						self.castName.move(ePoint(0, (self.csy // 2) + 5))
						self.castName.setFont(gFont(self.castNamefontType, int(self.castNamefontSize)))
						self.castName.setHAlign(eLabel.alignLeft)
						self.castName.setTransparent(1)
						self.castName.setZPosition(99)
						self.castName.show()
						
						self.castCaracter.setText(cCrctr)
						self.castCaracter.setBackgroundColor(parseColor(self.backgroundColor))
						self.castCaracter.setForegroundColor(parseColor(self.castCaracterColor))
						self.castCaracter.resize(eSize(self.csx, self.csy // 2))
						self.castCaracter.move(ePoint(0, (self.csy // 2) + 10 + int(self.castNamefontSize)))
						self.castCaracter.setFont(gFont(self.castCaracterfontType, int(self.castCaracterfontSize)))
						self.castCaracter.setHAlign(eLabel.alignLeft)
						self.castCaracter.setTransparent(1)
						self.castCaracter.setZPosition(99)
						self.castCaracter.show()
					else:
						self.castName.hide()
						self.castNamePic.hide()
				else:
					self.castName.hide()
					self.castNamePic.hide()
			except Exception as err:
				from Tools.xtraTool import errorlog
				errorlog(err, __file__)
		else:
			self.castName.hide()
			self.castNamePic.hide()
			return
			
	def GUIcreate(self, parent):
		self.instance = eWidget(parent)
		self.castName = eLabel(self.instance)
		self.castCaracter = eLabel(self.instance)
		self.castNamePic = ePixmap(self.instance)

	def GUIdelete(self):
		self.castName = None
		self.castCaracter = None
		self.castNamePic = None

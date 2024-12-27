# -*- coding: utf-8 -*-
# by digiteng...03.2024, 09.2024
from __future__ import absolute_import
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.Pixmap import Pixmap
from Components.config import config
from enigma import eEPGCache, eTimer, ePoint, eSize
import re
import os
import requests
from sys import version_info
from . import xtra_config
from Tools.xtraTool import REGEX, header
try:
	# from Tools.xtraTool import pathLocation
	pathLoc =  config.plugins.xtrvnt.loc.value
except:
	pathLoc = "/"
try:
	tmdb_api = config.plugins.xtrvnt.tmdbAPI.value
	if not tmdb_api: 
		tmdb_api = "3c3efcf47c3577558812bb9d64019d65"
except:
	tmdb_api = "3c3efcf47c3577558812bb9d64019d65"

py3 = version_info[0] == 3
try:
	if py3:
		from _thread import start_new_thread
		from urllib.request import urlopen, Request, quote
	else:
		from thread import start_new_thread
		from urllib2 import urlopen, Request, quote
except:
	pass


class xtraInfobarPoster(Screen):
	skin = """
<screen position="0,0" size="0,0" flags="wfNoBorder" zPosition="99" backgroundColor="#ff000000">
	<widget name="poster" position="0,0" size="185,278" transparent="1" cornerRadius="20" scale="stretch" zPosition="2" backgroundColor="#000000" />
</screen>"""

	def __init__(self, session):
		Screen.__init__(self, session)
		self.session = session
		self["poster"] = Pixmap()
		self.firstDelayTimer = eTimer()
		self.firstDelayTimer.callback.append(self.showPoster)
		# self.onLayoutFinish.append(self.showPoster)

	def getmc(self):
		self["poster"].hide()
		self.firstDelayTimer.start(100, True)

	def showPoster(self):
		try:
			self["poster"].hide()
			if str(config.plugins.xtrvnt.xPoster.value) == "True":
				event_name = None
				ref = None
				event = None
				ref = self.session.nav.getCurrentlyPlayingServiceReference()
				if ref is not None:
					epg = eEPGCache.getInstance()
					event = epg.lookupEventTime(ref, -1, 0)
					if event is None:
						self["poster"].hide()
						return
						return
					event_name = event.getEventName()
					title = REGEX.sub('', event_name).strip()

					pstrNm = "{}xtraEvent/poster/{}.jpg".format(config.plugins.xtrvnt.loc.value, title)
					# open("/tmp/pstrNmx.txt", "w").write(str(pstrNm))
					px, py = config.plugins.xtrvnt.infobarPosterPosX.value, config.plugins.xtrvnt.infobarPosterPosY.value
					sz, sy = config.plugins.xtrvnt.infobarPosterSizeX.value, round(config.plugins.xtrvnt.infobarPosterSizeX.value * 1.5)
					if os.path.exists(pstrNm):						
						self.instance.move(ePoint(px, py))
						self.instance.resize(eSize(int(sz), int(sy)))
						self["poster"].resize(eSize(int(sz), int(sy)))
						self["poster"].instance.setPixmapFromFile(pstrNm)
						self["poster"].instance.setScale(2)
						self["poster"].show()
					else:
						# self["poster"].hide()
						self.downloadPoster(title, pstrNm, event, px, py, sz, sy)
				else:
					self["poster"].hide()
					return
					return
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def hidePoster(self):
		self["poster"].hide()

	def downloadPoster(self, title, pstrNm, event, px, py, sz, sy):
		try:
			ref = None
			event = None
			info = ""
			srch = "multi"
			sd=""
			ed=""
			dr=0
			try:
				sd = event.getShortDescription()
			except:
				pass
			try:
				ed = event.getExtendedDescription()
			except:
				pass
			try:
				dr = event.getDuration() // 60
			except:
				pass
			fd = "{}{}{}".format(title, sd, ed)
			checkTV = [ "serial", "series", "serie", "serien", "série", "séries", "serious",
			"folge", "episodio", "episode", "épisode", "l'épisode", "ep.", 
			"staffel", "soap", "doku", "tv", "talk", "show", "news", "factual", "entertainment", "telenovela", 
			"dokumentation", "dokutainment", "documentary", "informercial", "information", "sitcom", "reality", 
			"program", "magazine", "mittagsmagazin", "т/с", "м/с", "сезон", "с-н", "эпизод", "сериал", "серия"	]
			checkMovie = ["film", "movie", "фильм", "кино", "ταινία", "película", "cinéma", "cine", "cinema", "filma", "spielfilm"]
			for i in checkMovie:
				if i in fd.lower():
					srch = "movie"
				elif int(dr) >= 66:
					srch = "movie"
			if srch != "movie":
				for i in checkTV:
					if i in fd.lower():
						srch = "tv"
						break
				if srch != "tv":
					if int(dr) <= 60:
						srch = "tv"

			url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&query={}".format(srch, tmdb_api, quote(title))
			if config.plugins.xtrvnt.searchLang.value == True:
				url_tmdb += "&language={}".format(self.getLanguage())
			poster = ""
			try:
				poster = requests.get(url_tmdb,	 headers=header).json()['results'][0]['poster_path']
			except:
				return
			url = "https://image.tmdb.org/t/p/w{}{}".format(sz, poster)

			open(pstrNm, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
			# self.delVerifyImage(pstrNm)
			if os.path.exists(pstrNm):						
				self.instance.move(ePoint(px, py))
				self.instance.resize(eSize(int(sz), int(sy)))
				self["poster"].resize(eSize(int(sz), int(sy)))
				self["poster"].instance.setPixmapFromFile(pstrNm)
				self["poster"].instance.setScale(2)
				self["poster"].show()

		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def getLanguage(self):
		try:
			from Components.Language import language
			lang = language.getLanguage()
			lang = lang[:2]
		except:
			try:
				lang = config.osd.language.value[:-3]
			except:
				lang = "en"
		return lang

	def delVerifyImage(self, pstrNm):
		try:
			img = Image.open(pstrNm)
			img.verify()
		except:
			pass
		try:
			os.remove(pstrNm)
		except:
			pass



class xtraInfobarPoster2(Screen):
	skin = """
<screen position="0,0" size="0,0" flags="wfNoBorder" zPosition="99" backgroundColor="#ff000000">
	<widget name="poster2" position="0,0" size="185,278" transparent="1" cornerRadius="20" scale="stretch" zPosition="2" backgroundColor="#000000" />
</screen>"""

	def __init__(self, session):
		Screen.__init__(self, session)
		self.session = session
		self["poster2"] = Pixmap()
		self.firstDelayTimer = eTimer()
		self.firstDelayTimer.callback.append(self.showPoster)
		# self.onLayoutFinish.append(self.showPoster)

	def getmc(self):
		self["poster2"].hide()
		self.firstDelayTimer.start(100, True)

	def showPoster(self):
		try:
			self["poster2"].hide()
			if str(config.plugins.xtrvnt.xPoster.value) == "True":
				event_name = None
				ref = None
				event = None
				ref = self.session.nav.getCurrentlyPlayingServiceReference()
				if ref is not None:
					epg = eEPGCache.getInstance()
					event = epg.lookupEventTime(ref, -1, 1)
					if event is None:
						self["poster2"].hide()
						return
						return
					event_name = event.getEventName()
					title2 = REGEX.sub('', event_name).strip()

					pstrNm2 = "{}xtraEvent/poster/{}.jpg".format(config.plugins.xtrvnt.loc.value, title2)
					# open("/tmp/pstrNmx.txt", "w").write(str(pstrNm))
					px2, py2 = config.plugins.xtrvnt.infobarPosterPosX2.value, config.plugins.xtrvnt.infobarPosterPosY2.value
					sz, sy = config.plugins.xtrvnt.infobarPosterSizeX.value, round(config.plugins.xtrvnt.infobarPosterSizeX.value * 1.5)
					if os.path.exists(pstrNm2):						
						self.instance.move(ePoint(px2, py2))
						self.instance.resize(eSize(int(sz), int(sy)))
						self["poster2"].resize(eSize(int(sz), int(sy)))
						self["poster2"].instance.setPixmapFromFile(pstrNm2)
						self["poster2"].instance.setScale(2)
						self["poster2"].show()
					else:
						# self["poster"].hide()
						self.downloadPoster(title2, pstrNm2, event, px2, py2, sz, sy)
				else:
					self["poster2"].hide()
					return
					return
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def hidePoster(self):
		self["poster2"].hide()

	def downloadPoster(self, title2, pstrNm2, event, px2, py2, sz, sy):
		try:
			ref = None
			event = None
			info = ""
			srch = "multi"
			sd=""
			ed=""
			dr=0
			try:
				sd = event.getShortDescription()
			except:
				pass
			try:
				ed = event.getExtendedDescription()
			except:
				pass
			try:
				dr = event.getDuration() // 60
			except:
				pass
			fd = "{}{}{}".format(title2, sd, ed)
			checkTV = [ "serial", "series", "serie", "serien", "série", "séries", "serious",
			"folge", "episodio", "episode", "épisode", "l'épisode", "ep.", 
			"staffel", "soap", "doku", "tv", "talk", "show", "news", "factual", "entertainment", "telenovela", 
			"dokumentation", "dokutainment", "documentary", "informercial", "information", "sitcom", "reality", 
			"program", "magazine", "mittagsmagazin", "т/с", "м/с", "сезон", "с-н", "эпизод", "сериал", "серия"	]
			checkMovie = ["film", "movie", "фильм", "кино", "ταινία", "película", "cinéma", "cine", "cinema", "filma", "spielfilm"]
			for i in checkMovie:
				if i in fd.lower():
					srch = "movie"
				elif int(dr) >= 66:
					srch = "movie"
			if srch != "movie":
				for i in checkTV:
					if i in fd.lower():
						srch = "tv"
						break
				if srch != "tv":
					if int(dr) <= 60:
						srch = "tv"

			url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&query={}".format(srch, tmdb_api, quote(title2))
			if config.plugins.xtrvnt.searchLang.value == True:
				url_tmdb += "&language={}".format(self.getLanguage())
			poster = ""
			try:
				poster = requests.get(url_tmdb,	 headers=header).json()['results'][0]['poster_path']
			except:
				return
			url = "https://image.tmdb.org/t/p/w{}{}".format(sz, poster)

			open(pstrNm2, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
			# self.delVerifyImage(pstrNm)
			if os.path.exists(pstrNm2):						
				self.instance.move(ePoint(px2, py2))
				self.instance.resize(eSize(int(sz), int(sy)))
				self["poster2"].resize(eSize(int(sz), int(sy)))
				self["poster2"].instance.setPixmapFromFile(pstrNm2)
				self["poster2"].instance.setScale(2)
				self["poster2"].show()

		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def getLanguage(self):
		try:
			from Components.Language import language
			lang = language.getLanguage()
			lang = lang[:2]
		except:
			try:
				lang = config.osd.language.value[:-3]
			except:
				lang = "en"
		return lang

	def delVerifyImage(self, pstrNm2):
		try:
			img = Image.open(pstrNm2)
			img.verify()
		except:
			pass
		try:
			os.remove(pstrNm2)
		except:
			pass

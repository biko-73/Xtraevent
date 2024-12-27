#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by digiteng....2024
from __future__ import absolute_import
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.Pixmap import Pixmap
from Components.Label import Label
from Components.ProgressBar import ProgressBar
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from Plugins.Extensions.xtraEvent.skins.xtraSkins import *
from Components.config import config
from enigma import eEPGCache, eTimer, getDesktop, eServiceReference, eListboxPythonMultiContent, gFont, RT_HALIGN_LEFT, RT_VALIGN_CENTER, RT_WRAP, iPlayableService, ePoint, eSize
from Screens.InfoBar import InfoBar, MoviePlayer
from Tools.LoadPixmap import LoadPixmap
from Components.Sources.List import List
import socket
import re
import os
import json
import NavigationInstance
from Components.MenuList import MenuList
from time import time, localtime
import requests
from Tools.xtraTool import intCheck, getLanguage, version, REGEX, header
from .xa import uts
from .xtra_config import *
import base64
from importlib import reload

selPerson=""
title = ""
srch=""
ytu = ""
trailer_url = ""
trailer_res = "720p"
beginTime=0
read_json=""
pathLoc = "/"
castFolder = "/"
cast_downloaded = 0
st=""
lst=[]
blst=[]
dPoster = dBackdrop = dBanner = dInfo = dCast = 0
infos=""
imgr = ""
img = "/etc/issue"
if os.path.exists(img):
	with open(img, "r") as f:
		imgr = f.read().lower()
try:
	pathLoc = "{}xtraEvent/".format(config.plugins.xtrvnt.loc.value)
except:
	pass

try:
	if config.plugins.xtrvnt.trailer.value == "IMDB":
		prgrsColor = "#00ffff00"
		logo_thumb = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/IMDB_thumb.png"
	else:
		prgrsColor = "#00ff0000"
		logo_thumb = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/YOUTUBE_thumb.png"
except:
	prgrsColor = "#00ffffff"
	logo_thumb = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/plugin.png"

epg = eEPGCache.getInstance()

class xtraInfo(Screen):

	def __init__(self, session):
		self.session = session
		Screen.__init__(self, session)
		if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
			if config.plugins.xtrvnt.xtraInfoSourceSkinTMDB.value == "skin1":
				self.skin = xtraInfo_1080_tmdb1
			elif config.plugins.xtrvnt.xtraInfoSourceSkinTMDB.value == "skin2":
				self.skin = xtraInfo_1080_tmdb2
			elif config.plugins.xtrvnt.xtraInfoSourceSkinTMDB.value == "skin3":
				self.skin = xtraInfo_1080_tmdb3
		elif config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
			if config.plugins.xtrvnt.xtraInfoSourceSkinIMDB.value == "skin1":
				self.skin = xtraInfo_1080_imdb1
			elif config.plugins.xtrvnt.xtraInfoSourceSkinIMDB.value == "skin2":
				self.skin = xtraInfo_1080_imdb2
		self.list = []
		self.blist = []
		
		self['key_red'] = Label(_('Close'))
		self['key_green'] = Label("\c0000c740 \c00??????Search")
		self['key_yellow'] = Label("\c00????00▶ \c00??????Trailer")
		self['key_blue'] = Label("\c0000???? \c00??????M. Search")
		if "openatv" in imgr :
			if config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
				self["actions"] = ActionMap(["xtraEventAction"],
				{
					"red": self.exit,
					"green": self.runmDwnld,
					"yellow": self.runTrailerPlay,
					"blue": self.mSearch,
					"cancel": self.exit,
					"ok": self.keyOK,
					"info": self.pinfo,
					"menu": self.xtraSetup,

					"left": self.keyLeft,
					"right": self.keyRight,
					"up": self.keyUp,
					"down": self.keyDown,
				},-1)
			else:
				self["actions"] = ActionMap(["xtraEventAction"],
				{
					"red": self.exit,
					"green": self.runmDwnld,
					"yellow": self.runTrailerPlay,
					"blue": self.mSearch,
					"cancel": self.exit,
					"ok": self.keyOK,
					"info": self.pinfo,
					"menu": self.xtraSetup,

					# "left": self.keyLeft,
					# "right": self.keyRight,
					# "up": self.keyUp,
					# "down": self.keyDown,
				},-1)
		else:
			self["actions"] = ActionMap(["xtraEventAction"],
			{
				"red": self.exit,
				"green": self.runmDwnld,
				"yellow": self.runTrailerPlay,
				# "blue": self.mSearch,
				"cancel": self.exit,
				"ok": self.keyOK,
				"info": self.pinfo,
				"menu": self.xtraSetup,

				# "left": self.keyLeft,
				# "right": self.keyRight,
				# "up": self.keyUp,
				# "down": self.keyDown,
			},-1)
		# self.setTitle(_())
		self['status'] = Label()
		self['info'] = Label()
		self['int_statu'] = Label()
		self['help'] = Label()
		self['description'] = Label()
		self["poster"] = Pixmap()
		self["backdrop"] = Pixmap()
		self["ratingStar"] = ProgressBar()
		self["logo0"] = Pixmap()
		self["logo1"] = Pixmap()
		self["logo2"] = Pixmap()
		self["logo3"] = Pixmap()
		for i in range(int(config.plugins.xtrvnt.IMDB_backdrop_number.value)):
			self["backdrop_{}".format(i)] = Pixmap()
		self['lft'] = Label("\c00999999")
		self['rght'] = Label("\c00999999")
		self['uup'] = Label("\c00999999")
		self['dwn'] = Label("\c00999999")
		self["castList"] = List(self.list)
		self["backList"] = List(self.blist)
		self.onCh = NavigationInstance.instance.getCurrentlyPlayingServiceReference()
		self.onLayoutFinish.append(self.runInfo)

	# def showInfos(self):
		# try:
			# ref = NavigationInstance.instance.getCurrentlyPlayingServiceReference()
			# ref = self.session.nav.getCurrentlyPlayingServiceReference().toString()
			# self.runInfo(ref)
		# except:
			# pass
			
	def runInfo(self):
		if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
			self.showInfoTMDB()
		elif config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
			self.showInfoIMDB()
			
	def showInfoTMDB(self):
		try:
			global title
			global srch
			global lst
			event = None
			info = ""
			srch = "multi"
			eventName = None
			dr = 0
			try:
				info = self.session.nav.getCurrentService().info()
				serviceName = info.getName()
				event = info.getEvent(0)
				eventName = event.getEventName()
			except:
				try:
					event = self.session.screen["Event_Now"].getEvent()
					eventName = event.getEventName()
				except:
					return
			if eventName is None:
				return
			title = REGEX.sub('', eventName).strip()
			self.setTitle(_(title))
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
			self['description'].setText(fd)
			self['description'].show()
			checkTV = [ "serial", "series", "serie", "serien", "série", "séries", "serious",
			"folge", "episodio", "episode", "épisode", "l'épisode", "ep.", 
			"staffel", "soap", "doku", "tv", "talk", "show", "news", "factual", "entertainment", "telenovela", 
			"dokumentation", "dokutainment", "documentary", "informercial", "information", "sitcom", "reality", 
			"program", "magazine", "mittagsmagazin", "т/с", "м/с", "сезон", "с-н", "эпизод", "сериал", "серия"	]
			checkMovie = ["film", "movie", "фильм", "кино", "ταινία", "película", "cinéma", "cine", "cinema", "filma"]
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
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
		pstrNm = "{}poster/{}.jpg".format(pathLoc, title)
		bckdrpNm = "{}backdrop/{}.jpg".format(pathLoc, title)
		rating_json = "{}infos/{}.json".format(pathLoc, title)
		castsFolder = "{}casts/{}".format(pathLoc, title)
		logoFolder = "{}logos/{}".format(pathLoc, title)
# poster	
		if os.path.exists(pstrNm):
			self["poster"].instance.setPixmapFromFile(pstrNm)
			self["poster"].instance.setScale(2)
			self["poster"].instance.show()
# backdrop
		if os.path.exists(bckdrpNm):
			self["backdrop"].instance.setPixmapFromFile(bckdrpNm)
			self["backdrop"].instance.setScale(2)
			self["backdrop"].instance.show()
# rating star
		rating = None
		if os.path.exists(rating_json):
			with open(rating_json) as f:
				ratingj = json.load(f)
				if 'tmdbRating' in str(ratingj):
					rating = ratingj['tmdbRating']
					if rating is not None:
						rtng = int(10 * float(rating))
						self["ratingStar"].instance.setRange(0, 100)
						self["ratingStar"].instance.setValue(rtng)
						self["ratingStar"].instance.show()
					else:
						self["ratingStar"].instance.hide()
# cast
		if os.path.isdir(castsFolder):
			castFiles = sorted(os.listdir(castsFolder))
			if castFiles:
				lst=[]
				for i in range(len(castFiles)):
					try:
						cf = castFiles[i]
						cpl = "{}/{}".format(castsFolder, cf)
						cp = LoadPixmap(cpl)
						cName = cf[:-4][3:].split("(")[0]
						cCrName = cf[:-4][3:].split("(")[1].replace(")", "")
						lst.append((cp, cName, cCrName))
					except Exception as err:
						from Tools.xtraTool import errorlog
						errorlog(err, __file__)
				self["castList"].setList(lst)

# network logo
		try:
			if os.path.isdir(logoFolder):
				logoFiles = os.listdir(logoFolder)
				if logoFiles:
					for i in range(len(logoFiles)):
						try:
							logoPicName = "{}/{}".format(logoFolder, logoFiles[i])
							if os.path.exists(logoPicName):
								self["logo{}".format(i)].instance.setPixmapFromFile(logoPicName)
								self["logo{}".format(i)].instance.setScale(0)
								self["logo{}".format(i)].instance.show()
						except:
							pass

		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

		if intCheck():
			self['int_statu'].setText("\c0040a579")
		else:
			self['int_statu'].setText("\c00333333")
		# Screen.hide(self)
		# Screen.show(self)

	def showInfoIMDB(self):
		try:
			global title
			global srch
			global lst
			global blst
			if intCheck():
				self['int_statu'].setText("\c0040a579")
			else:
				self['int_statu'].setText("\c00333333")
			event = None
			info = ""
			srch = "multi"
			eventName = None
			dr = 0
			try:
				info = self.session.nav.getCurrentService().info()
				serviceName = info.getName()
				event = info.getEvent(0)
				eventName = event.getEventName()
			except:
				try:
					event = self.session.screen["Event_Now"].getEvent()
					eventName = event.getEventName()
				except:
					return
			if eventName is None:
				return
			title = REGEX.sub('', eventName).strip()
			self.setTitle(_(title))
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
			checkMovie = ["film", "movie", "фильм", "кино", "ταινία", "película", "cinéma", "cine", "cinema", "filma"]
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
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
		try:
			pstrNm = "{}imdb/casts/{}/{}_poster.jpg".format(pathLoc, title, title)
			rating_json = "{}imdb/casts/{}/{}_info.json".format(pathLoc, title, title)
			castsFolder = "{}imdb/casts/{}/person/".format(pathLoc, title)
	# poster	
			if os.path.exists(pstrNm):
				self["poster"].instance.setPixmapFromFile(pstrNm)
				self["poster"].instance.setScale(2)
				self["poster"].instance.show()
	# backdrop
			blst=[]
			for i in range(int(config.plugins.xtrvnt.IMDB_backdrop_number.value)):
				try:
					bckdrpNm = "{}imdb/casts/{}/{}_backdrop_{}.jpg".format(pathLoc, title, title, str(i))
					self["backdrop_{}".format(i)].instance.setPixmapFromFile(bckdrpNm)
					self["backdrop_{}".format(i)].instance.setScale(2)
					self["backdrop_{}".format(i)].instance.show()
					bp = LoadPixmap(bckdrpNm)
					blst.append(bp)
				except:
					pass
			self["backList"].setList(blst)
	# rating star
			rating = None
			if os.path.exists(rating_json):
				with open(rating_json) as f:
					ratingj = json.load(f)
				rating = ratingj["rating"]
				rtng = int(10 * float(rating))
				self["ratingStar"].instance.setRange(0, 100)
				self["ratingStar"].instance.setValue(rtng)
				self["ratingStar"].instance.show()
			else:
				self["ratingStar"].instance.hide()
	# cast
			if os.path.isdir(castsFolder):
				castFiles = sorted(os.listdir(castsFolder))
				if castFiles:
					lst=[]
					cast_desc = ""
					for i in range(len(castFiles)):
						try:
							cf = castFiles[i]
							cpl = "{}{}/{}.jpg".format(castsFolder, cf, cf)
							# open("/tmp/cpl", "w").write(str(cpl))
							cp = LoadPixmap(cpl)
							cName = cf.split("(")[0]
							cCrName = ""
							lst.append((cp, cName, cCrName))
						except:
							pass
					self["castList"].setList(lst)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
		if intCheck():
			self['int_statu'].setText("\c0040a579")
		else:
			self['int_statu'].setText("\c00333333")

	def runmDwnld(self):
		global title
		global srch
		if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
			# self.tmdb_dwnld()
			start_new_thread(self.tmdb_dwnld, (srch, title))
		elif config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
			# self.imdb_dwnld()
			start_new_thread(self.imdb_dwnld, (title, srch))

	def tmdb_dwnld(self, srch, title):
		try:
			exec(uts, globals())
			d = self.session.open(downloads)
			d.tmdb(srch, title)
			d.logo(srch, title)
			d.close()
			self.showInfoTMDB()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def imdb_dwnld(self, title, srch):
		try:
			exec(uts, globals())
			d = self.session.open(downloads)
			d.imdb(srch, title)
			d.close()
			self.showInfoIMDB()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyLeft(self):
		try:
			if config.plugins.xtrvnt.xtraInf.value:
				if config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
					self['rght'].setText("\c00555555")
					self["backList"].goLeft()
					self['lft'].setText("\c004dee94")

		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyRight(self):
		try:
			if config.plugins.xtrvnt.xtraInf.value:
				if config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
					self["backList"].goRight()
					self['lft'].setText("\c00555555")
					self['rght'].setText("\c004dee94")

		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyUp(self):
		try:
			if config.plugins.xtrvnt.xtraInf.value:
				if config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
					self['dwn'].setText("\c00555555")
					self["castList"].goLineUp()
					self['uup'].setText("\c004dee94")
					self['uup'].show()

		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyDown(self):
		try:
			if config.plugins.xtrvnt.xtraInf.value:
				if config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
					self['uup'].setText("\c00555555")
					self["castList"].goLineDown()
					self['dwn'].setText("\c004dee94")
					self['dwn'].show()
				# elif config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
					# self["castList"].goLineDown()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def runTrailerPlay(self):
		start_new_thread(self.trailerPlayOn, ())

	def trailerPlayOn(self):
		try:
			global title
			global trailer_url
			global trailer_res
			trailer_url = ""
			if config.plugins.xtrvnt.trailer.value == "IMDB":
				imdb_id = ""
				try:
					imdb_id = read_json["imdb_id"]
				except:
					url = 'https://www.imdb.com/find/?q={}&ref_=nv_sr_sm'.format(quote(title))
					req = urlopen(Request(url, headers=header)).read()
					imdb_id = re.findall(b'href="/title/(.*?)\/\?ref_=fn_al_tt_1"', req)[0].decode()
				url= "https://www.imdb.com/title/{}/?ref_=nv_sr_srsg_0".format(imdb_id)
				req = urlopen(Request(url, headers=header))
				if req.code == 200:
					video_id = re.findall(b'"embedUrl":"https://www.imdb.com/video/imdb/(.*?)"', req.read())[0].decode()
					url = "https://www.imdb.com/video/{}/".format(video_id)
					req = Request(url, headers=header)
					req = urlopen(req).read()
					trailer_url = ""
					trailer_url=req.partition(b'"videoMimeType":"MP4","videoDefinition":"DEF_1080p","url":"')[2].partition(b'"')[0].strip()
					trailer_res = "1080p"
					if not trailer_url:
						trailer_url = req.partition(b'"videoMimeType":"MP4","videoDefinition":"DEF_720p","url":"')[2].partition(b'"')[0].strip()
						trailer_res = "720p"
						if not trailer_url:
							trailer_url = req.partition(b'"videoMimeType":"MP4","videoDefinition":"DEF_480p","url":"')[2].partition(b'"')[0].strip()
							trailer_res = "480p"
					trailer_url = trailer_url.decode("utf-8").replace("\\u0026", "&")
					self.session.open(xPlayer)
				else:
					self['key_yellow'].setText(_("\c00??5500No Trailer"))
					self['key_yellow'].show()
			elif config.plugins.xtrvnt.trailer.value == "Youtube":
				self.session.open(ytbPlayer)

		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
			self['key_yellow'].hide()
			self['key_yellow'].setText(_("\c00??0000No Trailer"))
			self['key_yellow'].show()

	def mSearch(self):
		exec(uts, globals())
		self.session.open(manuelSearch)

	def xtraSetup(self):
		try:
			exec(uts, globals())
			self.session.open(xtra)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def pinfo(self):
		self.session.open(infos)

	def keyOK(self):
		try:
			global selPerson
			selPerson = self["castList"].getCurrent()[1]
			self.session.open(xtraInfoPerson)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def exit(self):
		from Plugins.Extensions.xtraEvent import xm
		reload(xm)
		self.close(True)

class infos(Screen):
	skin = '''
<screen name="info" position="center,center" size="700,200" flags="wfNoBorder" backgroundColor="#50000000">
	<widget name="info" position="20,center" font="Regular; 30" size="660,200" foregroundColor="#00ffffff" backgroundColor="#50000000" zPosition="1" transparent="1" halign="left" valign="center" />
</screen>'''

	def __init__(self, session):
		Screen.__init__(self, session)
		self["actions"] = ActionMap(["xtraEventAction"],
			{
				"cancel":self.close,
				"ok":self.close,
			}, -2)
		self['info'] = Label()
		self.mc()

	def mc(self):
		# from . import xtra
		self['info'].setText("© xtraEvent {} by digiteng (2024)".format(version()))

class ytbPlayer(Screen):

	skin = '''
	<screen name="ytbPlayer" position="center,880" size="300,200" flags="wfNoBorder" backgroundColor="#50000000">
		<widget name="list" position="0,0" size="300,200" foregroundColor="#c5c5c5" scrollbarSliderBorderWidth="0" scrollbarWidth="5"	scrollbarSliderForegroundColor="#0a5699" scrollbarSliderBorderColor="##50000000" scrollbarMode="showOnDemand" transparent="1" zPosition="99"	 backgroundColor="#50000000" backgroundColorSelected="#000a566d" foregroundColorSelected="#00ffff" />
	</screen>'''
	def __init__(self, session):
		Screen.__init__(self, session)
		self.session = session
		self["list"] = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)

		self["list"].l.setFont(0, gFont('Regular', 20))
		self["list"].l.setFont(1, gFont('Regular', 18))
		self["actions"] = ActionMap(["xtraEventAction"],
			{
				"cancel":self.exit,
				"red":self.exit,
				"ok":self.keyOK,
			}, -1)
		self.onLayoutFinish.append(self.resList)

	def resList(self):
		try:
			res = []
			video_id = ""
			global title
			global trailer_url, trailer_res
			global ytu
			trailer_url = ""
			headers={}
			try:
				video_id = read_json["trailer"]
			except:
				ttitle = "{} trailer".format(title)
				url = 'https://www.youtube.com/results?search_query={}'.format(quote(ttitle))
				req = urlopen(Request(url, headers=header)).read().decode()
				yid = req.partition('https://i.ytimg.com/vi/')[2].partition('"text":"{}'.format(title))[0].strip()
				video_id = str(yid[:11])
			# video_id = "ozX-tHb2pMk" #4k
			#video_id = "OtX3VF7qFTs" # 720
			if video_id:
				url = 'https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW'
				VERSION = '1.9'
				USER_AGENT = 'com.google.android.youtube/%s (Linux; U; Android 12; US) gzip' % VERSION
				headers['content-type'] = 'application/json'
				headers['User-Agent'] = 'com.google.android.youtube/'
				# headers['User-Agent'] = 'Mozilla/5.0'
				data = {
					'videoId': video_id,
					'context': {
						'client': {
							'clientName': 'IOS',
							'clientVersion': '19.29.1',
							'deviceMake': 'Apple',
							'platform': 'MOBILE',
							'osName': 'iPhone',
							'osVersion': '17.5.1.21F90',
							'deviceModel': 'iPhone16,2'
						}
					}
				,
				'header': {
					'User-Agent': 'com.google.ios.youtube/19.29.1 (iPhone16,2; U; CPU iOS 17_5_1 like Mac OS X;)',
					'X-Youtube-Client-Name': '5'
				},
				'api_key': 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
				'require_js_player': False,
				'require_po_token': False

			}
				# headers['X-YouTube-Client-Version'] = VERSION
				# headers['User-Agent'] = USER_AGENT
				data = json.dumps(data).encode('utf8')
				req = urlopen(Request(url, data=data, headers=headers)).read().decode()
				cont = json.loads(req)
				
				# js = json.dumps(cont, ensure_ascii=False)

				# with open("/tmp/ytb.json", "w") as f:
					# f.write(js)
				
				vy={}
				vy2 = {}
				ytu={}
				formats = None
				adaptiveFormats = None
				if "streamingData" in cont:
					try:
						formats = cont["streamingData"]["formats"]
					except:
						pass
					try:
						adaptiveFormats = cont["streamingData"]["adaptiveFormats"]
					except:
						pass
				else:
					# print("NO")
					return
				for i in range(0, 20, 1):
					qualityLabel = ""
					try:
						qualityLabel = formats[i]["qualityLabel"]
						mimeType = formats[i]["mimeType"].split(";")[0]
						if mimeType == "video/mp4":
							vy[qualityLabel] = formats[i]
					except:
						pass
					try:
						qualityLabel = adaptiveFormats[i]["qualityLabel"]
						mimeType = adaptiveFormats[i]["mimeType"].split(";")[0]
						if mimeType == "video/mp4":
							vy2[qualityLabel] = adaptiveFormats[i]
					except:
						pass
				ytu = vy2 | vy
				if config.plugins.xtrvnt.trailerQuality.value == "sList":
					self.list=[]
					lyk = list(ytu.keys())
					for i in range(len(lyk)):
						tg = lyk[i]
						url = ytu[tg]["url"]
						self.list.append([" {}".format(tg), " {}".format(url)])
						res.append([
						(), 
						(eListboxPythonMultiContent.TYPE_TEXT, 5,1,190,36, 0, RT_HALIGN_LEFT, str(tg), 0x00ffffff, 0x00ffffff, None, None)
						])

					self["list"].l.setList(res)
					self["list"].show()
				elif config.plugins.xtrvnt.trailerQuality.value == "maxRes":
					if "2160p" in ytu.keys():
						try:
							trailer_url = str(ytu["2160p"]["url"])
							trailer_res = "2160p"
						except:
							pass
					elif "1440p" in ytu.keys():
						try:
							trailer_url = str(ytu["1440p"]["url"])
							trailer_res = "1440p"
						except:
							pass
					elif "1080p" in ytu.keys():
						try:
							trailer_url = str(ytu["1080p"]["url"])
							trailer_res = "1080p"
						except:
							pass
					elif "720p" in ytu.keys():
						try:
							trailer_url = str(ytu["720p"]["url"])
							trailer_res = "720p"
						except:
							pass							
					elif "480p" in ytu.keys():
						try:
							trailer_url = str(ytu["480p"]["url"])
							trailer_res = "480p"
						except:
							pass							
					elif "360p" in ytu.keys():
						try:
							trailer_url = str(ytu["360p"]["url"])
							trailer_res = "360p"
						except:
							pass							
					elif "240p" in ytu.keys():
						try:
							trailer_url = str(ytu["240p"]["url"])
							trailer_res = "240p"
						except:
							pass							
					# open("/tmp/traliler_url", "w").write(str(trailer_url))
					start_new_thread(self.trailerPlay, ())
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def trailerPlay(self):
		try:
			global trailer_url
			global title
			try:
			   tp = "{}".format(config.plugins.xtrvnt.trailerPlayer.value)
			except:
				tp = "4097"
			sref = eServiceReference(int(tp), 0, trailer_url.strip())
			if config.plugins.xtrvnt.trailerPlay.value == "xtraPlayer":
				self.session.open(xPlayer)
			else:
				self.session.open(MoviePlayer, sref)
			sref.setName(title)
			# self.session.open(MoviePlayer, sref)
			# self.close()
			
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyOK(self):
		try:
			global trailer_url
			global trailer_res
			global beginTime
			self.index = self['list'].getSelectionIndex()
			trailer_url = self.list[self.index][1]
			trailer_res = self.list[self.index][0]
			beginTime = int(time())
			start_new_thread(self.trailerPlay, ())
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)


	def keyDown(self):
		try:
			self["list"].instance.moveSelection(self["list"].instance.moveDown)
		except:
			pass
			
	def keyUp(self):
		try:
			self["list"].instance.moveSelection(self["list"].instance.moveUp)
		except:
			pass

	def exit(self):
		self.close(True)

class xPlayer(Screen):

	def __init__(self, session):
		Screen.__init__(self, session)
		self.session = session
		self.skin = """
<screen name="xPlayer" position="0,0" size="1920,1080" flags="wfNoBorder" backgroundColor="transparent">
  <widget name="vName" position="265,930" size="1400,40" font="Regular; 32" foregroundColor="white" backgroundColor="#15202b" zPosition="1" transparent="1" halign="center" valign="center" />
  <widget name="vInfo" position="265,983" size="1600,40" font="Regular; 26" foregroundColor="white" backgroundColor="#15202b" zPosition="2" transparent="1" halign="left" valign="center" />
  <widget name="vPoster" position="60,742" size="185,278" transparent="0" alphatest="off" zPosition="2" cornerRadius="20" scale="stretch" />
  <widget source="session.CurrentService" render="Label" position="1655,933" size="200,25" font="Regular;20" zPosition="5" halign="right" transparent="1">
	<convert type="ServicePosition">Remaining</convert>
  </widget>
  <widget source="session.CurrentService" render="Progress" size="1464,10" position="266,974"  cornerRadius="10" itemCornerRadius="10" zPosition="3" transparent="0" foregroundColor="{}" backgroundColor="#00444444">
	<convert type="ServicePosition">Position</convert>
  </widget>

  <eLabel name="" position="50,930" size="1820,100" zPosition="-1" transparent="0" backgroundColor="#15202b" cornerRadius="20" />
  <ePixmap position="1760,960" size="100,60" pixmap="{}" zPosition="5" transparent="1" alphatest="blend" />
</screen>""".format(prgrsColor, logo_thumb)

		self["actions"] = ActionMap(["xtraEventAction"],
			{
				"cancel":self.exit,
				"red":self.exit,
				"ok":self.keyOK,
			}, -2)
		self['vName'] = Label()
		self['vInfo'] = Label()
		self["vPoster"] = Pixmap()
		self["vProgress"] = ProgressBar()
		self.onCh = self.session.nav.getCurrentlyPlayingServiceReference()
		self.hideTimer = eTimer()
		self.hideTimer.callback.append(self.infobarHide)
		self.onClose.append(self.__onClose)
		self.onLayoutFinish.append(self.runPlay)

	def runPlay(self):
		try:
			global trailer_url
			global trailer_res
			global title
			global ytu
			trailer_res = str(trailer_res).strip()
			self['vName'].setText(str(title))
			self['vName'].show()
# trailer_info
			inf = []
			if config.plugins.xtrvnt.trailer.value == "Youtube":
				pstrNm = "{}poster/{}.jpg".format(pathLoc, title)
				if os.path.exists(pstrNm):
					self["vPoster"].instance.setPixmapFromFile(pstrNm)
					self["vPoster"].instance.setScale(2)
					self["vPoster"].instance.show()
				else:
					self["vPoster"].instance.hide()
				try:
					res = "{}x{}".format(ytu[trailer_res]["width"], ytu[trailer_res]["height"])
					inf.append(res)
					fps = "{}fps".format(ytu[trailer_res]["fps"])
					inf.append(fps) 
					vtyp = ytu[trailer_res]["mimeType"].split(";")[0]
					inf.append(vtyp)
				except:
					pass
				ms = int(ytu[trailer_res]["approxDurationMs"])
				sec = int((ms / 1000) % 60)
				min = int((ms / (1000 * 60)) % 60)
				hr = int((ms / (1000 * 60 * 60)) % 24)
				if hr <= 0:
					dur = "{}:{}".format(str(min).zfill(2), str(sec).zfill(2))
				else:
					dur = "{}:{}:{}".format(str(hr), str(min).zfill(2), str(sec).zfill(2))
				inf.append(dur)
			elif config.plugins.xtrvnt.trailer.value == "IMDB":
				pstrNm = "{}imdb/casts/{}/{}_poster.jpg".format(pathLoc, title, title)
				if os.path.exists(pstrNm):
					self["vPoster"].instance.setPixmapFromFile(pstrNm)
					self["vPoster"].instance.setScale(2)
					self["vPoster"].instance.show()
				else:
					self["vPoster"].instance.hide()
			else:
				inf.append(trailer_res)
			self.setHideTimer()
			try:
			   tp = "{}".format(config.plugins.xtrvnt.trailerPlayer.value)
			except:
				tp = "4097"
			sep_color = '\\c0000???? | '
			sep_color += '\\c00??????'
			trailer_info = sep_color.join(inf)
			self['vInfo'].setText(str(trailer_info))
			self['vInfo'].show()
			sref = eServiceReference(int(tp), 0, trailer_url.strip())
			self.session.nav.stopService()
			self.session.nav.playService(sref)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyOK(self):
		self.show()
		self.setHideTimer()
		
	def setHideTimer(self):
		infobar_timeout = 2
		infobar_timeout = int(config.usage.infobar_timeout.value)
		self.hideTimer.start(infobar_timeout * 1024, True)

	def infobarHide(self):
		self.hide()
		self.hideTimer.stop()

	def __onClose(self):
		self.session.nav.stopService()
		self.session.nav.playService(self.onCh)
		self.close()

	def exit(self):
		self.close()

class xtraInfoPerson(Screen):

	def __init__(self, session):
		self.session = session
		Screen.__init__(self, session)
		if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
			if config.plugins.xtrvnt.xtraInfoSourceSkinTMDB.value == "skin1":
				self.skin = xtraInfoPerson_1080_tmdb1
			elif config.plugins.xtrvnt.xtraInfoSourceSkinTMDB.value == "skin2":
				self.skin = xtraInfoPerson_1080_tmdb2
			elif config.plugins.xtrvnt.xtraInfoSourceSkinTMDB.value == "skin3":
				self.skin = xtraInfoPerson_1080_tmdb3
		elif config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
			if config.plugins.xtrvnt.xtraInfoSourceSkinIMDB.value == "skin1":
				self.skin = xtraInfoPerson_1080_imdb1
			elif config.plugins.xtrvnt.xtraInfoSourceSkinIMDB.value == "skin2":
				self.skin = xtraInfoPerson_1080_imdb2

		self.list = []

		self['key_red'] = Label(_('Close'))
		self['key_green'] = Label()
		self['key_yellow'] = Label()
		self['key_blue'] = Label()
		self["actions"] = ActionMap(["xtraEventAction"],
		{
			"red": self.exit,
			# "green": self.showInfos,
			# "yellow": self.runTrailerPlay,
			# "blue": self.mSearch,
			"cancel": self.exit,
			"ok": self.keyOK,
			"info": self.pinfo,
			# "menu": self.xtraSetup
		},-1)
		
		# self.setTitle(_())

		self['biography'] = Label()
		self['int_statu'] = Label()
		self["poster"] = Pixmap()
		self["backdrop"] = Pixmap()
		self["castList"] = List(self.list)
		
		self["known_for0"] = Pixmap()
		self["known_for1"] = Pixmap()
		self["known_for2"] = Pixmap()
		
		self["known_forText0"] = Label()
		self["known_forText1"] = Label()
		self["known_forText2"] = Label()
		self.onLayoutFinish.append(self.runPersonList)

	def runPersonList(self):
		try:
			# if intCheck():
				# self['int_statu'].setText("\c0040a579")
			# else:
				# self['int_statu'].setText("\c00333333")
			global lst
			# open("/tmp/lstt.txt","w").write(lst)
			# global selPerson
			self["castList"].setList(lst)
			# self["castList"].show()
			# selPerson = self["castList"].selectionEnabled()[1]
			start_new_thread(self.dPersonInfo, ())
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
			
	def dPersonInfo(self):
		global lst
		global selPerson
		if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
			for i in lst:
				try:
					selPerson = i[1]
					castsFolder = "{}casts/person/{}".format(pathLoc, selPerson)
					if not os.path.isdir(castsFolder):
						os.makedirs(castsFolder)
					p1 = "{}/p1.json".format(castsFolder)
					p2 = "{}/p2.json".format(castsFolder)
					if not os.path.exists(p1) or not os.path.exists(p2):
						url="https://api.themoviedb.org/3/search/person?api_key={}&query={}&language={}".format(tmdb_api, selPerson, getLanguage())
						res = requests.get(url, headers=header).json()
						js = json.dumps(res, ensure_ascii=False)
						with open(p1, "w") as f:
							f.write(js)
						pid = res["results"][0]["id"]
						url="https://api.themoviedb.org/3/person/{}?api_key={}&language={}".format(pid, tmdb_api, getLanguage())
						ress = requests.get(url, headers=header).json()
						js2 = json.dumps(ress, ensure_ascii=False)
						if ress["biography"] == "":
							getLang = "en"
							url = "https://api.themoviedb.org/3/person/{}?api_key={}&language={}".format(pid, tmdb_api, getLang)
							ress = requests.get(url, headers=header).json()
							js2 = json.dumps(ress, ensure_ascii=False)
						with open(p2, "w") as f:
							f.write(js2)
						pposter_url = "https://image.tmdb.org/t/p/w300{}".format(ress["profile_path"])
						open("{}/p.jpg".format(castsFolder), 'wb').write(requests.get(pposter_url, stream=True, allow_redirects=True).content)
						known_folder = "{}/known_for".format(castsFolder)
						if not os.path.isdir(known_folder):
							os.makedirs(known_folder)
						known_number = len(res["results"][0]["known_for"])
						for i in range(int(known_number)):
							try:
								try:
									actr = res["results"][0]["known_for"][i]["original_title"]
								except:
									try:
										actr = res["results"][0]["known_for"][i]["original_name"]
									except:
										actr = i
			  
								actr_pic_url = res["results"][0]["known_for"][i]["poster_path"]
								actr_url = "https://image.tmdb.org/t/p/w185{}".format(actr_pic_url)
								actr = REGEX.sub('', actr).strip()
								castPicName = "{}/{}.jpg".format(known_folder, actr)
								open(castPicName, 'wb').write(requests.get(actr_url, stream=True, allow_redirects=True).content)
							except:
								pass
						self.showPerson()
					else:
						self.showPerson()
				except Exception as err:
					from Tools.xtraTool import errorlog
					errorlog(err, __file__)
		elif config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
			for i in lst:
				try:
					selPerson = i[1]
					# castsFolder = "{}casts/person/{}".format(pathLoc, selPerson)
					cloc = "{}imdb/casts/{}/".format(pathLoc, selPerson)
					if not os.path.isdir(cloc):
						os.makedirs(cloc)

					known_folder = "{}/known_for".format(cloc)
					if not os.path.isdir(known_folder):
						os.makedirs(known_folder)
					for i in range(3):
						try:
							try:
								actr = res["results"][0]["known_for"][i]["original_title"]
							except:
								try:
									actr = res["results"][0]["known_for"][i]["original_name"]
								except:
									actr = i
		  
							actr_pic_url = res["results"][0]["known_for"][i]["poster_path"]
							actr_url = "https://image.tmdb.org/t/p/w185{}".format(actr_pic_url)
							actr = REGEX.sub('', actr).strip()
							castPicName = "{}/{}.jpg".format(known_folder, actr)
							if not os.path.exists(castPicName):
								open(castPicName, 'wb').write(requests.get(actr_url, stream=True, allow_redirects=True).content)
						except:
							pass
					self.showPerson()
				except Exception as err:
					from Tools.xtraTool import errorlog
					errorlog(err, __file__)

	def showPerson(self):
		if intCheck():
			self['int_statu'].setText("\c0040a579")
		else:
			self['int_statu'].setText("\c00333333")
		global selPerson
		global title
		if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
			try:
				castsFolder = "{}casts/person/{}".format(pathLoc, selPerson)
				p1 = "{}/p1.json".format(castsFolder)
				p2 = "{}/p2.json".format(castsFolder)
				with open(p1) as f:
					p1r = json.load(f)
				with open(p2) as f:
					p2r = json.load(f)
				name = ""
				bdd = ""
				bio = ""
				try:
					name = "\c000089fa{}".format(p2r['name'])
				except:
					name = ""
				try:
					bdd = "\c0000????Birthday : \c00bbbbbb{} / {}".format(p2r['birthday'], p2r['deathday'])
				except:
					bdd = ""
				try:
					bdp = "\c0000????Place of Birth: \c00bbbbbb{}".format(p2r["place_of_birth"])
				except:
					bdp = ""
				try:
					bio = "\c0000????Biography : \c00bbbbbb{}".format(p2r['biography'])
				except:
					bio = ""
				pstrNm = "{}/p.jpg".format(castsFolder, selPerson)
				bckdrpNm = "{}backdrop/{}.jpg".format(pathLoc, title)
				if os.path.exists(pstrNm):
					self["poster"].instance.setPixmapFromFile(pstrNm)
					self["poster"].instance.setScale(2)
					self["poster"].instance.show()
				if os.path.exists(bckdrpNm):
					self["backdrop"].instance.setPixmapFromFile(bckdrpNm)
					self["backdrop"].instance.setScale(2)
					self["backdrop"].instance.show()
				pdesc = "\n".join((name, bdd, bdp, bio))
				self['biography'].setText(pdesc)
				self['biography'].show()

				known_folder = "{}/known_for".format(castsFolder)
				if os.path.isdir(known_folder):
					castFiles = sorted(os.listdir(known_folder))
					for i in range(3):
						try:
							knf = "{}/{}".format(known_folder, castFiles[i])
							self["known_for{}".format(i)].instance.setPixmapFromFile(knf)
							self["known_for{}".format(i)].instance.setScale(2)
							self["known_for{}".format(i)].instance.show()
							
							self["known_forText{}".format(i)].instance.setText(castFiles[i][:-4])
							self["known_forText{}".format(i)].instance.setScale(2)
							self["known_forText{}".format(i)].instance.show()
						except:
							pass

			except Exception as err:
				from Tools.xtraTool import errorlog
				errorlog(err, __file__)
		elif config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
			try:
				ci = "{}imdb/casts/{}/person/{}/{}.json".format(pathLoc, title, selPerson, selPerson)
				with open(ci) as f:
					castsInfo = json.load(f)
				name = ""
				bdd = ""
				bio = ""
				try:
					name = "\c00ffcc00{}".format(castsInfo['name'])
				except:
					name = ""
				try:
					bdd = "\c00ffff99Birthday : \c00bbbbbb{} / {}".format(castsInfo['birthDate'], castsInfo['deathDate'])
				except:
					bdd = ""
				try:
					bdp = "\c00ffff99Place of Birth: \c00bbbbbb{}".format(castsInfo["birthLocation"])
				except:
					bdp = ""
				try:
					bio = "\c00ffff99Biography : \c00bbbbbb{}".format(castsInfo['bio'])
				except:
					bio = ""
				pstrNm = "{}imdb/casts/{}/person/{}/{}.jpg".format(pathLoc, title, selPerson, selPerson)
				if os.path.exists(pstrNm):
					self["poster"].instance.setPixmapFromFile(pstrNm)
					self["poster"].instance.setScale(2)
					self["poster"].instance.show()
				pdesc = "\n".join((name, bdd, bdp, bio))
				self['biography'].setText(pdesc)
				self['biography'].show()
				cf = "{}imdb/casts/{}/person/{}/knownForr".format(pathLoc, title, selPerson)
				if os.path.isdir(cf):
					castFiles = sorted(os.listdir(cf))
					for i in range(3):
						try:
							knf = "{}/{}".format(cf, castFiles[i])
							self["known_for{}".format(i)].instance.setPixmapFromFile(knf)
							self["known_for{}".format(i)].instance.setScale(2)
							self["known_for{}".format(i)].instance.show()
							
							self["known_forText{}".format(i)].instance.setText(castFiles[i][:-4])
							self["known_forText{}".format(i)].instance.setScale(2)
							self["known_forText{}".format(i)].instance.show()
						except:
							pass
			except Exception as err:
				from Tools.xtraTool import errorlog
				errorlog(err, __file__)

	def keyOK(self):
		try:
			global lst
			global selPerson
			selPerson = self["castList"].getCurrent()[1]
			self.setTitle(_(selPerson))
			self.showPerson()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
			
	# def xtraSetup(self):
		# pass
		# from . import xtra
		# self.session.open(xtra.xtra)

	def pinfo(self):
		self.session.open(infos)
		
	def exit(self):
		self.close()






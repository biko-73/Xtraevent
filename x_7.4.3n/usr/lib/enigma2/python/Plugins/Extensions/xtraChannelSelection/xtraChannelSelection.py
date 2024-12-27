# -*- coding: utf-8 -*-
# by digiteng ©
from __future__ import absolute_import
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from enigma import eEPGCache, eLabel, gFont, ePixmap, eTimer, eServiceReference, eServiceCenter, \
RT_HALIGN_LEFT, RT_HALIGN_CENTER, RT_VALIGN_CENTER , RT_WRAP, RT_HALIGN_RIGHT, \
eListboxPythonMultiContent, BT_SCALE, eListbox, iServiceInformation
from Components.Pixmap import Pixmap
from Tools.LoadPixmap import LoadPixmap
from Screens.MessageBox import MessageBox
from Tools import Notifications
from marshal import loads
from Components.Sources.List import List
from .xch_config import *
from Components.config import config, configfile, ConfigSubsection
from Components.ConfigList import ConfigListScreen
import skin
import os
import re
import requests
import json
from Components.Sources.CanvasSource import CanvasSource
from time import localtime, mktime, time
from datetime import datetime, date
from Components.ProgressBar import ProgressBar
from Components.Sources.ServiceEvent import ServiceEvent
from Components.Sources.Event import Event
from Components.Renderer.Picon import getPiconName
from ServiceReference import ServiceReference
from six.moves import reload_module
from Tools.xtraTool import REGEX, pRating
from skin import parseColor
try:
	from _thread import start_new_thread
except:
	try:
		from thread import start_new_thread
	except:
		pass
if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/xa.pyc"):
	from Plugins.Extensions.xtraEvent.xa import uts
if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/xm.pyc"):
	from Plugins.Extensions.xtraEvent.xm import apr
from .skins import xCHSkins
reload_module(xCHSkins)
from Plugins.Extensions.xtraChannelSelection.skins.xCHSkins import *
epgCache = eEPGCache.getInstance()
version = "v1.3.6"
try:
	pathLoc = config.plugins.xtrvnt.loc.value
except:
	pathLoc = ""
try:
	mc = "N/A"
	mc = os.popen("ifconfig eth0 | awk '/HWaddr/ {printf $5}'").read()
except:
	pass


service_types_tv = '1:7:1:0:0:0:0:0:0:0:(type == 1) || (type == 17) || (type == 22) || (type == 25) || (type == 31) || (type == 134) || (type == 195)'
eventImage = "/media/hdd/xtraEvent/poster/Blue Bloods.jpg"
n = 0
config.tv = ConfigSubsection()
config.tv.lastservice = ConfigText()
config.tv.lastroot = ConfigText()
pratePath = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/parental/"
imgNo="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film.jpg"
class xtraChannelSelection(Screen):

	def __init__(self, session):
		self.session = session
		Screen.__init__(self, session)
		
		if "atv" in imgr:
			if config.plugins.xCH.style.value == "grid":
				self.skin = xtraCh_Grid_1080
			elif config.plugins.xCH.style.value == "horizontal":
				self.skin = xtraCh_Hor_1080
			elif config.plugins.xCH.style.value == "horizontal_2":
				self.skin = xtraCh_Hor_1080_2
			elif config.plugins.xCH.style.value == "horizontal_3":
				self.skin = xtraCh_Hor_1080_3
			elif config.plugins.xCH.style.value == "vertical":
				self.skin = xtraCh_Ver_1080
			elif config.plugins.xCH.style.value == "vertical_2":
				self.skin = xtraCh_Ver_1080_2
			elif config.plugins.xCH.style.value == "vertical_3":
				self.skin = xtraCh_Ver_1080_3
		self.list  = []
		self["actions"] = ActionMap(["xtraChannelSelectionAction"],
			{
			"up": self.keyUp,
			"down": self.keyDown,
			"left": self.keyLeft,
			"right": self.keyRight,
			"cancel": self.exit,
			"red": self.exit,
			"green": self.xEpg,
			"yellow": self.xInfo,
			"blue": self.xBouquets,
			"ok": self.keyOk,
			"menu": self.keyMenu,
			"info": self.inf,
			}, -2)
		self["key_red"] = Label(_("Exit"))
		self["key_green"] = Label(_("xtraEpg"))
		self["key_yellow"] = Label(_("xtraInfo"))
		self["key_blue"] = Label(_("Bouquets"))
		self["ServiceEvent"] = ServiceEvent()
		self["Event"] = Event()
		self.indx = 0
		self["chList"] = List([])
		self['description'] = Label()
		self['short_description'] = Label()
		self['imdb'] = Label()
		self['infos'] = Label()
		self['eventTime'] = Label()
		self['primeTime'] = Label()
		self["primeTimeBackdrop"] = Pixmap()
		self["poster"] = Pixmap()
		self["picon"] = Pixmap()
		self["ratingStar"] = ProgressBar()
		self["parentalRating"] = Pixmap()
		for i in range(1, 5, 1):
			self["Backdrop{}".format(i)] = Pixmap()
			self["BackdropNm{}".format(i)] = Label()
		self.onLayoutFinish.append(self.delay)

	def delay(self):
		start_new_thread(self.getCh, ())

	def xBouquets(self):
		self.session.open(xtraChannelSelectionBouquets)

	def getCh(self):
		try:
			self["chList"].setList([])
			last_root = eServiceReference(config.tv.lastroot.value.split(";")[1])
			last_service = config.tv.lastservice.value
			try:
				cur_ref = self.session.nav.getCurrentlyPlayingServiceOrGroup()
				self.getEvent(cur_ref)
			except:
				pass
			serviceHandler = eServiceCenter.getInstance()
			services = serviceHandler.list(last_root).getContent("SRN", True) # S=ref R=ref.toString() N=chname
			# open("/tmp/services.py","w").write(str(services))
			chNum = 0
			ref = None
			sref = None
			chName = "N/A"
			evntNm = "N/A"
			chNum = ""
			progress = 0
			percent = ""
			imgNo = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film.jpg"
			chlst=[]
			for ref, sref, chName in services:
				event="N/A"
				evntNm = "N/A"
				percent = ""
				progress = 0
				eventImage = None
				img = None
				# chNum += 1
				cur_info=""
				service = ""
				info = ""
				prgrsback=""
				events = epgCache.lookupEvent(['IBDCT', (ref, 0, -1, 1)])
				if events:
					try:
						event = events[0][4]
						evntNm = REGEX.sub('', event).strip()
						if event:
							if config.plugins.xCH.Images.value == "Poster":
								img = "{}xtraEvent/poster/{}.jpg".format(pathLoc, evntNm)
								if os.path.exists(img):
									eventImage = LoadPixmap(img)
								else:
									eventImage = LoadPixmap(imgNo)
							elif config.plugins.xCH.Images.value == "Backdrop":
								img = "{}xtraEvent/backdropThumbnail/{}.jpg".format(pathLoc, evntNm)
								if os.path.exists(img):
									eventImage = LoadPixmap(img)
								else:
									eventImage = LoadPixmap(imgNo)
							elif config.plugins.xCH.Images.value == "Picon":
								try:
									img = getPiconName(str(ServiceReference(sref)))
									eventImage = LoadPixmap(img)
								except:
									eventImage = LoadPixmap(imgNo)
							elif config.plugins.xCH.Images.value == False:
								eventImage = LoadPixmap(imgNo)
							if config.plugins.xCH.style.value == "horizontal":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_200x10.png")
							elif config.plugins.xCH.style.value == "horizontal_2":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_200x10.png")
							elif config.plugins.xCH.style.value == "horizontal_3":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_300x7.png")
							elif config.plugins.xCH.style.value == "grid":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_300x7.png")
							elif config.plugins.xCH.style.value == "vertical":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_900x7.png")
							elif config.plugins.xCH.style.value == "vertical_3":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_165x7.png")
							if config.plugins.xCH.style.value == "horizontal_3":
								img = "{}xtraEvent/poster/{}.jpg".format(pathLoc, evntNm)
								if os.path.exists(img):
									eventImage = LoadPixmap(img)
								else:
									eventImage = LoadPixmap(imgNo)
							now = int(time())
							progress = (int(time()) - events[0][1]) * 100 // events[0][2]
							if progress > 0:
								percent = "%{}".format(progress)
						else:
							eventImage = LoadPixmap(imgNo)
							if config.plugins.xCH.style.value == "horizontal":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_200x10.png")
							elif config.plugins.xCH.style.value == "horizontal_2":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_200x10.png")
							elif config.plugins.xCH.style.value == "horizontal_3":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_300x7.png")
							elif config.plugins.xCH.style.value == "grid":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_300x7.png")
							elif config.plugins.xCH.style.value == "vertical":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_900x7.png")
							elif config.plugins.xCH.style.value == "vertical_3":
								prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_165x7.png")
					except:
						eventImage = LoadPixmap(imgNo)
				else:
					eventImage = LoadPixmap(imgNo)
					if config.plugins.xCH.style.value == "horizontal":
						prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_200x10.png")
					elif config.plugins.xCH.style.value == "horizontal_2":
						prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_200x10.png")
					elif config.plugins.xCH.style.value == "horizontal_3":
						prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_300x7.png")
					elif config.plugins.xCH.style.value == "grid":
						prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_300x7.png")
					elif config.plugins.xCH.style.value == "vertical":
						prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_900x7.png")
					elif config.plugins.xCH.style.value == "vertical_3":
						prgrsback = LoadPixmap("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/prgrss_back_165x7.png")
				chNum = sref.getChannelNum()
				if ref == cur_ref.toString():
					self.indx = chNum
					videoHeight = 0
					progressive = ""
					videoH=isDolbyIcon=isCrypted=isSubtIcon=isStreamIcon=isHDR=""
					service = self.session.nav.getCurrentService()
					if service:
						info = service.info()
					if info.getInfo(iServiceInformation.sIsCrypted) == 1:
						isCrypted = ""
					else:
						isCrypted = ""
					# sref = info.getInfoString(iServiceInformation.sServiceref)
					videoHeight = info.getInfo(iServiceInformation.sVideoHeight)
					videoWidth = info.getInfo(iServiceInformation.sVideoWidth)
					progressive = info.getInfo(iServiceInformation.sProgressive)
					progressive = "p" if progressive else "i"
					if videoHeight >= 240 and videoHeight < 720:
						videoH = ""
					elif videoHeight >= 720 and videoHeight < 1080:
						videoH = ""
					elif videoHeight >= 1080 and videoHeight < 2160:
						videoH = ""
					elif videoHeight >= 2160 and videoHeight < 3840:
						videoH = ""
					else:
						videoH = ""
					if videoWidth > 2160 and videoWidth <= 3840 and videoGamma == 1:
						isHDR = ""
					elif videoWidth > 2160 and videoWidth <= 3840 and videoGamma == 2:
						isHDR = ""
					elif videoWidth > 2160 and videoWidth <= 3840 and videoGamma == 3:
						isHDR = ""
					else:
						isHDR = ""
					audio = service.audioTracks()
					description = audio.getTrackInfo(audio.getCurrentTrack()).getDescription()
					isDolby = bool(description and description.split()[0] in ("AC3", "AC3+", "DTS", "DTS-HD", "AC4", "LPCM", "Dolby", "HE-AAC", "AAC+", "WMA"))
					subtitle = service and service.subtitle()
					isSubt = bool(subtitle and subtitle.getSubtitleList())
					if isSubt:
						isSubtIcon = ""
					else:
						isSubtIcon = ""
					isStream = service.streamed() is not None
					if isStream:
						isStreamIcon = ""
					else:
						isStreamIcon = ""
					if isDolby:
						isDolbyIcon = ""
					else:
						isDolbyIcon = ""
					aa = list((videoH, isDolbyIcon, isCrypted, isSubtIcon, isStreamIcon, isHDR))
					lst=[]
					for i in aa:
						if i != "":
							lst.append(i)
					cur_info = "   ".join(lst)
					open("/tmp/cur_info.txt","w").write(str(cur_info))
				chlst.append((eventImage, chName, evntNm, progress, ref, sref, percent, str(chNum), cur_info, prgrsback))
			self["chList"].setList(chlst)
			self["chList"].show()
			self.goindex()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def goindex(self):
		ref = self.session.nav.getCurrentlyPlayingServiceReference()
		chNum = int(ref.getChannelNum())
		# index = self["chList"].getCurrentIndex()
		if (ref.flags & eServiceReference.isMarker or ref.type == -1):
			self["chList"].setCurrentIndex(self.indx)
		else:
			self["chList"].setCurrentIndex(self.indx - 1)
		self["chList"].show()
		self.listRefresh()
		
	def listRefresh(self):
		self.changedEvent()

	def changedEvent(self):
		if not self.instance:
			return
		try:
			sel = self["chList"].getCurrent()
			ref = sel[4]
			cur = eServiceReference(ref)
			self["ServiceEvent"].newService(cur)
			self["Event"].newEvent(cur)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyOk(self):
		try:
			sel = self["chList"].getCurrent()
			ref = sel[4]
			config.tv.lastservice.value = ref
			config.tv.save()
			configfile.save()
			self.session.nav.stopService()
			self.session.nav.playService(eServiceReference(ref))
			self.close(ref)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyLeft(self):
		try:
			self["chList"].goLeft()
			sref = self["chList"].getCurrent()[5]
			self.getEvent(sref)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
		
	def keyRight(self):
		try:
			self["chList"].goRight()
			sref = self["chList"].getCurrent()[5]
			self.getEvent(sref)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyUp(self):
		try:
			self["chList"].up()
			sref = self["chList"].getCurrent()[5]
			self.getEvent(sref)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
		
	def keyDown(self):
		try:
			self["chList"].down()
			sref = self["chList"].getCurrent()[5]
			self.getEvent(sref)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def getEvent(self, sref):
		try:
			event = None
			eventName= "N/A"
			ShortDescription = "N/A"
			ExtendedDescription = "N/A"
			ParentalData = "N/A"
			Rated = None
			rate = None
			self["picon"].hide()
			event = epgCache.lookupEventTime(sref, -1, 0)
			# chNum = ref.getChannelNum()
			if event:
				eventName = event.getEventName()
				EventId = event.getEventId()
				ShortDescription = event.getShortDescription()
				ExtendedDescription = event.getExtendedDescription()
				ParentalData = event.getParentalData()
				# self.setTitle(_(eventName))
				self['short_description'].setText(_(str(ShortDescription)))
				self['short_description'].show()
				fd = "\c0000????Description:\c00eeeeee{}\n{}".format(ShortDescription, ExtendedDescription)
				self['description'].setText(_(fd))
				self['description'].show()
				piconName = str(getPiconName(str(ServiceReference(sref))))
				if os.path.exists(piconName):
					self["picon"].instance.setPixmapFromFile(piconName)
					self["picon"].instance.setScale(2)
					self["picon"].instance.show()
				else:
					self["picon"].hide()
				if eventName is None:
					return
				title = REGEX.sub('', eventName).strip()
				self.setTitle(_(title))
				pstrNm = "{}xtraEvent/poster/{}.jpg".format(pathLoc, title)
				rating_json = "{}xtraEvent/infos/{}.json".format(pathLoc, title)
				if os.path.exists(pstrNm):
					self["poster"].instance.setPixmapFromFile(pstrNm)
					self["poster"].instance.setScale(2)
					self["poster"].instance.show()
				else:
					self["poster"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film.jpg")
					self["poster"].instance.setScale(2)
					self["poster"].instance.show()
				imdbRating = ""
				imdbVotes = ""
				keyColor = "\c0000????"
				keyColorB = "\c00bbbbbb"
				if os.path.exists(rating_json):
					with open(rating_json) as f:
						read_json = json.load(f)
					try:
						imdbRating = read_json["imdbRating"]
					except:
						imdbRating = ""
					try:
						imdbVotes = read_json["imdbRatingVote"]
					except:
						imdbVotes = ""
					if imdbRating is not None:
						rtng = int(10 * float(imdbRating))
						self["ratingStar"].instance.setRange(0, 100)
						self["ratingStar"].instance.setValue(rtng)
						self["ratingStar"].instance.show()
					else:
						self["ratingStar"].hide()
					imdbRating = "\c0000????IMDB : \c00eeeeee{}({})".format(imdbRating, imdbVotes)
					self['imdb'].setText(imdbRating)
					self['imdb'].show()
				else:
					self["ratingStar"].hide()
					self["imdb"].hide()
				evnt=[]
				try:
					if "title" in str(read_json):
						tt = read_json["title"]
						evnt.append("{}Title : {}{}".format(keyColor, keyColorB, tt))
				except:
					pass
				try:
					if "release_date" in str(read_json):
						rd = read_json["release_date"]
						evnt.append("{}ReleaseDate : {}{}".format(keyColor, keyColorB, rd))
				except:
					pass
				try:
					if "countries" in str(read_json):
						rd = read_json["countries"]
						evnt.append("{}Countries : {}{}".format(keyColor, keyColorB, rd))
				except:
					pass
				try:
					if "budget" in str(read_json):
						rd = read_json["budget"]
						evnt.append("{}Budget : {}{}".format(keyColor, keyColorB, rd))
				except:
					pass
				try:
					if "revenue" in str(read_json):
						rd = read_json["revenue"]
						evnt.append("{}Revenue : {}{}".format(keyColor, keyColorB, rd))
				except:
					pass
				try:
					prs = ['(\d+). Staffel, Folge (\d+)', 'T(\d+) Ep.(\d+)', '"Episodio (\d+)" T(\d+)', '(\d+).* \(odc. (\d+).*\)']
					for i in prs:
						seg = re.search(i, fd)
						if seg:
							s = seg.group(1).zfill(2)
							e = seg.group(2).zfill(2)
							evnt.append("{}SE : {}S{}E{}".format(keyColor, keyColorB, s, e))
				except:
					pass
				try:
					if "genre" in str(read_json):
						Genre = read_json["genre"]
						evnt.append("{}Genre : {}{}".format(keyColor, keyColorB, Genre))
					else:
						genres = event.getGenreDataList()
						if genres:
							genre = genres[0]
							evnt.append("{}Genre : {}{}".format(keyColor, keyColorB, getGenreStringSub(genre[0], genre[1])))
				except:
					pass
				try:
					if "duration" in str(read_json):
						Duration = read_json["duration"]
						evnt.append("{}Duration : {}{} min".format(keyColor, keyColorB, Duration))
					else:
						drtn = round(event.getDuration()// 60)
						if drtn > 0:
							evnt.append("{}Duration : {}{}min".format(keyColor, keyColorB, drtn))
						else:
							prs = re.findall(r' \d+ Min', fd)
							if prs:
								drtn = round(prs[0])
								evnt.append("{}Duration : {}{}min".format(keyColor, keyColorB, drtn))
				except:
					pass
				try:
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
					evnt.append("{}Rated : {}{}".format(keyColor, keyColorB, rate))
					tc = "\n".join(evnt)
					self['infos'].setText(tc)
					self['infos'].show()
					rate = str(rate).strip()
					getRate = pRating(rate)
					if rate is not None:
						rateNm = "{}FSK_{}.png".format(pratePath, getRate)
						self["parentalRating"].instance.setPixmapFromFile(rateNm)
						self["parentalRating"].instance.setScale(1)
						self["parentalRating"].instance.show()
					else:
						self["parentalRating"].instance.setPixmapFromFile("{}FSK_NA.png".format(pratePath))
						self["parentalRating"].instance.setScale(1)
						self["parentalRating"].instance.show()
				except:
					pass
				etm = ""
				try:st = event.getBeginTime()
				except:pass
				try:duration = event.getDuration()
				except:pass
				try:et = st + duration
				except:pass
				try:begin = localtime(st)
				except:pass
				try:end = localtime(et)
				except: pass
				try: startend = "%02d:%02d - %02d:%02d" % (begin[3], begin[4], end[3], end[4])
				except:pass
				try:etm = "\\c0000??80{} \\c00??????{} \\c00????ff({}min)".format(startend, event.getEventName(), duration // 60)
				except:pass
				self['eventTime'].setText(etm)
				self['eventTime'].show()
# prime time
				primetime = "N/A"
				self.text = "N/A"
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
				epgCache.startTimeQuery(eServiceReference(sref), pt)
				evn = epgCache.getNextTimeEntry()
				eNm = ""
				try:
					eNm = evn.getEventName()
				except:
					pass
				bcdrpNm = "{}xtraEvent/backdrop/{}.jpg".format(pathLoc, eNm)
				if evn and (now.tm_hour <= prime_hour):
					bt = localtime(evn.getBeginTime())
					duration = round(evn.getDuration() // 60)
					primetime = "\c0000????Prime Time\n\c00aaaaaa%02d:%02d \n%smin\c00??????\n%s"%(bt[3], bt[4], duration, eNm)
				else:
					self.text = "N/A"
				self['primeTime'].setText(primetime)
				self['primeTime'].show()
				if os.path.exists(bcdrpNm):
					self["primeTimeBackdrop"].instance.setPixmapFromFile(bcdrpNm)
					self["primeTimeBackdrop"].instance.setScale(1)
					self["primeTimeBackdrop"].instance.show()
				else:
					self["primeTimeBackdrop"].hide()
# backdrop list...
				events = epgCache.lookupEvent(['IBDCTSERNX', (sref.toString(), 1, -1, -1)])
				if events is not None:
					for i in range(1, 5, 1):
						try:
							eventNames = events[i][4]
							bcdrpsNm = "{}xtraEvent/backdropThumbnail/{}.jpg".format(pathLoc, eventNames)
							if os.path.exists(bcdrpsNm):
								self["Backdrop{}".format(i)].instance.setPixmapFromFile(bcdrpsNm)
								self["Backdrop{}".format(i)].instance.setScale(1)
								self["Backdrop{}".format(i)].instance.show()
								self["BackdropNm{}".format(i)].setText(eventNames)
								self["BackdropNm{}".format(i)].show()
							else:
								self["Backdrop{}".format(i)].instance.setPixmapFromFile(imgNo)
								self["BackdropNm{}".format(i)].hide()
						except:
							pass
				else:
					for i in range(1, 5, 1):
						self["Backdrop{}".format(i)].instance.setPixmapFromFile(imgNo)
						self["BackdropNm{}".format(i)].hide()
			else:
				self["parentalRating"].instance.setPixmapFromFile("{}FSK_NA.png".format(pratePath))
				self["parentalRating"].instance.setScale(1)
				self["parentalRating"].instance.show()
				self['eventTime'].hide()
				self["ratingStar"].hide()
				self['poster'].hide()
				self['description'].hide()
				self['imdb'].hide()
				self['infos'].hide()
				self['primeTime'].hide()
				self["primeTimeBackdrop"].hide()
				self["short_description"].hide()
				for i in range(1, 5, 1):
					self["Backdrop{}".format(i)].hide()
					self["BackdropNm{}".format(i)].hide()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
			
	def keyMenu(self):
		self.session.open(xtraChannelSelectionSetup)

	def inf(self):
		self.session.open(infos)

	def xInfo(self):
		ref = self["chList"].getCurrent()[5].toString()
		cur_ref = self.session.nav.getCurrentlyPlayingServiceReference().toString()
		if ref == cur_ref:
			from Plugins.Extensions.xtraEvent.xtraInfo import xtraInfo
			self.session.open(xtraInfo)

	def xEpg(self):
		eRef = self["chList"].getCurrent()[5]
		ee = self.session.open(xtraChannelSelectionEpg)
		ee.eList(eRef)
		
	def exit(self):
		# config.plugins.xCH.style.save()
		# config.plugins.xCH.Images.save()
		configfile.save()
		self.close()

class xtraChannelSelectionSetup(Screen, ConfigListScreen):
	skin = """
<screen name="xtraChannelSelectionSetup" position="0,0" size="1920,1080" title="xtraChannelSelectionSetup" flags="wfNoBorder">
			<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/xtra_fhd_3.png" transparent="1" />
			<widget source="Title" render="Label" position="58,55" size="1120,60" font="xtraBold; 60" foregroundColor="#ffffff" backgroundColor="#005090" transparent="1" halign="center" valign="center" />
			<eLabel name="" text="" position="56,56" size="60,60" backgroundColor="#15202b" transparent="1" halign="right" font="xtraIcons2; 60" />
			<widget name="config" position="60,136" size="1120,720" font="Regular;28" foregroundColor="#ffffff" backgroundColor="#000000" itemHeight="45" scrollbarMode="showAllways" transparent="1" />
			<widget name="pic" position="1260,558" size="600,340" zPosition="9" transparent="1" cornerRadius="20" />
			<widget name="progress_bar" position="1260,460" size="600,20"  backgroundColor="#005090" zPosition="5" transparent="0" cornerRadius="20" />
			<widget name="progress_bar2" position="1260,460" size="600,20"	backgroundGradient="#000000,#000000,#000000,horizontal" zPosition="5"  transparent="0" cornerRadius="20" />
			
			<widget source="preview" render="Canvas" position="0,0"	  size="0,0"	zPosition="9" transparent="0" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text="" position="1500,220" size="150,150" foregroundColor="#777777" backgroundColor="#15202b" transparent="1" halign="center" font="xtraIcons2; 100" zPosition="9" />
</screen>
	"""

	def __init__(self, session):
		self.session = session
		Screen.__init__(self, session)
		list = []
		ConfigListScreen.__init__(self, list, session=session)
		self['key_red'] = Label(_('Close'))
		self['key_green'] = Label(_("Save"))
		self['key_yellow'] = Label(_(None))
		self['key_blue'] = Label(_(None))
		self["actions"] = ActionMap(["xtraChannelSelectionAction"],
		{
			"left": self.keyLeft,
			"down": self.keyDown,
			"up": self.keyUp,
			"right": self.keyRight,
			"red": self.exit,
			"green": self.exit,
			# "yellow": self.append,
			# "blue": self.ms,
			"cancel": self.exit,
			# "ok": self.exit,
			# "info": self.strg,
			# "menu": self.menuS
			# "usb": self.keyUSB,
		},-1)
		# self["chList"] = List([])
		self["pic"] = Pixmap()
		self["progress_bar"] = Label()
		self["progress_bar2"] = Label()
		self["preview"] = CanvasSource()
		self.setTitle(_("xtraChannelSelectionSetup"))

		self.timer = eTimer()
		self.timer.callback.append(self.setupList)
		self.onLayoutFinish.append(self.setupList)
		
	def setupList(self):
		try:
			for x in self["config"].list:
				if len(x) > 1:
					x[1].save()
			slist=[]
			slist.append(getConfigListEntry("Style", config.plugins.xCH.style))
			if config.plugins.xCH.style.value != "horizontal_3":
				slist.append(getConfigListEntry("Images", config.plugins.xCH.Images))
			slist.append(getConfigListEntry("Progress Color", config.plugins.xCH.ProgressColor))
			rgbclr1 = "#000000"
			rgbclr2 = "#000000"
			rgbclr3 = "#000000"
			if config.plugins.xCH.ProgressColor.value == "Color":
				self["progress_bar2"].hide()
				slist.append(getConfigListEntry(_("		\c00??7777Red"), config.plugins.xCH.colorR))
				slist.append(getConfigListEntry(_("		\c0088??99Green"), config.plugins.xCH.colorG))
				slist.append(getConfigListEntry(_("		\c000089faBlue"), config.plugins.xCH.colorB))
				self.cslider(self.RGB(int(config.plugins.xCH.colorR.value), int(config.plugins.xCH.colorG.value), int(config.plugins.xCH.colorB.value)))
				r5 = '{:02x}'.format(int(config.plugins.xCH.colorR.value)) + '{:02x}'.format(int(config.plugins.xCH.colorG.value)) + '{:02x}'.format(int(config.plugins.xCH.colorB.value))
				rgbclr = "#%s" %r5
				self["progress_bar"].setText(_("."))
				self["progress_bar"].instance.setBackgroundColor(parseColor(rgbclr))
				self["progress_bar"].instance.setForegroundColor(parseColor(rgbclr)) 
				self["progress_bar"].show()
				config.plugins.xCH.prgrsColor.value = rgbclr
				config.plugins.xCH.prgrsColor.save()
				configfile.save()
			elif config.plugins.xCH.ProgressColor.value == "Gradient":
				self["progress_bar"].hide()
				slist.append(getConfigListEntry("Progress Gradient Color", config.plugins.xCH.ProgressGradientColor))
				rgbclr1 = config.plugins.xCH.prgrsColor1.value
				rgbclr2 = config.plugins.xCH.prgrsColor2.value
				rgbclr3 = config.plugins.xCH.prgrsColor3.value
				if config.plugins.xCH.ProgressGradientColor.value == "Color1":
					slist.append(getConfigListEntry(_("		\c00??7777Red"), config.plugins.xCH.colorR1))
					slist.append(getConfigListEntry(_("		\c0088??99Green"), config.plugins.xCH.colorG1))
					slist.append(getConfigListEntry(_("		\c000089faBlue"), config.plugins.xCH.colorB1))
					self.cslider(self.RGB(int(config.plugins.xCH.colorR1.value), int(config.plugins.xCH.colorG1.value), int(config.plugins.xCH.colorB1.value)))
					r1 = '{:02x}'.format(int(config.plugins.xCH.colorR1.value)) + '{:02x}'.format(int(config.plugins.xCH.colorG1.value)) + '{:02x}'.format(int(config.plugins.xCH.colorB1.value))
					rgbclr1 = "#%s" %r1
					config.plugins.xCH.prgrsColor1.value = rgbclr1
					config.plugins.xCH.prgrsColor1.save()
					configfile.save()
				elif config.plugins.xCH.ProgressGradientColor.value == "Color2":
					slist.append(getConfigListEntry(_("		\c00??7777Red"), config.plugins.xCH.colorR2))
					slist.append(getConfigListEntry(_("		\c0088??99Green"), config.plugins.xCH.colorG2))
					slist.append(getConfigListEntry(_("		\c000089faBlue"), config.plugins.xCH.colorB2))
					self.cslider(self.RGB(int(config.plugins.xCH.colorR2.value), int(config.plugins.xCH.colorG2.value), int(config.plugins.xCH.colorB2.value)))
					r2 = '{:02x}'.format(int(config.plugins.xCH.colorR2.value)) + '{:02x}'.format(int(config.plugins.xCH.colorG2.value)) + '{:02x}'.format(int(config.plugins.xCH.colorB2.value))
					rgbclr2 = "#%s" %r2
					config.plugins.xCH.prgrsColor2.value = rgbclr2
					config.plugins.xCH.prgrsColor2.save()
					configfile.save()
				elif config.plugins.xCH.ProgressGradientColor.value == "Color3":
					self["progress_bar2"].hide()
					slist.append(getConfigListEntry(_("		\c00??7777Red"), config.plugins.xCH.colorR3))
					slist.append(getConfigListEntry(_("		\c0088??99Green"), config.plugins.xCH.colorG3))
					slist.append(getConfigListEntry(_("		\c000089faBlue"), config.plugins.xCH.colorB3))
					self.cslider(self.RGB(int(config.plugins.xCH.colorR3.value), int(config.plugins.xCH.colorG3.value), int(config.plugins.xCH.colorB3.value)))
					r3 = '{:02x}'.format(int(config.plugins.xCH.colorR3.value)) + '{:02x}'.format(int(config.plugins.xCH.colorG3.value)) + '{:02x}'.format(int(config.plugins.xCH.colorB3.value))
					rgbclr3 = "#%s" %r3
					config.plugins.xCH.prgrsColor3.value = rgbclr3
					config.plugins.xCH.prgrsColor3.save()
					configfile.save()
				self["progress_bar2"].instance.setBackgroundGradient(parseColor(rgbclr1), parseColor(rgbclr2), parseColor(rgbclr3),2,1)
				self["progress_bar2"].show()
			self.picShow()
			self["config"].l.setItemHeight(50)
			# self["config"].l.setSeparation(400)
			self["config"].list = slist
			self["config"].l.setList(slist)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def RGB(self, r, g, b):
		return r << 16 | g << 8 | b

	def cslider(self, fcolor):
		c = self["preview"]
		c.fill(0, 0, 1920,1080, fcolor)
		c.flush()

	def picShow(self):
		try:
			self["progress_bar"].hide()
			pict  = "/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/pic/{}.jpg".format(config.plugins.xCH.style.value)
			self['pic'].instance.setPixmapFromFile(pict)
			self['pic'].instance.setScale(2)
			self['pic'].instance.show()
			self["progress_bar"].show()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
			
	def keyLeft(self):
		ConfigListScreen.keyLeft(self)
		self.picShow()
		self.delay()

	def keyRight(self):
		ConfigListScreen.keyRight(self)
		self.picShow()
		self.delay()

	def keyDown(self):
		self["config"].instance.moveSelection(self["config"].instance.moveDown)
		self.delay()

	def keyUp(self):
		self["config"].instance.moveSelection(self["config"].instance.moveUp)
		self.delay()

	def delay(self):
		self.timer.start(100, True)

	def exit(self):
		for x in self["config"].list:
			if len(x) > 1:
				x[1].save()
		config.plugins.xCH.style.save()
		config.plugins.xCH.Images.save()
		configfile.save()
		self.close()

class xtraChannelSelectionBouquets(Screen):
	skin= """
<screen position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
  <widget source="bqList" render="Listbox" position="63,136" size="1109,783" backgroundColor="#15202b" itemGradientSelected="#1b4765,#25648d,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" scrollbarWidth="2" enableWrapAround="1" itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="320,181" spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showAlways" listOrientation="vertical" scrollbarForegroundColor="#0089fa" transparent="1" zPosition="99">
	<convert type="TemplatedMultiContent">
				{"template": [
				MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (35,35), png = 0, flags = BT_SCALE), #icon
				MultiContentEntryText(pos = (50,10), size = (1000,35), font=0, flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), # bq name

				],
				"fonts": [gFont("Regular", 24), gFont("Regular", 18)],
				"itemWidth" : 900,
				"itemHeight" : 50
				}
				</convert>
  </widget>
</screen>
  """
	def __init__(self, session):
		self.session = session
		Screen.__init__(self, session)
		self["actions"] = ActionMap(["xtraChannelSelectionAction"],
			{
			# "up": self.keyUp,
			# "down": self.keyDown,
			# "left": self.keyLeft,
			# "right": self.keyRight,
			"cancel": self.close,
			"red": self.close,
			# "green": self.keyzap,
			# "yellow": self.getProviders,
			"blue": self.getBouquets,
			"ok": self.keyOk,
			# "menu": self.keyMenu,
			}, -2)
		self["key_red"] = Label(_("Exit"))
		# self["key_green"] = Label(_("-"))
		# self["key_yellow"] = Label(_("Providers"))
		self["key_blue"] = Label(_("Bouquets"))
		self["bqList"] = List([])
		self.onLayoutFinish.append(self.getBouquets)

	def keyOk(self):
		try:
			index = self["bqList"].getCurrentIndex()
			self.showChannels(index)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def getBouquets(self):
		if config.usage.multibouquet.value:
			self.root = eServiceReference('1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "bouquets.tv" ORDER BY bouquet')
		else:
			self.root = eServiceReference('%s FROM BOUQUET "userbouquet.favourites.tv" ORDER BY bouquet'%(service_types_tv))
		self.title = "xtraBouquets"
		self.setTitle(_(self.title))
		try:
			serviceHandler = eServiceCenter.getInstance()
			services = serviceHandler.list(self.root)
			bouquets = services and services.getContent("SN", True)
			img = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/icons/directory.png"
			lists = []
			for bouquet in bouquets:
				dicon = LoadPixmap(img)
				lists.append((dicon, bouquet[1]))
			self["bqList"].setList(lists)
			self["bqList"].show()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def showChannels(self, index):
		try:
			serviceHandler = eServiceCenter.getInstance()
			tvbouquets = serviceHandler.list(self.root).getContent("SN")
			selBuq = eServiceReference(str(tvbouquets[index][0]))
			serviceHandler = eServiceCenter.getInstance()
			bplst = serviceHandler.list(selBuq).getContent("SN", True) # R=ref.toString() N=ch name
			bt = '1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "bouquets.tv" ORDER BY bouquet'
			last_root = ";".join([bt, selBuq.toString()])
			config.tv.lastroot.value = last_root
			config.tv.save()
			configfile.save()
			self.goChList()
			self.close()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def goChList(self):
		self.session.open(xtraChannelSelection)

class xtraChannelSelectionEpg(Screen):

	def __init__(self, session, eRef=None):
		self.session = session
		self.eRef = eRef
		Screen.__init__(self, session)
		self.skin = xtraCh_Epg_1
		self.list  = []
		self["actions"] = ActionMap(["xtraChannelSelectionAction"],
			{
			"up": self.keyUp,
			"down": self.keyDown,
			"left": self.keyLeft,
			"right": self.keyRight,
			"cancel": self.exit,
			"red": self.exit,
			# "green": self.xPlugin,
			# "yellow": self.xInfo,
			# "blue": self.xBouquets,
			# "ok": self.keyOk,
			# "menu": self.keyMenu,
			}, -2)
		self["key_red"] = Label(_("Exit"))
		self["key_green"] = Label()
		self["key_yellow"] = Label(_("xtraInfo"))
		self["key_blue"] = Label()
		self["epgList"] = List([])
		self['description'] = Label()
		self['short_description'] = Label()
		self['imdb'] = Label()
		self['infos'] = Label()
		self['eventTime'] = Label()
		self["poster"] = Pixmap()
		self["picon"] = Pixmap()
		self["parentalRating"] = Pixmap()
		self["ratingStar"] = ProgressBar()
		# self.onLayoutFinish.append(self.eList)
		
	def eList(self, eRef):
		try:
			elst=[]
			events = ""
			# ref = self.session.nav.getCurrentlyPlayingServiceReference().toString()
			# open("/tmp/erf.txt","w").write("{}".format(eRef.toString()))
			# return
			self.eRef = eRef
			events = epgCache.lookupEvent(['IBDCTSERNX', (eRef.toString(), 1, -1, -1)])
			for i in range(len(events)):
				eventName = events[i][4]
				bt = localtime(events[i][1])
				beginTime = "%02d:%02d"%(bt[3], bt[4])
				eventDate = "%02d.%02d.%02d"%(bt[2], bt[1], bt[0])
				day, month, year = (int(x) for x in eventDate.split('.'))
				eventDay = (date(year, month, day)).strftime('%a')
				duration = "%dmin" % (events[i][2] // 60)
				try:
					sDesc = events[i][5]
				except:
					sDesc = ""
				try:
					eDesc = events[i][6]
				except:
					eDesc = ""
				fDesc = "{}\n{}".format(sDesc, eDesc)
				# img = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film.jpg"
				eRef = events[i][7]
				evntNm = REGEX.sub('', eventName).strip()
				img = "{}xtraEvent/backdropThumbnail/{}.jpg".format(pathLoc, evntNm)
				# eventImage = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film.jpg"
				if os.path.exists(img):
					eventImage = LoadPixmap(img)
				else:
					img = "/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film.jpg"
					# piconName = str(getPiconName(str(ServiceReference(eRef))))
					# open("/tmp/picnm", "w").write(str(piconName))
					eventImage = LoadPixmap(img)
				eInf = "{} ● {} ● {} ● {}".format(eventDay, eventDate, beginTime, duration)
				
				elst.append((eventImage, eventName, eventDay, eventDate, beginTime, duration, fDesc, eInf, eRef))
			# open("/tmp/elstt", "w").write(str(elst))
			self["epgList"].setList(elst)
			self["epgList"].show()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyLeft(self):
		try:
			self["epgList"].goLeft()
			indx = self["epgList"].getIndex()
			self.getEvent(indx)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
		
	def keyRight(self):
		try:
			self["epgList"].goRight()
			indx = self["epgList"].getIndex()
			self.getEvent(indx)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def keyUp(self):
		try:
			self["epgList"].up()
			indx = self["epgList"].getIndex()
			self.getEvent(indx)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
		
	def keyDown(self):
		try:
			self["epgList"].down()
			indx = self["epgList"].getIndex()
			self.getEvent(indx)
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)

	def getEvent(self, indx):
		try:
			event = None
			eventName= "N/A"
			ShortDescription = "N/A"
			ExtendedDescription = "N/A"
			ParentalData = "N/A"
			self["picon"].hide()
			# sref = self.session.nav.getCurrentlyPlayingServiceReference().toString()
			events = epgCache.lookupEvent(['IBDCTSERNX', (self.eRef.toString(), 1, -1, -1)])
			if events:
				i = int(indx)
				eventName = events[i][4]
				bt = localtime(events[i][1])
				beginTime = "%02d:%02d"%(bt[3], bt[4])
				eventDate = "%02d.%02d.%02d"%(bt[2], bt[1], bt[0])
				day, month, year = (int(x) for x in eventDate.split('.'))
				eventDay = (date(year, month, day)).strftime('%a')
				duration = "%dmin" % (events[i][2] // 60)
				try:
					ShortDescription = events[i][5]
				except:
					ShortDescription = ""
				try:
					ExtendedDescription = events[i][6]
				except:
					ExtendedDescription = ""
				fd = "\c0000????Description:\c00eeeeee{}\n{}".format(ShortDescription, ExtendedDescription)
				self['description'].setText(_(fd))
				self['description'].show()
				piconName = str(getPiconName(str(ServiceReference(self.eRef.toString()))))
				if os.path.exists(piconName):
					self["picon"].instance.setPixmapFromFile(piconName)
					self["picon"].instance.setScale(2)
					self["picon"].instance.show()
				else:
					self["picon"].hide()
				if eventName is None:
					return
				title = REGEX.sub('', eventName).strip()
				self.setTitle(_(title))
				pstrNm = "{}xtraEvent/poster/{}.jpg".format(pathLoc, title)
				rating_json = "{}xtraEvent/infos/{}.json".format(pathLoc, title)
				if os.path.exists(pstrNm):
					self["poster"].instance.setPixmapFromFile(pstrNm)
					self["poster"].instance.setScale(2)
					self["poster"].instance.show()
				else:
					self["poster"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film.jpg")
					self["poster"].instance.setScale(2)
					self["poster"].instance.show()
				imdbRating = ""
				imdbVotes = ""
				keyColor = "\c0000????"
				keyColorB = "\c00bbbbbb"
				if os.path.exists(rating_json):
					with open(rating_json) as f:
						read_json = json.load(f)
					try:
						imdbRating = read_json["imdbRating"]
					except:
						imdbRating = ""
					try:
						imdbVotes = read_json["imdbRatingVote"]
					except:
						imdbVotes = ""
					if imdbRating is not None:
						rtng = int(10 * float(imdbRating))
						self["ratingStar"].instance.setRange(0, 100)
						self["ratingStar"].instance.setValue(rtng)
						self["ratingStar"].instance.show()
					else:
						self["ratingStar"].hide()
					imdbRating = "\c0000????IMDB : \c00eeeeee{}({})".format(imdbRating, imdbVotes)
					self['imdb'].setText(imdbRating)
					self['imdb'].show()
				else:
					self["ratingStar"].hide()
					self["imdb"].hide()
				evnt=[]
				try:
					if "release_date" in str(read_json):
						rd = read_json["release_date"]
						evnt.append("{}ReleaseDate : {}{}".format(keyColor, keyColorB, rd))
				except:
					pass
				try:
					if "countries" in str(read_json):
						rd = read_json["countries"]
						evnt.append("{}Countries : {}{}".format(keyColor, keyColorB, rd))
				except:
					pass
				try:
					if "budget" in str(read_json):
						rd = read_json["budget"]
						evnt.append("{}Budget : {}{}".format(keyColor, keyColorB, rd))
				except:
					pass
				try:
					if "revenue" in str(read_json):
						rd = read_json["revenue"]
						evnt.append("{}Revenue : {}{}".format(keyColor, keyColorB, rd))
				except:
					pass
				try:
					prs = ['(\d+). Staffel, Folge (\d+)', 'T(\d+) Ep.(\d+)', '"Episodio (\d+)" T(\d+)', '(\d+).* \(odc. (\d+).*\)']
					for i in prs:
						seg = re.search(i, fd)
						if seg:
							s = seg.group(1).zfill(2)
							e = seg.group(2).zfill(2)
							evnt.append("{}SE : {}S{}E{}".format(keyColor, keyColorB, s, e))
				except:
					pass
				try:
					if "genre" in str(read_json):
						Genre = read_json["genre"]
						evnt.append("{}Genre : {}{}".format(keyColor, keyColorB, Genre))
					else:
						genres = event.getGenreDataList()
						if genres:
							genre = genres[0]
							evnt.append("{}Genre : {}{}".format(keyColor, keyColorB, getGenreStringSub(genre[0], genre[1])))
				except:
					pass
				try:
					if "duration" in str(read_json):
						Duration = read_json["duration"]
						evnt.append("{}Duration : {}{} min".format(keyColor, keyColorB, Duration))
					else:
						drtn = round(event.getDuration()// 60)
						if drtn > 0:
							evnt.append("{}Duration : {}{}min".format(keyColor, keyColorB, drtn))
						else:
							prs = re.findall(r' \d+ Min', fd)
							if prs:
								drtn = round(prs[0])
								evnt.append("{}Duration : {}{}min".format(keyColor, keyColorB, drtn))
				except:
					pass
				try:
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
					evnt.append("{}Rated : {}{}".format(keyColor, keyColorB, rate))
					tc = "\n".join(evnt)
					self['infos'].setText(tc)
					self['infos'].show()
					rate = str(rate).strip()
					getRate = pRating(rate)
					if rate is not None:
						rateNm = "{}FSK_{}.png".format(pratePath, getRate)
						self["parentalRating"].instance.setPixmapFromFile(rateNm)
						self["parentalRating"].instance.setScale(1)
						self["parentalRating"].instance.show()
					else:
						self["parentalRating"].instance.setPixmapFromFile("{}FSK_NA.png".format(pratePath))
						self["parentalRating"].instance.setScale(1)
						self["parentalRating"].instance.show()
				except:
					pass

				etm = ""
				try:st = event.getBeginTime()
				except:pass
				try:duration = event.getDuration()
				except:pass
				try:et = st + duration
				except:pass
				try:begin = localtime(st)
				except:pass
				try:end = localtime(et)
				except: pass
				try: startend = "%02d:%02d - %02d:%02d" % (begin[3], begin[4], end[3], end[4])
				except:pass
				try:etm = "\\c0000??80{} \\c00??????{} \\c00????ff({}min)".format(startend, event.getEventName(), duration // 60)
				except:pass
				self['eventTime'].setText(etm)
				self['eventTime'].show()
			else:
				self["parentalRating"].instance.setPixmapFromFile("{}FSK_NA.png".format(pratePath))
				self["parentalRating"].instance.setScale(1)
				self["parentalRating"].instance.show()
				self['eventTime'].hide()
				self["ratingStar"].hide()
				self['poster'].hide()
				self['description'].hide()
				self['imdb'].hide()
				self['infos'].hide()
		except Exception as err:
			from Tools.xtraTool import errorlog
			errorlog(err, __file__)
	
	def exit(self):
		self.close()

class infos(Screen):
	skin = '''
<screen name="infos" position="center,center" size="700,200" flags="wfNoBorder" backgroundColor="#50000000">
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
		self['info'].setText("© xtraChannelSelection {}\nby digiteng (2024)".format(version))





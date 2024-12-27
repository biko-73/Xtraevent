#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from Components.config import config, configfile, ConfigYesNo, ConfigSubsection, \
getConfigListEntry, ConfigSelection, ConfigText, ConfigInteger, ConfigSelectionNumber, \
ConfigDirectory, ConfigClock, NoSave
from Components.ConfigList import ConfigListScreen

try:
	import sys
	infoPY = sys.version_info[0]
	if infoPY == 3:
		from builtins import str
		from builtins import range
		from builtins import object
		from configparser import ConfigParser
		from _thread import start_new_thread
		from urllib.request import urlopen, Request, quote
	else:
		from ConfigParser import ConfigParser
		from thread import start_new_thread
		from urllib2 import urlopen, Request, quote
except Exception as err:
	from Tools.xtraTool import errorlog
	errorlog(err, __file__)


try:
	from Components.Language import language
	lang = language.getLanguage()
	lang = lang[:2]
except:
	try:
		lang = config.osd.language.value[:-3]
	except:
		lang = "en"

lang_path = r"/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/languages"
try:
	lng = ConfigParser()
	if infoPY == 3:
		lng.read(lang_path,	 encoding='utf8')
	else:
		lng.read(lang_path)
	lng.get(lang, "0")
except:
	try:
		lang="en"
		lng = ConfigParser()
		if infoPY == 3:
			lng.read(lang_path,	 encoding='utf8')
		else:
			lng.read(lang_path)
	except:
		lng.read(lang_path,	 encoding='utf8')

config.plugins.xtrvnt = ConfigSubsection()
config.plugins.xtrvnt.loc = ConfigDirectory(default='/')
config.plugins.xtrvnt.searchMOD = ConfigSelection(default = lng.get(lang, '14'), choices = [(lng.get(lang, '13')), (lng.get(lang, '14')), (lng.get(lang, '14a'))])
config.plugins.xtrvnt.searchNUMBER = ConfigSelectionNumber(0, 999, 1, default=0)
config.plugins.xtrvnt.timerMod = ConfigSelection(default="Disable", choices=[
	("Disable", "Disable"), 
	("Period", "Period"), 
	("Clock", "Clock"), 
	])
config.plugins.xtrvnt.timerHour = ConfigSelectionNumber(1, 168, 1, default=1)
config.plugins.xtrvnt.timerClock = ConfigClock(default=0)
config.plugins.xtrvnt.searchMANUELnmbr = ConfigSelectionNumber(0, 999, 1, default=1)
config.plugins.xtrvnt.searchMANUELyear = ConfigInteger(default = 0, limits=(0, 9999))
config.plugins.xtrvnt.imgNmbr = ConfigSelectionNumber(0, 999, 1, default=1)
config.plugins.xtrvnt.searchModManuel = ConfigSelection(default = lng.get(lang, '16'), choices = [(lng.get(lang, '16')), (lng.get(lang, '17'))])
config.plugins.xtrvnt.EMCloc = ConfigDirectory(default='/')
config.plugins.xtrvnt.apis = ConfigYesNo(default = False)
config.plugins.xtrvnt.tmdbAPI = ConfigText(default="", visible_width=100, fixed_size=False)
config.plugins.xtrvnt.tvdbAPI = ConfigText(default="", visible_width=100, fixed_size=False)
config.plugins.xtrvnt.omdbAPI = ConfigText(default="", visible_width=100, fixed_size=False)
config.plugins.xtrvnt.fanartAPI = ConfigText(default="", visible_width=100, fixed_size=False)
config.plugins.xtrvnt.searchMANUEL_EMC = ConfigText(default="movies name", visible_width=100, fixed_size=False)
config.plugins.xtrvnt.searchMANUEL = ConfigText(default="event name", visible_width=100, fixed_size=False)
config.plugins.xtrvnt.searchLang = ConfigYesNo(default = False)
config.plugins.xtrvnt.tmdb = ConfigYesNo(default = False)
config.plugins.xtrvnt.tmdb_poster = ConfigYesNo(default = False)
config.plugins.xtrvnt.tmdb_backdrop = ConfigYesNo(default = False)
config.plugins.xtrvnt.IMDB_backdrop_number = ConfigSelectionNumber(1, 99, 1, default=1)
config.plugins.xtrvnt.tmdb_info = ConfigYesNo(default = False)
config.plugins.xtrvnt.tmdb_cast = ConfigYesNo(default = False)
config.plugins.xtrvnt.tvdb = ConfigYesNo(default = False)
config.plugins.xtrvnt.tvdb_poster = ConfigYesNo(default = False)
config.plugins.xtrvnt.tvdb_backdrop = ConfigYesNo(default = False)
config.plugins.xtrvnt.tvdb_banner = ConfigYesNo(default = False)
config.plugins.xtrvnt.maze = ConfigYesNo(default = False)
config.plugins.xtrvnt.fanart = ConfigYesNo(default = False)
config.plugins.xtrvnt.fanart_poster = ConfigYesNo(default = False)
config.plugins.xtrvnt.fanart_backdrop = ConfigYesNo(default = False)
config.plugins.xtrvnt.fanart_banner = ConfigYesNo(default = False)
config.plugins.xtrvnt.bing = ConfigYesNo(default = False)
config.plugins.xtrvnt.extra = ConfigYesNo(default = False)
config.plugins.xtrvnt.extra2 = ConfigYesNo(default = False)
config.plugins.xtrvnt.poster = ConfigYesNo(default = False)
config.plugins.xtrvnt.banner = ConfigYesNo(default = False)
config.plugins.xtrvnt.backdrop = ConfigYesNo(default = False)
config.plugins.xtrvnt.info = ConfigYesNo(default = False)
config.plugins.xtrvnt.act = ConfigYesNo(default = False)
config.plugins.xtrvnt.cnfgSel = ConfigSelection(default = "poster", choices = [("poster"), ("banner"), ("backdrop"), ("EMC")])
config.plugins.xtrvnt.TMDB_poster_size = ConfigSelection(default="w185", choices = [
	("w92", "92x138"), 
	("w154", "154x231"), 
	("w185", "185x278"), 
	("w342", "342x513"), 
	("w500", "500x750"), 
	("w780", "780x1170"), 
	("original", "ORIGINAL")])
config.plugins.xtrvnt.TVDB_poster_size = ConfigSelection(default="thumbnail", choices = [
	("thumbnail", "340x500"), 
	("fileName", "original(680x1000)")])
config.plugins.xtrvnt.TMDB_backdrop_size = ConfigSelection(default="w300", choices = [
	("w300", "300x170"), 
	("w780", "780x440"), 
	("w1280", "1280x720"),
	("original", "ORIGINAL")])
config.plugins.xtrvnt.TVDB_backdrop_size = ConfigSelection(default="thumbnail", choices = [
	("thumbnail", "640x360"), 
	("fileName", "original(1920x1080)")])
config.plugins.xtrvnt.FANART_poster_size = ConfigSelection(default="4", choices = [
	("4", "250x356"), 
	("2", "500x713"), 
	("1", "1000x1426")])
config.plugins.xtrvnt.FANART_backdrop_size = ConfigSelection(default="2", choices = [
	("10", "100x56"), 
	("4", "250x140"),
	("2", "500x281"), 
	("1", "1000x562")])
config.plugins.xtrvnt.imdb_poster_size = ConfigSelection(default="185", choices = [
	("185", "185x278"), 
	("344", "344x510"), 
	("500", "500x750")])
config.plugins.xtrvnt.PB = ConfigSelection(default="posters", choices = [
	("posters", "Poster"), 
	("backdrops", "Backdrop")])
config.plugins.xtrvnt.srcs = ConfigSelection(default="TMDB", choices = [
	('TMDB', 'TMDB'), 
	('TVDB', 'TVDB'), 
	('FANART', 'FANART'), 
	('IMDB(poster)', 'IMDB(poster)'), 
	('Bing', 'Bing'), 
	('Google', 'Google')])
config.plugins.xtrvnt.searchType = ConfigSelection(default="tv", choices = [
	('tv', 'TV'), 
	('movie', 'MOVIE'), 
	('multi', 'MULTI')])
config.plugins.xtrvnt.FANART_search_type = ConfigSelection(default="tv", choices = [
	('tv', 'TV'),
	('movies', 'MOVIE')])
config.plugins.xtrvnt.TVDB_banner_size = ConfigSelection(default="1", choices = [
	("1", "758x140"), 
	("2", "379x70"),
	("4", "190x35")])
config.plugins.xtrvnt.FANART_banner_size = ConfigSelection(default="1", choices = [
	("1", "1000x185"), 
	("2", "500x92"),
	("4", "250x46"),
	("8", "125x23")
	])
config.plugins.xtrvnt.EXTRA_backdrop_size = ConfigSelection(default="android-image-840-473", choices = [
	("android-image-840-473", "840x473"),
	("android-image-640-360", "640x360"), 
	("android-image-480-270", "480x270"),  
	("android-image-320-180", "320x180"),  
	("android-image-240-135", "240x135"), 
	("android-image-110-62", "110x62"), 
	("android-image-83-47", "83x47"), 
	])
config.plugins.xtrvnt.trailer = ConfigSelection(default = "IMDB", choices = [("IMDB"), ("Youtube")])
config.plugins.xtrvnt.trailerQuality = ConfigSelection(default='maxRes', choices=[('sList', 'Selectable List'), ('maxRes', 'Maksimum Resolution')])
config.plugins.xtrvnt.trailerPlayer = ConfigSelection(default='4097', choices=[('4097', _('Default')), ('5002', _('Exteplayer3')), ('5001', _('Gstplayer'))])
config.plugins.xtrvnt.trailerPlay = ConfigSelection(default = "MoviePlayer", choices = [("MoviePlayer"), ("xtraPlayer")])
config.plugins.xtrvnt.xtraInf = ConfigYesNo(default = False)
config.plugins.xtrvnt.xtraInfoSource = ConfigSelection(default = "TMDB", choices = [("TMDB"), ("IMDB")])
config.plugins.xtrvnt.xtraInfoSourceSkinTMDB = ConfigSelection(default = "skin1", choices = [("skin1"), ("skin2"), ("skin3")])
config.plugins.xtrvnt.xtraInfoSourceSkinIMDB = ConfigSelection(default = "skin1", choices = [("skin1"), ("skin2")])
config.plugins.xtrvnt.xtraCast = ConfigYesNo(default = True)
config.plugins.xtrvnt.tmdb_cast_size = ConfigSelection(default="w92", choices = [
	("w92", "92x138"), 
	("w154", "154x231"), 
	("w185", "185x278"), 
	("w342", "342x513"), 
	("w500", "500x750")])
config.plugins.xtrvnt.tmdb_cast_number = ConfigSelectionNumber(0, 999, 5, default=10)
config.plugins.xtrvnt.xPoster = ConfigYesNo(default = False)
config.plugins.xtrvnt.infobarPosterSizeX = ConfigSelectionNumber(0, 1920, 5, default=185)
config.plugins.xtrvnt.infobarPosterPosX = ConfigSelectionNumber(0, 1920, 5, default=40)
config.plugins.xtrvnt.infobarPosterPosY = ConfigSelectionNumber(0, 1080, 5, default=400)
config.plugins.xtrvnt.backdropThumbnail = ConfigYesNo(default = False)
config.plugins.xtrvnt.backdropThumbnailSize = ConfigSelection(default="300,170", choices = [("300,170", "300x170"), ("100,60", "100x60")])
config.plugins.xtrvnt.infobarPosterPosX2 = ConfigSelectionNumber(0, 1920, 5, default=1700)
config.plugins.xtrvnt.infobarPosterPosY2 = ConfigSelectionNumber(0, 1080, 5, default=400)

try:
	tmdb_api = "3c3efcf47c3577558812bb9d64019d65"
	tvdb_api = "a99d487bb3426e5f3a60dea6d3d3c7ef"
	fanart_api = "6d231536dea4318a88cb2520ce89473b"
	if config.plugins.xtrvnt.tmdbAPI.value:
		tmdb_api = config.plugins.xtrvnt.tmdbAPI.value
	if config.plugins.xtrvnt.tvdbAPI.value:
		tvdb_api = config.plugins.xtrvnt.tvdbAPI.value
	if config.plugins.xtrvnt.fanartAPI.value:
		fanart_api = config.plugins.xtrvnt.fanartAPI.value
except Exception as err:
	from Tools.xtraTool import errorlog
	errorlog(err, __file__)


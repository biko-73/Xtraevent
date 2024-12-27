# -*- coding: utf-8 -*-
# by digiteng...04.2024
from __future__ import absolute_import
from Components.Converter.Converter import Converter
from Components.Element import cached
from Components.config import config
import re
import os
import json
from enigma import iPlayableService
from Components.Converter.Poll import Poll
from Tools.xtraTool import REGEX, pathLoc

class xtraInfo2(Poll, Converter):
	def __init__(self, type):
		Converter.__init__(self, type)
		Poll.__init__(self)
		self.type = type
		self.poll_interval = 1000
		self.poll_enabled = True

	@cached
	def getText(self):
		event = self.source.event
		if event:
			evnt = event.getEventName()
			evntNm = REGEX.sub('', evnt).strip()
			rating_json = "{}xtraEvent/infos/{}.json".format(pathLoc, evntNm)
			fd = "{}{}{}".format(event.getEventName(), event.getShortDescription(), event.getExtendedDescription())
			evnt = []
			if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
				rating_json = "{}xtraEvent/infos/{}.json".format(pathLoc, evntNm)
				if os.path.exists(rating_json):
					with open(rating_json) as f:
						read_json = json.load(f)
				else:
					return
				if str(self.type).startswith("\c"):
					keyColor = self.type.split(",")[0]
					keyColorB = self.type.split(",")[1]
				else:
					keyColor = "\c00??????"
					keyColorB = "\c00??????"
				try:
					if "\n" in self.type:
						if "Title" in self.type:
							try:
								titl = read_json["title"]
								evnt.append(titl)
							except:
								pass
						if "Description" in self.type:
							try:
								if "desc" in str(read_json):
									descr = read_json["desc"]
									evnt.append("{}Description :{}".format(keyColor, keyColorB))
									evnt.append(descr)
								else:
									evnt.append("{}Description :{}".format(keyColor, keyColorB))
									evnt.append(fd)
							except:
								pass
						if "Actors" in self.type:
							try:
								evnt.append("{}Actors :{}".format(keyColor, keyColorB))
								for i in range(len(read_json["actors"].keys())):
									actr = list(read_json["actors"].keys())[i]
									evnt.append("{}".format(actr))
							except:
								pass
						if "Crews" in self.type:
							try:
								evnt.append("{}Crews :{}".format(keyColor, keyColorB))
								for i in range(len(read_json["crews"].keys())):
									actr = list(read_json["crews"].keys())[i]
									evnt.append("{}".format(actr))
							except:
								pass
						if "Genre" in self.type:
							try:
								evnt.append("{}Genre :{}".format(keyColor, keyColorB))
								actr = read_json["genre"]
								evnt.append("{}".format(actr))
							except:
								pass
						tc = "\n".join(evnt)
						return tc
				except Exception as err:
					from Tools.xtraTool import errorlog
					errorlog(err, __file__)
				try:
					if "compact" in self.type:
						if "Genre" in self.type:
							try:
								# evnt.append("{}Genre :{}".format(keyColor, keyColorB))
								actr = read_json["genre"]
								evnt.append("{}".format(actr))
							except:
								pass
							
						if "Duration" in self.type:
							try:
								# evnt.append("{}Duration :{}".format(keyColor, keyColorB))
								actr = read_json["duration"]
								evnt.append("{}".format(actr))
							except:
								pass
						if "Rated" in self.type:
							try:
								# evnt.append("{}Rated :{}".format(keyColor, keyColorB))
								actr = read_json["rated"]
								evnt.append("{}".format(actr))
							except:
								pass
						if "Year" in self.type:
							try:
								# evnt.append("{}rYear :{}".format(keyColor, keyColorB))
								actr = read_json["release_date"]
								evnt.append("{}".format(actr))
							except:
								try:
									actr = read_json["AirDate"]
									evnt.append("{}".format(actr))
								except:
									pass
						if "Countries" in self.type:
							try:
								# evnt.append("{}rYear :{}".format(keyColor, keyColorB))
								actr = read_json["countries"]
								evnt.append("{}".format(actr))
							except:
								pass
						tc = " ● ".join(evnt)
						return tc
				except Exception as err:
					from Tools.xtraTool import errorlog
					errorlog(err, __file__)

			elif config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
				rating_json = "{}xtraEvent/imdb/casts/{}/{}_info.json".format(pathLoc, evntNm, evntNm)
				if os.path.exists(rating_json):
					with open(rating_json) as f:
						read_json = json.load(f)
				else:
					return
				if str(self.type).startswith("\c"):
					keyColor = self.type.split(",")[0]
					keyColorB = self.type.split(",")[1]
				else:
					keyColor = "\c00??????"
					keyColorB = "\c00??????"
				if "Title" in self.type:
					try:
						titl = read_json["orjTitle"]
						evnt.append("{}Original title : {}{}".format(keyColor, keyColorB, titl))
					except:
						pass
				if "Description" in self.type:
					try:
						descr = read_json["description"]
						evnt.append("{}Description :{}{}".format(keyColor, keyColorB, descr))
					except:
						pass
				if "Director" in self.type:
					try:
						dctr = read_json["director"]
						evnt.append("{}Director :{}{}".format(keyColor, keyColorB, dctr))
					except:
						pass

				if "Writers" in self.type:
					try:
						wctr = read_json["writer"]
						evnt.append("{}Writers :{}{}".format(keyColor, keyColorB, wctr))
					except:
						try:
							cctr = read_json["creators"]
							evnt.append("{}Creators :{}{}".format(keyColor, keyColorB, cctr))
						except:
							pass
				if "Actors" in self.type:
					try:
						actr = read_json["cast"]
						evnt.append("{}Actors :{}{}".format(keyColor, keyColorB, actr))
					except:
						pass
						
				if "Genre" in self.type:
					try:
						actr = read_json["genre"]
						evnt.append("{}".format(actr))
					except:
						pass
				if "Duration" in self.type:
					try:
						actr = read_json["duration"]
						evnt.append("{}".format(actr))
					except:
						pass
				if "Rated" in self.type:
					try:
						actr = read_json["rated"]
						evnt.append("{}".format(actr))
					except:
						pass
				if "releaseYear" in self.type:
					try:
						actr = read_json["releaseYear"]
						evnt.append("{}".format(actr))
					except:
						pass
				if " " in self.type:
					tc = "\n".join(evnt)
				elif "•" in self.type:
					tc = " • ".join(evnt)
				else:
					tc = " ".join(evnt)
				return tc
		else:
			return
	text = property(getText)
	
	def changed(self, what):
		if what[0] == self.CHANGED_POLL:
			Converter.changed(self, what)
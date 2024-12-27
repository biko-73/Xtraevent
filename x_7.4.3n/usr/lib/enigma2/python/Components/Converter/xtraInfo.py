# -*- coding: utf-8 -*-
# by digiteng...07.2020 - 11.2020 - 11.2021
# FOR INFO
# <widget source="session.Event_Now" render="Label" position="50,545" size="930,400" font="Regular; 32" halign="left" transparent="1" zPosition="2" backgroundColor="background">
	# <convert type="xtraInfo">Title,Year,Description</convert>
# </widget>
# 
# FOR IMDB RATING STAR...
# <ePixmap pixmap="xtra/star_b.png" position="990,278" size="200,20" alphatest="blend" zPosition="2" transparent="1" />
# <widget source="ServiceEvent" render="Progress" pixmap="xtra/star.png" position="990,278" size="200,20" alphatest="blend" transparent="1" zPosition="2" backgroundColor="background">
	# <convert type="xtraInfo">imdbRatingValue</convert>
# </widget>
from __future__ import absolute_import
from Components.Converter.Converter import Converter
from Components.Element import cached
from Components.config import config
from Components.Converter.xtraEventGenre import getGenreStringSub
import re
import json
import os
from Components.Converter.Poll import Poll
tc="n/a"
from Tools.xtraTool import REGEX, pathLoc

class xtraInfo(Poll, Converter):
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
			fd = "{}\n{}\n{}".format(event.getEventName(), event.getShortDescription(), event.getExtendedDescription())
			evnt = []
			if str(self.type).startswith("\c"):
				keyColor = self.type.split(",")[0]
				keyColorB = self.type.split(",")[1]
			else:
				keyColor = "\c00??????"
				keyColorB = "\c00??????"
			if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
				rating_json = "{}xtraEvent/infos/{}.json".format(pathLoc, evntNm)
				try:
					if os.path.exists(rating_json):
						with open(rating_json) as f:
							read_json = json.load(f)
					else:
						return
				except:
					return

				# keyColor = "\c0000??00"
				if self.type == "tmdbRatingFull":
					try:
						TMDBrating = int(read_json["tmdbRating"]) * 10
						TMDBvote = read_json["tmdbVote"]
						evnt.append("{}TMDB : {}{}%({})".format(keyColor, keyColorB, TMDBrating, TMDBvote))
					except:
						pass
				elif self.type == "tmdbRatingSimple":
					try:
						tmdbRating = read_json["tmdbRating"]
						evnt.append("{}".format(tmdbRating))
					except:
						pass
				elif self.type == "tmdbRating":
					try:
						tmdbRating = read_json["tmdbRating"]
						evnt.append("{}TMDB : {}{}".format(keyColor, keyColorB, tmdbRating))
					except:
						pass

				if "Title" in self.type:
					try:
						if "title" in str(read_json):
							title = read_json['title']
							evnt.append("{}Title : {}{}".format(keyColor, keyColorB, title))
					except:
						evnt.append("{}Title : {}{}".format(keyColor, keyColorB, event.getEventName()))
				if "Rated" in self.type:
					try:
						if "title" in str(read_json): 
							Rated = read_json["rated"]
							if Rated != None:
								evnt.append("{}Rated : {}{}".format(keyColor, keyColorB, Rated))
						if Rated == None:
							parentName = ''
							prs = ['[aA]b ((\d+))', '[+]((\d+))', 'Od lat: ((\d+))', '(\d+)[+]', '(TP)', '[-](\d+)']
							for i in prs:
								prr = re.search(i, fd)
								if prr:
									parentName = prr.group(1)
									parentName = parentName.replace('7', '6').replace('10', '12').replace('TP', '0')
									evnt.append("{}Rated : {}{}+".format(keyColor, keyColorB, parentName))
									break
							if parentName == '':
								try:
									age = ''
									rating = event.getParentalData()
									if rating:
										age = rating.getRating()
										evnt.append("{}Rated : {}{}+".format(keyColor, keyColorB, age))
								except:
									pass			
					except:
						pass
				if "Duration" in self.type:
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
				if "Genre" in self.type:
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
				if "SE" in self.type:
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
				if "ReleaseDate" in self.type:
					try:
						if "release_date" in str(read_json):
							rd = read_json["release_date"]
							evnt.append("{}ReleaseDate : {}{}".format(keyColor, keyColorB, rd))
					except:
						pass
				if "AirDate" in self.type:
					try:
						year = ''
						fd = fd.replace('(', '').replace(')', '')
						fdl = ['\d{4} [A-Z]+','[A-Z]*,.* \d{4}', '[A-Z]+ \d{4}', '[A-Z][a-z]+\s\d{4}', '\+\d+\s\d{4}']
						for i in fdl:
							year = re.findall(i, fd)
							if year:
								year = re.sub(r'\(.*?\)|\.|\+\d+', ' ', year[0]).strip()
								evnt.append("{}AirDate : {}{}".format(keyColor, keyColorB, year))
								break
					except:
						pass
				if "Budget" in self.type:
					try:
						if "budget" in str(read_json):
							rd = read_json["budget"]
							evnt.append("{}Budget : {}{}".format(keyColor, keyColorB, rd))
					except:
						pass
				if "Revenue" in self.type:
					try:
						if "revenue" in str(read_json):
							rd = read_json["revenue"]
							evnt.append("{}Revenue : {}{}".format(keyColor, keyColorB, rd))
					except:
						pass
				if "Countries" in self.type:
					try:
						if "countries" in str(read_json):
							rd = read_json["countries"]
							evnt.append("{}Countries : {}{}".format(keyColor, keyColorB, rd))
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
					# self.poll_interval = 1000
					# self.poll_enabled = True
				if "Actors" in self.type:
					try:
						evnt.append("{}Actors :{}".format(keyColor, keyColorB))
						for i in range(len(read_json["actors"].keys())):
							actr = list(read_json["actors"].keys())[i]
							evnt.append("{}".format(actr))
					except:
						pass
				if "Director" in self.type:
					try:
						if "director" in str(read_json):
							rd = read_json["director"]
							evnt.append("{}Director : {}{}".format(keyColor, keyColorB, rd))
						elif "creator" in str(read_json):
							rd = read_json["creator"]
							evnt.append("{}Creator : {}{}".format(keyColor, keyColorB, rd))
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
				# tc = '\\c0000??00 '
				# tc += '\n\\c00??????'
				# tc = tc.join(evnt)
				if " " in self.type:
					tc = "\n".join(evnt)
				elif "•" in self.type:
					tc = " • ".join(evnt)
				else:
					tc = "...".join(evnt)
				return tc

			elif config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
				rating_json = "{}xtraEvent/imdb/casts/{}/{}_info.json".format(pathLoc, evntNm, evntNm)
				if os.path.exists(rating_json):
					with open(rating_json) as f:
						read_json = json.load(f)
				else:
					return
				if self.type == "imdbRating":
					try:
						IMDBrating = read_json["rating"]
						IMDBvote = read_json["ratingVote"]
						evnt = "{}IMDB : {}{}({})".format(keyColor, keyColorB, IMDBrating, IMDBvote)
					except:
						pass
				if self.type == "imdbRating2":
					try:
						imdbRating = read_json["rating"]
						imdbVotes = read_json["ratingVote"]
						evnt = "{}\n{}".format(imdbRating, imdbVotes)
					except:
						pass
				# elif "imdbRatingSimple" in self.type:
					# try:
						# imdbRating = read_json["rating"]
						# evnt.append("{}".format(imdbRating))
					# except:
						# pass
				# elif "iRating" in self.type:
					# try:
						# imdbRating = read_json["rating"]
						# evnt.append("{}IMDB : {}{}".format(keyColor, keyColorB, imdbRating))
					# except:
						# pass
					# tc = " ".join(evnt)
				return evnt

		else:
			return
	text = property(getText)

	@cached
	def getValue(self):
		event = self.source.event
		if event:
			evnt = event.getEventName()
			evntNm = REGEX.sub('', evnt).strip()
			if config.plugins.xtrvnt.xtraInfoSource.value == "TMDB":
				rating_json = "{}xtraEvent/infos/{}.json".format(pathLoc, evntNm)
			elif config.plugins.xtrvnt.xtraInfoSource.value == "IMDB":
				rating_json = "{}xtraEvent/imdb/casts/{}/{}_info.json".format(pathLoc, evntNm, evntNm)
			if os.path.exists(rating_json):
				with open(rating_json) as f:
					read_json = json.load(f)
				try:
					if self.type == "imdbRatingValue":
						try:
							imdbRatingValue = read_json["rating"]
							if imdbRatingValue:
								return int(10*(float(imdbRatingValue)))
							else:
								return 0
						except:
							return 0
					elif self.type == "tmdbRatingValue":
						try:
							tmdbRatingValue = read_json["tmdbRating"]
							if tmdbRatingValue:
								return int(10*(float(tmdbRatingValue)))
							else:
								return 0
						except:
							return 0
				except:
					return 0
		else:
			return 0
		# self.poll_interval = 1000
		# self.poll_enabled = True
	value = property(getValue)
	range = 100
	def changed(self, what):
		if what[0] == self.CHANGED_POLL:
			Converter.changed(self, what)

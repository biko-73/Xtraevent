# by digiteng...10.2020, 02.2022, 08.2022

from Components.Converter.Converter import Converter
from Components.Element import cached
from time import time, localtime
from Components.Converter.Poll import Poll

class xtraEventInfo(Poll, Converter):

	def __init__(self, type):
		Converter.__init__(self, type)
		Poll.__init__(self)
		self.type = type
		self.poll_interval = 1000
		self.poll_enabled = True
		
	@cached
	def getText(self):
		event = None
		progres = None
		event = self.source.event
		if event is None:
			return "No Event Information"
		st = event.getBeginTime()
		duration = event.getDuration()
		et = st + duration
		now = int(time())
		remaining = et - now
		progressing = now - st
		begin = localtime(st)
		end = localtime(et)
		startend = "%02d:%02d - %02d:%02d" % (begin[3], begin[4], end[3], end[4])
		# progres = int(progressing * 100 // duration)

		if self.type == "EventName":
			return event.getEventName()
		elif self.type == "ShortDescription":
			return event.getShortDescription()
		elif self.type == "ExtendedDescription":
			return event.getExtendedDescription()
		elif self.type == "FullDescription":
			return "{}\n{}".format(event.getShortDescription(), event.getExtendedDescription())

		elif self.type == "Duration":
			return "{}min".format(str(duration // 60))
		elif self.type == "Remaining":
			return "{}min".format(str(remaining // 60))
		elif self.type == "Progressing":
			return "{}min".format(progressing // 60)
		elif self.type == "RemainingDuration":
			return "{}/{}min".format(remaining // 60, duration // 60)
		elif self.type == "ProgressingDuration":
			return "({} / {}min)".format(progressing // 60, duration // 60)
		elif self.type == "StartEndTime":
			begin = localtime(st)
			end = localtime(et)
			return "%02d:%02d - %02d:%02d" % (begin[3], begin[4], end[3], end[4])

		elif self.type == "EventNameCompact":
			return "\\c0000??80{} \\c00??????{} \\c00????ff({}min)".format(startend, event.getEventName(), duration // 60)
		elif self.type == "EventNameCompactShort":
			begin = localtime(st)
			startend = "%02d:%02d" % (begin[3], begin[4])	
			return "\\c0000??80{}-\\c00??????{}".format(startend, event.getEventName())
		elif self.type == "BeginEndTime":
			return startend
	text = property(getText)

	def changed(self, what):
		if what[0] != self.CHANGED_SPECIFIC:
			Converter.changed(self, what)


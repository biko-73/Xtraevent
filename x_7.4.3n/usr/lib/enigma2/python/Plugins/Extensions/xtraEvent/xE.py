# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from importlib import reload

class xe(Screen):
	skin = """
	<screen position="center,center" size="700,200" title="" flags="wfNoBorder" backgroundColor="#222230">
		<eLabel name="r" position="0,0" size="160,10" transparent="0" backgroundColor="#ef4c4c" />
		<widget name="infox" position="0,0" size="700,200" transparent="1" font="Regular; 30" foregroundColor="#cccccc" backgroundColor="#202d33" halign="center" valign="center" zPosition="1" />
	</screen>
	"""

	def __init__(self, session):
		Screen.__init__(self, session)
		self.session = session

		self["actions"] = ActionMap(["xtraEventAction"], 
		{
			"ok": self.noActv,
			"red": self.exit,
			"cancel": self.exit,
		}, -1)
		self['infox'] = Label()
		self.onLayoutFinish.append(self.noActv)

	def noActv(self):
		try:
			self['infox'].setText("Contact,\nhttps://www.patreon.com/digiteng")
			self['infox'].show()
		except Exception as err:from Tools.xtraTool import errorlog;errorlog(err,__file__)

	def exit(self):
		from Plugins.Extensions.xtraEvent import xm
		reload(xm)
		self.close()
		
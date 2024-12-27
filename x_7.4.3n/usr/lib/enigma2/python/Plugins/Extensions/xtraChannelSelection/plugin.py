# -*- coding: utf-8 -*-

from Plugins.Plugin import PluginDescriptor
from Components.config import config, configfile
from six.moves import reload_module
from .skins import xCHSkins
# from .skins import xch_config
from . import xtraChannelSelection
import os
from enigma import addFont
addFont("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/fonts/arial.ttf", "xtraRegular", 100, 1)
addFont("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/fonts/arialbd.ttf", "xtraBold", 100, 1)
addFont("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/fonts/xFont.ttf", "xtraIcons", 100, 1)
addFont("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/fonts/xtraicons.ttf", "xtraIcons2", 100, 1)
try:
	if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/plugin.pyc"):
		os.system("rm -fv /usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/plugin.py")
	if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/xtraChannelSelection.pyc"):
		os.system("rm -fv /usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/xtraChannelSelection.py")
	if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/skins/xCHSkins.pyc"):
		os.system("rm -fv /usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/skins/xCHSkins.py")
	if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/skins/xch_config.pyc"):
		os.system("rm -fv /usr/lib/enigma2/python/Plugins/Extensions/xtraChannelSelection/xch_config.py")
except:
	pass
try:
	mc = "N/A"
	mc = os.popen("ifconfig eth0 | awk '/HWaddr/ {printf $5}'").read()
except:
	pass
def main(session, **kwargs):
	try:
		reload_module(xCHSkins)
		# reload_module(xch_config)
		reload_module(xtraChannelSelection)
		from Plugins.Extensions.xtraEvent.xm import apr
		if mc in apr:
			session.open(xtraChannelSelection.xtraChannelSelection)
		else:
			from Plugins.Extensions.xtraEvent import xE
			session.open(xE.xe)
	except Exception as err:
		from Tools.xtraTool import errorlog
		errorlog(err, __file__)

def Plugins(**kwargs):
	plist = []
	plist.append(PluginDescriptor(name="xtraChannelSelection {}".format(xtraChannelSelection.version), description="xtraChannelSelection...", where = PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main))
	return plist
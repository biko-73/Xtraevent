
import os
from Components.config import config
from ..xch_config import *
imgr = ""
img = "/etc/issue"
if os.path.exists(img):
	with open(img, "r") as f:
		imgr = f.read().lower()
prgrs = ""
try:
	prgrsColor = "%s" %config.plugins.xCH.prgrsColor.value
	prgrsColor1 = "%s" %config.plugins.xCH.prgrsColor1.value
	prgrsColor2 = "%s" %config.plugins.xCH.prgrsColor2.value
	prgrsColor3 = "%s" %config.plugins.xCH.prgrsColor3.value
	psx, psy = 300, 170
	ph = 5
	# ph = int(config.plugins.xCH.ProgressHeight.value)
	if config.plugins.xCH.Images.value == "Backdrop":
		if config.plugins.xCH.style.value == "horizontal" or config.plugins.xCH.style.value == "horizontal_2":	  
			psx, psy = 220, 132
		elif config.plugins.xCH.style.value == "vertical" or config.plugins.xCH.style.value == "vertical_3":
			psx, psy = 100, 60
		elif config.plugins.xCH.style.value == "vertical_2":
			psx, psy = 190,102
	elif config.plugins.xCH.Images.value == "Poster":
		if config.plugins.xCH.style.value == "vertical":
			psx, psy = 40, 60
		elif config.plugins.xCH.style.value == "vertical_2" or config.plugins.xCH.style.value == "vertical_3":
			psx, psy = 60, 90
		elif config.plugins.xCH.style.value == "horizontal" or config.plugins.xCH.style.value == "horizontal_2":
			psx, psy = 100, 150
		# elif config.plugins.xCH.style.value == "horizontal_3":
			# psx, psy = 185, 278
	elif config.plugins.xCH.Images.value == "Picon":
		if config.plugins.xCH.style.value == "grid":	  
			psx, psy = 220, 132
		elif config.plugins.xCH.style.value == "vertical" or config.plugins.xCH.style.value == "vertical_2" or config.plugins.xCH.style.value == "vertical_3":
			psx, psy = 100, 60
		elif config.plugins.xCH.style.value == "horizontal" or config.plugins.xCH.style.value == "horizontal_2":
			psx, psy = 220, 132
		# elif config.plugins.xCH.style.value == "horizontal_3":
			# psx, psy = 190, 102

	if config.plugins.xCH.style.value == "vertical":
		chNm = 'MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = ("%d","%d"), png = 0, flags = BT_KEEP_ASPECT_RATIO | BT_HALIGN_CENTER | BT_SCALE, cornerRadius=10)'%(psx, psy)
		if config.plugins.xCH.ProgressColor.value == "Color":
			prgrsColor1 = ""
			prgrsColor2 = ""
			prgrsColor3 = ""
		prgrs = 'MultiContentEntryProgress(pos=(120,67), size=(900,7), percent=-3, borderWidth=0, foreColor="%s", foreColorSelected="%s", startColor="%s", midColor="%s", endColor="%s", cornerRadius=10, cornerEdges=15)'%(prgrsColor, prgrsColor, prgrsColor1, prgrsColor2, prgrsColor3)
		if config.plugins.xCH.Images.value == "Poster":
			chNm = 'MultiContentEntryPixmap(pos = (10,10), size = ("%d","%d"), png = 0, flags =	 BT_SCALE, cornerRadius=10)'%(psx, psy)
	elif config.plugins.xCH.style.value == "vertical_2":
		chNm = 'MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = ("%d","%d"), png = 0, flags = BT_KEEP_ASPECT_RATIO | BT_HALIGN_CENTER | BT_SCALE, cornerRadius=10)'%(psx, psy)
		if config.plugins.xCH.ProgressColor.value == "Color":
			prgrsColor1 = ""
			prgrsColor2 = ""
			prgrsColor3 = ""
		prgrs = 'MultiContentEntryProgress(pos=(10,160), size=(180,2), percent=-3, borderWidth=0, foreColor="%s", foreColorSelected="%s", startColor="%s", midColor="%s", endColor="%s", cornerRadius=10, cornerEdges=15)'%(prgrsColor, prgrsColor, prgrsColor1, prgrsColor2, prgrsColor3)
		if config.plugins.xCH.Images.value == "Poster":
			chNm = 'MultiContentEntryPixmap(pos = (65,10), size = ("%d","%d"), png = 0, flags = BT_SCALE, cornerRadius=10)'%(psx, psy)
	elif config.plugins.xCH.style.value == "vertical_3":
		chNm = 'MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = ("%d","%d"), png = 0, flags = BT_KEEP_ASPECT_RATIO | BT_HALIGN_CENTER | BT_SCALE, cornerRadius=10)'%(psx, psy)
		if config.plugins.xCH.ProgressColor.value == "Color":
			prgrsColor1 = ""
			prgrsColor2 = ""
			prgrsColor3 = ""
		prgrs = 'MultiContentEntryProgress(pos=(487,19), size=(165,7), percent=-3, borderWidth=0, foreColor="%s", foreColorSelected="%s", startColor="%s", midColor="%s", endColor="%s", cornerRadius=10, cornerEdges=15)'%(prgrsColor, prgrsColor, prgrsColor1, prgrsColor2, prgrsColor3)
		if config.plugins.xCH.Images.value == "Poster":
			chNm = 'MultiContentEntryPixmap(pos = (10,10), size = ("%d","%d"), png = 0, flags =	 BT_SCALE, cornerRadius=10)'%(psx, psy)
	elif config.plugins.xCH.style.value == "horizontal":
		chNm = 'MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = ("%d","%d"), png = 0, flags = BT_KEEP_ASPECT_RATIO | BT_HALIGN_CENTER | BT_SCALE, cornerRadius=10)'%(psx, psy)
		if config.plugins.xCH.ProgressColor.value == "Color":
			prgrsColor1 = ""
			prgrsColor2 = ""
			prgrsColor3 = ""
		prgrs = 'MultiContentEntryProgress(pos=(10,242), size=(200,10), percent=-3, borderWidth=0, foreColor="%s", foreColorSelected="%s", startColor="%s", midColor="%s", endColor="%s", cornerRadius=10, cornerEdges=15)'%(prgrsColor, prgrsColor, prgrsColor1, prgrsColor2, prgrsColor3)
		if config.plugins.xCH.Images.value == "Poster":
			chNm = 'MultiContentEntryPixmap(pos = (70,10), size = ("%d","%d"), png = 0, flags = BT_SCALE, cornerRadius=10)'%(psx, psy)
	elif config.plugins.xCH.style.value == "horizontal_3":
		chNm = 'MultiContentEntryPixmapAlphaBlend(pos = (0,0), size = (185,278), png = 0, flags = BT_SCALE, cornerRadius=10)'
		if config.plugins.xCH.ProgressColor.value == "Color":
			prgrsColor1 = ""
			prgrsColor2 = ""
			prgrsColor3 = ""
		prgrs = 'MultiContentEntryProgress(pos=(10,335), size=(165,7), percent=-3, borderWidth=0, foreColor="%s", foreColorSelected="%s", startColor="%s", midColor="%s", endColor="%s", cornerRadius=10, cornerEdges=15)'%(prgrsColor, prgrsColor, prgrsColor1, prgrsColor2, prgrsColor3)
	elif config.plugins.xCH.style.value == "grid":
		chNm = 'MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = ("%d", "%d"), png = 0, flags = BT_KEEP_ASPECT_RATIO | BT_HALIGN_CENTER | BT_SCALE, cornerRadius=10)'%(psx, psy)
		if config.plugins.xCH.ProgressColor.value == "Color":
			prgrsColor1 = ""
			prgrsColor2 = ""
			prgrsColor3 = ""
		prgrs = 'MultiContentEntryProgress(pos=(12,235), size=(300,7), percent=-3, borderWidth=0, foreColor="%s", foreColorSelected="%s", startColor="%s", midColor="%s", endColor="%s", cornerRadius=10, cornerEdges=15)'%(prgrsColor, prgrsColor, prgrsColor1, prgrsColor2, prgrsColor3)
	elif config.plugins.xCH.style.value == "horizontal_2":
		if config.plugins.xCH.ProgressColor.value == "Color":
			prgrsColor1 = ""
			prgrsColor2 = ""
			prgrsColor3 = ""
		prgrs = 'MultiContentEntryProgress(pos=(10,242), size=(200,10), percent=-3, borderWidth=0, foreColor="%s", foreColorSelected="%s", startColor="%s", midColor="%s", endColor="%s", cornerRadius=10, cornerEdges=15)'%(prgrsColor, prgrsColor, prgrsColor1, prgrsColor2, prgrsColor3)
except Exception as err:
	from Tools.xtraTool import errorlog
	errorlog(err, __file__)

xtraCh_Ver_1080 = """
<screen name="xtraChannelSelection" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
	<widget source="Title" render="Label" position="60,53" size="1118,60" font="xtraRegular; 45" foregroundColor="#c5c5c5" backgroundColor="#15202b" transparent="1" />
	<widget source="chList" render="Listbox" position="63,136" size="1120,780" backgroundColor="#15202b" itemGradientSelected="#1b4765,#1b4765,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" scrollbarWidth="2" enableWrapAround="1" itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="1200,85" spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showAlways" listOrientation="vertical" scrollbarForegroundColor="#0089fa" transparent="1" zPosition="99">
		<convert type="TemplatedMultiContent">
					{"template": [
					%s,
					MultiContentEntryText(pos = (120,10), size = (1000,30), font=4, flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), # ch name
					MultiContentEntryText(pos = (120,37), size = (1000,30), font=1, flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), # event name
					MultiContentEntryPixmapAlphaBlend(pos = (110,58), size = (920,25), png = 9, flags = BT_SCALE),
					%s,
					MultiContentEntryText(pos = (920,40), size = (100,30), font=1, flags = RT_HALIGN_RIGHT, text = 6, color="#0000ffff", color_sel="#0000ffff"), # percent
					MultiContentEntryText(pos=(520,10), size=(500,30), font=3, flags=RT_HALIGN_RIGHT, text=8, color="#00ffffff", color_sel="#00ffffff"),
					],
					"fonts": [gFont("xtraRegular", 20), gFont("xtraRegular", 18), gFont("xtraRegular", 12), gFont("xtraIcons2", 20), gFont("xtraBold", 20)],
					"itemWidth" : 1100,
					"itemHeight" : 80
					}
					</convert>
	</widget>
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<widget name="description" position="1260,500" size="600,250" transparent="1" font="xtraRegular;18" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="poster" position="1260,130" size="185,278" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget name="ratingStar" position="1260,412" size="200,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star.png" transparent="1" zPosition="2" alphatest="blend" />
	<ePixmap position="1260,412" size="200,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star_back.png" transparent="1" zPosition="1" alphatest="blend" />
	<widget name="imdb" position="1471,410" size="400,22" transparent="1" font="xtraRegular;18" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="infos" position="1460,130" size="400,278" transparent="1" font="xtraRegular;18" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="eventTime" position="1260,450" size="600,26" transparent="1" font="xtraRegular;22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="parentalRating" position="1384,346" size="60,60" alphatest="blend" zPosition="5" transparent="1" />
	<widget name="primeTime" position="1570,760" size="300,170" transparent="1" font="xtraRegular; 24" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="9" />
	<widget name="primeTimeBackdrop" position="1260,760" size="300,170" transparent="1" alphatest="off" zPosition="9" cornerRadius="20" scale="stretch" />
	<eLabel name="menu" text="" position="1272,975" size="40,40" backgroundColor="#15202b" transparent="1" halign="left" font="xtraIcons2; 20" />
	<eLabel name="infox" text="" position="1807,968" size="40,40" backgroundColor="#15202b" transparent="1" halign="right" font="xtraIcons2; 30" />
</screen>
"""%(chNm, prgrs)

xtraCh_Ver_1080_2 = """
<screen name="xtraChannelSelection" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">

<widget source="chList" render="Listbox" position="10,10" size="207,1030" backgroundColor="#15202b" itemGradientSelected="#1b4765,#25648d,horizontal" 
borderWidth="0" borderColor="green" scrollbarLength="auto" scrollbarWidth="2" enableWrapAround="1" itemCornerRadius="10" 
itemAlignment="center" cornerRadius="10" selectionZoomSize="1200,85" spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" 
scrollbarMode="showNever" listOrientation="vertical" scrollbarForegroundColor="#0089fa" transparent="1" zPosition="99">
<convert type="TemplatedMultiContent">
			{"template": [
			%s,
			MultiContentEntryText(pos = (10,120), size = (200,20), font=0, flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), # ch name
			MultiContentEntryText(pos = (10,140), size = (200,20), font=1, flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), # event name
			%s,
			# MultiContentEntryProgress(pos=(10,160), size=(180,2), percent=-3, borderWidth=0, foreColor="#0089fa", foreColorSelected="#0089fa", backColor="#222222", backColorSelected="#222222", startColor="#0089fa", midColor="#ff0000", endColor="#00dd00", startColorSelected="#0089fa", midColorSelected="#ff0000", endColorSelected="#00dd00", cornerRadius=10, cornerEdges=15), # Progress
			# MultiContentEntryText(pos = (90,40), size = (100,30), font=1, flags = RT_HALIGN_RIGHT, text = 6, color="#0000ffff", color_sel="#0000ffff"), # percent
			],
			"fonts": [gFont("xtraRegular", 16), gFont("xtraRegular", 12)],
			"itemWidth" : 207,
			"itemHeight" : 165
			}
			</convert>
</widget>

<eLabel backgroundColor="#ff8080" cornerRadius="20" position="150,1058" size="10,10" transparent="0" zPosition="1" />
<eLabel backgroundColor="#84ff80" cornerRadius="20" position="475,1058" size="10,10" transparent="0" zPosition="1" />
<eLabel backgroundColor="#ffee80" cornerRadius="20" position="800,1058" size="10,10" transparent="0" zPosition="1" />
<eLabel backgroundColor="#80e8ff" cornerRadius="20" position="1125,1058" size="10,10" transparent="0" zPosition="1" />
<widget name="key_red" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="170,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
<widget name="key_green" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="495,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
<widget name="key_yellow" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="820,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
<widget name="key_blue" render="Label" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1145,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
<eLabel name="" text="" position="1450,1050" size="30,30" foregroundColor="#00bbbbbb" backgroundColor="#50000000" transparent="1" font="xtraIcons; 26 " zPosition="99" />
<eLabel name="" text="Setup" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1485,1050" size="100,30" halign="left" transparent="1" zPosition="9" />


</screen>
"""%(chNm, prgrs)
	# <eLabel backgroundColor="#15202b" cornerRadius="20" position="40,40" size="700,1000" transparent="0" zPosition="0" />
	# <eLabel backgroundColor="#15202b" cornerRadius="20" position="780,40" size="1100,1000" transparent="0" zPosition="0" />
xtraCh_Ver_1080_3 = """
<screen name="xtraChannelSelection" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
    <eLabel backgroundColor="#1e2e3d" cornerRadius="20" position="40,40" size="700,1000" transparent="0" zPosition="0" />
	<eLabel backgroundColor="#15202b" cornerRadius="20" position="780,40" size="1100,1000" transparent="0" zPosition="0" />
	<widget source="Title" render="Label" cornerRadius="20" position="50,50" size="680,60" font="Regular; 30" foregroundColor="#c5c5c5" backgroundColor="#0c1319" halign="center" valign="center" transparent="0" zPosition="3" />
	<widget source="chList" render="Listbox" position="50,125" size="680,880" backgroundColor="#15202b" itemGradientSelected="#1b4765,#1b4765,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" scrollbarWidth="2" enableWrapAround="1" itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="1200,85" spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showAlways" listOrientation="vertical" scrollbarForegroundColor="#0089fa" transparent="1" zPosition="99">
		<convert type="TemplatedMultiContent">
			{"template": [
			%s,
			MultiContentEntryText(pos = (120,10), size = (400,30), font=4, flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), # ch name
			MultiContentEntryText(pos = (120,37), size = (400,30), font=1, flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), # event name
			MultiContentEntryPixmapAlphaBlend(pos = (480,10), size = (175,25), png = 9, flags = BT_SCALE),
			%s,
			MultiContentEntryText(pos = (550,40), size = (100,30), font=1, flags = RT_HALIGN_RIGHT, text = 6, color="#0000ffff", color_sel="#0000ffff"), # percent
			MultiContentEntryText(pos=(520,10), size=(500,30), font=3, flags=RT_HALIGN_RIGHT, text=8, color="#00ffffff", color_sel="#00ffffff"),
			],
			"fonts": [gFont("xtraRegular", 20), gFont("xtraRegular", 18), gFont("xtraRegular", 12), gFont("xtraIcons2", 20), gFont("xtraBold", 20)],
			"itemWidth" : 680,
			"itemHeight" : 80
			}
			</convert>
	</widget>

	<widget source="global.CurrentTime" render="Label" position="1683,0" size="200,45" font="xtraRegular; 38" valign="center" halign="right" transparent="1" foregroundColor="#111122" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<widget name="description" position="800,440" size="1060,300" transparent="1" font="Regular; 26" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="poster" position="800,60" size="185,278" transparent="1" alphatest="off" zPosition="2" cornerRadius="20" scale="stretch" />
	<widget name="ratingStar" position="800,350" size="200,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star.png" transparent="1" zPosition="2" alphatest="blend" />
	<ePixmap position="800,350" size="200,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star_back.png" transparent="1" zPosition="1" alphatest="blend" />
	<widget name="imdb" position="1009,350" size="400,22" transparent="1" font="xtraRegular;18" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="infos" position="1000,61" size="500,278" transparent="1" font="Regular; 22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="eventTime" position="801,400" size="600,26" transparent="1" font="xtraRegular;22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="parentalRating" position="925,271" size="60,60" alphatest="blend" zPosition="5" transparent="1" />
	<widget name="primeTime" position="1560,250" size="300,170" transparent="1" font="Regular; 22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="9" />
	<widget name="primeTimeBackdrop" position="1565,60" size="300,170" transparent="1" alphatest="off" zPosition="9" cornerRadius="20" scale="stretch" />
	<widget name="Backdrop1" position="800,800" size="250,140" transparent="1" alphatest="off" zPosition="9" cornerRadius="20" scale="stretch" />
	<widget name="Backdrop2" position="1070,800" size="250,140" transparent="1" alphatest="off" zPosition="9" cornerRadius="20" scale="stretch" />
	<widget name="Backdrop3" position="1340,800" size="250,140" transparent="1" alphatest="off" zPosition="9" cornerRadius="20" scale="stretch" />
	<widget name="Backdrop4" position="1610,800" size="250,140" transparent="1" alphatest="off" zPosition="9" cornerRadius="20" scale="stretch" />
	<widget name="BackdropNm1" position="800,950" size="250,80" transparent="1" font="Regular; 22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="9" />
	<widget name="BackdropNm2" position="1070,950" size="250,80" transparent="1" font="Regular; 22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="9" />
	<widget name="BackdropNm3" position="1340,950" size="250,80" transparent="1" font="Regular; 22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="9" />
	<widget name="BackdropNm4" position="1610,950" size="250,80" transparent="1" font="Regular; 22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="9" />

	<eLabel name="infox" text="" position="1840,1043" size="30,30" foregroundColor="#00bbbbbb" backgroundColor="#15202b" transparent="1" halign="right" font="xtraIcons2; 30" zPosition="2" />
	<eLabel backgroundColor="#ff8080" cornerRadius="20" position="150,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#84ff80" cornerRadius="20" position="475,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#ffee80" cornerRadius="20" position="800,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#80e8ff" cornerRadius="20" position="1125,1058" size="10,10" transparent="0" zPosition="1" />
	<widget name="key_red" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="170,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="495,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="820,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1145,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<eLabel name="" text="" position="1450,1050" size="30,30" foregroundColor="#00bbbbbb" backgroundColor="#50000000" transparent="1" font="xtraIcons; 26 " zPosition="99" />
	<eLabel name="" text="Setup" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1485,1050" size="100,30" halign="left" transparent="1" zPosition="9" />

</screen>
"""%(chNm, prgrs)

xtraCh_Grid_1080 = """
<screen position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="#50000000">
	<widget source="chList" render="Listbox" position="0,0" size="1920,1080" backgroundColor="#15202b" 
	itemGradientSelected="#1b4765,#25648d,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" 
	scrollbarWidth="2" enableWrapAround="1"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="330,257" 
	spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showAlways" listOrientation="grid" 
	scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="0">
	  <convert type="TemplatedMultiContent">
			{"template": [
			%s,
			MultiContentEntryText(pos = (10,180), size = (300,30), font=2, flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), # ch name
			MultiContentEntryText(pos = (10,210), size = (300,30), font=1, flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), # event name
			MultiContentEntryPixmapAlphaBlend(pos = (0,225), size = (320,25), png = 9, flags = BT_SCALE),
			# MultiContentEntryProgress(pos=(12,235), size=(300,7), percent=-3, borderWidth=0, foreColor="#0089fa", foreColorSelected="#0089fa", backColor=None, backColorSelected=None, startColor="#0089fa", midColor="#ff0000", endColor="#00dd00", startColorSelected="#0089fa", midColorSelected="#ff0000", endColorSelected="#00dd00", cornerRadius=5, cornerEdges=15), # Progress
			%s,
			],
			"fonts": [gFont("xtraRegular", 18), gFont("xtraRegular", 16), gFont("xtraBold", 18)],
			"itemWidth" : 320,
			"itemHeight" : 250
			}
			</convert>
	</widget>
	<eLabel backgroundColor="#ff8080" cornerRadius="20" position="150,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#84ff80" cornerRadius="20" position="475,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#ffee80" cornerRadius="20" position="800,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#80e8ff" cornerRadius="20" position="1125,1058" size="10,10" transparent="0" zPosition="1" />
	<widget name="key_red" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="170,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="495,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="820,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1145,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<eLabel name="" text="" position="1450,1050" size="30,30" foregroundColor="#00bbbbbb" backgroundColor="#50000000" transparent="1" font="xtraIcons; 26 " zPosition="99" />
	<eLabel name="" text="Setup" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1485,1050" size="100,30" halign="left" transparent="1" zPosition="9" />

</screen>"""%(chNm, prgrs)

xtraCh_Hor_1080 = """
<screen name="xtraChannelSelection" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="#ff000000">
	<widget source="chList" render="Listbox" position="0,750" size="1920,300" backgroundColor="#15202b" 
	itemGradientSelected="#1b4765,#25648d,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" 
	scrollbarWidth="2" enableWrapAround="1"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="230,283" 
	spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showNever" listOrientation="horizontal" 
	scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="9">
	  <convert type="TemplatedMultiContent">
			{"template": [
			%s,
			MultiContentEntryText(pos = (10,180), size = (200,30), font=2, flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), # ch name
			MultiContentEntryText(pos = (10,210), size = (200,30), font=1, flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), # event name
			MultiContentEntryPixmapAlphaBlend(pos = (4,235), size = (213,25), png = 9, flags = BT_SCALE),
			%s,
			# MultiContentEntryProgress(pos=(10,242), size=(200,10), percent=-3, borderWidth=0, foreColor="#0089fa", foreColorSelected="#0089fa", backColor=None, backColorSelected=None, startColor="#0089fa", midColor="#ff0000", endColor="#00dd00", startColorSelected="#0089fa", midColorSelected="#ff0000", endColorSelected="#00dd00", cornerRadius=10, cornerEdges=15), # Progress
			MultiContentEntryText(pos = (10,270), size = (300,30), font=1, flags = RT_HALIGN_LEFT, text = 6, color="#0000ffff", color_sel="#0000ffff"), # percent
			],
			"fonts": [gFont("xtraRegular", 18), gFont("xtraRegular", 16), gFont("xtraRegular", 18)],
			"itemWidth" : 240,
			"itemHeight" : 300
			}
			</convert>
	</widget>
	<eLabel backgroundColor="#ff8080" cornerRadius="20" position="150,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#84ff80" cornerRadius="20" position="475,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#ffee80" cornerRadius="20" position="800,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#80e8ff" cornerRadius="20" position="1125,1058" size="10,10" transparent="0" zPosition="1" />
	<widget name="key_red" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="170,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="495,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="820,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1145,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<eLabel name="" text="" position="1450,1050" size="30,30" foregroundColor="#00bbbbbb" backgroundColor="#50000000" transparent="1" font="xtraIcons; 26 " zPosition="99" />
	<eLabel name="" text="Setup" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1485,1050" size="100,30" halign="left" transparent="1" zPosition="9" />

</screen>"""%(chNm, prgrs)

xtraCh_Hor_1080_2 = """
<screen	name="xtraChannelSelection" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="#ff000000">

	<widget source="chList" render="Listbox" position="0,750" size="1920,300" backgroundColor="#15202b" 
	itemGradientSelected="#1b4765,#25648d,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" 
	scrollbarWidth="2" enableWrapAround="1"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="230,283" 
	spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showNever" listOrientation="horizontal" 
	scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="9">
	  <convert type="TemplatedMultiContent">
			{"template": [
			%s,
			MultiContentEntryText(pos = (10,180), size = (200,30), font=2, flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), # ch name
			MultiContentEntryText(pos = (10,210), size = (200,30), font=1, flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), # event name
			MultiContentEntryPixmapAlphaBlend(pos = (4,235), size = (213,25), png = 9, flags = BT_SCALE),
			%s,
			# MultiContentEntryProgress(pos=(10,242), size=(200,10), percent=-3, borderWidth=0, foreColor="#0089fa", foreColorSelected="#0089fa", backColor=None, backColorSelected=None, startColor="#0089fa", midColor="#ff0000", endColor="#00dd00", startColorSelected="#0089fa", midColorSelected="#ff0000", endColorSelected="#00dd00", cornerRadius=10, cornerEdges=15), # Progress
			MultiContentEntryText(pos = (10,270), size = (300,30), font=1, flags = RT_HALIGN_LEFT, text = 6, color="#0000ffff", color_sel="#0000ffff"), # percent
			],
			"fonts": [gFont("xtraRegular", 18), gFont("xtraRegular", 16), gFont("xtraBold", 18)],
			"itemWidth" : 240,
			"itemHeight" : 300
			}
			</convert>
	</widget>

	<eLabel backgroundColor="#ff8080" cornerRadius="20" position="150,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#84ff80" cornerRadius="20" position="475,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#ffee80" cornerRadius="20" position="800,1058" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#80e8ff" cornerRadius="20" position="1125,1058" size="10,10" transparent="0" zPosition="1" />
	<widget name="key_red" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="170,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="495,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="820,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1145,1050" size="255,45" halign="left" transparent="1" zPosition="1" />
	<eLabel name="" text="" position="1450,1050" size="30,30" foregroundColor="#00bbbbbb" backgroundColor="#50000000" transparent="1" font="xtraIcons; 26 " zPosition="99" />
	<eLabel name="" text="Setup" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="1485,1050" size="100,30" halign="left" transparent="1" zPosition="9" />
	
	<eLabel backgroundColor="#50000000" cornerRadius="20" position="center,20" size="1700,70" transparent="0" zPosition="-1" />
	<widget name="short_description" position="center,20" size="1200,70" transparent="0" font="xtraRegular;18" foregroundColor="#c5c5c5" backgroundColor="#50000000" cornerRadius="20" halign="center" valign="center" zPosition="1" />
	<widget name="picon" position="120,25" size="100,60" transparent="1" alphatest="blend" zPosition="1 " cornerRadius="20" scale="stretch" />
</screen>"""%(chNm, prgrs)

xtraCh_Hor_1080_3 = """
<screen name="xtraChannelSelection" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="#ff000000">
	<widget source="chList" render="Listbox" position="0,center" size="1920,350" backgroundColor="#15202b" 
	itemGradientSelected="#1b4765,#25648d,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" 
	scrollbarWidth="2" enableWrapAround="1"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="230,283" 
	spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showNever" listOrientation="horizontal" 
	scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="9">
	  <convert type="TemplatedMultiContent">
			{"template": [
			%s,
			MultiContentEntryText(pos = (10,285), size = (175,22), font=0, flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), # ch name
			MultiContentEntryText(pos = (10,310), size = (175,22), font=1, flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), # event name
			MultiContentEntryPixmapAlphaBlend(pos = (3,325), size = (175,25), png = 9, flags = BT_SCALE),
			%s,
			# MultiContentEntryProgress(pos=(10,335), size=(165,7), percent=-3, borderWidth=0, foreColor="#0089fa", foreColorSelected="#0089fa", backColor=None, backColorSelected=None, startColor="#0089fa", midColor="#ff0000", endColor="#00dd00", startColorSelected="#0089fa", midColorSelected="#ff0000", endColorSelected="#00dd00", cornerRadius=10, cornerEdges=15), # Progress
			# MultiContentEntryText(pos = (10,270), size = (60,30), font=1, flags = RT_HALIGN_LEFT, text = 6, color="#0000ffff", color_sel="#0000ffff"), # percent
			],
			"fonts": [gFont("xtraBold", 18), gFont("xtraRegular", 16)],
			"itemWidth" : 185,
			"itemHeight" : 350
			}
			</convert>
	</widget>

</screen>"""%(chNm, prgrs)


xtraCh_Epg_1 = """
<screen name="xtraChannelSelectionEpg" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
	<widget source="Title" render="Label" position="60,53" size="1118,60" font="xtraBold; 45" foregroundColor="#c5c5c5" backgroundColor="#15202b" transparent="1" halign="center" />
	<eLabel name="" text="" position="60,60" size="40,40" foregroundColor="#c5c5c5" backgroundColor="#15202b" transparent="1" halign="center" font="xtraIcons2; 40" />
	
	<widget source="epgList" render="Listbox" position="60,120" size="1100,780" backgroundColor="#15202b" itemGradientSelected="#1b4765,#25648d,horizontal" 
	borderWidth="0" borderColor="green" scrollbarLength="auto" scrollbarWidth="2" enableWrapAround="1" itemCornerRadius="10" 
	itemAlignment="center" cornerRadius="10" selectionZoomSize="1200,85" spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" 
	scrollbarMode="showNever" listOrientation="vertical" scrollbarForegroundColor="#0089fa" transparent="1" zPosition="99">
	<convert type="TemplatedMultiContent">
				{"template": [
				MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (100,60), png = 0, flags = BT_KEEP_ASPECT_RATIO | BT_HALIGN_CENTER | BT_SCALE, cornerRadius=10), #img
				MultiContentEntryText(pos = (120,10), size = (900,30), font=2, flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), # event name
				MultiContentEntryText(pos = (120,40), size = (900,30), font=1, flags = RT_HALIGN_LEFT, text = 7, color="#00cccccc", color_sel="#00eeeeee"), # event day
				# MultiContentEntryText(pos = (120,70), size = (900,30), font=1, flags = RT_HALIGN_LEFT, text = 6, color="#00cccccc", color_sel="#00eeeeee"), # event day

				],
				"fonts": [gFont("xtraRegular", 18), gFont("xtraRegular", 22), gFont("xtraBold", 24)],
				"itemWidth" : 1100,
				"itemHeight" : 80
				}
				</convert>
	</widget>
	
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>

	<widget name="description" position="1260,450" size="600,440" transparent="1" font="xtraRegular;22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="poster" position="1260,130" size="185,278" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget name="ratingStar" position="1260,410" size="200,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star.png" transparent="1" zPosition="2" alphatest="blend" />
	<ePixmap position="1260,410" size="200,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star_back.png" transparent="1" zPosition="1" alphatest="blend" />
	<widget name="imdb" position="1470,410" size="600,600" transparent="1" font="xtraRegular;18" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="infos" position="1455,130" size="400,600" transparent="1" font="xtraRegular;18" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="eventTime" position="1260,912" size="500,26" transparent="1" font="xtraRegular;22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="99" />
	<widget name="parentalRating" position="1260,850" size="60,60" alphatest="blend" zPosition="5" transparent="1" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
</screen>
"""





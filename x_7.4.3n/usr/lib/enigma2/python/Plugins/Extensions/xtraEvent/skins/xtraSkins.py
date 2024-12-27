#!/usr/bin/python
# -*- coding: utf-8 -*-
# by digiteng
# 09.2024
from __future__ import absolute_import
import os
from Components.config import config
from ..xtra_config import *
imgr = ""
img = "/etc/issue"
if os.path.exists(img):
	with open(img, "r") as f:
		imgr = f.read().lower()
xifs = None
try:
	xifs = config.plugins.xtrvnt.xtraInfoSource.value
	tskn = config.plugins.xtrvnt.xtraInfoSourceSkinTMDB.value
	iskn = config.plugins.xtrvnt.xtraInfoSourceSkinIMDB.value
except Exception as err:
	from Tools.xtraTool import errorlog
	errorlog(err, __file__)
aListbox=" "
if "openatv" in imgr:
	if xifs == "TMDB":
		if tskn == "skin1":
			aListbox = """
			<widget source="castList" render="Listbox" position="1240,110" size="620,330" backgroundColor="#15202b" 
			itemGradientSelected="#1b4765,#25648d,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" 
			scrollbarWidth="2" enableWrapAround="1"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="134,240" 
			spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showAlways" listOrientation="grid" 
			scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="99">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (92,138), png = 0, flags = BT_SCALE, cornerRadius=10), 
					MultiContentEntryText(pos = (5,150), size = (120,20), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					MultiContentEntryText(pos = (5,167), size = (120,60), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraRegular", 12), gFont("xtraRegular", 10)],
					"itemWidth" : 112,
					"itemHeight" : 200
					}
					</convert>
			</widget>
			"""
		elif tskn == "skin2" or "skin3":
			aListbox = """
			<widget source="castList" render="Listbox" position="60,600" size="1800,300" backgroundColor="#50000000" 
			itemGradientSelected="#3fafd7,#3fafd7,horizontal" borderWidth="0" borderColor="black" scrollbarLength="auto" 
			scrollbarWidth="1" enableWrapAround="0"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10"	 
			spacingColor="#50000000" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showNever" listOrientation="grid" 
			scrollbarForegroundColor="#3f8e73" transparent="1"	zPosition="99">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (5,5), size = (185,278), png = 0, flags = BT_SCALE, cornerRadius=10), 
					MultiContentEntryText(pos = (10,238), size = (175,20), flags = RT_HALIGN_CENTER, text = 1, color="#00ffffff", color_sel="#00ffffff", backcolor="#50000000", backcolor_sel="#50000000"), 
					MultiContentEntryText(pos = (10,258), size = (175,20), flags = RT_HALIGN_CENTER, text = 2, color="#0000ffff", color_sel="#0000ffff", backcolor="#50000000", backcolor_sel="#50000000"), 
					],
					"fonts": [gFont("xtraRegular", 12), gFont("xtraRegular", 10)],
					"itemWidth" : 195,
					"itemHeight" : 288
					}
					</convert>
			</widget>
			"""
	elif xifs == "IMDB":
		if iskn == "skin1":
			aListbox = """
			<widget source="castList" render="Listbox" position="1260,150" size="600,800" backgroundColor="#15202b" 
			itemGradientSelected="#1b4765,#25648d,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" 
			scrollbarWidth="2" enableWrapAround="0"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="134,240" 
			spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showAlways" listOrientation="orHorizontal" 
			scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="99">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (140,140), png = 0, flags = BT_SCALE, cornerRadius=70), 
					MultiContentEntryText(pos = (175,15), size = (400,30), flags = RT_HALIGN_LEFT, font=0, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, font=1, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					# MultiContentEntryText(pos = (175,80), size = (200,100), flags = RT_HALIGN_LEFT | RT_VALIGN_TOP, font=2, text = 3, color="#00cccccc", color_sel="#00ffffff"),
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20), gFont("xtraRegular", 12)],
					"itemWidth" : 600,
					"itemHeight" : 200
					}
					</convert>
			</widget>
			"""
		elif iskn == "skin2":
			aListbox = """
			<widget source="castList" render="Listbox" position="1506,130" size="350,840" backgroundColor="#15202b" 
			itemGradientSelected="#284157,#284157,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" 
			scrollbarWidth="2" enableWrapAround="1"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="134,240" 
			spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showAlways" listOrientation="orHorizontal" 
			scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="5">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (105,10), size = (140,140), png = 0, flags = BT_SCALE, cornerRadius=70), 
					MultiContentEntryText(pos = (10,160), size = (330,30), flags = RT_HALIGN_CENTER, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					# MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20)],
					"itemWidth" : 350,
					"itemHeight" : 210
					}
					</convert>
			</widget>
			
			<widget source="backList" render="Listbox" position="530,225" size="905,605" backgroundColor="#20000000" 
			itemGradientSelected="#20000000,#20000000,horizontal" borderWidth="0" 
			enableWrapAround="1" itemCornerRadius="10" itemAlignment="center" cornerRadius="10" 
			spacingColor="#20000000" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showNever" listOrientation="grid" 
			scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="1">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (0,0), size = (900,600), png = 0, flags = BT_SCALE, cornerRadius=20), 
					# MultiContentEntryText(pos = (10,160), size = (330,30), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					# MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20)],
					"itemWidth" : 900,
					"itemHeight" : 600
					}
					</convert>
			</widget>
			"""
elif "openpli" in imgr or "vix" in imgr:
	if xifs == "TMDB":
		if tskn == "skin1":
			aListbox += """
			<widget source="castList" render="Listbox" position="1260,160" size="600,231" backgroundColor="#15202b" backgroundColorSelected="#0089fa" 
			scrollbarOffset="0" scrollbarMode="showAlways" scrollbarForegroundColor="#0089fa" itemCornerRadius="10" cornerRadius="10" 
			enableWrapAround="1" transparent="1" scrollbarSliderForegroundColor="#0089fa" scrollbarBackgroundColor="#15202b">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (92,138), png = 0, flags = BT_SCALE | RT_HALIGN_CENTER, backcolor="#15202b", backcolor_sel="#15202b"),
					MultiContentEntryText(pos = (5,155), size = (107,25), flags = RT_HALIGN_CENTER, text = 1, color="#00ffffff", color_sel="#00ffffff", backcolor="#15202b"),
					MultiContentEntryText(pos = (5,172), size = (107,60), flags = RT_HALIGN_CENTER, text = 2, color="#0000ffff", color_sel="#0000ffff", backcolor="#15202b"),
					],
					"fonts": [gFont("xtraRegular", 12), gFont("xtraRegular", 10)],
					"itemWidth" : 112,
					"itemHeight" : 230,
					"orientation" : "orHorizontal"
					}
					</convert>
			</widget>"""
		elif tskn == "skin2":
			aListbox = """
			<widget source="castList" render="Listbox" position="60,700" size="1220,222" backgroundColor="#15202b" backgroundColorSelected="#0089fa" 
			scrollbarOffset="0" scrollbarMode="showAlways" scrollbarForegroundColor="#0089fa" itemCornerRadius="10" cornerRadius="10" 
			enableWrapAround="1" transparent="1" scrollbarSliderForegroundColor="#0089fa" scrollbarBackgroundColor="#15202b">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (92,138), png = 0, flags = BT_SCALE), 
					MultiContentEntryText(pos = (5,150), size = (120,20), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					MultiContentEntryText(pos = (5,167), size = (120,60), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraRegular", 12), gFont("xtraRegular", 10)],
					"itemWidth" : 112,
					"itemHeight" : 200,
					"orientation" : "orHorizontal"
					}
					</convert>
			</widget>
			"""
	elif xifs == "IMDB":
		if iskn == "skin1":
			aListbox = """
			<widget source="castList" render="Listbox" position="1260,150" size="600,800" backgroundColor="#15202b" backgroundColorSelected="#eeaa00"  
			scrollbarOffset="0" scrollbarMode="showAlways" scrollbarForegroundColor="#eeee00" itemCornerRadius="20" cornerRadius="20" 
			enableWrapAround="1" transparent="1" scrollbarSliderForegroundColor="#eebb00" scrollbarBackgroundColor="#15202b">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (140,140), png = 0, flags = BT_SCALE), 
					MultiContentEntryText(pos = (175,15), size = (400,30), flags = RT_HALIGN_LEFT, font=0, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, font=1, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					# MultiContentEntryText(pos = (175,80), size = (200,100), flags = RT_HALIGN_LEFT | RT_VALIGN_TOP, font=2, text = 3, color="#00cccccc", color_sel="#00ffffff"),
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20), gFont("xtraRegular", 12)],
					"itemWidth" : 600,
					"itemHeight" : 200,
					"orientation" : "orVertical"
					}
					</convert>
			</widget>
			"""
		elif iskn == "skin2":
			aListbox = """
			<widget source="castList" render="Listbox" position="1506,130" size="350,840" backgroundColor="#15202b" backgroundColorSelected="#eeaa00" 
			scrollbarOffset="0" scrollbarMode="showAlways" scrollbarForegroundColor="#0089fa" itemCornerRadius="20" 
			enableWrapAround="1" transparent="1" scrollbarSliderForegroundColor="#0089fa" scrollbarBackgroundColor="#15202b">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (105,10), size = (140,140), png = 0, flags = BT_SCALE), 
					MultiContentEntryText(pos = (10,160), size = (330,30), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					# MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20)],
					"itemWidth" : 350,
					"itemHeight" : 210,
					"orientation" : "orVertical"
					}
					</convert>
			</widget>
			<widget name="backdrop_0" position="530,225" size="900,600" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />

			"""

elif "openbh" in imgr:
	if xifs == "TMDB":
		if tskn == "skin1":
			aListbox += """
			<widget source="castList" render="Listbox" position="1280,160" size="560,230" zPosition="2" backgroundColor="#15202b" backgroundColorSelected="#1b4765" borderWidth="0" borderColor="#0089fa"
			scrollbarMode="showAlways" scrollbarWidth="2" scrollbarSliderForegroundColor="#0089fa" scrollbarBackgroundColor="#15202b" itemCornerRadius="10" cornerRadius="10" 
			noWrap="1" transparent="1">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (92,138), png = 0, flags = BT_SCALE | RT_HALIGN_CENTER, corner_radius=10, corner_edges=15, backcolor="#15202b", backcolor_sel="#15202b"),
					MultiContentEntryText(pos = (5,155), size = (107,25), flags = RT_HALIGN_CENTER, text = 1, color="#00ffffff", color_sel="#00ffffff", backcolor="#15202b"),
					MultiContentEntryText(pos = (5,172), size = (107,60), flags = RT_HALIGN_CENTER, text = 2, color="#0000ffff", color_sel="#0000ffff", backcolor="#15202b"),
					],
					"fonts": [gFont("xtraRegular", 12), gFont("xtraRegular", 10)],
					"itemWidth" : 112,
					"itemHeight" : 230,
					"orientation" : "orHorizontal"
					}
					</convert>
			</widget>
			"""
		elif tskn == "skin2":
			aListbox = """
			<widget source="castList" render="Listbox" position="60,700" size="1120,222" backgroundColor="#15202b" 
			scrollbarMode="showAlways" scrollbarWidth="2" scrollbarSliderForegroundColor="#0089fa" scrollbarBackgroundColor="#15202b" itemCornerRadius="10" cornerRadius="10" 
			noWrap="1" transparent="1">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (92,138), png = 0, flags = BT_SCALE, corner_radius=10), 
					MultiContentEntryText(pos = (5,150), size = (120,20), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					MultiContentEntryText(pos = (5,167), size = (120,60), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraRegular", 12), gFont("xtraRegular", 10)],
					"itemWidth" : 112,
					"itemHeight" : 200,
					"orientation" : "orHorizontal"
					}
					</convert>
			</widget>
			"""
	elif xifs == "IMDB":
		if iskn == "skin1":
			aListbox = """
			<widget source="castList" render="Listbox" position="1260,150" size="600,800" backgroundColor="#15202b" 
			scrollbarMode="showAlways" scrollbarWidth="2" scrollbarSliderForegroundColor="#0089fa" scrollbarBackgroundColor="#15202b" itemCornerRadius="10" cornerRadius="10" 
			noWrap="1" transparent="1">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (140,140), png = 0, flags = BT_SCALE, corner_radius=70), 
					MultiContentEntryText(pos = (175,15), size = (400,30), flags = RT_HALIGN_LEFT, font=0, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, font=1, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					# MultiContentEntryText(pos = (175,80), size = (200,100), flags = RT_HALIGN_LEFT | RT_VALIGN_TOP, font=2, text = 3, color="#00cccccc", color_sel="#00ffffff"),
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20), gFont("xtraRegular", 12)],
					"itemWidth" : 600,
					"itemHeight" : 200,
					"orientation" : "orVertical"
					}
					</convert>
			</widget>
			"""
		elif iskn == "skin2":
			aListbox = """
			<widget source="castList" render="Listbox" position="1506,130" size="350,840" backgroundColor="#15202b" 
			scrollbarMode="showAlways" scrollbarWidth="2" scrollbarSliderForegroundColor="#0089fa" scrollbarBackgroundColor="#15202b" itemCornerRadius="10" cornerRadius="10" 
			noWrap="1" transparent="1">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (105,10), size = (140,140), png = 0, flags = BT_SCALE, corner_radius=70), 
					MultiContentEntryText(pos = (10,160), size = (330,30), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					# MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20)],
					"itemWidth" : 350,
					"itemHeight" : 210,
					"orientation" : "orVertical"
					}
					</convert>
			</widget>
			<widget name="backdrop_0" position="530,225" size="900,600" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />


			"""

elif "pure2" in imgr:
	if xifs == "TMDB":
		if tskn == "skin1":
			aListbox = """
			<widget source="castList" render="Listbox" position="1260,160" size="600,231" backgroundColorSelected="#15202b" 
			scrollbarWidth="5" scrollbarMode="showAlways" scrollbarForegroundColor="#0089fa" scrollbarBackgroundColor="#15202b" scrollbarBorderWidth="0" 
			backgroundColor="#15202b"	 enableWrapAround="1" transparent="1">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (0,0), size = (154,231), png = 0, flags = BT_SCALE, backcolor="#15202b", backcolor_sel="#15202b", cornerRadius=10), 
					MultiContentEntryText(pos = (175,10), size = (300,30), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff", backcolor="#15202b", backcolor_sel="#15202b"), 
					MultiContentEntryText(pos = (175,40), size = (300,60), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff", backcolor="#15202b", backcolor_sel="#15202b"), 
					],
					"fonts": [gFont("xtraRegular", 24), gFont("xtraRegular", 16)],
					"itemHeight" : 231
					}
					</convert>
			</widget>
			"""
		elif tskn == "skin2":
			aListbox = """
			<widget source="castList" render="Listbox" position="60,700" size="1220,222" backgroundColorSelected="#15202b" 
			scrollbarWidth="5" scrollbarMode="showAlways" scrollbarForegroundColor="#0089fa" scrollbarBackgroundColor="#15202b" scrollbarBorderWidth="0" 
			backgroundColor="#15202b"	 enableWrapAround="1" transparent="1">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (92,138), png = 0, flags = BT_SCALE, cornerRadius=10), 
					MultiContentEntryText(pos = (5,150), size = (120,20), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					MultiContentEntryText(pos = (5,167), size = (120,60), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraRegular", 12), gFont("xtraRegular", 10)],
					"itemHeight" : 200,"orientation" : "orHorizontal"
					}
					</convert>
			</widget>
			"""
	elif xifs == "IMDB":
		if iskn == "skin1":
			aListbox = """
			<widget source="castList" render="Listbox" position="1260,150" size="600,800" backgroundColor="#15202b" 
			itemGradientSelected="#1b4765,#25648d,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" 
			scrollbarWidth="2" enableWrapAround="0"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="134,240" 
			spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showAlways" listOrientation="orHorizontal" 
			scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="99">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (10,10), size = (140,140), png = 0, flags = BT_SCALE, cornerRadius=70), 
					MultiContentEntryText(pos = (175,15), size = (400,30), flags = RT_HALIGN_LEFT, font=0, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, font=1, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					# MultiContentEntryText(pos = (175,80), size = (200,100), flags = RT_HALIGN_LEFT | RT_VALIGN_TOP, font=2, text = 3, color="#00cccccc", color_sel="#00ffffff"),
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20), gFont("xtraRegular", 12)],
					"itemWidth" : 600,
					"itemHeight" : 200
					}
					</convert>
			</widget>
			"""
		elif iskn == "skin2":
			aListbox = """
			<widget source="castList" render="Listbox" position="1506,130" size="350,840" backgroundColor="#15202b" 
			itemGradientSelected="#284157,#284157,horizontal" borderWidth="0" borderColor="green" scrollbarLength="auto" 
			scrollbarWidth="2" enableWrapAround="1"	 itemCornerRadius="10" itemAlignment="center" cornerRadius="10" selectionZoomSize="134,240" 
			spacingColor="#15202b" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showAlways" listOrientation="orHorizontal" 
			scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="5">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (105,10), size = (140,140), png = 0, flags = BT_SCALE, cornerRadius=70), 
					MultiContentEntryText(pos = (10,160), size = (330,30), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					# MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20)],
					"itemWidth" : 350,
					"itemHeight" : 210
					}
					</convert>
			</widget>
			
			<widget source="backList" render="Listbox" position="530,225" size="905,605" backgroundColor="#20000000" 
			itemGradientSelected="#20000000,#20000000,horizontal" borderWidth="0" 
			enableWrapAround="1" itemCornerRadius="10" itemAlignment="center" cornerRadius="10" 
			spacingColor="#20000000" itemSpacing="5,5" scrollbarOffset="0" scrollbarMode="showNever" listOrientation="grid" 
			scrollbarForegroundColor="#0089fa" transparent="1"	zPosition="1">
			  <convert type="TemplatedMultiContent">
					{"template": [
					MultiContentEntryPixmapAlphaBlend(pos = (0,0), size = (900,600), png = 0, flags = BT_SCALE, cornerRadius=20), 
					# MultiContentEntryText(pos = (10,160), size = (330,30), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff"), 
					# MultiContentEntryText(pos = (175,50), size = (400,30), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff"), 
					],
					"fonts": [gFont("xtraBold", 24), gFont("xtraRegular", 20)],
					"itemWidth" : 900,
					"itemHeight" : 600
					}
					</convert>
			</widget>
			"""

else:
	aListbox += """
	<widget source="castList" render="Listbox" position="1260,160" size="600,231" backgroundColorSelected="#15202b" 
	scrollbarOffset="0" scrollbarMode="showAlways" scrollbarForegroundColor="#0089fa"
	backgroundColor="#15202b" enableWrapAround="1" transparent="1">
	  <convert type="TemplatedMultiContent">
			{"template": [
			MultiContentEntryPixmapAlphaBlend(pos = (0,0), size = (154,231), png = 0, flags = BT_SCALE, backcolor="#15202b", backcolor_sel="#15202b"), 
			MultiContentEntryText(pos = (175,10), size = (300,30), flags = RT_HALIGN_LEFT, text = 1, color="#00ffffff", color_sel="#00ffffff", backcolor="#15202b", backcolor_sel="#15202b"), 
			MultiContentEntryText(pos = (175,40), size = (300,60), flags = RT_HALIGN_LEFT, text = 2, color="#0000ffff", color_sel="#0000ffff", backcolor="#15202b", backcolor_sel="#15202b"), 
			],
			"fonts": [gFont("xtraRegular", 24), gFont("xtraRegular", 16)],
			"itemHeight" : 231
			}
			</convert>
	</widget>
"""
xtra_1080 = """
<screen name="xtra" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
	<widget source="Title" render="Label" position="60,53" size="1118,60" font="xtraRegular; 45" foregroundColor="#c5c5c5" backgroundColor="#15202b" transparent="1" />
	<widget name="config" position="60,143" size="1118,765" itemHeight="45" font="xtraRegular;34" foregroundColor="#c5c5c5" foregroundColorSelected="#ffffff" backgroundColor="#15202b" itemCornerRadius="10" itemGradientSelected="#1b4765,#25648d,horizontal" transparent="1" />
	<widget name="strg" position="1260,500" size="600,203" transparent="1" font="xtraRegular;24" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="2" />
	<widget name="logo" position="1362,169" size="400,216" zPosition="9" transparent="1" alphatest="blend" />
	<widget source="help" position="1260,905" size="600,30" render="Label" font="xtraRegular; 24" foregroundColor="#f3fc92" backgroundColor="#15202b" halign="left" valign="center" transparent="1" />
	<widget name="status" position="1260,450" size="600,45" transparent="1" font="xtraRegular;30" foregroundColor="#92f1fc" backgroundColor="#15202b" />
	<widget name="statuss" position="200,500" size="800,80" transparent="1" font="xtraRegular;30" foregroundColor="#00ffffff" backgroundColor="#15202b" zPosition="99"	/>
	<widget name="infox" position="1260,495" size="600,200" transparent="1" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,60" size="40,40" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" transparent="1" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1235,965" size="150,45" transparent="1" halign="center" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1735,965" size="150,45" transparent="1" halign="center" font="xtraRegular; 30" />
	<widget source="session.CurrentService" render="Progress" position="1260,730" size="600,10" foregroundColor="#b3dd9c" backgroundColor="#435156" transparent="0" cornerRadius="10" zPosition="2">
		<convert type="xtraDiskInfos">flashProgress</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="1260,750" size="600,30" font="xtraRegular; 24" transparent="1" foregroundColor="#00c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="xtraDiskInfos">flashInfo</convert>
	</widget>
	<widget source="session.CurrentService" render="Progress" position="1260,810" size="600,10" foregroundColor="#b3dd9c" backgroundColor="#435156" transparent="0" cornerRadius="10" zPosition="2">
		<convert type="xtraDiskInfos">diskProgress</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="1260,830" size="600,30" font="xtraRegular; 24" transparent="1" foregroundColor="#00c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="xtraDiskInfos">diskInfo</convert>
	</widget>
</screen>
"""
download_1080 = """
<screen name="downloads" position="40,940" size="1860,100" title="downloads..." flags="wfNoBorder" cornerRadius="20" backgroundColor="#15202b">
	<widget source="Title" render="Label" position="25,10" size="600,30" font="xtraBold; 22" foregroundColor="#c5c5c5" backgroundColor="#15202b" transparent="1" />
	<widget name="status" position="60,895" size="1120,44" transparent="1" font="xtraRegular;22" foregroundColor="#92f1fc" backgroundColor="#15202b" />
	<widget name="infox" position="25,40" size="600,60" transparent="1" font="xtraRegular; 20" noWrap="1" zPosition="9" foregroundColor="#c5c5c5" backgroundColor="#15202b" valign="top" />
	<widget name="info2" position="700,10" size="600,100" transparent="1" font="xtraRegular; 14" zPosition="9" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" />
	<eLabel backgroundColor="#00ff00" cornerRadius="20" position="1100,70" size="20,20" transparent="0" />
	<eLabel backgroundColor="#0089fa" cornerRadius="20" position="1400,70" size="20,20" transparent="0" />
	<widget name="key_green" render="Label" font="xtraRegular; 18" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="1130,70" size="255,20" halign="left" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 18" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="1430,70" size="255,20" halign="left" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1540,5" size="300,45" font="xtraRegular; 22" transparent="1" halign="right" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="2">
		<convert type="ClockToText">Default</convert>
	</widget>
	<widget name="int_statu" font="xtraIcons; 24" position="1813,56" size="30,30" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" transparent="1" />
</screen>
"""
manuel_1080 = """
<screen name="manuelSearch" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
	<widget source="Title" render="Label" position="60,60" size="1118,60" font="xtraRegular; 45" foregroundColor="#ffffff" backgroundColor="#15202b" transparent="1" />
	<widget source="session.CurrentService" render="Label" position="60,120" size="957,60" zPosition="2" font="xtraRegular; 45" transparent="1" backgroundColor="#15202b" valign="center">
		<convert type="ServiceName">Name</convert>
	</widget>
	<widget name="config" position="60,190" size="1118,588" itemHeight="45" font="xtraRegular;34" foregroundColor="#c5c5c5" foregroundColorSelected="#ffffff" backgroundColor="#15202b" itemCornerRadius="10" itemGradientSelected="#1b4765,#25648d,horizontal" scrollbarMode="showOnDemand" scrollbarSliderBorderWidth="0" scrollbarWidth="3" scrollbarSliderForegroundColor="#0d71aa" transparent="1" />
	<widget name="logo" position="1374,171" size="400,216" zPosition="5" transparent="1" alphatest="blend" />
	<widget name="status" position="60,885" size="1118,40" transparent="1" font="xtraRegular;36" foregroundColor="#92f1fc" backgroundColor="#15202b" />
	<widget name="infox" position="1270,965" size="600,45" transparent="1" font="xtraRegular;30" halign="center" foregroundColor="#ffffff" backgroundColor="#15202b" />
	<widget name="Picture" position="1260,480" size="278,417" zPosition="5" transparent="1" />
	<widget name="progress" position="60,840" size="1120,12" foregroundColor="#0089fa" backgroundColor="#435156" cornerRadius="12" itemCornerRadius="12" transparent="0" zPosition="5" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<eLabel name="" position="60,180" size="1118, 2" backgroundColor="#898989" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,60" size="40,40" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" transparent="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
</screen>
"""
selbuq_1080 = """
<screen name="selBouquets" position="center,center" size="1920,1080" title="xtraEvent v1" backgroundColor="#ffffff">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
	<widget source="Title" render="Label" position="60,53" size="1118,60" font="xtraRegular; 45" foregroundColor="#c5c5c5" backgroundColor="#15202b" transparent="1" />
	<widget name="list" position="60,143" size="1118,765" itemHeight="45" font="xtraRegular;36" 
	foregroundColor="#c5c5c5" foregroundColorSelected="#ffffff" 
	backgroundColor="#15202b"  
	scrollbarMode="showOnDemand" scrollbarSliderBorderWidth="0" scrollbarWidth="3" scrollbarSliderForegroundColor="#0d71aa" 
	itemCornerRadius="10" itemGradientSelected="#1b4765,#25648d,horizontal"	 
	transparent="1" />
	<widget name="status" position="1260,450" size="600,45" transparent="1" font="xtraRegular;30" foregroundColor="#92f1fc" backgroundColor="#15202b" />
	<widget name="infox" position="1260,495" size="600,405" transparent="1" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="center" valign="top" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,60" size="40,40" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" transparent="1" />
</screen>"""
# <widget render="xtraCircleProgress" position="1260,760" size="60,60" source="global.CurrentTime" mode="rtng" scale="2" pixmapCircle="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150orange.png" pixmapCircleBack="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150back.png" backgroundColor="#15202b" zPosition="3" transparent="1" />
xtraInfo_1080_tmdb1 = """
<screen name="xtraInfo" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
	<widget source="Title" render="Label" position="30,55" size="1165,60" font="xtraRegular; 34" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#15202b" transparent="1" />
	<widget name="poster" position="1260,475" size="185,278" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget name="backdrop" position="115,130" size="1000,560" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget render="xtraCircleProgress" source="session.FrontendStatus" mode="rating" scale="2" 
	pixmapCircle="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150blue1.png" 
	pixmapCircleBack="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150back.png" 
	position="1260,760" size="60,60" backgroundColor="#15202b" zPosition="3" transparent="1" />
	<widget source="session.Event_Now" position="115,730" size="1000,220" font="xtraRegular; 22" render="Label" options="movetype=running,startdelay=8000,steptime=60,direction=top,startpoint=0,wrap=1,always=0,repeat=2,oneshot=1" halign="left" transparent="1" zPosition="5" foregroundColor="#00ffffff" backgroundColor="#15202b" valign="top">
		<convert type="xtraInfo2">\c0000????,\c00??????,\n, Description</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="1330,780" size="300,30" font="xtraRegular; 22" halign="left" transparent="1" zPosition="5"	backgroundColor="#15202b" valign="center">
		<convert type="xtraInfo2">tmdbRatingFull</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="1459,475" size="410,278" font="xtraRegular; 20" halign="left" transparent="1" zPosition="2" backgroundColor="#15202b" valign="top">
		<convert type="xtraInfo2">\c0000????,\c00??????,Title, AirDate, Rated, Genre, Countries, Budget, Revenue, Duration, SE</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="1260,402" size="600,22" font="xtraRegular; 18" halign="left" transparent="1" zPosition="2" backgroundColor="#15202b" valign="center">
		<convert type="xtraInfo2">\c0000????,\c00??????,Director</convert>
	</widget>
	<widget source="session.Event_Now" backgroundColor="#15202b" font="xtraRegular; 24" zPosition="2" halign="left" position="1257,912" size="500,28" render="Label" transparent="1" foregroundColor="#00cccccc">
		<convert type="xtraEventInfo">EventNameCompact</convert>
	</widget>	 
	<widget source="session.Event_Now" render="Progress" position="60,945" size="1110,2" foregroundColor="#000089fa" backgroundColor="#435156" transparent="0" zPosition="2">
		<convert type="EventTime">Progress</convert>
	</widget>
	<widget source="help" position="662,890" size="500,40" render="Label" font="xtraRegular;28" foregroundColor="#f3fc92" backgroundColor="#15202b" halign="center" valign="center" transparent="1" />
	<widget name="status" position="61,891" size="600,45" transparent="1" font="xtraRegular;30" foregroundColor="#92f1fc" backgroundColor="#15202b" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraIcons;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraIcons;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraIcons; 30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1315,970" size="150,45" transparent="1" halign="left" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1650,970" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,60" size="40,40" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" transparent="1" />
	<eLabel name="menu" text="♪" position="1272,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="left" font="xtraRegular; 40" />
	<eLabel name="infox" text="█" position="1807,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="right" font="xtraRegular; 40" />
	<ePixmap position="48,338" size="1135,372" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/shdw7.png" transparent="1" alphatest="blend" />
	<ePixmap position="115,130" size="1000,559" zPosition="0" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film3.jpg" transparent="1" cornerRadius="20" scale="stretch" />
	<ePixmap position="50,50" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/TMDB_thumb.png" backgroundColor="#15202b" alphatest="blend" transparent="1" scale="stretch" />
	<widget name="logo0" position="1260,835" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<widget name="logo1" position="1367,835" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<widget name="logo2" position="1459,835" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<widget name="logo3" position="1551,835" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<eLabel name="" text="Casts" position="1260,122" size="200,20" font="xtraRegular;18" foregroundColor="#0000ffff" backgroundColor="#15202b" halign="left" valign="top" zPosition="1" transparent="1" />
	{}
</screen>
""".format(aListbox)
xtraInfoPerson_1080_tmdb1 = """
<screen name="xtraInfoPerson" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
	<ePixmap position="50,50" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/TMDB_thumb.png" backgroundColor="#15202b" alphatest="blend" transparent="1" scale="stretch" />
	<widget source="Title" render="Label" position="30,55" size="1165,60" font="xtraRegular; 34" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#15202b" transparent="1" />
	<widget name="biography" position="400,140" size="763,770" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="2" />
	<widget name="pinfo" position="70,605" size="300,60" transparent="1" font="xtraRegular;22" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="2" />
	<widget name="poster" position="70,140" size="300,450" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget name="known_for0" position="1260,500" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_for1" position="1465,500" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_for2" position="1670,500" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText0" position="1260,800" size="185,90" transparent="1"	 font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText1" position="1465,800" size="185,90" transparent="1"	 font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText2" position="1670,800" size="185,90" transparent="1"	 font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget source="help" position="60,883" size="300,60" render="Label" font="xtraRegular;28" foregroundColor="#f3fc92" backgroundColor="#15202b" halign="left" valign="center" transparent="1" />
	<widget name="status" position="1259,873" size="600,45" transparent="1" font="xtraRegular;30" foregroundColor="#92f1fc" backgroundColor="#15202b" />
	<!--<widget name="int_statu" position="1819,60" size="40,40" transparent="1" text="●" font="xtraIcons; 36" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" halign="center" /> -->
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1315,970" size="150,45" transparent="1" halign="left" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1650,970" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,60" size="40,40" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" transparent="1" />
	<eLabel name="menu" text="♪" position="1272,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="left" font="xtraRegular; 40" />
	<eLabel name="infox" text="█" position="1807,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="right" font="xtraRegular; 40" />
	<eLabel name="" text="Casts" position="1260,122" size="200,20" font="xtraRegular;18" foregroundColor="#0000ffff" backgroundColor="#15202b" halign="left" valign="top" zPosition="1" transparent="1" />
	<eLabel name="" text="Known For" position="1260,457" size="200,40" font="xtraRegular;20" foregroundColor="#0000ffff" backgroundColor="#15202b" halign="left" valign="top" zPosition="1" transparent="1" />
	{}
</screen>
""".format(aListbox)
	# <widget source="session.Event_Now" backgroundColor="#15202b" font="xtraRegular; 24" zPosition="2" halign="left" position="1257,912" size="500,34" render="Label" transparent="1" foregroundColor="#cccccc">
		# <convert type="xtraEventInfo">EventNameCompact</convert>
	# </widget>
# <ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="{}" transparent="1" />
# <ePixmap position="0,0" size="1920,1080" zPosition="-2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/tmdb_back.png" transparent="1" />
xtraInfo_1080_tmdb2 = """
<screen name="xtraInfo" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<widget name="poster" position="60,140" size="185,278" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget name="backdrop" position="1260,144" size="600,360" transparent="1" alphatest="off" zPosition="5" cornerRadius="20" scale="stretch" />
	<widget source="session.Event_Now" render="Label" position="300,140" size="1000,40" font="xtraBold; 32" halign="left" transparent="1" zPosition="5" foregroundColor="#00ffffff" backgroundColor="#50000000" valign="top">
		<convert type="xtraInfo2">\c0000????,\c00??????,\n, Title</convert>
	</widget>
	<widget render="xtraCircleProgress" source="session.FrontendStatus" mode="rating" scale="2" pixmapCircle="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150blue1.png" pixmapCircleBack="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150back.png" position="300,235" size="60,60" backgroundColor="#20000000" zPosition="3" transparent="1" />
	<widget source="session.Event_Now"	position="64,454" size="1100,220" render="xtraRunningText" options="movetype=running,startdelay=8000,steptime=60,direction=top,startpoint=0,wrap=1,always=0,repeat=2,oneshot=1" font="xtraRegular; 22" halign="left" transparent="1" zPosition="5" foregroundColor="#00ffffff" backgroundColor="#50000000" valign="top">
		<convert type="xtraInfo2">\c0000????,\c00??????,\n, Description</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="386,250" size="500,30" font="Regular; 24" halign="left" transparent="1" zPosition="5" backgroundColor="#50000000" valign="center">
		<convert type="xtraInfo2">tmdbRatingFull</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="300,191" size="800,30" font="Regular; 24" halign="left" transparent="1" zPosition="2" backgroundColor="#50000000" valign="top">
		<convert type="xtraInfo2">\c0000????,\c00??????, compact, Year, Rated, Genre, Countries, Duration</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="300,330" size="600,30" font="Regular; 24" halign="left" transparent="1" zPosition="2" backgroundColor="#50000000" valign="center">
		<convert type="xtraInfo2">\c0000????,\c00??????,Director</convert>
	</widget>
	<widget source="session.Event_Now" backgroundColor="#50000000" font="xtraRegular; 24" zPosition="2" halign="left" position="1262,533" size="600,28" render="Label" transparent="1" foregroundColor="#00cccccc">
		<convert type="xtraEventInfo">EventNameCompact</convert>
	</widget>	 
	<widget source="session.Event_Now" render="Progress" position="60,945" size="1800,2" foregroundColor="#000089fa" backgroundColor="#435156" transparent="0" zPosition="2">
		<convert type="EventTime">Progress</convert>
	</widget>
	<eLabel backgroundColor="#ff8080" cornerRadius="20" position="60,977" size="10,10" transparent="0" zPosition="1" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="75,965" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraIcons;30" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="555,375" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="300,375" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraIcons; 30" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="830,375" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,40" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#50000000" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1315,970" size="150,45" transparent="1" halign="left" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1650,970" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,40" size="40,40" foregroundColor="#1edb76" backgroundColor="#50000000" zPosition="2" transparent="1" />
	<eLabel name="menu" text="♪" position="1272,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="left" font="xtraRegular; 40" />
	<eLabel name="infox" text="█" position="1807,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="right" font="xtraRegular; 40" />
	<eLabel name="" position="0,0" size="1920,1080" transparent="0" backgroundColor="#20000000" zPosition="-5" />
	<eLabel name="" position="0,120" size="1920,2" transparent="0" backgroundColor="#00dcfc" zPosition="0" />
	<ePixmap position="30,30" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/TMDB_thumb.png" backgroundColor="#50000000" alphatest="blend" transparent="1" scale="stretch" />
	<widget name="logo0" position="1300,800" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<widget name="logo1" position="1450,800" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<widget name="logo2" position="1600,800" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<widget name="logo3" position="1750,800" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	{}
</screen>
""".format(aListbox)
xtraInfoPerson_1080_tmdb2 = """
<screen name="xtraInfoPerson" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<eLabel name="" position="0,120" size="1920,2" transparent="0" backgroundColor="#00dcfc" zPosition="0" />
	<ePixmap position="30,30" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/TMDB_thumb.png" backgroundColor="#20000000" alphatest="blend" transparent="1" scale="stretch" />
	<widget name="biography" position="401,140" size="763,524" transparent="1" font="Regular; 18" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="left" valign="top" zPosition="2" />
	<widget name="pinfo" position="70,605" size="300,60" transparent="1" font="xtraRegular;22" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="left" valign="top" zPosition="2" />
	<widget name="poster" position="70,140" size="300,450" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget name="known_for0" position="1260,140" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_for1" position="1465,140" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_for2" position="1670,140" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText0" position="1260,440" size="185,120" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText1" position="1466,440" size="185,120" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText2" position="1670,440" size="185,120" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="status" position="1259,873" size="600,45" transparent="1" font="xtraRegular;30" foregroundColor="#92f1fc" backgroundColor="#20000000" />
	<!--<widget name="int_statu" position="1819,60" size="40,40" transparent="1" text="●" font="xtraIcons; 36" foregroundColor="#1edb76" backgroundColor="#20000000" zPosition="2" halign="center" /> -->
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="75,965" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,40" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#20000000" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1315,970" size="150,45" transparent="1" halign="left" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1650,970" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,40" size="40,40" foregroundColor="#1edb76" backgroundColor="#20000000" zPosition="2" transparent="1" />
	<eLabel name="menu" text="♪" position="1272,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="left" font="xtraRegular; 40" />
	<eLabel name="infox" text="█" position="1807,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="right" font="xtraRegular; 40" />
	<eLabel backgroundColor="#ff8080" cornerRadius="20" position="60,977" size="10,10" transparent="0" zPosition="1" />
	<eLabel name="" position="0,0" size="1920,1080" transparent="0" backgroundColor="#20000000" zPosition="-5" />
{}
</screen>
""".format(aListbox)
black="#000000"
transparent="#ff000000"
	# <eRectangle backgroundGradient="#000000,#111115,#222225,horizontal" position="300,230" size="100,70" zPosition="2" cornerRadius="10" scale="stretch" />
# <eLabel backgroundColor="#222225" position="300,230" size="100,70" zPosition="2" cornerRadius="10" scale="stretch" />





xtraInfo_1080_tmdb3 = """
<screen name="xtraInfo" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/back_fhd2.png" backgroundColor="#ff000000" alphatest="blend" transparent="1" />
	<widget name="poster" position="60,140" size="185,278" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget name="backdrop" position="0,0" size="1920,1080" transparent="1" alphatest="off" zPosition="-5" scale="stretch" />
	<widget source="session.Event_Now" render="Label" position="300,140" size="1000,40" font="xtraBold; 32" halign="left" transparent="1" zPosition="5" foregroundColor="#00ffffff" backgroundColor="#50000000" valign="top">
		<convert type="xtraInfo2">\c0000????,\c00??????,\n, Title</convert>
	</widget>
	
	<eLabel backgroundColor="#111115" position="300,230" size="80,80" zPosition="2" cornerRadius="50" scale="stretch" />
	<widget render="xtraCircleProgress" source="session.FrontendStatus" position="310,240" size="60,60" backgroundColor="#111115" mode="rating" scale="2" pixmapCircle="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150blue1.png" pixmapCircleBack="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/circleProgress/prgrs150back.png" zPosition="3" transparent="1" />
	
	<widget source="session.Event_Now" position="64,454" size="1100,220" render="xtraRunningText" options="movetype=running,startdelay=3000,steptime=60,direction=top,startpoint=0,wrap=1,always=0,repeat=2,oneshot=1" font="xtraRegular; 22" halign="left" transparent="1" zPosition="5" foregroundColor="#00ffffff" backgroundColor="#50000000" valign="top">
		<convert type="xtraInfo2">\c0000????,\c00??????,\n, Description</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="410,255" size="500,30" font="xtraRegular; 24" halign="left" transparent="1" zPosition="5" backgroundColor="#50000000" valign="center">
		<convert type="xtraInfo2">tmdbRatingFull</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="300,191" size="800,30" font="xtraRegular; 24" halign="left" transparent="1" zPosition="2" backgroundColor="#50000000" valign="top">
		<convert type="xtraInfo2">\c0000????,\c00??????, compact, Year, Rated, Genre, Countries, Duration</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="300,330" size="600,30" font="xtraRegular; 24" halign="left" transparent="1" zPosition="2" backgroundColor="#50000000" valign="center">
		<convert type="xtraInfo2">\c0000????,\c00??????,Director</convert>
	</widget>
	<widget source="session.Event_Now" backgroundColor="#50000000" font="xtraRegular; 24" zPosition="2" halign="right" position="1060,915" size="800,30" render="Label" transparent="1" foregroundColor="#00cccccc">
		<convert type="xtraEventInfo">EventNameCompact</convert>
	</widget>	 
	<widget source="session.Event_Now" render="Progress" position="60,945" size="1800,2" foregroundColor="#000089fa" backgroundColor="#435156" transparent="0" zPosition="2">
		<convert type="EventTime">Progress</convert>
	</widget>
	<eLabel backgroundColor="#ff8080" cornerRadius="20" position="60,977" size="10,10" transparent="0" zPosition="1" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="75,965" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraIcons;30" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="555,375" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="300,375" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraIcons; 30" foregroundColor="#c5c5c5" backgroundColor="#50000000" position="830,375" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,40" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#50000000" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1315,970" size="150,45" transparent="1" halign="left" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1650,970" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,40" size="40,40" foregroundColor="#1edb76" backgroundColor="#50000000" zPosition="2" transparent="1" />
	<eLabel name="menu" text="♪" position="1272,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="left" font="xtraRegular; 40" />
	<eLabel name="infox" text="█" position="1807,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="right" font="xtraRegular; 40" />
	
	<eLabel name="" position="0,120" size="1920,2" transparent="0" backgroundColor="#00dcfc" zPosition="0" />
	<ePixmap position="30,30" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/TMDB_thumb.png" backgroundColor="#50000000" alphatest="blend" transparent="1" scale="stretch" />
	<widget name="logo0" position="1522,140" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<widget name="logo1" position="1619,140" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<widget name="logo2" position="1715,140" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	<widget name="logo3" position="1811,140" size="92,92" transparent="1" alphatest="blend" zPosition="11" />
	{}
	<widget name="statusicon" position="450,45" size="20,20" zPosition="99" alphatest="on" pixmaps="icons/marker.png,icons/music.png,icons/folder.png"/>

</screen>
""".format(aListbox)


# <eLabel name="" position="0,0" size="1920,1080" transparent="0" backgroundColor="#20000000" zPosition="-5" />

xtraInfoPerson_1080_tmdb3 = """
<screen name="xtraInfoPerson" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
  <ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/back_fhd2.png" backgroundColor="transparent" alphatest="blend" transparent="1" />
  <widget name="backdrop" position="0,0" size="1920,1080" transparent="1" alphatest="off" zPosition="-5" scale="stretch" />
  <eLabel name="" position="0,120" size="1920,2" transparent="0" backgroundColor="#dcfc" zPosition="0" />
  <ePixmap position="30,30" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/TMDB_thumb.png" backgroundColor="#20000000" alphatest="blend" transparent="1" scale="stretch" />
  <widget name="biography" position="401,140" size="850,450" transparent="1" font="xtraRegular; 20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="left" valign="top" zPosition="2" />
  <widget name="pinfo" position="70,605" size="300,60" transparent="1" font="xtraRegular;22" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="left" valign="top" zPosition="2" />
  <widget name="poster" position="70,140" size="300,450" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
  <widget name="known_for0" position="1315,140" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
  <widget name="known_for1" position="1510,140" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
  <widget name="known_for2" position="1705,140" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
  <widget name="known_forText0" position="1315,430" size="185,50" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
  <widget name="known_forText1" position="1510,430" size="185,50" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
  <widget name="known_forText2" position="1705,430" size="185,50" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
  <!--<widget name="int_statu" position="1819,60" size="40,40" transparent="1" text="●" font="xtraIcons; 36" foregroundColor="#1edb76" backgroundColor="#20000000" zPosition="2" halign="center" /> -->
  <widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="75,965" size="255,45" halign="left" transparent="1" zPosition="1" />
  <widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
  <widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
  <widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
  <widget source="global.CurrentTime" render="Label" position="1259,40" size="600,40" font="xtraRegular; 30" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#50000000" zPosition="1">
	<convert type="ClockToText">Default</convert>
  </widget>

  <eLabel name="" text=" INFO" position="1650,970" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
  <widget name="int_statu" font="xtraIcons; 30" position="1828,45" size="40,40" foregroundColor="#1edb76" backgroundColor="#50000000" zPosition="2" transparent="1" />

  <eLabel name="infox" text="█" position="1807,964" size="40,40" backgroundColor="tb" transparent="1" halign="right" font="xtraRegular; 40" />
  <eLabel backgroundColor="#ff8080" cornerRadius="20" position="60,977" size="10,10" transparent="0" zPosition="1" />

{}
</screen>
""".format(aListbox)


xtraInfo_1080_imdb1 = """
<screen name="xtraInfo" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
	<widget source="Title" render="Label" position="30,55" size="1165,60" font="xtraRegular; 34" halign="center" valign="center" foregroundColor="white" backgroundColor="#15202b" transparent="1" />
	<widget name="poster" position="60,130" size="185,278" transparent="1" alphatest="off" zPosition="5" cornerRadius="20" scale="stretch" />
	<widget name="backdrop_0" position="60,760" size="300,170" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget name="backdrop_1" position="460,760" size="300,170" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget name="backdrop_2" position="860,760" size="300,170" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />


	<widget name="backdrop_0" position="60,760" size="300,170" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<ePixmap position="60,430" size="200,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star_back.png" transparent="1" zPosition="1" alphatest="blend" />
	<widget name="ratingStar" position="60,430" size="200,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star.png" transparent="1" zPosition="2" alphatest="blend" />
	<widget source="session.Event_Now" render="Label" position="60,460" size="300,30" font="xtraRegular; 22" halign="left" transparent="1" zPosition="5" backgroundColor="#111111" valign="center">
		<convert type="xtraInfo">imdbRating</convert>
	</widget>
	<widget source="session.Event_Now" position="60,500" size="1042,341" render="xtraRunningText" options="movetype=running,startdelay=8000,steptime=60,direction=top,startpoint=0,wrap=1,always=0,repeat=2,oneshot=1" font="xtraRegular; 22" halign="left" transparent="1" zPosition="5" foregroundColor="white" backgroundColor="#15202b" valign="top">
		<convert type="xtraInfo2">\c00ffcc00,\c00??????,Description</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="300,130" size="600,30" font="xtraBold; 24" halign="left" transparent="1" zPosition="2" backgroundColor="#15202b" valign="top">
		<convert type="xtraInfo2">Title</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="300,160" size="600,130" font="xtraRegular; 20" halign="left" transparent="1" zPosition="2" backgroundColor="#15202b" valign="top">
		<convert type="xtraInfo2">\c00ffff99,\c00??????, Writers, Director, Actors</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="300,250" size="900,30" font="xtraRegular; 20" halign="left" transparent="1" zPosition="2" backgroundColor="#20000000" valign="top">
		<convert type="xtraInfo2">•releaseYear,Rated,Duration</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="60,700" size="1100,30" font="xtraRegular; 24" cornerRadius="30" halign="center" transparent="0" zPosition="2" backgroundColor="#284157" valign="center">
		<convert type="xtraInfo2">Genre</convert>
	</widget>
	<widget source="session.Event_Now" render="Progress" position="60,945" size="1110,2" foregroundColor="blue" backgroundColor="#435156" transparent="0" zPosition="9">
		<convert type="EventTime">Progress</convert>
	</widget>
	<widget source="help" position="662,890" size="500,40" render="Label" font="xtraRegular;28" foregroundColor="#f3fc92" backgroundColor="#15202b" halign="center" valign="center" transparent="1" />
	<widget name="status" position="61,891" size="600,45" transparent="1" font="xtraRegular;30" foregroundColor="#92f1fc" backgroundColor="#15202b" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraIcons;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraIcons;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraIcons; 30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1315,970" size="150,45" transparent="1" halign="left" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1650,970" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,60" size="40,40" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" transparent="1" />
	<eLabel name="menu" text="♪" position="1272,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="left" font="xtraRegular; 40" />
	<eLabel name="infox" text="█" position="1807,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="right" font="xtraRegular; 40" />
	<ePixmap position="60,50" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/IMDB_thumb.png" backgroundColor="#15202b" alphatest="blend" transparent="1" scale="stretch" />
	<eLabel name="" text="Casts" position="1260,122" size="200,20" font="xtraRegular;18" foregroundColor="b7" backgroundColor="#15202b" halign="left" valign="top" zPosition="1" transparent="1" />
	%s
</screen>"""%(aListbox)
xtraInfoPerson_1080_imdb1 = """
<screen name="xtraInfoPerson" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd_3.png" transparent="1" />
	<ePixmap position="60,50" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/IMDB_thumb.png" backgroundColor="#15202b" alphatest="blend" transparent="1" scale="stretch" />
	<widget source="Title" render="Label" position="30,55" size="1165,60" font="xtraRegular; 34" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#15202b" transparent="1" />
	<widget name="biography" position="70,527" size="1096,409" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="left" valign="top" zPosition="2" />
	<widget name="poster" position="70,135" size="140,140" transparent="1" alphatest="off" zPosition="1" cornerRadius="30" scale="stretch" />
	<!--<widget name="int_statu" position="1819,60" size="40,40" transparent="1" text="●" font="xtraRegular; 36" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" halign="center" /> -->
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="60,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="345,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="630,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#15202b" position="915,965" size="255,45" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#15202b" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1315,970" size="150,45" transparent="1" halign="left" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1650,970" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,60" size="40,40" foregroundColor="#1edb76" backgroundColor="#15202b" zPosition="2" transparent="1" />
	<eLabel name="menu" text="♪" position="1272,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="left" font="xtraRegular; 40" />
	<eLabel name="infox" text="█" position="1807,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="right" font="xtraRegular; 40" />
	<eLabel name="" text="Casts" position="1260,122" size="200,20" font="xtraRegular;18" foregroundColor="#0000ffff" backgroundColor="#15202b" halign="left" valign="top" zPosition="1" transparent="1" />
	<eLabel name="" text="Known For" position="347,135" size="200,40" font="xtraRegular;20" foregroundColor="#0000ffff" backgroundColor="#15202b" halign="right" valign="top" zPosition="1" transparent="1" />
	<widget name="known_for0" position="555,135" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_for1" position="765,135" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_for2" position="975,135" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText0" position="555,430" size="185,90" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText1" position="765,430" size="185,90" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText2" position="975,430" size="185,90" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#15202b" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	{}
</screen>
""".format(aListbox)

xtraInfo_1080_imdb2 = """
<screen name="xtraInfo" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<widget source="Title" render="Label" position="60,90" size="1165,60" font="xtraBold; 34" halign="left" valign="center" foregroundColor="white" backgroundColor="#20000000" transparent="1" />
	<widget name="poster" position="60,225" size="400,600" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<widget source="session.Event_Now" render="Label" position="60,155" size="1425,26" font="xtraRegular; 20" halign="left" transparent="1" zPosition="2" backgroundColor="#20000000" valign="top">
		<convert type="xtraInfo2">\c00ffff99,\c00cccccc, Title</convert>
	</widget>
	<ePixmap position="900,140" size="72,70" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star1_back.png" transparent="1" zPosition="1" alphatest="blend" />
	<widget name="ratingStar" position="900,140" size="72,70" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/star/star1.png" transparent="1" zPosition="9" alphatest="blend" />
	<widget source="session.Event_Now" render="Label" position="990,145" size="350,60" font="xtraRegular; 24" halign="left" transparent="1" zPosition="9" backgroundColor="#20000000" valign="center">
		<convert type="xtraInfo2">imdbRating2</convert>
	</widget>
	<widget source="session.Event_Now" position="550,750" size="860,70" render="Label" font="xtraRegular; 16" halign="left" transparent="1" zPosition="99" foregroundColor="#cccccc" backgroundColor="#50000000" valign="top">
		<convert type="xtraInfo2">\c00ffcc00,\c00ffffff,Description</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="60,845" size="1425,28" font="Regular; 24" halign="left" transparent="1" zPosition="2" backgroundColor="#20000000" valign="top">
		<convert type="xtraInfo2">\c00ffff99,\c00ffffff,Director</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="60,890" size="1425,28" font="Regular; 24" halign="left" transparent="1" zPosition="2" backgroundColor="#20000000" valign="top">
		<convert type="xtraInfo2">\c00ffff99,\c00??????,Writers</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="60,935" size="1425,28" font="Regular; 24" halign="left" transparent="1" zPosition="2" backgroundColor="#20000000" valign="top">
		<convert type="xtraInfo2">\c00ffff99,\c00??????,Actors</convert>
	</widget>
	<widget source="session.Event_Now" render="Label" position="60,185" size="1425,30" font="xtraRegular; 20" halign="left" transparent="1" zPosition="2" backgroundColor="#20000000" valign="top">
		<convert type="xtraInfo2">\c00ffff99,\c00??????,•releaseYear,Rated,Duration,Genre</convert>
	</widget>

	<widget source="session.Event_Now" render="Progress" position="60,980" size="1800,2" foregroundColor="blue" backgroundColor="#435156" transparent="0" zPosition="9">
		<convert type="EventTime">Progress</convert>
	</widget>
	<eLabel backgroundColor="#ff8080" cornerRadius="20" position="60,1017" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#80ff80" cornerRadius="20" position="345,1017" size="10,10" transparent="0" zPosition="1" />
	<eLabel backgroundColor="#80ff" cornerRadius="20" position="910,1017" size="10,10" transparent="0" zPosition="1" />
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="80,1000" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraIcons;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="365,1000" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraIcons;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="645,1000" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraIcons; 30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="935,1000" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1265,33" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#20000000" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1315,1000" size="150,45" transparent="1" halign="left" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1650,1000" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
	<widget name="int_statu" font="xtraIcons; 30" position="1869,35" size="40,40" foregroundColor="#1edb76" backgroundColor="#20000000" zPosition="2" transparent="1" />
	<eLabel name="menu" text="♪" position="1272,999" size="40,40" backgroundColor="tb" transparent="1" halign="left" font="xtraRegular; 40" />
	<eLabel name="infox" text="█" position="1807,999" size="40,40" backgroundColor="tb" transparent="1" halign="right" font="xtraRegular; 40" />
	<ePixmap position="60,15" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/IMDB_thumb.png" backgroundColor="#20000000" alphatest="blend" transparent="1" scale="stretch" />
	{}
	<widget name="uup" position="1800,140" size="40,40" transparent="0" halign="center" valign="center" font="xtraIcons; 22" zPosition="5" foregroundColor="#c5c5c5" backgroundColor="#333333" cornerRadius="30" />
	<widget name="dwn" position="1800,920" size="40,40" transparent="0" halign="center" valign="center" font="xtraIcons; 22" zPosition="5" foregroundColor="#c5c5c5" backgroundColor="#333333" cornerRadius="30" />
	<widget name="lft" position="550,540" size="40,40" transparent="0" halign="center" valign="center" font="xtraIcons; 22" zPosition="5" foregroundColor="#c5c5c5" backgroundColor="#333333" cornerRadius="30" />
	<widget name="rght" position="1370,540" size="40,40" transparent="0" halign="center" valign="center" font="xtraIcons; 22" zPosition="5" foregroundColor="#c5c5c5" backgroundColor="#333333" cornerRadius="30" />

	<eLabel name="" position="0,0" size="1920,1080" transparent="0" backgroundColor="#20000000" zPosition="-2" />
	<eLabel name="" position="540,740" size="880,70" transparent="0" zPosition="2" backgroundColor="#50000000" cornerRadius="20" scale="stretch" />


</screen>
""".format(aListbox)

	# <eLabel name="" text="˄" position="1800,140" size="40,40" transparent="0" halign="center" valign="center" font="xtraRegular; 40" zPosition="5" foregroundColor="#c5c5c5" backgroundColor="#20000000" cornerRadius="30" />
	# <eLabel name="" text="˅" position="1800,920" size="40,40" transparent="0" halign="center" valign="center" font="xtraRegular; 40" zPosition="5" foregroundColor="#c5c5c5" backgroundColor="#20000000" cornerRadius="30" />

	# <eLabel name="" text="˂" position="550,500" size="40,40" transparent="0" halign="center" valign="center" font="xtraRegular; 40" zPosition="5" foregroundColor="#c5c5c5" backgroundColor="#20000000" cornerRadius="30" />
	# <eLabel name="" text="˃" position="1370,500" size="40,40" transparent="0" halign="center" valign="center" font="xtraRegular; 40" zPosition="5" foregroundColor="#c5c5c5" backgroundColor="#20000000" cornerRadius="30" />

xtraInfoPerson_1080_imdb2 = """
<screen name="xtraInfoPerson" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<eLabel name="" position="0,-3" size="1920,1080" transparent="0" backgroundColor="#20000000" zPosition="-5" />
	<ePixmap position="844,6" size="100,60" zPosition="9" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/logos/IMDB_thumb.png" backgroundColor="#20000000" alphatest="blend" transparent="1" scale="stretch" />
	<widget source="Title" render="Label" position="70,55" size="1165,60" font="xtraRegular; 34" halign="left" valign="center" foregroundColor="#00ffffff" backgroundColor="#20000000" transparent="1" />
	<widget name="biography" position="70,527" size="1096,409" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="left" valign="top" zPosition="2" />
	<widget name="poster" position="70,135" size="185,185" transparent="1" alphatest="off" zPosition="1" cornerRadius="20" scale="stretch" />
	<eLabel backgroundColor="#ff8080" cornerRadius="20" position="60,977" size="10,10" transparent="0" zPosition="1" />	
	<widget name="key_red" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="80,965" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_green" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="365,965" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_yellow" render="Label" font="xtraRegular;30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="610,965" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget name="key_blue" render="Label" font="xtraRegular; 30" foregroundColor="#c5c5c5" backgroundColor="#20000000" position="935,965" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="xtraRegular; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#20000000" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1315,970" size="150,45" transparent="1" halign="left" font="xtraRegular; 30" />
	<eLabel name="" text=" INFO" position="1650,970" size="150,45" transparent="1" halign="right" font="xtraRegular; 30" />
	<widget name="int_statu" font="xtraIcons; 30" position="1828,60" size="40,40" foregroundColor="#1edb76" backgroundColor="#20000000" zPosition="2" transparent="1" />
	<eLabel name="menu" text="♪" position="1272,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="left" font="xtraRegular; 40" />
	<eLabel name="infox" text="█" position="1807,964" size="40,40" backgroundColor="#50000000" transparent="1" halign="right" font="xtraRegular; 40" />
	<eLabel name="" text="Casts" position="1260,122" size="200,20" font="xtraRegular;18" foregroundColor="#0000ffff" backgroundColor="#20000000" halign="left" valign="top" zPosition="1" transparent="1" />
	<eLabel name="" text="Known For" position="347,135" size="200,40" font="xtraRegular;20" foregroundColor="#0000ffff" backgroundColor="#20000000" halign="right" valign="top" zPosition="1" transparent="1" />
	<widget name="known_for0" position="555,135" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_for1" position="765,135" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_for2" position="975,135" size="185,278" transparent="1" alphatest="off" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText0" position="555,430" size="185,90" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText1" position="765,430" size="185,90" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	<widget name="known_forText2" position="975,430" size="185,90" transparent="1" font="xtraRegular;20" foregroundColor="#c5c5c5" backgroundColor="#20000000" halign="center" valign="top" zPosition="11" cornerRadius="20" scale="stretch" />
	{}
</screen>
""".format(aListbox)
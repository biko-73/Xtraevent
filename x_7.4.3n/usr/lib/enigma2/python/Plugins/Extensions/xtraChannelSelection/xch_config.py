
from Components.config import config, configfile, ConfigYesNo, ConfigSubsection, ConfigSelection, getConfigListEntry, ConfigText, ConfigSelectionNumber, ConfigSlider
from Components.ConfigList import ConfigListScreen

config.plugins.xCH = ConfigSubsection()
config.plugins.xCH.style = ConfigSelection(default = "vertical", choices = [("horizontal"), ("horizontal_2"), ("horizontal_3"), ("grid"), ("vertical"), ("vertical_2"), ("vertical_3")])
config.plugins.xCH.epgX = ConfigYesNo(default = False)
config.plugins.xCH.Images = ConfigSelection(default="Backdrop", choices=[
	("Poster"), 
	("Backdrop"),
	("Picon"),	   
	])

config.plugins.xCH.ProgressColor = ConfigSelection(default = "Color", choices = [("Color"), ("Gradient")])
config.plugins.xCH.colorR = ConfigSlider(default=120, increment=50, limits=(0,255))
config.plugins.xCH.colorG = ConfigSlider(default=120, increment=50, limits=(0,255))
config.plugins.xCH.colorB = ConfigSlider(default=120, increment=50, limits=(0,255))

config.plugins.xCH.colorR1 = ConfigSlider(default=120, increment=50, limits=(0,255))
config.plugins.xCH.colorG1 = ConfigSlider(default=120, increment=50, limits=(0,255))
config.plugins.xCH.colorB1 = ConfigSlider(default=120, increment=50, limits=(0,255))

config.plugins.xCH.colorR2 = ConfigSlider(default=120, increment=50, limits=(0,255))
config.plugins.xCH.colorG2 = ConfigSlider(default=120, increment=50, limits=(0,255))
config.plugins.xCH.colorB2 = ConfigSlider(default=120, increment=50, limits=(0,255))

config.plugins.xCH.colorR3 = ConfigSlider(default=120, increment=50, limits=(0,255))
config.plugins.xCH.colorG3 = ConfigSlider(default=120, increment=50, limits=(0,255))
config.plugins.xCH.colorB3 = ConfigSlider(default=120, increment=50, limits=(0,255))

config.plugins.xCH.ProgressGradientColor = ConfigSelection(default = "Color1", choices = [("Color1"), ("Color2"), ("Color3")])
config.plugins.xCH.prgrsColor = ConfigText(default="000000")
config.plugins.xCH.prgrsColor1 = ConfigText(default="000000")
config.plugins.xCH.prgrsColor2 = ConfigText(default="000000")
config.plugins.xCH.prgrsColor3 = ConfigText(default="000000")




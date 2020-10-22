# -*- coding: utf-8 -*-
# Copyright (C) 2020 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import addonHandler
import globalVars
import gui
import wx
import shutil
import os
addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.manifest['name'] == "zRadio":
			dirOrigen =os.path.join(globalVars.appArgs.configPath)
			dirDestino =os.path.join(globalVars.appArgs.configPath, "zRadio")
			fileOptions = os.path.join(dirOrigen, "opciones.dat")
			fileOptionsRadio = os.path.join(dirOrigen, "opt_radio.dat")
			fileFavRadio = os.path.join(dirOrigen, "fav_radios.dat")
			if os.path.exists(dirDestino):
				pass
			else:
				os.mkdir(os.path.join(dirOrigen, "zRadio"))
				if os.path.isfile(fileOptions):
					shutil.move(fileOptions, os.path.join(dirDestino, "opciones.dat"))
				if os.path.isfile(fileOptionsRadio):
					shutil.move(fileOptionsRadio, os.path.join(dirDestino, "opt_radio.dat"))
				if os.path.isfile(fileFavRadio):
					shutil.move(fileFavRadio, os.path.join(dirDestino, "fav_radios.dat"))


			break

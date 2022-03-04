# -*- coding: utf-8 -*-
# Copyright (C) 2020 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

# import the necessary modules (NVDA)
import globalPluginHandler
import addonHandler
import gui
import globalVars
import ui
import wx
import wx.adv
from scriptHandler import script
from tones import beep
from threading import Thread
# import the necessary modules (Python)
from . import xgui
from .chkConexion import InternetChecker
from .variables import *
from .pubsub import pub
try:
	from .raspado import *
except:
	pass

# For translation
addonHandler.initTranslation()

chkInternet = InternetChecker()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()

		self._MainWindows = None

		# Creation of our menu.
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		# Translators: Name of the item in the tools menu
		self.menuItem = self.toolsMenu.Append(wx.ID_ANY, _("&zRadio para NVDA"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.dlgPrincipal, self.menuItem)

	def terminate(self):
		try:
			self.toolsMenu .Remove(self.menuItem)
		except Exception:
			pass
		try:
			if not self._MainWindows:
				self._MainWindows.Destroy()
		except (AttributeError, RuntimeError):
			pass
		super().terminate()

	def dlgPrincipal(self, event):
		if chkInternet.test_internet("https://www.google.es") == False:
			# Translators: Error message for not having internet
			xguiMsg = \
_("""zRadio necesita internet para ser ejecutado.
Asegurese de que tiene todo correcto.""")
			xgui.Mensaje(xguiMsg,
				# Translators: Message window title: Error
				_("Error"), 0)
			return

		self.launchOpciones()

# Calling the main window of the plug-in
		if not self._MainWindows:
			self._MainWindows = MainWindows(gui.mainFrame)

		if not self._MainWindows.IsShown():
			gui.mainFrame.prePopup()
			self._MainWindows.Show()

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Muestra la ventana principal de zRadio"), category= "zRadio")
	def script_dlgPrincipal(self, gesture):
		wx.CallAfter(self.dlgPrincipal, None)

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Bajar volumen"), category= "zRadio")
	def script_BajarVolumen(self, gesture):
		global volumenGeneral
		if volumenGeneral == 0:
			# Translators: Volume warning message -
			ui.message(_("No se puede bajar más el volumen ya se encuentra al 0%"))
		else:
			if not self._MainWindows:
				vol1 = volumenGeneral - 1
				volumenGeneral = vol1
				player.volumen(volumenGeneral)
			else:
				wx.CallAfter(pub.sendMessage, "VolumenMenos")

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Subir volumen"), category= "zRadio")
	def script_SubirVolumen(self, gesture):
		global volumenGeneral
		if volumenGeneral == 100:
			# Translators: Volume warning message +
			ui.message(_("No se puede subir más el volumen ya se encuentra al 100%"))
		else:
			if not self._MainWindows:
				vol1 = volumenGeneral + 1
				volumenGeneral = vol1
				player.volumen(volumenGeneral)
			else:
				wx.CallAfter(pub.sendMessage, "VolumenMas")

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Detener reproducción"), category= "zRadio")
	def script_Detener(self, gesture):
		global nombreTitulo, urlReproducir, controlON, controlSilenciar
		if controlON == False:
			# Translators: Information message
			ui.message(_("No hay nada reproduciéndose"))
		else:
			if not self._MainWindows:
				player.mute(False)
				player.stop()
				controlON = False
				controlSilenciar = False
				nombreTitulo = ""
				urlReproducir = ""
			else:
				wx.CallAfter(pub.sendMessage, "Detener", event=None)

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Recargar reproducción"), category= "zRadio")
	def script_Recargar(self, gesture):
		global nombreTitulo, urlReproducir, controlON, controlSilenciar
		if urlReproducir == "":
			# Translators: Information message
			ui.message(_("No hay nada para recargar"))
		else:
			if not self._MainWindows:
				if chkInternet.test_internet(urlReproducir) == False:
					# Translators: Error information message when loading the station
					xguiMsg = \
_("""No se pudo cargar la emisora.

Asegúrese de que tiene conexión a internet.

Otros motivos pueden ser que la emisora tenga problemas en estos momentos.

Inténtelo más tarde.""")
					xgui.Mensaje(xguiMsg,
						# Translators: Message window title: Error
						_("Error"), 0)
					controlON = False
					controlSilenciar = False
					nombreTitulo = ""
					urlReproducir = ""
					player.mute(False)
					player.stop()
				else:
					if controlSilenciar == True:
						controlSilenciar = False
						player.mute(False)
					player.volumen(volumenGeneral)
					player.play(urlReproducir)
			else:
				wx.CallAfter(pub.sendMessage, "Recargar", event=None)

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Poner y quitar silencio"), category= "zRadio")
	def script_Silenciar(self, gesture):
		global controlSilenciar
		if controlON == False:
			# Translators: Information message
			ui.message(_("No hay nada para silenciar"))
		else:
			if not self._MainWindows:
				if controlSilenciar == False:
					player.mute(True)
					controlSilenciar = True
				else:
					player.mute(False)
					controlSilenciar = False
			else:
				wx.CallAfter(pub.sendMessage, "Silenciar", event=None)

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Saber emisora en reproducción"), category= "zRadio")
	def script_TituloEmisora(self, gesture):
		if nombreTitulo == "":
			# Translators: Information message
			ui.message("No hay nada reproduciéndose")
		else:
			# Translators: Information message with the name of the station loaded in memory
			ui.message(_("Emisora en memoria: %s") % nombreTitulo)

	def launchOpciones(self):
		global Radios, gen_nombre_radios, gen_url_radios, fav_nombre_radios, fav_url_radios, PestañaGeneralRadioOpciones
		if Radios == None:
			Radios = Raspado_Radios()
### Radio
			Opciones.Cargar_Opciones_Radio()
			PestañaGeneralRadioOpciones = Opciones.PestañaGeneralRadioOpciones
			if PestañaGeneralRadioOpciones[0] == "":
				# Translators: Message without stations
				gen_nombre_radios = [_("Sin emisoras.")]
				gen_url_radios = []
			elif  PestañaGeneralRadioOpciones[0] == "Pais":
				Radios.Resultado_Paises(PestañaGeneralRadioOpciones[1])
				gen_nombre_radios = Radios.nombre_radios_pais
				gen_url_radios = Radios.url_radios_pais
			elif  PestañaGeneralRadioOpciones[0] == "Idioma":
				Radios.Resultado_Idioma_Global(PestañaGeneralRadioOpciones[1])
				gen_nombre_radios = Radios.nombre_radios_pais
				gen_url_radios = Radios.url_radios_pais
			elif  PestañaGeneralRadioOpciones[0] == "Etiqueta":
				Radios.Resultado_Tag_Global(PestañaGeneralRadioOpciones[1])
				gen_nombre_radios = Radios.nombre_radios_pais
				gen_url_radios = Radios.url_radios_pais

			Opciones.Cargar_Buffer_Favoritos_Radio()
			fav_nombre_radios = Opciones.fav_nombre_radios
			fav_url_radios = Opciones.fav_url_radios

	def runAction(self, valor):
		global nombreTitulo, urlReproducir, controlON, controlSilenciar

		self.launchOpciones()

		try:
			if valor == 1:
				temp1 = fav_nombre_radios[0]
				temp2 = fav_url_radios[0]
			elif valor == 2:
				temp1 = fav_nombre_radios[1]
				temp2 = fav_url_radios[1]
			elif valor == 3:
				temp1 = fav_nombre_radios[2]
				temp2 = fav_url_radios[2]
			elif valor == 4:
				temp1 = fav_nombre_radios[3]
				temp2 = fav_url_radios[3]
			elif valor == 5:
				temp1 = fav_nombre_radios[4]
				temp2 = fav_url_radios[4]
			if chkInternet.test_internet(temp2) == False:
				# Translators: Error information message when loading the station
				xguiMsg = \
_("""No se pudo cargar la emisora.

Asegúrese de que tiene conexión a internet.

Otros motivos pueden ser que la emisora tenga problemas en estos momentos.

Inténtelo más tarde.""")
				ui.message(xguiMsg)
			else:
				if valor == 1:
					nombreTitulo = fav_nombre_radios[0]
					urlReproducir = fav_url_radios[0]
				elif valor == 2:
					nombreTitulo = fav_nombre_radios[1]
					urlReproducir = fav_url_radios[1]
				elif valor == 3:
					nombreTitulo = fav_nombre_radios[2]
					urlReproducir = fav_url_radios[2]
				elif valor == 4:
					nombreTitulo = fav_nombre_radios[3]
					urlReproducir = fav_url_radios[3]
				elif valor == 5:
					nombreTitulo = fav_nombre_radios[4]
					urlReproducir = fav_url_radios[4]
				if not self._MainWindows:
					if controlON == True:
						if controlSilenciar == True:
							controlSilenciar = False
							player.mute(False)
						player.volumen(volumenGeneral)
						player.play(urlReproducir)
					else:
						controlON = True
						player.inicio()
						player.volumen(volumenGeneral)
						player.play(urlReproducir)
				else:
					wx.CallAfter(pub.sendMessage, "EmisorasRapidas")
		except IndexError:
			if valor == 1:
				# Translators: Information message
				ui.message(_("No tiene ninguna emisora en Favoritos en la posición 1"))
			elif valor == 2:
				# Translators: Information message
				ui.message(_("No tiene ninguna emisora en Favoritos en la posición 2"))
			elif valor == 3:
				# Translators: Information message
				ui.message(_("No tiene ninguna emisora en Favoritos en la posición 3"))
			elif valor == 4:
				# Translators: Information message
				ui.message(_("No tiene ninguna emisora en Favoritos en la posición 4"))
			elif valor == 5:
				# Translators: Information message
				ui.message(_("No tiene ninguna emisora en Favoritos en la posición 5"))

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Reproducir emisora rápidamente 1"), category= "zRadio")
	def script_Rapida1(self, gesture):
		self.runAction(1)

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Reproducir emisora rápidamente 2"), category= "zRadio")
	def script_Rapida2(self, gesture):
		self.runAction(2)

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Reproducir emisora rápidamente 3"), category= "zRadio")
	def script_Rapida3(self, gesture):
		self.runAction(3)

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Reproducir emisora rápidamente 4"), category= "zRadio")
	def script_Rapida4(self, gesture):
		self.runAction(4)

	# Translators: Description for Input Gestures dialog for zRadio
	@script(gesture=None, description= _("Reproducir emisora rápidamente 5"), category= "zRadio")
	def script_Rapida5(self, gesture):
		self.runAction(5)

if globalVars.appArgs.secure:
	GlobalPlugin = globalPluginHandler.GlobalPlugin # noqa: F811 

class MainWindows(wx.Dialog):
	def __init__(self, parent):
		WIDTH = 800
		HEIGHT = 600
		pos = xgui._calculatePosition(WIDTH, HEIGHT)

		# Translators: zRadio window title
		super(MainWindows, self).__init__(parent, -1, title=_("zRadio para NVDA"), pos = pos, size = (WIDTH, HEIGHT))

		self.Panel = wx.Panel(self)

#
		self.RadioDLG = xgui.RadioPrincipal(self.Panel)
		self.RadioDLG.volumenBarra.SetValue(volumenGeneral)
		self.RadioDLG.volumenBarra.Bind(wx.EVT_SLIDER, self.on_set_volume)
		self.RadioDLG.TreeBook.Bind(wx.EVT_TREEBOOK_PAGE_CHANGED, self.CambioPestañaRadio)
		self.RadioDLG.DetenerBTN.Bind(wx.EVT_BUTTON, self.DetenerBoton)
		self.RadioDLG.RecargarBTN.Bind(wx.EVT_BUTTON, self.RecargarBoton)
		self.RadioDLG.SilenciarBTN.Bind(wx.EVT_BUTTON, self.SilenciarBoton)
		self.Bind(wx.EVT_CHAR_HOOK, self.onTeclasRapidas)
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CANCEL)
		self.RadioDLG.AccionBTN.Bind(wx.EVT_BUTTON,self.mostrar_menu_accion)
		self.menu_accion()

#
		self.RadioGeneralDLG = xgui.RadioGeneral(self.RadioDLG.page_1)
		self.RadioGeneralDLG.listbox_radio.Append(gen_nombre_radios)
		self.RadioGeneralDLG.listbox_radio.SetSelection(0)
		self.RadioGeneralDLG.Buscar_radioBTN.Bind(wx.EVT_BUTTON, self.BuscarRadioGeneral)
		self.RadioGeneralDLG.texto_busqueda_radio.Bind(wx.EVT_TEXT_ENTER, self.BuscarRadioGeneral)
		self.RadioGeneralDLG.listbox_radio.Bind(wx.EVT_KEY_UP, self.onTeclasGeneral)
		self.RadioGeneralDLG.listbox_radio.Bind(wx.EVT_CONTEXT_MENU,self.menuContextualLanzador)
		self.menuContextual()

#
		self.RadioFavoritosDLG = xgui.RadioFavoritos(self.RadioDLG.page_2)
		self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.Bind(wx.EVT_BUTTON, self.BuscarRadioFavoritos)
		self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.Bind(wx.EVT_TEXT_ENTER, self.BuscarRadioFavoritos)
		self.RadioFavoritosDLG.listbox_radio_favoritos.Bind(wx.EVT_KEY_UP, self.onTeclasFavoritos)
		self.RadioFavoritosDLG.listbox_radio_favoritos.Bind(wx.EVT_CONTEXT_MENU,self.menuContextualLanzador)
		self.menuContextual()

#
		self.RadioBusquedaDLG = xgui.RadioBusqueda(self.RadioDLG.page_3)
		self.RadioBusquedaDLG.ch_categorias_radio.Append(listaCategoriasBusquedaRadios)
		self.RadioBusquedaDLG.ch_categorias_radio.SetSelection(0)
		self.RadioBusquedaDLG.ch_categorias_radio.Bind(wx.EVT_CHOICE, self.SelectorCategoriaRadioBusqueda)
		self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.Bind(wx.EVT_BUTTON, self.BuscarCategoriaRadio)
		self.RadioBusquedaDLG.texto_busqueda_categoria.Bind(wx.EVT_TEXT_ENTER, self.BuscarCategoriaRadio)
		self.RadioBusquedaDLG.lb_categorias_radio.Bind(wx.EVT_KEY_UP, self.onTeclasBuscador)
		self.RadioBusquedaDLG.lb_categorias_radio.Bind(wx.EVT_CONTEXT_MENU,self.menuContextualLanzador)
		self.menuContextual()

		pub.subscribe(self.BajarVol, "VolumenMenos")
		pub.subscribe(self.SubirVol, "VolumenMas")
		pub.subscribe(self.DetenerBoton, "Detener")
		pub.subscribe(self.RecargarBoton, "Recargar")
		pub.subscribe(self.SilenciarBoton, "Silenciar")
		pub.subscribe(self.ComprobarUrl_Rapidos, "EmisorasRapidas")

		if controlON == True:
			self.onBotonesReproductor()
			self.RadioDLG.DetenerBTN.SetFocus()
			if controlSilenciar == True:
				# Translators: Change button name to Remove Mute
				self.RadioDLG.SilenciarBTN.SetLabel(_("Quitar &Silencio"))

	def onTeclasRapidas(self, event):
		if (event.AltDown(), event.GetKeyCode()) == (True, 86): #  ALT+V Lleva el foco al control de volumen.
			self.RadioDLG.volumenBarra.SetFocus()
		else:
			event.Skip()

	def CambioPestañaRadio(self, event):
		indice = event.GetSelection() # me da el indice de la pestaña

		if indice == 0:
			if PestañaGeneralRadioOpciones[0] == "":
					self.RadioGeneralDLG.listbox_radio.Clear()
					self.RadioGeneralDLG.listbox_radio.Append(gen_nombre_radios)
					self.RadioGeneralDLG.listbox_radio.SetSelection(0)
					self.RadioDLG.AccionBTN.Disable()
			else:
				# Translators: Search button name
				if self.RadioGeneralDLG.Buscar_radioBTN.GetLabel() == _(_("&Buscar")):
					self.RadioGeneralDLG.listbox_radio.Clear()
					self.RadioGeneralDLG.listbox_radio.Append(gen_nombre_radios)
					self.RadioGeneralDLG.listbox_radio.SetSelection(0)
					self.RadioDLG.AccionBTN.Disable()
			event.Skip()

		elif indice == 1:
			if len(fav_nombre_radios) == 0:
				self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
				# Translators: Message in listbox favorites, no favorites
				self.RadioFavoritosDLG.listbox_radio_favoritos.Append(_("No hay favoritos."))
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)
				self.RadioDLG.AccionBTN.Enable()
			else:
				# Translators: Search button name
				if self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.GetLabel() == _(_("&Buscar")):
					self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
					self.RadioFavoritosDLG.listbox_radio_favoritos.Append(fav_nombre_radios)
					self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)
					self.RadioDLG.AccionBTN.Enable()
			event.Skip()

		elif indice == 2:
			self.RadioDLG.AccionBTN.Disable()
			event.Skip()

	def SelectorCategoriaRadioBusqueda(self, event):
		indice = self.RadioBusquedaDLG.ch_categorias_radio.GetSelection() # me da el indice de la seleccion
		nombre_seleccion = self.RadioBusquedaDLG.ch_categorias_radio.    GetString(event.GetSelection()) # Me da el nombre de la seleccion

		if indice == 0:
			# Translators: Search button name
			if self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.GetLabel() == _("&Buscar"):
				# Translators: Searchable tag name
				self.RadioBusquedaDLG.busqueda_categoria_radio.SetLabel(_("Búsqueda general:"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				# Translators: Message in the search listbox, Waiting for a search
				self.RadioBusquedaDLG.lb_categorias_radio.Append(_("Esperando una búsqueda."))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
				self.RadioBusquedaDLG.ch_categorias_radio.SetFocus()
			else:
				# Translators: Searchable tag name
				self.RadioBusquedaDLG.busqueda_categoria_radio.SetLabel(_("Búsqueda general:"))
				# Translators: Search button name
				self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				# Translators: Message in the search listbox, Waiting for a search
				self.RadioBusquedaDLG.lb_categorias_radio.Append(_("Esperando una búsqueda."))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
				self.RadioBusquedaDLG.ch_categorias_radio.SetFocus()

		elif indice == 1:
			# Translators: Search button name
			if self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.GetLabel() == _("&Buscar"):
				# Translators: Searchable tag name
				self.RadioBusquedaDLG.busqueda_categoria_radio.SetLabel(_("Buscar pais:"))
				Radios.Paises_Español()
				Radios.Paises_Cantidad_Emisoras()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				for nombre_item, numero_item in zip(Radios.paises_radio_español, Radios.paises_numero_emisoras):
					# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
					self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
			else:
				# Translators: Searchable tag name
				self.RadioBusquedaDLG.busqueda_categoria_radio.SetLabel(_("Buscar pais:"))
				# Translators: Search button name
				self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				Radios.Paises_Español()
				Radios.Paises_Cantidad_Emisoras()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				for nombre_item, numero_item in zip(Radios.paises_radio_español, Radios.paises_numero_emisoras):
					# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
					self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)

		elif indice == 2:
			# Translators: Search button name
			if self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.GetLabel() == _("&Buscar"):
				# Translators: Searchable tag name
				self.RadioBusquedaDLG.busqueda_categoria_radio.SetLabel(_("Buscar idioma:"))
				Radios.Resultado_Idioma()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				for nombre_item, numero_item in zip(Radios.nombre_idioma, Radios.cantidad_idioma):
					# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
					self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
			else:
				# Translators: Searchable tag name
				self.RadioBusquedaDLG.busqueda_categoria_radio.SetLabel(_("Buscar idioma:"))
				# Translators: Search button name
				self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				Radios.Resultado_Idioma()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				for nombre_item, numero_item in zip(Radios.nombre_idioma, Radios.cantidad_idioma):
					# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
					self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)

		elif indice == 3:
			# Translators: Search button name
			if self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.GetLabel() == _("&Buscar"):
				# Translators: Searchable tag name
				self.RadioBusquedaDLG.busqueda_categoria_radio.SetLabel(_("Buscar etiqueta:"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				# Translators: Message in the search listbox, Waiting for a search
				self.RadioBusquedaDLG.lb_categorias_radio.Append(_("Esperando una búsqueda."))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
				self.RadioBusquedaDLG.ch_categorias_radio.SetFocus()
			else:
				# Translators: Searchable tag name
				self.RadioBusquedaDLG.busqueda_categoria_radio.SetLabel(_("Buscar etiqueta:"))
				# Translators: Search button name
				self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				# Translators: Message in the search listbox, Waiting for a search
				self.RadioBusquedaDLG.lb_categorias_radio.Append(_("Esperando una búsqueda."))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
				self.RadioBusquedaDLG.ch_categorias_radio.SetFocus()

	def BuscarRadioGeneral(self, event):
		global nombre_emisoras_temporal_busqueda, url_emisoras_temporal_busqueda

		indice_listbox = self.RadioGeneralDLG.listbox_radio.GetSelection()
		str_listbox = self.RadioGeneralDLG.listbox_radio.GetString(indice_listbox)

		# Translators: Search button name
		if self.RadioGeneralDLG.Buscar_radioBTN.GetLabel() == _("&Buscar"):
			# Translators: Message there are no stations
			if str_listbox == _("Sin emisoras."):
				# Translators: Message there are no stations
				xguiMsg = \
_("""No hay emisoras para buscar.""")
				xgui.Mensaje(xguiMsg,
					# Translators: Message window title: Error
					_("Error"), 0)
				self.RadioGeneralDLG.texto_busqueda_radio.Clear()
				self.RadioGeneralDLG.texto_busqueda_radio.SetFocus()
			else:
				if self.RadioGeneralDLG.texto_busqueda_radio.GetValue() == "":
					# Translators: Blank search message
					xguiMsg = \
_("""El campo de búsqueda esta vacío, escriba algo antes para poder realizar la búsqueda.""")
					xgui.Mensaje(xguiMsg,
						# Translators: Message window title: Error
						_("Error"), 0)
					self.RadioGeneralDLG.texto_busqueda_radio.SetFocus()
				else:
					buscar = self.RadioGeneralDLG.texto_busqueda_radio.GetValue()
					nombre_emisoras_temporal_busqueda = []
					url_emisoras_temporal_busqueda = []
					for item in gen_nombre_radios:
						if buscar.lower() in item.lower():
							nombre_emisoras_temporal_busqueda.append(item)

					for i in nombre_emisoras_temporal_busqueda:
						posicion = gen_nombre_radios.index(i)
						url_emisoras_temporal_busqueda.append(gen_url_radios[posicion])

					if len(nombre_emisoras_temporal_busqueda) == 0:
						# Translators: Message not found results
						xguiMsg = \
_("""No se encontraron resultados.
Haga una búsqueda más específica.""")
						xgui.Mensaje(xguiMsg,
							# Translators: Message window title: Error
							_("Error"), 0)
						# Translators: Search button name
						self.RadioGeneralDLG.Buscar_radioBTN.SetLabel(_("&Buscar"))
						self.RadioGeneralDLG.texto_busqueda_radio.Clear()
						self.RadioGeneralDLG.texto_busqueda_radio.SetFocus()
					else:
						# Translators: Clean button name
						self.RadioGeneralDLG.Buscar_radioBTN.SetLabel(_("&Limpiar"))
						self.RadioGeneralDLG.listbox_radio.Clear()
						self.RadioGeneralDLG.listbox_radio.Append(nombre_emisoras_temporal_busqueda)
						self.RadioGeneralDLG.listbox_radio.SetSelection(0)
						self.RadioGeneralDLG.listbox_radio.SetFocus()

		else:
			nombre_emisoras_temporal_busqueda = []
			url_emisoras_temporal_busqueda = []
			# Translators: Search button name
			self.RadioGeneralDLG.Buscar_radioBTN.SetLabel(_("&Buscar"))
			self.RadioGeneralDLG.texto_busqueda_radio.Clear()
			self.RadioGeneralDLG.listbox_radio.Clear()
			self.RadioGeneralDLG.listbox_radio.Append(gen_nombre_radios )
			self.RadioGeneralDLG.listbox_radio.SetSelection(0)
			self.RadioGeneralDLG.texto_busqueda_radio.SetFocus()

	def BuscarRadioFavoritos(self, event):
		global temporal_nombre_radio_favoritos, temporal_url_radio_favoritos


		# Translators: Search button name
		if self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.GetLabel() == _("&Buscar"):
			if self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.GetValue() == "":
				# Translators: Blank search message
				xguiMsg = \
_("""El campo de búsqueda esta vacío, escriba algo antes para poder realizar la búsqueda.""")
				xgui.Mensaje(xguiMsg,
					# Translators: Message window title: Error
					_("Error"), 0)
				self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.SetFocus()
			else:
				buscar = self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.GetValue()
				temporal_nombre_radio_favoritos = []
				temporal_url_radio_favoritos = []
				for item in fav_nombre_radios:
					if buscar.lower() in item.lower():
						temporal_nombre_radio_favoritos.append(item)

				for i in temporal_nombre_radio_favoritos:
					posicion = fav_nombre_radios.index(i)
					temporal_url_radio_favoritos.append(fav_url_radios[posicion])

				if len(temporal_nombre_radio_favoritos) == 0:
					# Translators: Message not found results
					xguiMsg = \
_("""No se encontraron resultados.
Haga una búsqueda más específica.""")
					xgui.Mensaje(xguiMsg,
						# Translators: Message window title: Error
						_("Error"), 0)
					# Translators: Search button name
					self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.SetLabel(_("&Buscar"))
					self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.Clear()
					self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.SetFocus()
				else:
					# Translators: Clean button name
					self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.SetLabel(_("&Limpiar"))
					self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
					self.RadioFavoritosDLG.listbox_radio_favoritos.Append(temporal_nombre_radio_favoritos)
					self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)
					self.RadioFavoritosDLG.listbox_radio_favoritos.SetFocus()
		else:
			temporal_nombre_radio_favoritos = []
			temporal_url_radio_favoritos = []
			# Translators: Search button name
			self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.SetLabel(_("&Buscar"))
			self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.Clear()
			self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
			self.RadioFavoritosDLG.listbox_radio_favoritos.Append(fav_nombre_radios)
			self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)
			self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.SetFocus()

	def BuscarCategoriaRadio(self, event):
		indice = self.RadioBusquedaDLG.ch_categorias_radio.GetSelection() # me da el indice de la seleccion

		# Translators: Search button name
		if self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.GetLabel() == _("&Buscar"):
			if self.RadioBusquedaDLG.texto_busqueda_categoria.GetValue() == "":
				# Translators: Blank search message
				xguiMsg = \
_("""El campo de búsqueda esta vacío, escriba algo antes para poder realizar la búsqueda.""")
				xgui.Mensaje(xguiMsg,
					# Translators: Message window title: Error
					_("Error"), 0)
				self.RadioBusquedaDLG.texto_busqueda_categoria.SetFocus()
			else:
				if indice == 0:
					# Translators: Clean button name
					self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Limpiar"))
					self.RadioBusquedaDLG.lb_categorias_radio.Clear()
					getValue = self.RadioBusquedaDLG.texto_busqueda_categoria.GetValue()
					Radios.Buscar_Radio_General(getValue, False)
					for i in range(0, len(Radios.url_busqueda_general_radio)):
						self.RadioBusquedaDLG.lb_categorias_radio.Append(Radios.nombre_busqueda_general_radio[i])

					if len(Radios.nombre_busqueda_general_radio) == 0:
						# Translators: Message not found results
						xguiMsg = \
_("""No se encontraron resultados.
Haga una búsqueda más específica.""")
						xgui.Mensaje(xguiMsg,
							# Translators: Message window title: Error
							_("Error"), 0)
						# Translators: Search button name
						self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
						self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
						self.RadioBusquedaDLG.texto_busqueda_categoria.SetFocus()
						self.RadioBusquedaDLG.lb_categorias_radio.Clear()
						# Translators: Message waiting for a search
						self.RadioBusquedaDLG.lb_categorias_radio.Append(_("Esperando una búsqueda."))
						self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
					else:
						self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
						self.RadioBusquedaDLG.lb_categorias_radio.SetFocus()

				elif indice == 1:
					# Translators: Clean button name
					self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Limpiar"))
					self.RadioBusquedaDLG.lb_categorias_radio.Clear()
					getValue = self.RadioBusquedaDLG.texto_busqueda_categoria.GetValue()
					Radios.Buscar_Pais(getValue)
					for nombre_item, numero_item in zip(Radios.resultado_pais_busqueda_nombre, Radios.resultado_pais_busqueda_numero):
						# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
						self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))

					if len(Radios.resultado_pais_busqueda_nombre) == 0:
						# Translators: Message not found results
						xguiMsg = \
_("""No se encontraron resultados.
Haga una búsqueda más específica.""")
						xgui.Mensaje(xguiMsg,
							# Translators: Message window title: Error
							_("Error"), 0)
						# Translators: Search button name
						self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
						self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
						self.RadioBusquedaDLG.texto_busqueda_categoria.SetFocus()
						self.RadioBusquedaDLG.lb_categorias_radio.Clear()
						for nombre_item, numero_item in zip(Radios.paises_radio_español, Radios.paises_numero_emisoras):
							# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
							self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))
						self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
					else:
						self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
						self.RadioBusquedaDLG.lb_categorias_radio.SetFocus()

				elif indice == 2:
					# Translators: Clean button name
					self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Limpiar"))
					self.RadioBusquedaDLG.lb_categorias_radio.Clear()
					getValue = self.RadioBusquedaDLG.texto_busqueda_categoria.GetValue()
					Radios.Buscar_Idioma(getValue)
					for nombre_item, numero_item in zip(Radios.busqueda_nombre_idioma, Radios.busqueda_cantidad_idioma):
						# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
						self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))

					if len(Radios.busqueda_nombre_idioma) == 0:
						# Translators: Message not found results
						xguiMsg = \
_("""No se encontraron resultados.
Haga una búsqueda más específica.""")
						xgui.Mensaje(xguiMsg,
							# Translators: Message window title: Error
							_("Error"), 0)
						# Translators: Search button name
						self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
						self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
						self.RadioBusquedaDLG.texto_busqueda_categoria.SetFocus()
						self.RadioBusquedaDLG.lb_categorias_radio.Clear()
						for nombre_item, numero_item in zip(Radios.nombre_idioma, Radios.cantidad_idioma):
							# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
							self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))
						self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
					else:
						self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
						self.RadioBusquedaDLG.lb_categorias_radio.SetFocus()

				elif indice == 3:
					# Translators: Clean button name
					self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Limpiar"))
					self.RadioBusquedaDLG.lb_categorias_radio.Clear()
					getValue = self.RadioBusquedaDLG.texto_busqueda_categoria.GetValue()
					Radios.Buscar_Tag(getValue)
					for nombre_item, numero_item in zip(Radios.busqueda_nombre_tag, Radios.busqueda_cantidad_tag):
						# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
						self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))

					if len(Radios.busqueda_nombre_tag) == 0:
						# Translators: Message not found results
						xguiMsg = \
_("""No se encontraron resultados.
Haga una búsqueda más específica.""")
						xgui.Mensaje(xguiMsg,
							# Translators: Message window title: Error
							_("Error"), 0)
						# Translators: Search button name
						self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
						self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
						self.RadioBusquedaDLG.texto_busqueda_categoria.SetFocus()
						self.RadioBusquedaDLG.lb_categorias_radio.Clear()
						# Translators: Message waiting for a search
						self.RadioBusquedaDLG.lb_categorias_radio.Append(_("Esperando una búsqueda."))
						self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
					else:
						self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
						self.RadioBusquedaDLG.lb_categorias_radio.SetFocus()

		else:
			if indice == 0:
				# Translators: Search button name
				self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				self.RadioBusquedaDLG.texto_busqueda_categoria.SetFocus()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				# Translators: Message waiting for a search
				self.RadioBusquedaDLG.lb_categorias_radio.Append(_("Esperando una búsqueda."))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
			elif indice == 1:
				# Translators: Search button name
				self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				self.RadioBusquedaDLG.texto_busqueda_categoria.SetFocus()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				for nombre_item, numero_item in zip(Radios.paises_radio_español, Radios.paises_numero_emisoras):
					# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
					self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)
			elif indice == 2:
				# Translators: Search button name
				self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				self.RadioBusquedaDLG.texto_busqueda_categoria.SetFocus()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				for nombre_item, numero_item in zip(Radios.nombre_idioma, Radios.cantidad_idioma):
					# Translators: Warning do not change the content of what is between the keys. Message with the number of stations
					self.RadioBusquedaDLG.lb_categorias_radio.Append(_("{} número de emisoras: {}").format(nombre_item, numero_item))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)

			elif indice == 3:
				# Translators: Search button name
				self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.SetLabel(_("&Buscar"))
				self.RadioBusquedaDLG.texto_busqueda_categoria.Clear()
				self.RadioBusquedaDLG.texto_busqueda_categoria.SetFocus()
				self.RadioBusquedaDLG.lb_categorias_radio.Clear()
				# Translators: Message waiting for a search
				self.RadioBusquedaDLG.lb_categorias_radio.Append(_("Esperando una búsqueda."))
				self.RadioBusquedaDLG.lb_categorias_radio.SetSelection(0)

	def menu_accion(self):
		self.menuaccion = wx.Menu()

		# Translators: context menu item
		self.newfav = self.menuaccion.Append(wx.ID_ANY, _("&Nueva emisora"))
		self.Bind(wx.EVT_MENU, self.NuevoFavorito, self.newfav)
		# Translators: context menu item
		self.editfav = self.menuaccion.Append(wx.ID_ANY, _("&Editar emisora"))
		self.Bind(wx.EVT_MENU, self.EditarFavorito, self.editfav)
		# Translators: context menu item
		self.delFav = self.menuaccion.Append(wx.ID_ANY, _("&Quitar de favoritos"))
		self.Bind(wx.EVT_MENU, self.BorrarFavorito, self.delFav)

	def mostrar_menu_accion(self,event):
		position = self.RadioDLG.AccionBTN.GetPosition()
		self.PopupMenu(self.menuaccion,position)
		pass

	def NuevoFavorito(self, event):
		global controleditor
		# Translators: title of dialog
		dlg = DialogoNewEdit(_("Añadir nueva emisora"))
		dlg.ShowModal()
		if controleditor == True:
			controleditor = False
			Opciones.Guardar_Buffers(fileFavRadio, fav_nombre_radios, fav_url_radios)
			Opciones.Cargar_Buffer_Favoritos_Radio()
			if len(fav_nombre_radios) == 0:
				# Translators: Search button name
				self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.SetLabel(_("&Buscar"))
				self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.Clear()
				self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
				# Translators: Message no favorites
				self.RadioFavoritosDLG.listbox_radio_favoritos.Append(_("No hay favoritos."))
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)
			else:
				# Translators: Search button name
				self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.SetLabel(_("&Buscar"))
				self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.Clear()
				self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
				self.RadioFavoritosDLG.listbox_radio_favoritos.Append(fav_nombre_radios)
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)
		self.RadioFavoritosDLG.listbox_radio_favoritos.SetFocus()

	def EditarFavorito(self, event):
		global controleditor
		indice = self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection()
		# Translators: title of dialog
		dlg = DialogoNewEdit(_("Editar emisora"), fav_nombre_radios[indice], fav_url_radios[indice], indice)
		dlg.ShowModal()
		if controleditor == True:
			controleditor = False
			Opciones.Guardar_Buffers(fileFavRadio, fav_nombre_radios, fav_url_radios)
			Opciones.Cargar_Buffer_Favoritos_Radio()
			if len(fav_nombre_radios) == 0:
				# Translators: Search button name
				self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.SetLabel(_("&Buscar"))
				self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.Clear()
				self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
				# Translators: Message no favorites
				self.RadioFavoritosDLG.listbox_radio_favoritos.Append(_("No hay favoritos."))
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)
			else:
				# Translators: Search button name
				self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.SetLabel(_("&Buscar"))
				self.RadioFavoritosDLG.texto_busqueda_radio_favoritos.Clear()
				self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
				self.RadioFavoritosDLG.listbox_radio_favoritos.Append(fav_nombre_radios)
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)
		self.RadioFavoritosDLG.listbox_radio_favoritos.SetFocus()

	def BorrarFavorito(self, event):
		if self.RadioFavoritosDLG.listbox_radio_favoritos.GetString(self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection()) == _("No hay favoritos."):
			pass
		else:
			self.Quitar_Favoritos(None)

	def menuContextual(self):
		self.contextual_busqueda_radio1 = wx.Menu()
		# Translators: context menu item
		self.item1 = self.contextual_busqueda_radio1.Append(wx.ID_ANY, _("Reproducir"))
		self.Bind(wx.EVT_MENU, self.Reproducir_Radio, self.item1)
		# Translators: context menu item
		self.item2 = self.contextual_busqueda_radio1.Append(wx.ID_ANY, _("Agregar a favoritos"))
		self.Bind(wx.EVT_MENU, self.Agregar_Favoritos, self.item2)
		# Translators: context menu item
		self.item3 = self.contextual_busqueda_radio1.Append(wx.ID_ANY, _("Copiar URL"))
		self.Bind(wx.EVT_MENU, self.Copiar_Url, self.item3)

		self.contextual_busqueda_radio2 = wx.Menu()
		# Translators: context menu item
		self.item1_pc = self.contextual_busqueda_radio2.Append(wx.ID_ANY, _("Poner por defecto en General"))
		self.Bind(wx.EVT_MENU, self.AñadirDefectoGeneral, self.item1_pc)

		self.contextual_favoritos_radio1 = wx.Menu()
		# Translators: context menu item
		self.item1 = self.contextual_favoritos_radio1.Append(wx.ID_ANY, _("Reproducir"))
		self.Bind(wx.EVT_MENU, self.Reproducir_Radio, self.item1)
		# Translators: context menu item
		self.item2 = self.contextual_favoritos_radio1.Append(wx.ID_ANY, _("Quitar de favoritos"))
		self.Bind(wx.EVT_MENU, self.Quitar_Favoritos, self.item2)
		# Translators: context menu item
		self.item3 = self.contextual_favoritos_radio1.Append(wx.ID_ANY, _("Copiar URL"))
		self.Bind(wx.EVT_MENU, self.Copiar_Url, self.item3)

		self.contextual_favoritos_radio2 = wx.Menu()
		# Translators: context menu item
		self.item1 = self.contextual_favoritos_radio2.Append(wx.ID_ANY, _("Reproducir"))
		self.Bind(wx.EVT_MENU, self.Reproducir_Radio, self.item1)
		# Translators: context menu item
		self.item2 = self.contextual_favoritos_radio2.Append(wx.ID_ANY, _("Copiar URL"))
		self.Bind(wx.EVT_MENU, self.Copiar_Url, self.item2)

	def menuContextualLanzador(self,event):
		indice_choice = self.RadioBusquedaDLG.ch_categorias_radio.GetSelection() # me da el indice de la seleccion
		indice = self.RadioDLG.TreeBook.GetSelection()

		if indice == 0:
			if self.RadioGeneralDLG.listbox_radio.GetSelection() == -1:
				event.Skip()
			else:
				# Translators: Message without stations
				if self.RadioGeneralDLG.listbox_radio.GetString(self.RadioGeneralDLG.listbox_radio.GetSelection()) == _("Sin emisoras."):
					event.Skip()
				else:
					position = event.GetPosition()
					self.PopupMenu(self.contextual_busqueda_radio1,position)

		elif indice == 1:
			if self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection() == -1:
				event.Skip()
			else:
				# Translators: Message no favorites
				if self.RadioFavoritosDLG.listbox_radio_favoritos.GetString(self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection()) == _("No hay favoritos."):
					event.Skip()
				else:
					# Translators: Search button name
					if self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.GetLabel() == _("&Buscar"):
						position = event.GetPosition()
						self.PopupMenu(self.contextual_favoritos_radio1,position)
					else:
						position = event.GetPosition()
						self.PopupMenu(self.contextual_favoritos_radio2,position)

		elif indice == 2:
			if self.RadioBusquedaDLG.lb_categorias_radio.GetSelection() == -1:
				event.Skip()
			# Translators: Message waiting for a search
			elif self.RadioBusquedaDLG.lb_categorias_radio.GetString(self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()) == "Esperando una búsqueda.":
				event.Skip()
			elif indice_choice == 0:
				position = event.GetPosition()
				self.PopupMenu(self.contextual_busqueda_radio1,position)
			elif indice_choice == 1:
				position = event.GetPosition()
				self.PopupMenu(self.contextual_busqueda_radio2,position)
			elif indice_choice == 2:
				position = event.GetPosition()
				self.PopupMenu(self.contextual_busqueda_radio2,position)
			elif indice_choice == 3:
				position = event.GetPosition()
				self.PopupMenu(self.contextual_busqueda_radio2,position)

			else:
				event.Skip()

	def Reproducir_Radio(self, event):
		indice = self.RadioDLG.TreeBook.GetSelection() # me da el indice de la pestaña

		if indice == 0:
			indice_listbox = self.RadioGeneralDLG.listbox_radio.GetSelection()
			str_listbox = self.RadioGeneralDLG.listbox_radio.GetString(indice_listbox)

			# Translators: Search button name
			if self.RadioGeneralDLG.Buscar_radioBTN.GetLabel() == _("&Buscar"):
				nombreTitulo = str_listbox
				urlReproducir = gen_url_radios[indice_listbox]
			else:
				nombreTitulo = str_listbox
				urlReproducir = url_emisoras_temporal_busqueda[indice_listbox]

		if indice == 1:
			indice_listbox = self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection()
			str_listbox = self.RadioFavoritosDLG.listbox_radio_favoritos.GetString(indice_listbox)
			# Translators: Search button name
			if self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.GetLabel() == _("&Buscar"):
				nombreTitulo = str_listbox
				urlReproducir = fav_url_radios[indice_listbox]
			else:
				nombreTitulo = str_listbox
				urlReproducir = temporal_url_radio_favoritos[indice_listbox]

		if indice == 2:
			indice_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()
			str_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetString(indice_listbox)
			nombreTitulo = str_listbox
			urlReproducir = Radios.url_busqueda_general_radio[indice_listbox]

		self.ComprobarUrl(nombreTitulo, urlReproducir)

	def Agregar_Favoritos(self, event):
		indice = self.RadioDLG.TreeBook.GetSelection() # me da el indice de la pestaña

		if indice == 0:
			indice_listbox = self.RadioGeneralDLG.listbox_radio.GetSelection()
			str_listbox = self.RadioGeneralDLG.listbox_radio.GetString(indice_listbox)
			# Translators: Search button name
			if self.RadioGeneralDLG.Buscar_radioBTN.GetLabel() == _("&Buscar"):
				fav_nombre_radios.append(str_listbox)
				fav_url_radios.append(gen_url_radios[indice_listbox])
			else:
				fav_nombre_radios.append(str_listbox)
				fav_url_radios.append(url_emisoras_temporal_busqueda[indice_listbox])
			Opciones.Guardar_Buffers(fileFavRadio, fav_nombre_radios, fav_url_radios)
			# Translators: Title of the notification
			notify = wx.adv.NotificationMessage(title=_("Información"),
				# Translators: Notification message
				message=_("Se agrego la emisora {} a favoritos.").format(str_listbox), parent=None, flags=wx.ICON_INFORMATION)
			notify.Show(timeout=10)

		if indice == 2:
			indice_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()
			str_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetString(indice_listbox)
			fav_nombre_radios.append(str_listbox)
			fav_url_radios.append(Radios.url_busqueda_general_radio[indice_listbox])
			Opciones.Guardar_Buffers(fileFavRadio, fav_nombre_radios, fav_url_radios)
			# Translators: Title of the notification
			notify = wx.adv.NotificationMessage(title=_("Información"),
				# Translators: Notification message
				message=_("Se agrego la emisora {} a favoritos.").format(str_listbox), parent=None, flags=wx.ICON_INFORMATION)
			notify.Show(timeout=10)

	def Quitar_Favoritos(self, event):
		indice_listbox = self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection()
		del fav_nombre_radios[indice_listbox]
		del fav_url_radios[indice_listbox]
		Opciones.Guardar_Buffers(fileFavRadio, fav_nombre_radios, fav_url_radios)
		Opciones.Cargar_Buffer_Favoritos_Radio()
		if len(fav_nombre_radios) == 0:
			self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
			# Translators: Message no favorites
			self.RadioFavoritosDLG.listbox_radio_favoritos.Append(_("No hay favoritos."))
			self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)
		else:
			self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
			self.RadioFavoritosDLG.listbox_radio_favoritos.Append(fav_nombre_radios)
			self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(0)

	def Copiar_Url(self, event):
		indice = self.RadioDLG.TreeBook.GetSelection() # me da el indice de la pestaña

		if indice == 0:
			indice_listbox = self.RadioGeneralDLG.listbox_radio.GetSelection()
			str_listbox = self.RadioGeneralDLG.listbox_radio.GetString(indice_listbox)
			# Translators: Search button name
			if self.RadioGeneralDLG.Buscar_radioBTN.GetLabel() == _("&Buscar"):
				texto_portapapeles =wx.TextDataObject(str(gen_url_radios[indice_listbox]))
				if wx.TheClipboard.Open():
					wx.TheClipboard.SetData(texto_portapapeles)
					wx.TheClipboard.Close()

					# Translators: Title of the notification
					notify = wx.adv.NotificationMessage(title=_("Información"),
						# Translators: Notification message
						message=_("Se a copiado la URL de la emisora {} al portapapeles. Ya puede compartirla.").format(str_listbox), parent=None, flags=wx.ICON_INFORMATION)
					notify.Show(timeout=10)
			else:
				texto_portapapeles =wx.TextDataObject(str(url_emisoras_temporal_busqueda[indice_listbox]))
				if wx.TheClipboard.Open():
					wx.TheClipboard.SetData(texto_portapapeles)
					wx.TheClipboard.Close()
					# Translators: Title of the notification
					notify = wx.adv.NotificationMessage(title=_("Información"),
						# Translators: Notification message
						message=_("Se a copiado la URL de la emisora {} al portapapeles. Ya puede compartirla.").format(str_listbox), parent=None, flags=wx.ICON_INFORMATION)
					notify.Show(timeout=10)

		if indice == 1:
			indice_listbox = self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection()
			str_listbox = self.RadioFavoritosDLG.listbox_radio_favoritos.GetString(indice_listbox)
			# Translators: Search button name
			if self.RadioFavoritosDLG.Buscar_radioBTN_favoritos.GetLabel() == _("&Buscar"):
				texto_portapapeles =wx.TextDataObject(str(fav_url_radios[indice_listbox]))
				if wx.TheClipboard.Open():
					wx.TheClipboard.SetData(texto_portapapeles)
					wx.TheClipboard.Close()
					# Translators: Title of the notification
					notify = wx.adv.NotificationMessage(title=_("Información"),
						# Translators: Notification message
						message=_("Se a copiado la URL de la emisora {} al portapapeles. Ya puede compartirla.").format(str_listbox), parent=None, flags=wx.ICON_INFORMATION)
					notify.Show(timeout=10)
			else:
				texto_portapapeles =wx.TextDataObject(str(temporal_url_radio_favoritos[indice_listbox]))
				if wx.TheClipboard.Open():
					wx.TheClipboard.SetData(texto_portapapeles)
					wx.TheClipboard.Close()
					# Translators: Title of the notification
					notify = wx.adv.NotificationMessage(title=_("Información"),
						# Translators: Notification message
						message=_("Se a copiado la URL de la emisora {} al portapapeles. Ya puede compartirla.").format(str_listbox), parent=None, flags=wx.ICON_INFORMATION)
					notify.Show(timeout=10)

		if indice == 2:
			indice_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()
			str_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetString(indice_listbox)
			texto_portapapeles =wx.TextDataObject(str(Radios.url_busqueda_general_radio[indice_listbox]))
			if wx.TheClipboard.Open():
				wx.TheClipboard.SetData(texto_portapapeles)
				wx.TheClipboard.Close()
				# Translators: Title of the notification
				notify = wx.adv.NotificationMessage(title=_("Información"),
					# Translators: Notification message
					message=_("Se a copiado la URL de la emisora {} al portapapeles. Ya puede compartirla.").format(str_listbox), parent=None, flags=wx.ICON_INFORMATION)
				notify.Show(timeout=10)

	def AñadirDefectoGeneral(self, event):
		global PestañaGeneralRadioOpciones, gen_nombre_radios, gen_url_radios

		indice = self.RadioBusquedaDLG.ch_categorias_radio.GetSelection() # me da el indice de la seleccion

		if indice == 1:
			# Translators: Search button name
			if self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.GetLabel() == _("&Buscar"):
				indice_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()
				pais = Radios.paises_radio_abreviado[indice_listbox]
				PestañaGeneralRadioOpciones = ["Pais", str(pais)]
				lista_opciones = [PestañaGeneralRadioOpciones]
				Opciones.Guardar_Opciones_Radio(lista_opciones)
				Radios.Resultado_Paises(pais)
				gen_nombre_radios = Radios.nombre_radios_pais
				gen_url_radios = Radios.url_radios_pais
			else:
				indice_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()
				pais = Radios.resultado_pais_busqueda_abreviado[indice_listbox]
				PestañaGeneralRadioOpciones = ["Pais", str(pais)]
				lista_opciones = [PestañaGeneralRadioOpciones]
				Opciones.Guardar_Opciones_Radio(lista_opciones)
				Radios.Resultado_Paises(pais)
				gen_nombre_radios = Radios.nombre_radios_pais
				gen_url_radios = Radios.url_radios_pais

		if indice == 2:
			# Translators: Search button name
			if self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.GetLabel() == _("&Buscar"):
				indice_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()
				lenguaje = Radios.nombre_idioma[indice_listbox]
				Radios.Resultado_Idioma_Global(lenguaje)
				PestañaGeneralRadioOpciones = ["Idioma", str(lenguaje)]
				lista_opciones = [PestañaGeneralRadioOpciones]
				Opciones.Guardar_Opciones_Radio(lista_opciones)
				gen_nombre_radios = Radios.nombre_radios_pais
				gen_url_radios = Radios.url_radios_pais
			else:
				indice_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()
				lenguaje = Radios.busqueda_nombre_idioma[indice_listbox]
				Radios.Resultado_Idioma_Global(lenguaje)
				PestañaGeneralRadioOpciones = ["Idioma", str(lenguaje)]
				lista_opciones = [PestañaGeneralRadioOpciones]
				Opciones.Guardar_Opciones_Radio(lista_opciones)
				gen_nombre_radios = Radios.nombre_radios_pais
				gen_url_radios = Radios.url_radios_pais

		if indice == 3:
			# Translators: Search button name
			if self.RadioBusquedaDLG.Buscar_Categoria_RadioBTN.GetLabel() == _("&Buscar"):
				indice_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()
				tag = Radios.nombre_tag[indice_listbox]
				Radios.Resultado_Tag_Global(tag)
				PestañaGeneralRadioOpciones = ["Etiqueta", str(tag)]
				lista_opciones = [PestañaGeneralRadioOpciones]
				Opciones.Guardar_Opciones_Radio(lista_opciones)
				gen_nombre_radios = Radios.nombre_radios_pais
				gen_url_radios = Radios.url_radios_pais
			else:
				indice_listbox = self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()
				tag = Radios.busqueda_nombre_tag[indice_listbox]
				Radios.Resultado_Tag_Global(tag)
				PestañaGeneralRadioOpciones = ["Etiqueta", str(tag)]
				lista_opciones = [PestañaGeneralRadioOpciones]
				Opciones.Guardar_Opciones_Radio(lista_opciones)
				gen_nombre_radios = Radios.nombre_radios_pais
				gen_url_radios = Radios.url_radios_pais

	def 	on_set_volume(self, event):
		global volumenGeneral
		volumenGeneral = self.RadioDLG.volumenBarra.GetValue()
		player.volumen(volumenGeneral)

	def ComprobarUrl(self, nombre, url):
		global nombreTitulo, urlReproducir, controlON, controlSilenciar
		if chkInternet.test_internet(url) == False:
			# Translators: Error information message when loading the station
			xguiMsg = \
_("""No se pudo cargar la emisora.

Asegúrese de que tiene conexión a internet.

Otros motivos pueden ser que la emisora tenga problemas en estos momentos.

Inténtelo más tarde.""")
			xgui.Mensaje(xguiMsg,
				# Translators: Message window title: Error
				_("Error"), 0)
			indice = self.RadioDLG.TreeBook.GetSelection() # me da el indice de la pestaña
			if indice == 0:
				self.RadioGeneralDLG.listbox_radio.SetFocus()
			elif indice == 1:
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetFocus()
			elif indice == 2:
				self.RadioBusquedaDLG.lb_categorias_radio.SetFocus()
		else:
			nombreTitulo = nombre
			urlReproducir = url
			if controlON == True:
				if controlSilenciar == True:
					controlSilenciar = False
					# Translators: Silence button name
					self.RadioDLG.SilenciarBTN.SetLabel(_("&Silenciar"))
					player.mute(False)
				player.volumen(volumenGeneral)
				player.play(urlReproducir)
				self.RadioDLG.DetenerBTN.SetFocus()
			else:
				controlON = True
				self.onBotonesReproductor()
				player.inicio()
				player.volumen(volumenGeneral)
				player.play(urlReproducir)
				self.RadioDLG.DetenerBTN.SetFocus()

	def ComprobarUrl_Rapidos(self):
		global controlON, controlSilenciar

		if chkInternet.test_internet(urlReproducir) == False:
			# Translators: Error information message when loading the station
			xguiMsg = \
_("""No se pudo cargar la emisora.

Asegúrese de que tiene conexión a internet.

Otros motivos pueden ser que la emisora tenga problemas en estos momentos.

Inténtelo más tarde.""")
			xgui.Mensaje(xguiMsg,
				# Translators: Message window title: Error
				_("Error"), 0)
			indice = self.RadioDLG.TreeBook.GetSelection() # me da el indice de la pestaña
			if indice == 0:
				self.RadioGeneralDLG.listbox_radio.SetFocus()
			elif indice == 1:
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetFocus()
			elif indice == 2:
				self.RadioBusquedaDLG.lb_categorias_radio.SetFocus()
		else:
			if controlON == True:
				if controlSilenciar == True:
					controlSilenciar = False
					# Translators: Silence button name
					self.RadioDLG.SilenciarBTN.SetLabel(_("&Silenciar"))
					player.mute(False)
				player.volumen(volumenGeneral)
				player.play(urlReproducir)
				self.RadioDLG.DetenerBTN.SetFocus()
			else:
				controlON = True
				self.onBotonesReproductor()
				player.inicio()
				player.volumen(volumenGeneral)
				player.play(urlReproducir)
				self.RadioDLG.DetenerBTN.SetFocus()

	def BajarVol(self):
		global volumenGeneral
		vol1 = volumenGeneral - 1
		volumenGeneral = vol1
		player.volumen(volumenGeneral)
		self.RadioDLG.volumenBarra.SetValue(volumenGeneral)

	def SubirVol(self):
		global volumenGeneral
		vol1 = volumenGeneral + 1
		volumenGeneral = vol1
		player.volumen(volumenGeneral)
		self.RadioDLG.volumenBarra.SetValue(volumenGeneral)

	def onBotonesReproductor(self):
		self.RadioDLG.DetenerBTN.Enable()
		self.RadioDLG.RecargarBTN.Enable()
		self.RadioDLG.SilenciarBTN.Enable()

	def offBotonesReproductor(self):
		self.RadioDLG.DetenerBTN.Disable()
		self.RadioDLG.RecargarBTN.Disable()
		# Translators: Silence button name
		self.RadioDLG.SilenciarBTN.SetLabel(_("&Silenciar"))
		self.RadioDLG.SilenciarBTN.Disable()

	def DetenerBoton(self, event):
		global controlON, controlSilenciar, nombreTitulo, urlReproducir
		player.mute(False)
		player.stop()
		self.offBotonesReproductor()
		controlON = False
		controlSilenciar = False
		nombreTitulo = ""
		urlReproducir = ""
		indice = self.RadioDLG.TreeBook.GetSelection() # me da el indice de la pestaña
		if indice == 0:
			self.RadioGeneralDLG.listbox_radio.SetFocus()
		elif indice == 1:
			self.RadioFavoritosDLG.listbox_radio_favoritos.SetFocus()
		elif indice == 2:
			self.RadioBusquedaDLG.lb_categorias_radio.SetFocus()

	def RecargarBoton(self, event):
		global controlON, controlSilenciar, nombreTitulo, urlReproducir
		if chkInternet.test_internet(urlReproducir) == False:
			# Translators: Error information message when loading the station
			xguiMsg = \
_("""No se pudo cargar la emisora.

Asegúrese de que tiene conexión a internet.

Otros motivos pueden ser que la emisora tenga problemas en estos momentos.

Inténtelo más tarde.""")
			xgui.Mensaje(xguiMsg,
				# Translators: Message window title: Error
				_("Error"), 0)
			controlON = False
			controlSilenciar = False
			nombreTitulo = ""
			urlReproducir = ""
			self.offBotonesReproductor()
			# Translators: Silence button name
			self.RadioDLG.SilenciarBTN.SetLabel(_("&Silenciar"))
			player.mute(False)
			player.stop()
			indice = self.RadioDLG.TreeBook.GetSelection() # me da el indice de la pestaña
			if indice == 0:
				self.RadioGeneralDLG.listbox_radio.SetFocus()
			elif indice == 1:
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetFocus()
			elif indice == 2:
				self.RadioBusquedaDLG.lb_categorias_radio.SetFocus()
		else:
			self.offBotonesReproductor()
			self.onBotonesReproductor()
			# Translators: Silence button name
			self.RadioDLG.SilenciarBTN.SetLabel(_("&Silenciar"))
			if controlSilenciar == True:
				controlSilenciar = False
				player.mute(False)
			player.volumen(volumenGeneral)
			player.play(urlReproducir)
			self.RadioDLG.DetenerBTN.SetFocus()

	def SilenciarBoton(self, event):
		global controlSilenciar
		if controlON == True:
			# Translators: Silence button name
			if self.RadioDLG.SilenciarBTN.GetLabel() == _("&Silenciar"):
				player.mute(True)
				# Translators: Change button name to Remove Mute
				self.RadioDLG.SilenciarBTN.SetLabel(_("Quitar &Silencio"))
				controlSilenciar = True
			else:
				player.mute(False)
				# Translators: Silence button name
				self.RadioDLG.SilenciarBTN.SetLabel(_("&Silenciar"))
				controlSilenciar = False

	def onTeclasGeneral(self, event):
		if self.RadioGeneralDLG.listbox_radio.GetSelection() == -1:
			pass
		else:
			if self.RadioGeneralDLG.listbox_radio.GetString(self.RadioGeneralDLG.listbox_radio.GetSelection()) == _("Sin emisoras."):
				pass
			else:
				if event.GetKeyCode() ==32:
					self.Reproducir_Radio(None)

	def onTeclasFavoritos(self, event):
		if self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection() == -1:
			pass
		else:
			if self.RadioFavoritosDLG.listbox_radio_favoritos.GetString(self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection()) == _("No hay favoritos."):
				pass
			else:
				if event.GetKeyCode() ==32:
					self.Reproducir_Radio(None)

		if (event.AltDown(), event.GetKeyCode()) == (True, 315):
			self.moveup(None)
			event.Skip()
		if (event.AltDown(), event.GetKeyCode()) == (True, 317):
			self.movedown(None)
			event.Skip()

	def moveup(self, event):
		global fav_nombre_radios, fav_url_radios
		indice = self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection()
		totalLista = len(fav_nombre_radios) - 1
		if totalLista == -1:
			pass
		else:
			if indice == 0:
				beep(100,150)
			else:
				fav_nombre_radios.insert(indice - 1, fav_nombre_radios.pop(indice))
				fav_url_radios.insert(indice - 1, fav_url_radios.pop(indice))
				self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
				self.RadioFavoritosDLG.listbox_radio_favoritos.Append(fav_nombre_radios)
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(indice - 1)
				Opciones.Guardar_Buffers(fileFavRadio, fav_nombre_radios, fav_url_radios)

	def movedown(self, event):
		global fav_nombre_radios, fav_url_radios
		indice = self.RadioFavoritosDLG.listbox_radio_favoritos.GetSelection()
		totalLista = len(fav_nombre_radios) - 1
		if totalLista == -1:
			pass
		else:
			if indice == totalLista:
				beep(200,150)
			else:
				fav_nombre_radios.insert(indice + 1, fav_nombre_radios.pop(indice))
				fav_url_radios.insert(indice + 1, fav_url_radios.pop(indice))
				self.RadioFavoritosDLG.listbox_radio_favoritos.Clear()
				self.RadioFavoritosDLG.listbox_radio_favoritos.Append(fav_nombre_radios)
				self.RadioFavoritosDLG.listbox_radio_favoritos.SetSelection(indice + 1)
				Opciones.Guardar_Buffers(fileFavRadio, fav_nombre_radios, fav_url_radios)

	def onTeclasBuscador(self, event):
		indice_choice = self.RadioBusquedaDLG.ch_categorias_radio.GetSelection() # me da el indice de la seleccion
		indice = self.RadioDLG.TreeBook.GetSelection()

		if indice == 2:
			if self.RadioBusquedaDLG.lb_categorias_radio.GetSelection() == -1:
				event.Skip()
			# Translators: Message waiting for a search
			elif self.RadioBusquedaDLG.lb_categorias_radio.GetString(self.RadioBusquedaDLG.lb_categorias_radio.GetSelection()) == "Esperando una búsqueda.":
				event.Skip()
			elif indice_choice == 0:
				if event.GetKeyCode() ==32:
					self.Reproducir_Radio(None)

	def onClose(self, event):
		Opciones.Guardar_Buffers(fileFavRadio, fav_nombre_radios, fav_url_radios)
		lista_opciones = [volumenGeneral]
		Opciones.Guardar_Opciones(lista_opciones)
		self.Destroy()
		gui.mainFrame.postPopup()

class DialogoNewEdit(wx.Dialog):
	def __init__(self, titulo, nombre = None, url = None, valor = None):
		WIDTH = 600
		HEIGHT = 200
		pos = xgui._calculatePosition(WIDTH, HEIGHT)

		super(DialogoNewEdit, self).__init__(None, -1, title=titulo, pos = pos, size = (WIDTH, HEIGHT))

		self.Panel = wx.Panel(self)

#
		self.DialogoN_E = xgui.DialogoNuevoEditar(self.Panel)
		self.DialogoN_E.AceptarBTN.Bind(wx.EVT_BUTTON, self.AceptarBoton)
		self.DialogoN_E.CancelarBTN.Bind(wx.EVT_BUTTON, self.CancelarBoton)
		self.Bind(wx.EVT_CLOSE, self.CancelarBoton)
		self.Bind(wx.EVT_CHAR_HOOK, self.onEscape)

		self.valor = valor

		if nombre == None:
			pass
		else:
			self.DialogoN_E.texto_emisora.SetValue(nombre)
			self.DialogoN_E.texto_url.SetValue(url)

	def AceptarBoton(self, event):
		global controleditor
		if self.DialogoN_E.texto_emisora.GetValue() == "":
			# Translators: error message, you cannot leave the field
			xguiMsg = \
_("""No puede dejar el campo Nombre de la emisora en blanco.
Asegúrese de introducir un nombre correcto.""")
			xgui.Mensaje(xguiMsg,
				# Translators: Message window title: Error
				_("Error"), 0)
			self.DialogoN_E.texto_emisora.SetFocus()
		else:
			if self.DialogoN_E.texto_url.GetValue() == "":
				# Translators: error message, you cannot leave the field
				xguiMsg = \
_("""No puede dejar el campo de la URL de la emisora en blanco.
Asegúrese de introducir una dirección correcta.""")
				xgui.Mensaje(xguiMsg,
					# Translators: Message window title: Error
					_("Error"), 0)
				self.DialogoN_E.texto_url.SetFocus()
			else:
				if self.valor == None:
					controleditor = True
					fav_nombre_radios.append(self.DialogoN_E.texto_emisora.GetValue())
					fav_url_radios.append(self.DialogoN_E.texto_url.GetValue())
				else:
					controleditor = True
					del fav_nombre_radios[self.valor]
					del fav_url_radios[self.valor]
					fav_nombre_radios.append(self.DialogoN_E.texto_emisora.GetValue())
					fav_url_radios.append(self.DialogoN_E.texto_url.GetValue())
				self.Destroy()

	def CancelarBoton(self, event):
		self.Destroy()

	def onEscape(self, event):
		if event.GetKeyCode() == 27: # Pulsamos ESC y cerramos la ventana
			self.Destroy()
		else:
			event.Skip()

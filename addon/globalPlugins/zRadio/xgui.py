#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import addonHandler

# For translation
addonHandler.initTranslation()

# Function taken from the Emoticons plug-in
def _calculatePosition(width, height):
	w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
	h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
	# Centre of the screen
	x = w / 2
	y = h / 2
	# Minus application offset
	x -= (width / 2)
	y -= (height / 2)
	return (x, y)

class RadioPrincipal():
	def __init__(self, frame):

		self.frame = frame

		self.TreeBook = wx.Treebook(self.frame)

		self.page_1 = wx.Panel(self.TreeBook)
		self.page_2 = wx.Panel(self.TreeBook)
		self.page_3 = wx.Panel(self.TreeBook)

		# Translators: Main category name
		self.TreeBook.AddPage(self.page_1, _("General"))
		# Translators: Main category name
		self.TreeBook.AddPage(self.page_2, _("Favoritos"))
		# Translators: Main category name
		self.TreeBook.AddPage(self.page_3, _("Buscador"))

########## Botones Multimedia
		# Translators: Stop button name
		self.DetenerBTN = wx.Button(self.frame, wx.ID_ANY, _("&Detener"))
		self.DetenerBTN.Disable()
		# Translators: Reload button name
		self.RecargarBTN = wx.Button(self.frame, wx.ID_ANY, _("&Recargar"))
		self.RecargarBTN.Disable()
		# Translators: Silence button name
		self.SilenciarBTN = wx.Button(self.frame, wx.ID_ANY, _("&Silenciar"))
		self.SilenciarBTN.Disable()
		self.volumenBarra = wx.Slider(self.frame, wx.ID_ANY, 0, 0, 100, size=(100, -1))

########## Botones generales
		self.AccionBTN = wx.Button(self.frame, wx.ID_ANY, "&Acción")
		self.AccionBTN.Disable()
		self.HerramientasBTN = wx.Button(self.frame, wx.ID_ANY, "&Herramientas")
		self.HerramientasBTN.Disable()
		self.AyudaBTN = wx.Button(self.frame, wx.ID_ANY, "Ayuda F1")
		self.AyudaBTN.Disable()
		# Translators: Exit button name
		self.SalirBTN = wx.Button(self.frame, wx.ID_CANCEL, _("Salir Alt + F4"))

		sizer_TreeBook = wx.BoxSizer(wx.VERTICAL)
		sizer_TreeBook_BTN_multimedia = wx.BoxSizer(wx.HORIZONTAL)
		sizer_TreeBook_BTN_general = wx.BoxSizer(wx.HORIZONTAL)

		sizer_TreeBook.Add(self.TreeBook, 1, wx.ALL|wx.EXPAND, 5)

		sizer_TreeBook_BTN_multimedia.Add(self.DetenerBTN, 2, wx.CENTER, 5)
		sizer_TreeBook_BTN_multimedia.Add(self.RecargarBTN, 2, wx.CENTER, 5)
		sizer_TreeBook_BTN_multimedia.Add(self.SilenciarBTN, 2, wx.CENTER, 5)
		sizer_TreeBook_BTN_multimedia.Add(self.volumenBarra, 2, wx.CENTER, 5)

		sizer_TreeBook.Add(sizer_TreeBook_BTN_multimedia, 0, wx.CENTER, 5)

		sizer_TreeBook_BTN_general.Add(self.AccionBTN, 2, wx.CENTER, 5)
		sizer_TreeBook_BTN_general.Add(self.HerramientasBTN, 2, wx.CENTER, 5)
		sizer_TreeBook_BTN_general.Add(self.AyudaBTN, 2, wx.CENTER, 5)
		sizer_TreeBook_BTN_general.Add(self.SalirBTN, 2, wx.CENTER, 5)

		sizer_TreeBook.Add(sizer_TreeBook_BTN_general, 0, wx.CENTER, 5)

		self.frame.SetSizer(sizer_TreeBook)

class RadioGeneral():
	def __init__(self, frame):

		self.frame = frame

		# Translators: name of a label
		busqueda_radio = wx.StaticText(self.frame, wx.ID_ANY, label=_("Busqueda emisoras:"))
		self.texto_busqueda_radio = wx.TextCtrl(self.frame, wx.ID_ANY)
		# Translators: Search button name
		self.Buscar_radioBTN = wx.Button(self.frame, wx.ID_ANY, _("&Buscar"))
		# Translators: name of a label
		listado_radio = wx.StaticText(self.frame, wx.ID_ANY, label=_("Listado de emisoras:"))
		self.listbox_radio = wx.ListBox(self.frame)

		sizeV = wx.BoxSizer(wx.VERTICAL)
		sizeV1 = wx.BoxSizer(wx.VERTICAL)
		sizeH = wx.BoxSizer(wx.HORIZONTAL)

		sizeV1.Add(busqueda_radio, 0, wx.EXPAND)
		sizeH.Add(self.texto_busqueda_radio, 1, wx.EXPAND)
		sizeH.Add(self.Buscar_radioBTN, 0, wx.EXPAND)
		sizeV1.Add(sizeH, 0, wx.EXPAND)

		sizeV.Add(sizeV1, 0, wx.EXPAND)

		sizeV.Add(listado_radio, 0, wx.EXPAND)
		sizeV.Add(self.listbox_radio, 1, wx.EXPAND)

		self.frame.SetSizer(sizeV)

class RadioFavoritos():
	def __init__(self, frame):

		self.frame = frame

		# Translators: name of a label
		busqueda_radio_favoritos = wx.StaticText(self.frame, wx.ID_ANY, label=_("Busqueda emisoras favoritas:"))
		self.texto_busqueda_radio_favoritos = wx.TextCtrl(self.frame, wx.ID_ANY)
		# Translators: Search button name
		self.Buscar_radioBTN_favoritos = wx.Button(self.frame, wx.ID_ANY, _("&Buscar"))
		# Translators: name of a label
		listado_radio_favoritos = wx.StaticText(self.frame, wx.ID_ANY, label=_("Listado de emisoras favoritas:"))
		self.listbox_radio_favoritos = wx.ListBox(self.frame)

		sizerV = wx.BoxSizer(wx.VERTICAL)
		sizerV1 = wx.BoxSizer(wx.VERTICAL)
		sizerH = wx.BoxSizer(wx.HORIZONTAL)

		sizerV1.Add(busqueda_radio_favoritos, 0, wx.EXPAND)
		sizerH.Add(self.texto_busqueda_radio_favoritos, 1, wx.EXPAND)
		sizerH.Add(self.Buscar_radioBTN_favoritos, 0, wx.EXPAND)
		sizerV1.Add(sizerH, 0, wx.EXPAND)

		sizerV.Add(sizerV1, 0, wx.EXPAND)

		sizerV.Add(listado_radio_favoritos, 0, wx.EXPAND)
		sizerV.Add(self.listbox_radio_favoritos, 1, wx.EXPAND)

		self.frame.SetSizer(sizerV)

class RadioBusqueda():
	def __init__(self, frame):

		self.frame = frame

		# Translators: name of a label
		listado_categorias_radio_buscar = wx.StaticText(self.frame, wx.ID_ANY, label=_("Seleccione una categoría:"))
		self.ch_categorias_radio = wx.Choice(self.frame, wx.ID_ANY)
		self.ch_categorias_radio.SetSelection(0)

		# Translators: name of a label
		self.busqueda_categoria_radio = wx.StaticText(self.frame, wx.ID_ANY, label=_("Búsqueda general de radios:"))
		self.texto_busqueda_categoria = wx.TextCtrl(self.frame, wx.ID_ANY)
		# Translators: Search button name
		self.Buscar_Categoria_RadioBTN = wx.Button(self.frame, wx.ID_ANY, _("&Buscar"))

		# Translators: Message waiting for a search
		lista2 = [_("Esperando una búsqueda.")]
		# Translators: name of a label
		listado_categoria_listbox_radio = wx.StaticText(self.frame, wx.ID_ANY, label=_("Resultado:"))
		self.lb_categorias_radio = wx.ListBox(self.frame, choices = lista2)
		self.lb_categorias_radio.SetSelection(0)

		sizeV = wx.BoxSizer(wx.VERTICAL)
		sizeV1 = wx.BoxSizer(wx.VERTICAL)
		sizeH = wx.BoxSizer(wx.HORIZONTAL)

		sizeV.Add(listado_categorias_radio_buscar, 0, wx.EXPAND)
		sizeV.Add(self.ch_categorias_radio, 0, wx.EXPAND)

		sizeV1.Add(self.busqueda_categoria_radio, 0, wx.EXPAND)
		sizeH.Add(self.texto_busqueda_categoria, 1, wx.EXPAND)
		sizeH.Add(self.Buscar_Categoria_RadioBTN, 0, wx.EXPAND)
		sizeV1.Add(sizeH, 0, wx.EXPAND)

		sizeV.Add(sizeV1, 0, wx.EXPAND)

		sizeV.Add(listado_categoria_listbox_radio, 0, wx.EXPAND)
		sizeV.Add(self.lb_categorias_radio, 1, wx.EXPAND)

		self.frame.SetSizer(sizeV)

class Mensaje():
	def __init__(self, mensaje, titulo, valor):

		self.mensaje = mensaje
		self.titulo = titulo
		if valor == 0:
			self.parametro = wx.OK | wx.ICON_ERROR
		elif valor == 1:
			self.parametro = wx.OK | wx.ICON_INFORMATION
		dlg = wx.MessageDialog(None, self.mensaje, self.titulo, self.parametro)
		# Translators: Acept button name
		dlg.SetOKLabel(_("&Aceptar"))
		dlg.ShowModal()
		dlg.Destroy()

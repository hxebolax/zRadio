# -*- coding: utf-8 -*-
# Copyright (C) 2020 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import sys
import os
from .pathlib import Path
import pickle
import ctypes
try:
	from .raspado import *
except:
	pass
import globalVars
import addonHandler

# For translation
addonHandler.initTranslation()

dir = addonHandler._getDefaultAddonPaths()
dirDatos =os.path.join(globalVars.appArgs.configPath, "zRadio")
dirLib =os.path.join(dir[0], "zRadio", "globalPlugins","zRadio", "lib")
fileOptions = os.path.join(dirDatos, "opciones.dat")
fileOptionsRadio = os.path.join(dirDatos, "opt_radio.dat")
fileFavRadio = os.path.join(dirDatos, "fav_radios.dat")
fileCountry = os.path.join(dirLib, "paises.dat")

class Guardar_Cargar():
	def __init__(self):

		self.version = 1
		self.volumen = 50

		self.fav_nombre_radios = []
		self.fav_url_radios = []

		self.PestañaGeneralRadioOpciones = ["", ""]

	def Guardar_Opciones(self, lista):
		archivo = open(	fileOptions, "wb")
		pickle.dump(self.version, archivo)
		for i in lista:
			pickle.dump(i, archivo)
		archivo.close()

	def Cargar_Opciones(self):
		if os.path.isfile(fileOptions):
			archivo = open(	fileOptions, 'rb')
			self.version = pickle.load(archivo)
			if self.version == 1:	
				self.volumen = pickle.load(archivo)
			archivo.close()
		else:
			lista_opciones = [self.volumen]
			Guardar_Cargar.Guardar_Opciones(self, lista_opciones)
			Guardar_Cargar.Cargar_Opciones(self)

	def Guardar_Opciones_Radio(self, lista):
		archivo = open(	fileOptionsRadio, "wb")
		pickle.dump(self.version, archivo)
		for i in lista:
			pickle.dump(i, archivo)
		archivo.close()

	def Cargar_Opciones_Radio(self):
		if os.path.isfile(fileOptionsRadio):
			archivo = open(	fileOptionsRadio, 'rb')
			self.version = pickle.load(archivo)
			if self.version == 1:	
				self.PestañaGeneralRadioOpciones = pickle.load(archivo)
			archivo.close()
		else:
			lista_opciones = [self.PestañaGeneralRadioOpciones]
			Guardar_Cargar.Guardar_Opciones_Radio(self, lista_opciones)
			Guardar_Cargar.Cargar_Opciones_Radio(self)

	def Guardar_Buffers(self, file,  *args):
		archivo = open(file, "wb")
		for i in args:
			pickle.dump(i, archivo)
		archivo.close()

	def Cargar_Buffer_Favoritos_Radio(self):
		if os.path.isfile(fileFavRadio):
			archivo = open(fileFavRadio, 'rb')
			self.fav_nombre_radios = pickle.load(archivo)
			self.fav_url_radios = pickle.load(archivo)
			archivo.close()
		else:
			Guardar_Cargar.Guardar_Buffers(self, fileFavRadio, self.fav_nombre_radios, self.fav_url_radios)

### Variables Raspado
Opciones = Guardar_Cargar()
try:
	Radios = Raspado_Radios()
except:
	pass
### Listas
listaCategoriasBusquedaRadios = [
	# Translators: Options for the search category combobox
	_("Búsqueda general de radios"),
	# Translators: Options for the search category combobox
	_("Búsqueda por países"),
	# Translators: Options for the search category combobox
	_("Búsqueda por idioma"),
	# Translators: Options for the search category combobox
	_("Búsqueda por etiqueta")]

### Variables generales
nombreTitulo = "" # Adquiere el titulo de la ventana para cuando se reproduce
urlReproducir = "" # La dirección a reproducir

### Controles
control1 = False
controlON = False
controlSilenciar = False
controleditor = False

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
temporal_nombre_radio_favoritos = []
temporal_url_radio_favoritos = []
# Translators: Message without stations
nombre_emisoras_temporal = [_("Sin emisoras.")]
url_emisoras_temporal = []
nombre_emisoras_temporal_busqueda = []
url_emisoras_temporal_busqueda = []

### Variantes configuración
Opciones.Cargar_Opciones()
volumenGeneral = int(Opciones.volumen)


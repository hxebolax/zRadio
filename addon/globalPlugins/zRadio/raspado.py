# -*- coding: utf-8 -*-
# Copyright (C) 2020 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import pickle
import json
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pyradios import RadioBrowser
import pandas as pd

class Raspado_Radios():
	def __init__(self):

		self.nombre_radios_pais = []
		self.url_radios_pais = []
		self.resultado_pais_busqueda_nombre = []
		self.resultado_pais_busqueda_numero = []
		self.resultado_pais_busqueda_abreviado = []

		self.nombre_busqueda_general_radio = []
		self.url_busqueda_general_radio = []

		self.nombre_idioma = []
		self.cantidad_idioma = []
		self.busqueda_nombre_idioma = []
		self.busqueda_cantidad_idioma = []

		self.nombre_tag = []
		self.cantidad_tag = []
		self.busqueda_nombre_tag = []
		self.busqueda_cantidad_tag = []

		self.paises_radio_español = []
		self.paises_radio_abreviado = []
		self.paises_numero_emisoras = []
		self.paises_numero_total_emisoras = ""

		self.rb = RadioBrowser()
		self.datos_pais = pd.DataFrame(self.rb.countries())

	def Paises_Español(self, valor):
		nombre_paises_español = valor
		d = Raspado_Radios.load_obj(nombre_paises_español)
		claves = Raspado_Radios.keys_only(d)
		valores = Raspado_Radios.values_only(d)
		diccionario = dict(zip(claves, valores))
		self.temporal = []
		self.paises_radio_abreviado = []
		for i in range(len(self.datos_pais)):
			self.temporal.append(self.datos_pais.iloc[i]["name"])
			self.paises_radio_abreviado.append(self.datos_pais.iloc[i]["name"])
		for i in self.temporal:
			self.paises_radio_español.append(diccionario[i.upper()])

	def Paises_Bandera(self):
		for i in range(len(self.datos_pais)):
			self.paises_radio_abreviado.append(self.datos_pais.iloc[i]["name"])

	def Paises_Cantidad_Emisoras(self):
		for i in range(len(self.datos_pais)):
			self.paises_numero_emisoras.append(self.datos_pais.iloc[i]["stationcount"])

	def Suma_Total_Emisoras_Paises(self):
		self.temporal = []
		for i in range(len(self.datos_pais)):
			self.temporal.append(self.datos_pais.iloc[i]["stationcount"])
		self.paises_numero_total_emisoras = 0
		for i in self.temporal:
			self.paises_numero_total_emisoras = self.paises_numero_total_emisoras + i

	def Actualizar_Pais(self):
		self.paises_radio_español = []
		self.paises_radio_abreviado = []
		self.paises_numero_emisoras = []
		self.paises_numero_total_emisoras = ""
		Raspado_Radios.Paises_Español(self)
		Raspado_Radios.Paises_Bandera(self)
		Raspado_Radios.Paises_Cantidad_Emisoras(self)
		Raspado_Radios.Suma_Total_Emisoras_Paises(self)

	def Buscar_Pais(self, valor):
		self.resultado_pais_busqueda_nombre = []
		self.resultado_pais_busqueda_numero = []
		self.resultado_pais_busqueda_abreviado = []
		for item in self.paises_radio_español:
			if valor.lower() in item.lower():
				self.resultado_pais_busqueda_nombre.append(item)

		for i in self.resultado_pais_busqueda_nombre:
			posicion = self.paises_radio_español.index(i)
			self.resultado_pais_busqueda_numero.append(self.paises_numero_emisoras[posicion])
			self.resultado_pais_busqueda_abreviado.append(self.paises_radio_abreviado[posicion])

	def Resultado_Paises(self, valor):
		datos_frame = pd.DataFrame(self.rb.stations_by_countrycode(valor))
		self.nombre_radios_pais = []
		self.url_radios_pais = []
		for i in range(0, len(datos_frame)):
			self.nombre_radios_pais.append(datos_frame.iloc[i, 2])
			self.url_radios_pais.append(datos_frame.iloc[i, 3])

	def Buscar_Radio_General(self, valor, valor1=True):
		datos_frame = pd.DataFrame(self.rb.search(name=valor, name_exact=valor1))
		self.nombre_busqueda_general_radio = []
		self.url_busqueda_general_radio = []
		for i in range(0, len(datos_frame)):
			self.nombre_busqueda_general_radio.append(datos_frame.iloc[i, 2])
			self.url_busqueda_general_radio.append(datos_frame.iloc[i, 3])

	def Resultado_Idioma(self):
		datos_lenguaje = pd.DataFrame(self.rb.languages())
		self.nombre_idioma = []
		self.cantidad_idioma = []
		for i in range(len(datos_lenguaje)):
			self.nombre_idioma.append(datos_lenguaje.iloc[i]["name"])
			self.cantidad_idioma.append(datos_lenguaje.iloc[i]["stationcount"])

	def Buscar_Idioma(self, valor):
		datos_lenguaje = pd.DataFrame(self.rb.languages())
		filtro = datos_lenguaje[datos_lenguaje.iloc[:, 0].str.contains(valor, case=False)]
		self.busqueda_nombre_idioma = []
		self.busqueda_cantidad_idioma = []

		for i in range(len(filtro)):
			self.busqueda_nombre_idioma.append(filtro.iloc[i]["name"])
			self.busqueda_cantidad_idioma.append(filtro.iloc[i]["stationcount"])

	def Resultado_Idioma_Global(self, valor):
		pandas_radio_lenguaje = pd.DataFrame(self.rb.stations_by_language(valor))
		self.nombre_radios_pais = []
		self.url_radios_pais = []
		for i in range(0, len(pandas_radio_lenguaje)):
			self.nombre_radios_pais.append(pandas_radio_lenguaje.iloc[i, 2])
			self.url_radios_pais.append(pandas_radio_lenguaje.iloc[i, 3])

	def Resultado_Tag(self):
		datos_genero = pd.DataFrame(self.rb.tags())
		self.nombre_tag = []
		self.cantidad_tag = []
		for i in range(len(datos_genero)):
			self.nombre_tag.append(datos_genero.iloc[i]["name"])
			self.cantidad_tag.append(datos_genero.iloc[i]["stationcount"])

	def Buscar_Tag(self, valor):
		datos_genero = pd.DataFrame(self.rb.tags())
		filtro = datos_genero[datos_genero.iloc[:, 0].str.contains(valor, case=False)]
		self.busqueda_nombre_tag = []
		self.busqueda_cantidad_tag = []

		for i in range(len(filtro)):
			self.busqueda_nombre_tag.append(filtro.iloc[i]["name"])
			self.busqueda_cantidad_tag.append(filtro.iloc[i]["stationcount"])

	def Resultado_Tag_Global(self, valor):
		pandas_tag = pd.DataFrame(self.rb.stations_by_tag(valor))
		self.nombre_radios_pais = []
		self.url_radios_pais = []
		for i in range(0, len(pandas_tag)):
			self.nombre_radios_pais.append(pandas_tag.iloc[i, 2])
			self.url_radios_pais.append(pandas_tag.iloc[i, 3])

	def saber_pais_conexion(self):
		url = 'http://ipinfo.io/json'
		response = urlopen(url)
		data = json.load(response)

		IP=data['ip']
		org=data['org']
		city = data['city']
		country=data['country']
		region=data['region']
		return country

	def load_obj(name ):
		with open(name, 'rb') as f:
			return pickle.load(f)
	def save_obj(obj, name):
		with open(name, 'wb') as f:
			pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

	def keys_only(flat_dict):
		return [k for k,v in flat_dict.items()]
	def values_only(flat_dict):
		return [v for k,v in flat_dict.items()]


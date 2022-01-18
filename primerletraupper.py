#!/usr/bin/env python
# -*- coding: utf-8 -*-
texto = input("Ingrese texto: ")
mayus = "si"
textoListo = ""
letras = {
"a" : "A", "b" : "B", "c" : "C"}
for i in texto:
	if mayus == "si":
		i = letras[i]
	if " " in i:
		mayus = "si"
	else:
		mayus = "no"
	textoListo = textoListo + i
print (textoListo)
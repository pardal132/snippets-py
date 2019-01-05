#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('csv',help='arquivo .csv que será processado e incluso no shapefile')
parser.add_argument('shapefile',help='arquivo .shp no qual os atributos serão inclusos')
parser.add_argument('coeficiente',help='coeficiente multiplicativo a ser aplicado sobre os valores do csv',type=float)
parser.add_argument('-col','--colunas',help='lista dos headers das colunas do .csv que serão processadas, separados por ","')
parser.add_argument('-pref','--prefixo',help='prefixo adicionado aos headers das colunas ao serem inseridos no shapefile')
parser.add_argument('-v','--verbose',help='aumenta a quantidade de avisos mostrados',action='count',default=0)
args = parser.parse_args()
print(args)

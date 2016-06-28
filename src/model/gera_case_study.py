"""
	GeraCaseStudy
	---------------------------------
	version: 0.0.1
	date: Jun 18, 2016
"""

import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from model.gera import gera

class gera_case_study:

	gera = gera()
	gera.run()


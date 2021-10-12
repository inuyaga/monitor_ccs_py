# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="Monitor Ventas CCS", 
 version="1.0", 
 description="Breve descripcion", 
 author="Mario Esteban Hernandez Hernandez", 
 author_email="hdez.marioe@gmail.com", 
 url="#", 
 license="N/a", 
 scripts=["monitor_ui_css.py"],
 console=["monitor_ui_css.py"],
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)
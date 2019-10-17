#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:55:34 2019

@author: michal
"""
from os.path import join
from jobNode import GaussianNode

def addSPcorrections(graph, node, theoryLow = "B3LYP/6-31G(d,p)", theoryHigh = "B3LYP/6-311+G(2d,2p)", basename = ""):
    newDir = join(node, basename+"TZ")
    newNode = GaussianNode("tz.inp", newDir)
    newNode.routeSection = """%Chk=checkp.chk
%Mem=100GB
#P """+theoryHigh+"""
# nosymm
# Gfinput IOP(6/7=3)  Pop=full  Density  Test 
# Units(Ang,Deg)
"""
    newNode.verification = "SP"
    newNode.readResults = True
    graph.add_node(newDir, data = newNode)
    graph.add_edge(node, newDir)
    
    newDir = join(node, basename+"PCM")
    newNode = GaussianNode("pcm.inp", newDir)
    newNode.routeSection = """%Chk=checkp.chk
%Mem=100GB
#P """+theoryLow+"""
# nosymm SCRF(Solvent=Generic, Read)
# Gfinput IOP(6/7=3)  Pop=full  Density  Test 
# Units(Ang,Deg)
"""
    newNode.additionalSection = """
stoichiometry=H2O1
solventname=Water2
eps=4
epsinf=1.77556
"""
    newNode.verification = "SP"
    newNode.readResults = True
    graph.add_node(newDir, data = newNode)
    graph.add_edge(node, newDir)
    
    newDir = join(node, basename+"TZ_PCM")
    newNode = GaussianNode("tz_pcm.inp", newDir)
    newNode.routeSection = """%Chk=checkp.chk
%Mem=100GB
#P """+theoryHigh+"""
# nosymm
# Gfinput IOP(6/7=3)  Pop=full  Density  Test 
# Units(Ang,Deg)
"""
    newNode.additionalSection = """
stoichiometry=H2O1
solventname=Water2
eps=4
epsinf=1.77556
"""
    newNode.verification = "SP"
    newNode.readResults = True
    graph.add_node(newDir, data = newNode)
    graph.add_edge(node, newDir)
    
def addZPE(graph, node, expectedImaginaryFreqs = 0, theory = "B3LYP/6-31G(d,p)", basename = ""):
    newDir = join(node, basename + "freq")
    newNode = GaussianNode("freq.inp", newDir)
    newNode.verification = "Freq"
    newNode.readResults = True
    newNode.routeSection = """%Chk=checkp.chk
%Mem=100GB
#P """+theory+"""
# Freq nosymm
# Gfinput IOP(6/7=3)  Pop=full  Density  Test 
# Units(Ang,Deg)
"""
    newNode.noOfExcpectedImaginaryFrequetions = expectedImaginaryFreqs
    graph.add_node(newDir, data = newNode)
    graph.add_edge(node, newDir)
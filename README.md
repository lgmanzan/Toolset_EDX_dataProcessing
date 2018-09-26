# Toolset_EDX_dataProcessing

Authors: Lorena Gonzalez-Manzano and J. Maria de Fuentes

Organization: Universidad Carlos III de Madrid

This is the code of the paper "Design recommendations for online cybersecurity courses"  accepted in Computers and Security in 2018.

This code has been developed to ease the process of extracting MOOC performance data, we hereby present the proposed framework. It is presented as a Python open-source framework freely available.

This framework is composed of a pair of folders, scripts and statistics together with a pair of execution files, StructureDevelopment_edX.cmd and Statistics_edX.cmd. On the one hand, scripts folder contains all required scripts to create a sqlite3 database called moocDB.db, with all required data stored in it. These scripts should be initially executed running StructureDevelopment_edX.cmd. On the other hand, statistics folder contains a set of scripts to obtain statistics from data. These scripts can be executed after the creation of the database through the use of Statistics_edX.cmd. Note that execution files are prepared for Windows operating systems but as they run Python, they can be easily adapted to any other operating system.

All additional information can be found in the paper


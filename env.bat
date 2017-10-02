
@echo off
set PYTHONDIR=c:\Python27a
set PATH=%PYTHONDIR%;%PATH%

set PYTHONPATH=%~dp0;%~dp0/datamodel;%~dp0/services;%PYTHONPATH%

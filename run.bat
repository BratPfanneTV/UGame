rem Test
title UGame-Console
cd files
if "%1" == "-ip" (
if "%2" == "" (
	set ip=213.202.229.164
) else (
	set ip=%2
)
) else (
	set ip=213.202.229.164
)
if "%3" == "-port" (
if "%4" == "" (
	set port=1103
) else (
	set port=%2
)
) else (
	set port=1103
)
..\system\python main.py -ip %ip%:%port%
@echo off
cd ..
title Debug Four Dragon of Apocalypse
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
	set port=80
) else (
	set port=%2
)
) else (
	set port=80
)
..\system\python main.py -ip %ip%:%port%
@echo off
cd ..
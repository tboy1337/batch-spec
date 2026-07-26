@echo off
cmd /c exit 5
start "" cmd /c exit 9
echo EL=%ERRORLEVEL%

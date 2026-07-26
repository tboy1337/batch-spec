@echo off
for /f "tokens=*" %%a in ("   spaced") do echo star=%%a
for /f "delims=" %%a in ("   spaced") do echo keep=%%a

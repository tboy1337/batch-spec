@echo off
for /f "tokens=1,3 delims=," %%a in ("one,two,three") do echo A=%%a B=%%b

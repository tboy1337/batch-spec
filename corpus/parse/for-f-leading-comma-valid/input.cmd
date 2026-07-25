@echo off
for /f "tokens=1,2,3 delims=," %%a in (",a,b") do echo %%a %%b %%c

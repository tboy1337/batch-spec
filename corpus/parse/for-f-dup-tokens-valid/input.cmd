@echo off
for /f "tokens=1,2,1 delims=," %%a in ("A,B,C") do echo %%a %%b %%c

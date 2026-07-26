@echo off
set "opts=tokens=1,3 delims=,"
for /f "%opts%" %%a in ("one,two,three") do echo A=%%a B=%%b

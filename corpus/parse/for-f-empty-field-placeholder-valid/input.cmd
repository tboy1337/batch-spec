@echo off
setlocal EnableDelayedExpansion
set "line=a,,b"
set "line=!line:,,=,__EMPTY__,!"
for /f "tokens=1-3 delims=," %%a in ("!line!") do echo %%a %%b %%c

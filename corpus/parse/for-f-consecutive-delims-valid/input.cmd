@echo off
for /f "tokens=1,2 delims=," %%i in ("a,,b") do echo %%i %%j

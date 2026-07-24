@echo off
for /f "tokens=1,2 delims=, " %%a in ("a,b c") do echo %%a %%b

@echo off
for /f "tokens=1-3 delims=," %%a in (",b,c") do echo %%a
exit /b 0

@echo off
for /f "delims=" %%a in ('echo line1^&echo.^&echo line2') do echo %%a

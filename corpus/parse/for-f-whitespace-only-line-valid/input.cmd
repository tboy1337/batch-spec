@echo off
for /f "delims=" %%a in ("   ") do echo KEEP=%%a
for /f %%b in ("   ") do echo STRIP=%%b

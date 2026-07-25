@echo off
for /f "delims=" %%a in ("line1" "" "line2") do echo %%a

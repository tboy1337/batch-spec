@echo off
cmd /c exit 7
for /f %%a in (nosuch-xyz.txt) do echo %%a

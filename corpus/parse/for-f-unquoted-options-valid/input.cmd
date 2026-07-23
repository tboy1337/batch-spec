@echo off
for /f tokens^=1^,2 delims^=, %%a in (data.txt) do echo %%a

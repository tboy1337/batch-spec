@echo off
for /f "skip=2 tokens=*" %%a in (t.txt) do echo %%a

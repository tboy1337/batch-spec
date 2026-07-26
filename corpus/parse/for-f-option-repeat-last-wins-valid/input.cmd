@echo off
for /f "tokens=1 tokens=2 delims=," %%a in ("a,b,c") do echo %%a
for /f "skip=1 skip=2 eol=;" %%a in (data.txt) do echo %%a

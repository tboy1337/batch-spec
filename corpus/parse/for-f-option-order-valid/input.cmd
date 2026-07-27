@echo off
for /f "tokens=1 delims=," %%a in ("a,b") do echo %%a
for /f "delims=, tokens=1" %%a in ("a,b") do echo %%a

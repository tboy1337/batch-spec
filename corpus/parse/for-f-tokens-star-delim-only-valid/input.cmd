@echo off
for /f "tokens=* delims=x" %%A in ("xxx") do echo STAR=%%A
for /f "tokens=1,* delims=x" %%A in ("xxx") do echo ONESTAR=%%A

@echo off
for /f "skip=1 tokens=1" %%a in ("line1 line2") do echo %%a

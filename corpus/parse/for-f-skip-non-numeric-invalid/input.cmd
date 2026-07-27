@echo off
for /f "skip=xyz tokens=1" %%a in ("a b") do echo %%a

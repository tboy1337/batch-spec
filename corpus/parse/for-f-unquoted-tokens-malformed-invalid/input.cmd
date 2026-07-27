@echo off
for /F tokens^=1-2-3 %%a in ("a b c d") do echo %%a

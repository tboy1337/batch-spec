@echo off
for /F tokens^=1-2^ delims^=^, %%A in ("a,b,c") do echo %%A-%%B

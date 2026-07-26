@echo off
for /l %%i in (5,1,3) do echo should-not-run
echo after

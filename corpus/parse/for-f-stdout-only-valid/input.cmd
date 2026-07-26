@echo off
for /f %%a in ('cmd /c "echo OUT&echo ERR 1>&2"') do echo %%a

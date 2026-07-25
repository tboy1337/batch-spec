@echo off
goto :main
:lab
echo %1
goto :eof
:main
for %%i in (one) do call :lab %%i

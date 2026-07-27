@echo off
call :t hello
goto :eof
:t
echo bad=%1:~0,2%
set "s=%~1"
echo via=%s:~0,2%
goto :eof

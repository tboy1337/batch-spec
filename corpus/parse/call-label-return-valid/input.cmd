@echo off
call :sub arg1
goto :eof
:sub
echo %1
goto :eof

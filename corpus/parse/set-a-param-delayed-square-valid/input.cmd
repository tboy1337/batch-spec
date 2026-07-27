@echo off
setlocal EnableDelayedExpansion
set n=3
call :sq n
echo n=%n%
goto :eof
:sq
set /a %~1=!%~1!*!%~1!
goto :eof

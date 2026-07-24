@echo off
call :add total 1 2
echo %total%
goto :eof
:add
set /a %~1=%~2+%~3
goto :eof

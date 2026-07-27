@echo off
call :t foo_bar
goto :eof
:t
echo bad=%1:_=-%
set "s=%~1"
echo via=%s:_=-%
goto :eof

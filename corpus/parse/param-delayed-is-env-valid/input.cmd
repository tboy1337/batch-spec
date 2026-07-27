@echo off
setlocal EnableDelayedExpansion
call :t hello
goto :eof
:t
set "1=ENV"
echo pct=%1
echo bang=!1!
goto :eof

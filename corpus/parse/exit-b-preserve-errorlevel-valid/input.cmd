@echo off
call :inner
echo after=%ERRORLEVEL%
goto :eof
:inner
cmd /c exit 7
exit /b

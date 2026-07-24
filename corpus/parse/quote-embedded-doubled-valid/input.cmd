@echo off
call :show "a""b"
goto :eof
:show
echo %~1
exit /b 0

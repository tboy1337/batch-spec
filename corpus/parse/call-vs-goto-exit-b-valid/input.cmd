@echo off
call :Abort
echo AFTER_CALL
goto :eof
:Abort
exit /b 3

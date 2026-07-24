@echo off
goto :skip
:run
echo ran
goto :eof
:skip
call :run
echo after_call

@echo off
call :show a,b c=d e;f
goto :eof
:show
echo %1 %2 %3 %4 %5
goto :eof

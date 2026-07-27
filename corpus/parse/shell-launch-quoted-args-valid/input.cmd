@echo off
call :show "C:\path one.ext" "D:\path two.ext"
goto :eof
:show
echo P1=%~1
echo P2=%~2

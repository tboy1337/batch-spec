@echo off
call :sub
echo after
goto :eof
:sub
echo in-sub
:tail
echo in-tail

@echo off
call :t “hello” world
goto :eof
:t
echo 1=%1
echo 2=%2
goto :eof

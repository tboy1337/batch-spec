@echo off
call :t a b
goto :eof
:t
echo before %1 %2
shift
echo after %1 %2
goto :eof

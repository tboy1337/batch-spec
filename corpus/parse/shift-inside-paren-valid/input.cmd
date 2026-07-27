@echo off
call :t one two
goto :eof
:t
(
shift
echo %1
)
goto :eof

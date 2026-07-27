@echo off
call :t one two
goto :eof
:t
(
shift
echo INSIDE=%1
)
echo AFTER=%1
goto :eof

@echo off
echo MAIN1
call :Unfenced
echo AFTER_CALL
goto :eof
:Unfenced
echo IN_LABEL

@echo off
call :outer >call_redir_audit.txt
echo AFTER
goto :eof
:outer
echo OUTER
call :inner
goto :eof
:inner
echo INNER
goto :eof

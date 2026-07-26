@echo off
echo parent=%CMDCMDLINE%
call child.cmd
echo after=%CMDCMDLINE%

@echo off
rem See expansion.yaml set_assignment.bat_vs_cmd_errorlevel for .bat vs .cmd after ASSOC
cmd /C exit 42
assoc >nul

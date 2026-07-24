@echo off
rem .bat preserves ERRORLEVEL after successful SET; .cmd clears to 0
cmd /C exit 42
set FOO=1

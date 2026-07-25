@echo off
setlocal DisableExtensions EnableDelayedExpansion
set BAR=abcdef
echo bang=!BAR:~1,2!
echo pct=%BAR:~1,2%

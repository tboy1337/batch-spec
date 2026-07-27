@echo off
setlocal EnableDelayedExpansion
set survive=OUTER
setlocal
set survive=LOCAL
(endlocal & echo %survive% & echo !survive!)

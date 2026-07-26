@echo off
setlocal DisableDelayedExpansion
set "V=aa!bb!cc"
setlocal EnableDelayedExpansion
echo PCT=%V%
echo BANG=!V!

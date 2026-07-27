@echo off
setlocal EnableDelayedExpansion
set i=1
set "arr[1]=alpha"
set "arr[!i!]=beta"
echo !arr[1]!

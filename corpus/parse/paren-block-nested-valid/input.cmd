@echo off
setlocal EnableDelayedExpansion
set x=outer
(
set x=mid
(
set x=inner
echo %x% !x!
)
)

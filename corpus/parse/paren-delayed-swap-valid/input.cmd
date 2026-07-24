@echo off
setlocal EnableDelayedExpansion
set a=1
set b=2
(
set a=!b!
set b=!a!
)

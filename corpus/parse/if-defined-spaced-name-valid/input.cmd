@echo off
set "a b=1"
if defined a echo A_ONLY
if defined "a b" echo QUOTED
echo PCT=%a b%

@echo off
set "b=true==true"
if not %b% echo bad
set "b=false==x"
if not %b% echo good

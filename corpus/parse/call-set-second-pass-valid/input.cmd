@echo off
set name=other
set other=value
call set "out=%%%name%%%"
echo %out%

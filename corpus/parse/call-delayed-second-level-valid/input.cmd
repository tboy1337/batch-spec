@echo off
setlocal EnableDelayedExpansion
set food=fruit
set fruit=apple
call set "got=%%%food%%%"
echo !got!

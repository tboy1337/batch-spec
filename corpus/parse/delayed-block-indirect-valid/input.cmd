@echo off
setlocal EnableDelayedExpansion
set name=outer
set prefix=pre
for %%i in (1) do (
  set name=inner
  echo !prefix%name%!
)

@echo off
setlocal EnableDelayedExpansion
set foodNYC=bagel
set city=OLD
for %%x in (1) do (
  set city=NYC
  call echo %%food!city!%%
)

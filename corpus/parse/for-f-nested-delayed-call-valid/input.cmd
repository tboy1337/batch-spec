@echo off
setlocal EnableDelayedExpansion
set LIST=
for %%a in (1 2) do (
  for /f %%b in ("%%a") do (
    set LIST=!LIST! %%b
    call :reparse %%b
  )
)
goto :eof
:reparse
echo R=%~1
goto :eof

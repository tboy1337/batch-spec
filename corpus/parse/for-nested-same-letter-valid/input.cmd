@echo off
for %%A in (outer) do (
  for %%A in (inner) do echo %%A
  echo %%A
)

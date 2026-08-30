@echo off
for %%F in (report.log) do (
    if exist %%F (
      echo --- %%F (found) ---
    )
)

@echo off
for /f "tokens=5,7,1-3" %%a in ("A B C D E F G H") do echo SORT=%%a %%b %%c %%d %%e
for /f "tokens=1-3,5,7" %%a in ("A B C D E F G H") do echo EQ=%%a %%b %%c %%d %%e

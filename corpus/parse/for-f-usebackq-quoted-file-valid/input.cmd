@echo off
FOR /F "usebackq tokens=*" %%i IN ("input file.txt") DO echo %%i

@echo off
FOR /F "usebackq tokens=*" %%i IN (`echo hello`) DO echo %%i

@echo off
for /f "usebackq tokens=*" %%a in ('literal string') do echo %%a

@echo off
for /f "eol=" %%a in ("#keep") do echo %%a
for /f "eol= delims=," %%a in ("#keep,x") do echo %%a

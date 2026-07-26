@echo off
set COUNT=0
for %%i in (nosuch_zzz_audit_*.xyz) do set /a COUNT+=1
echo COUNT=%COUNT%

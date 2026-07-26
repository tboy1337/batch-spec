@echo off
call foo_label_audit
echo AFTER
goto :eof
:foo_label_audit
echo HIT

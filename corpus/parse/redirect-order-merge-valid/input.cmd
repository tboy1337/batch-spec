@echo off
dir nosuch >out.txt 2>&1
dir nosuch 2>&1 >out2.txt

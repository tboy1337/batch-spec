@echo off
type file.txt | findstr pat >out.txt
type file.txt >out2.txt | findstr pat >out3.txt


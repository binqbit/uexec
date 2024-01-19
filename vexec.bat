@echo off
color b
cd /d %~dp0

if "%1" == "--key" (
    call python .\src\main.py %*
) else if "%1" == "--admin" (
    setlocal EnableDelayedExpansion
    set all_args=%*
    set args=!all_args:~8!
    powershell -Command "Start-Process cmd -ArgumentList '/c %~dp0\vexec.bat !args!' -Verb RunAs"
) else (
    call python .\src\main.py %*
)
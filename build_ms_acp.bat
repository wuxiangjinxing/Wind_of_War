set path=C:\Python26;%PATH%
@echo off
python process_acp.py
@del *.pyc
echo.
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul
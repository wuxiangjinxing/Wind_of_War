set path=C:\Python26;%PATH%
@echo off
@del Process_Log.txt
echo Getting Header Files .........
copy ".\header files\*.*" ".\" >>Process_Log.txt
echo Getting ID Files .........
copy ".\ID files\*.*" ".\" >>Process_Log.txt
echo Getting Process Files .........
copy ".\process files\*.*" ".\" >>Process_Log.txt
echo Start Processing...
echo ______________________________
echo.
python factionize_items_all.py

@del *.pyc
@del header_*.py
copy ".\ID_*.py" ".\ID files\" >>Process_Log.txt
@del ID_*.py
@del process_*.py
echo.
echo All Finish ...
echo Cleaning up...
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul
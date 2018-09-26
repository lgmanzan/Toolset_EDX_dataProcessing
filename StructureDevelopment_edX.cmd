

echo start

REM %1 dir of scripts
REM %2 dir of data
REM %3 number of exams in total in all lectures (not including the final exam
REM %4 number of readings in total in all lectures
REM %5 folder of python.exe

cd %5

python.exe %1CreateTables.py

echo end CreateTables

python.exe %1preprocessStorageVideosMainTable.py %2Data_tables_videos.csv

echo end preprocessStorageVideosMainTable

python.exe %1preprocessStorageExamsReadingsMainTable.py %2Data_tables_examsReadings.csv

echo end preprocessStorageVideosMainTable


python.exe %1preprocessStorageAllVideo.py %2Videos %2changeNamesFromedXtoidVideo.csv

echo 'end preprocessStorageAllVideo'


python.exe %1preprocessStorageAllExamsReadings.py %2Data_tables_marks.csv %3 %4

echo end preprocessStorageAllExamsReading

python.exe %1preprocessStorageAllComments.py %2Data_tables_comments.csv


echo 'end preprocessStorageAllComments'

python.exe %1CreateStorageTableUsers.py %2usersProfilePreprocessed.csv

echo end usersProfilePreprocessed




echo start

REM %1 dir of scripts
REM %2 place to leave results
REM %3 folder of python.exe

cd %3

python.exe %1StatisticQueries_WhoHasPerformedComments.py > %2WhoHasPerformedComments.txt

echo end WhoHasPerformedComments

python.exe %1StatisticQueries_WhoHasCybersecurityInterest.py > %2WhoHasCybersecurityInterest.txt

echo end WhoHasCybersecurityInterest

python.exe %1StatisticQueries_WhoHasAnsweredBetterToExamsReadings.py > %2WhoHasAnsweredBetterToExamsReadings.txt

echo end WhoHasCybersecurityInterest

python.exe %1StatisticQueries_WhoHasAnsweredBetterFinalExam.py > %2StatisticQueries_WhoHasAnsweredBetterFinalExam.txt

echo end StatisticQueries_WhoHasAnsweredBetterFinalExam

python.exe %1StatisticQueries_WhoHasSeenMoreVideosPerLecture.py > %2StatisticQueries_WhoHasSeenMoreVideosPerLecture.txt

echo end StatisticQueries_WhoHasSeenMoreVideosPerLecture

python.exe %1StatisticQueries.py > %2StatisticQueries.txt

echo end StatisticQueries

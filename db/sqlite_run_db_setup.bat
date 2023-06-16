@echo off
sqlite3 sqlite_soloproject.db ".read sqlite_db_setup.sql"
sqlite3 sqlite_soloproject.db ".read db_populate.sql"
pause
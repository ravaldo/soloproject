@echo off
psql -U postgres -d soloproject -f db_setup.sql
pause
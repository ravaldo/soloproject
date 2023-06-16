@echo off
psql -U postgres -d soloproject -f postgres_db_setup.sql
psql -U postgres -d soloproject -f db_populate.sql
pause
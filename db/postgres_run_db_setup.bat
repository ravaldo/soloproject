@echo off
psql -U postgres -d soloproject -f db_setup_postgres.sql
psql -U postgres -d soloproject -f db_setup_inserts.sql
pause
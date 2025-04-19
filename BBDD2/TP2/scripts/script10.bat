@echo off
mongodump --version 

mongodump --db empresa --out ./backups

mongorestore --db empresa ./backups



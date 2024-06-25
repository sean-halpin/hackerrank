
Create postgres role, req'd by scripts in Data folder
```
➜  Data docker exec -it postgres bash
root@d35f8fd2a201:/# psql -U admin -d mydatabase
psql (16.3 (Debian 16.3-1.pgdg120+1))
Type "help" for help.

mydatabase=# CREATE ROLE postgres WITH LOGIN SUPERUSER PASSWORD 'admin';
```

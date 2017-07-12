## WHAT IS THIS?
This is a project created to test how many requests a Django API can handle. This will help the CIS team decide on what framework to use for the FCIS.

## Local Setup
*P.S.: Replace `<database user>` and `<database name>`, `<host>` and `<port>` with actual values.*

Clone the repo

`cd` into the folder and install dependencies:
```bash
pip install -r requirements.txt
```

### Database
Run the following commands to:


##### Create the database:
```bash
psql -f database_files/stripped_ddl/db_create.sql
```


##### Create tables:
```sql
psql -d <database name> -f database_files/stripped_ddl/create_tables.sql
```
P.S.: After running the create tables script, connect to the database and grant all privileges to the database user:
```sql
$ psql
# \c <database name>
# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;
```


##### Drop tables:
```sql
psql -d <database name> -f database_files/stripped_ddl/drop_tables.sql
```


##### Drop the database:
```sql
psql -f database_files/stripped_ddl/db_drop.sql
```


##### Seeding the database with dummy test data:
```sql
psql -U <database user> <database name> < database_files/stripped_ddl/dbexport.pgsql
```


#### Connect to Database
Create a file named `.env` in the root of the project and add the following entries. See `.env.temp` file for sample

```
DB_NAME="<database name>"
DB_USER="<database user>"
DB_PASSWORD="<database password>"
DB_HOST=127.0.0.1
DB_PORT=5432
```
The `.env` file has been gitignored.

### Collecting Static files
```
./manage.py collectstatic
```


### Running the API:
1. Start the server using `./manage.py runserver`
2. Go to `localhost:8000/api/v1/docs` to see the live documentation for available endpoints.
3. Go to `localhost:8000/api/v1` to access the API's root page.

### Running the API with gunicorn:
1. Start the gunicorn server using `gunicorn cis_api.wsgi --pythonpath=cis_api -w=2 --log-file -` (Optional: -w `<number of workers>`)
2. Repeat steps 2 and/or 3 in **Running the API** section
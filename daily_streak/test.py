

CREATE LOGIN saas_qa_v1 WITH PASSWORD='RJ25y3HSmX9W';

CREATE USER saas_qa_v1 FOR LOGIN saas_qa_v1 WITH DEFAULT_SCHEMA=[saas_qa_v1];

EXEC sp_addrolemember 'dbmanager', 'saas_qa_v1';



CREATE USER saas_qa_v1 FOR LOGIN saas_qa_v1 WITH DEFAULT_SCHEMA=[saas_qa_v1]

CREATE SCHEMA saas_qa_v1;

EXEC sp_addrolemember 'db_datawriter', 'saas_qa_v1'

EXEC sp_addrolemember 'db_datareader', 'saas_qa_v1'

GRANT CREATE TABLE TO saas_qa_v1;

GRANT SELECT,INSERT,ALTER,REFERENCES,UPDATE,DELETE ON SCHEMA:: saas_qa_v1 to saas_qa_v1;
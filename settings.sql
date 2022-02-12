DROP DATABASE mangaq_backend;
DROP USER mangaq_backenduser;
CREATE DATABASE mangaq_backend;
CREATE USER mangaq_backenduser WITH PASSWORD 'mangaq_backend';
GRANT ALL PRIVILEGES ON DATABASE mangaq_backend TO mangaq_backenduser;
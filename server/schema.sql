create table IF NOT EXISTS measurement (
	id INTEGER NOT NULL PRIMARY KEY,
	sensor TEXT,
	value REAL,
	timestamp DATE DEFAULT CURRENT_TIMESTAMP
)
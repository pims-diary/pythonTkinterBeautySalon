# Scripts

### Create Database
`CREATE DATABASE BeautySalon;`

### Create Users Table:
```
CREATE TABLE Users(
  	username VARCHAR(64),
  	password VARCHAR(128)
);
```

### Create Customers Table:
```
CREATE TABLE Customers(
	customerId INT NOT NULL,
  	name VARCHAR(128),
  	email VARCHAR(128),
	phone VARCHAR(128),
	type VARCHAR(64),
	PRIMARY KEY(customerId)
);
```
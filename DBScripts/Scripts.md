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
	isNew bit,
	PRIMARY KEY(customerId)
);
```

### Create Offerings Table:
```
CREATE TABLE Offerings(
	offeringId INT NOT NULL,
  	offeringName VARCHAR(128),
  	offeringType VARCHAR(128),
	description VARCHAR(128),
	price VARCHAR(128),
	PRIMARY KEY(offeringId)
);
```

### Insert a Row in Offerings Table
```
INSERT INTO Offerings(
    offeringId, 
    offeringName, 
    description, 
    offeringType, 
    price
) VALUES (
    5009, 
    'Olive Oil Styling Gel', 
    'Olive oil helps your scalp naturally regulate its own moisturizing system', 
    'Product', 
    25.00
)
```
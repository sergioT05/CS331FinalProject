CREATE TABLE RENTAL_BRANCH (
BranchID INT NOT NULL AUTO_INCREMENT,
   	 Street_Address VARCHAR(100),
 City VARCHAR(50),
 	State VARCHAR(20),
 	Zip_Code VARCHAR(10),
    ContactInformation VARCHAR(100),
    PRIMARY KEY (BranchID)
);

CREATE TABLE CUSTOMER (
CustomerID INT NOT NULL,
C_FName VARCHAR(50) NOT NULL,
 C_LName VARCHAR(50) NOT NULL,
	DateOfBirth DATE,
	Phone VARCHAR(15),
	Email VARCHAR(50) NOT NULL,
	Password VARCHAR(255) NOT NULL,
Street_Address VARCHAR(100), 
City VARCHAR(50),
 State VARCHAR(20), 
Zip_Code VARCHAR(10),
    PRIMARY KEY (CustomerID),
    UNIQUE (Email)
);

CREATE TABLE CAR (
	CarID INT NOT NULL AUTO_INCREMENT,
	LicensePlateNumber VARCHAR(8) NOT NULL,
	Model VARCHAR(50),
	Brand	VARCHAR(50),
	Category VARCHAR(50),
	YearOfManufacture INT,
	RentalStatus VARCHAR(50),
	BranchID INT NOT NULL,
	UNIQUE (LicensePlateNumber),
	PRIMARY KEY (CarID),
	FOREIGN KEY(BranchID) REFERENCES RENTAL_BRANCH(BranchID)
);

CREATE TABLE RENTAL_AGREEMENT (
	Rental_ID INT NOT NULL AUTO_INCREMENT,
	Start_Date DATE NOT NULL,
	End_Date DATE,
	DailyRate FLOAT,
	TotalCost FLOAT,
	CustomerID INT NOT NULL,
	CarID INT NOT NULL,
    PRIMARY KEY (Rental_ID),
    FOREIGN KEY(CustomerID) REFERENCES CUSTOMER(CustomerID),
    FOREIGN KEY(CarID) REFERENCES CAR(CarID)
);

CREATE TABLE PAYMENT (
	Payment_ID INT NOT NULL AUTO_INCREMENT,
	PDate DATE NOT NULL,
	Amount FLOAT,
	Method VARCHAR(50),
	Rental_ID INT NOT NULL,
	PRIMARY KEY (Payment_ID),
	FOREIGN KEY(Rental_ID) REFERENCES RENTAL_AGREEMENT(Rental_ID)
);

CREATE TABLE STAFF_MEMBER (
	EmployeeID INT NOT NULL AUTO_INCREMENT,
S_FName VARCHAR(50) NOT NULL,
 S_LName VARCHAR(50) NOT NULL, 
	Role VARCHAR(50),
	Salary FLOAT,
	BranchID INT NOT NULL,
	Password VARCHAR(255) NOT NULL,
	PRIMARY KEY (EmployeeID),
	FOREIGN KEY(BranchID) REFERENCES RENTAL_BRANCH(BranchID)
);

CREATE TABLE MAINTENANCE_RECORD (
	MaintenanceID INT NOT NULL AUTO_INCREMENT,
	MDate DATE NOT NULL,
	DescriptionOfWork VARCHAR(250),
	Cost FLOAT,
	CarID INT NOT NULL,
	PRIMARY KEY (MaintenanceID),
	FOREIGN KEY(CarID) REFERENCES CAR(CarID)
);



INSERT INTO RENTAL_BRANCH (Street_Address, City, State, Zip_Code, ContactInformation)
VALUES ('123 Market ST', 'Newark', 'NJ', '07102', '973-555-0101');
INSERT INTO RENTAL_BRANCH (Street_Address, City, State, Zip_Code, ContactInformation)
VALUES ('456 Grove St', 'Jersey City', 'NJ', '07302', '201-555-0102');
INSERT INTO RENTAL_BRANCH (Street_Address, City, State, Zip_Code, ContactInformation)
VALUES ('789 Oak Tree Rd', 'Edison', 'NJ', '08620', '732-555-0103');
INSERT INTO RENTAL_BRANCH (Street_Address, City, State, Zip_Code, ContactInformation)
VALUES ('101 Hooper Ave', 'Toms River', 'NJ', '08753', '908-555-0104');
INSERT INTO RENTAL_BRANCH (Street_Address, City, State, Zip_Code, ContactInformation)
VALUES ('202 Main St', 'Paterson', 'NJ', '07505', '862-555-0105');


INSERT INTO STAFF_MEMBER (S_FName, S_LName, Role, Salary, BranchID, Password)
VALUES ('Super', 'Admin', 'Admin', 80000, 1, 'admin123');


INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('ABC-123', 'IS500', 'Lexus', 'Sedan', 2022, 'rented', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('XYZ-987', 'Mustang GT', 'Ford', 'Coupe', 2019, 'available', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('SUV-555', 'M5', 'BMW', 'Sedan', 2024, 'under maintenance', 2);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('DEF-345', 'Model Y', 'Tesla', 'SUV', 2023, 'available', 3);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('XWH-643', 'Bronco', 'Ford', 'SUV', 2022, 'available', 4);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('AGC-574', 'M4 Competition', 'BMW', 'coupe', 2023, 'under maintenance', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('YTE-243', 'Bronco', 'Ford', 'SUV', 2022, 'available', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('EIO-362', 'Civic', 'Honda', 'Sedan', 2025, 'available', 1);
 INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('JKL-001', 'Camry', 'Toyota', 'Sedan', 2023, 'available', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('JKL-002', 'Corolla', 'Toyota', 'Sedan', 2022, 'available', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('JKL-003', 'Accord', 'Honda', 'Sedan', 2024, 'available', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('JKL-004', 'Altima', 'Nissan', 'Sedan', 2021, 'available', 5);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('JKL-005', 'Tahoe', 'Chevrolet', 'SUV', 2023, 'available', 5);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('JKL-006', 'Suburban', 'Chevrolet', 'SUV', 2022, 'available', 3);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('JKL-007', 'Explorer', 'Ford', 'SUV', 2024, 'available', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('JKL-008', 'Mustang', 'Ford', 'Coupe', 2023, 'available', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('JKL-009', 'Challenger', 'Dodge', 'Coupe', 2022, 'available', 2);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('RNT-101', 'Model 3', 'Tesla', 'Sedan', 2023, 'rented', 4);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('RNT-102', 'Model S', 'Tesla', 'Sedan', 2022, 'rented', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('RNT-103', 'X5', 'BMW', 'SUV', 2024, 'rented', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('RNT-104', 'C-Class', 'Mercedes', 'Sedan', 2023, 'rented', 4);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('MNT-201', 'Wrangler', 'Jeep', 'SUV', 2021, 'under maintenance', 1);
INSERT INTO CAR (LicensePlateNumber, Model, Brand, Category, YearOfManufacture, RentalStatus, BranchID)
 VALUES ('MNT-202', '911 Carrera', 'Porsche', 'Coupe', 2022, 'under maintenance', 1);




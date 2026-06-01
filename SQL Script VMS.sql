-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema scm
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema scm
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `scm` DEFAULT CHARACTER SET utf8mb3 ;
USE `scm` ;

-- -----------------------------------------------------
-- Table `scm`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`categories` (
  `CategoryID` INT NOT NULL AUTO_INCREMENT,
  `CategoryName` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`CategoryID`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`customers` (
  `CustomerID` INT NOT NULL AUTO_INCREMENT,
  `CustomerName` VARCHAR(45) NULL DEFAULT NULL,
  `Phone` VARCHAR(45) NULL DEFAULT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `Address` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`CustomerID`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`salesorders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`salesorders` (
  `SalesID` INT NOT NULL AUTO_INCREMENT,
  `SalesDate` DATETIME NULL DEFAULT NULL,
  `CustomerID` INT NULL DEFAULT NULL,
  `TotalAmount` DECIMAL(10,2) NULL DEFAULT NULL,
  `Status` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`SalesID`),
  INDEX `CustomerID_idx` (`CustomerID` ASC) VISIBLE,
  CONSTRAINT `fk_salesorders_customers`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `scm`.`customers` (`CustomerID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`payments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`payments` (
  `PaymentID` INT NOT NULL AUTO_INCREMENT,
  `SalesID` INT NULL DEFAULT NULL,
  `PaymentDate` DATETIME NULL DEFAULT NULL,
  `Amount` DECIMAL(10,2) NULL DEFAULT NULL,
  `PaymentMethod` VARCHAR(45) NULL DEFAULT NULL,
  `Status` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`PaymentID`),
  INDEX `SalesID_idx` (`SalesID` ASC) VISIBLE,
  CONSTRAINT `fk_payments_salesorders`
    FOREIGN KEY (`SalesID`)
    REFERENCES `scm`.`salesorders` (`SalesID`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`products` (
  `ProductID` INT NOT NULL AUTO_INCREMENT,
  `ProductName` VARCHAR(45) NULL DEFAULT NULL,
  `Description` VARCHAR(45) NULL DEFAULT NULL,
  `CategoryID` INT NULL DEFAULT NULL,
  `BuyingPrice` DECIMAL(10,2) NULL DEFAULT NULL,
  `SellingPrice` DECIMAL(10,2) NULL DEFAULT NULL,
  `MeasurementUnits` VARCHAR(45) NULL DEFAULT NULL,
  `Quantity` INT NULL DEFAULT NULL,
  `LastUpdated` DATETIME NULL DEFAULT NULL,
  `LastPurchasePrice` DECIMAL(10,2) NULL DEFAULT NULL,
  `LastPurchaseDate` DATETIME NULL DEFAULT NULL,
  `LastSellPrice` DECIMAL(10,2) NULL DEFAULT NULL,
  `LastSellDate` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`ProductID`),
  INDEX `CategoryID_idx` (`CategoryID` ASC) VISIBLE,
  CONSTRAINT `fk_products_categories`
    FOREIGN KEY (`CategoryID`)
    REFERENCES `scm`.`categories` (`CategoryID`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`suppliers` (
  `SupplierID` INT NOT NULL AUTO_INCREMENT,
  `SupplierName` VARCHAR(45) NULL DEFAULT NULL,
  `Phone` VARCHAR(20) NULL DEFAULT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `Address` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`SupplierID`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`purchaseorders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`purchaseorders` (
  `PurchaseID` INT NOT NULL AUTO_INCREMENT,
  `PurchaseDate` DATETIME NULL DEFAULT NULL,
  `SupplierID` INT NULL DEFAULT NULL,
  `TotalAmount` DECIMAL(10,2) NULL DEFAULT NULL,
  `Status` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`PurchaseID`),
  INDEX `SupplierID_idx` (`SupplierID` ASC) VISIBLE,
  CONSTRAINT `fk_purchaseorders_suppliers`
    FOREIGN KEY (`SupplierID`)
    REFERENCES `scm`.`suppliers` (`SupplierID`))
ENGINE = InnoDB
AUTO_INCREMENT = 15
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`purchasedetail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`purchasedetail` (
  `PurchaseID` INT NOT NULL,
  `ProductID` INT NOT NULL,
  `Quantity` INT NULL DEFAULT NULL,
  `UnitPrice` DECIMAL(10,2) NULL DEFAULT NULL,
  `ReceivedQty` INT NULL DEFAULT NULL,
  PRIMARY KEY (`PurchaseID`, `ProductID`),
  INDEX `ProductID_idx` (`ProductID` ASC) VISIBLE,
  CONSTRAINT `fk_purchasedetail_products`
    FOREIGN KEY (`ProductID`)
    REFERENCES `scm`.`products` (`ProductID`),
  CONSTRAINT `fk_purchasedetail_purchaseorders`
    FOREIGN KEY (`PurchaseID`)
    REFERENCES `scm`.`purchaseorders` (`PurchaseID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`roles` (
  `RoleID` INT NOT NULL AUTO_INCREMENT,
  `RoleName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`RoleID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`salesdetail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`salesdetail` (
  `SalesID` INT NOT NULL,
  `ProductID` INT NOT NULL,
  `Quantity` INT NULL DEFAULT NULL,
  `UnitPrice` DECIMAL(10,2) NULL DEFAULT NULL,
  `Discount` DECIMAL(10,2) NULL DEFAULT NULL,
  `Subtotal` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`SalesID`, `ProductID`),
  INDEX `ProductID_idx` (`ProductID` ASC) VISIBLE,
  CONSTRAINT `fk_salesdetail_products`
    FOREIGN KEY (`ProductID`)
    REFERENCES `scm`.`products` (`ProductID`),
  CONSTRAINT `fk_salesdetail_salesorders`
    FOREIGN KEY (`SalesID`)
    REFERENCES `scm`.`salesorders` (`SalesID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`supplierpayments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`supplierpayments` (
  `SupplierPaymentsID` INT NOT NULL AUTO_INCREMENT,
  `PurchaseID` INT NULL DEFAULT NULL,
  `SupplierID` INT NULL DEFAULT NULL,
  `PaymentDate` DATETIME NULL DEFAULT NULL,
  `Amount` DECIMAL(10,2) NULL DEFAULT NULL,
  `PaymentMethod` VARCHAR(45) NULL DEFAULT NULL,
  `Status` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`SupplierPaymentsID`),
  INDEX `PurchaseID_idx` (`PurchaseID` ASC) VISIBLE,
  CONSTRAINT `fk_supplierpayments_purchaseorders`
    FOREIGN KEY (`PurchaseID`)
    REFERENCES `scm`.`purchaseorders` (`PurchaseID`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `scm`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scm`.`users` (
  `UserID` INT NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(255) NOT NULL,
  `RoleID` INT NULL DEFAULT NULL,
  `CreatedAt` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  INDEX `fk_users_roles` (`RoleID` ASC) VISIBLE,
  CONSTRAINT `fk_users_roles`
    FOREIGN KEY (`RoleID`)
    REFERENCES `scm`.`roles` (`RoleID`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

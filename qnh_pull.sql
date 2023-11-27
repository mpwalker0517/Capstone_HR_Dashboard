SELECT `contacts`.`ContactName` as 'Employee', `userdefinedfields`.`UserDefinedFieldID` as 'Product',`userdefinedfields`.`Name` as 'Assessment',`userdefinedvalues`.`UDFValue` as 'Score_Date'
FROM `mwalkerlcs-morgan_rm12`.`userdefinedfields`
INNER JOIN `mwalkerlcs-morgan_rm12`.`userdefinedvalues` ON `userdefinedfields`.`UserDefinedFieldID`=`userdefinedvalues`.`UserDefinedFieldID`
INNER JOIN `mwalkerlcs-morgan_rm12`.`contacts` ON `contacts`.`EntityKeyID`=`userdefinedvalues`.`EntityKeyID`
INNER JOIN `mwalkerlcs-morgan_rm12`.`leases` ON `contacts`.`EntityKeyID`=`leases`.`CustomerID`
WHERE `userdefinedfields`.`EntityTypeID`=1 AND `leases`.`MoveOutDate` IS NULL 
AND `userdefinedfields`.`UserDefinedFieldID` = 37 OR `userdefinedfields`.`UserDefinedFieldID` = 38 OR `userdefinedfields`.`UserDefinedFieldID` = 39 OR `userdefinedfields`.`UserDefinedFieldID` = 40;
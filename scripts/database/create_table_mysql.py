from sqlalchemy import (create_engine, exc, MetaData, Table, Column, Integer, DECIMAL, String, Float, TEXT, TIMESTAMP ,ForeignKeyConstraint)
import config

try:
    engine = create_engine(f"mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db_name}", echo=False)
    print('Database connected.')
except exc.SQLAlchemyError as e:
    print("Database not connected", e)

metadata = MetaData(bind=engine)

person_table = Table('person_table', metadata,
    Column('BusinessEntityID',         Integer, primary_key=True),
    Column('PersonType',               String(10), index=True),
    Column('NameStyle',                Integer),
    Column('Title',                   String(10)),
    Column('FirstName',               String(50)),
    Column('MiddleName',              String(50)),
    Column('LastName',                String(50)),
    Column('Suffix',                  String(10)),
    Column('EmailPromotion',          Integer),
    Column('AdditionalContactInfo',    TEXT),
    Column('Demographics',             TEXT),
    Column('rowguid',                 String(100)),
    Column('ModifiedDate',             TIMESTAMP),
)

customer_table = Table('customer_table', metadata,
    Column('CustomerID',         Integer, primary_key=True),
    Column('PersonID',           Integer),
    Column('StoreID',            Integer),
    Column('TerritoryID',        Integer),
    Column('AccountNumber',      String(50)),
    Column('rowguid',            String(100)),
    Column('ModifiedDate',       TIMESTAMP),
    ForeignKeyConstraint(['PersonID'], ['person_table.BusinessEntityID'], name='FK_Customer_Person_PersonID')
)

sales_order_header_table = Table('sales_order_header_table', metadata,
    Column('SalesOrderID',         Integer, primary_key=True),
    Column('RevisionNumber',           Integer),
    Column('OrderDate',            TIMESTAMP),
    Column('DueDate',        TIMESTAMP),
    Column('ShipDate',      TIMESTAMP),
    Column('Status',            Integer),
    Column('OnlineOrderFlag',            Integer),
    Column('SalesOrderNumber',            String(30)),
    Column('PurchaseOrderNumber',            String(30)),
    Column('AccountNumber',            String(30)),
    Column('CustomerID',            Integer),
    Column('SalesPersonID',            Integer),
    Column('TerritoryID',            Integer),
    Column('BillToAddressID',            Integer),
    Column('ShipToAddressID',            Integer),
    Column('ShipMethodID',            Integer),
    Column('CreditCardID',            Integer),
    Column('CreditCardApprovalCode',            String(30)),
    Column('CurrencyRateID',            Integer),
    Column('SubTotal',            DECIMAL(10, 2)),
    Column('TaxAmt',            DECIMAL(10, 2)),
    Column('Freight',            DECIMAL(10, 2)),
    Column('TotalDue',            DECIMAL(15, 2)),
    Column('Comment',            TEXT),
    Column('rowguid',            String(100)),
    Column('ModifiedDate',       TIMESTAMP),
    ForeignKeyConstraint(['CustomerID'], ['customer_table.CustomerID'], name='FK_SalesOrderHeader_Customer_CustomerID')
)

sales_order_detail_table = Table('sales_order_detail_table', metadata,
    Column('SalesOrderID',         Integer, primary_key=True),
    Column('SalesOrderDetailID',         Integer, primary_key=True),
    Column('CarrierTrackingNumber',           String(30)),
    Column('OrderQty',            Integer),
    Column('ProductID',        Integer),
    Column('SpecialOfferID',      Integer),
    Column('UnitPrice',            DECIMAL(10, 2)),
    Column('UnitPriceDiscount',            Float),
    Column('LineTotal',            DECIMAL(10, 2)),
    Column('rowguid',            String(100)),
    Column('ModifiedDate',       TIMESTAMP),
    ForeignKeyConstraint(['SalesOrderID'], ['sales_order_header_table.SalesOrderID'],
                         name='FK_SalesOrderDetail_SalesOrderHeader_SalesOrderID')
)

special_offer_product_table = Table('special_offer_product_table', metadata,
    Column('SpecialOfferID',         Integer, primary_key=True),
    Column('ProductID',         Integer, primary_key=True),
    Column('rowguid',            String(100)),
    Column('ModifiedDate',       TIMESTAMP),
    # ForeignKeyConstraint(['ProductID'], ['sales_order_detail_table.ProductID'],
    #                      name='FK_SalesOrderDetail_SpecialOfferProduct_SpecialOfferProductID')
)

product_table = Table('product_table', metadata,
    Column('ProductID',         Integer, primary_key=True),
    Column('Name',       String(50)),
    Column('ProductNumber',       String(30)),
    Column('MakeFlag',            Integer),
    Column('FinishedGoodsFlag',   Integer),
    Column('Color',            String(20)),
    Column('SafetyStockLevel',  Integer),
    Column('ReorderPoint',      Integer),
    Column('StandardCost',      DECIMAL(10, 2)),
    Column('ListPrice',         DECIMAL(10, 2)),
    Column('Size',            String(10)),
    Column('SizeUnitMeasureCode', String(10)),
    Column('WeightUnitMeasureCode',   String(10)),
    Column('Weight',         String(10)),
    Column('DaysToManufacture',   Integer),
    Column('ProductLine',         String(20)),
    Column('Class',            String(10)),
    Column('Style',            String(10)),
    Column('ProductSubcategoryID',     Integer),
    Column('ProductModelID',            Integer),
    Column('SellStartDate',            TIMESTAMP),
    Column('SellEndDate',            TIMESTAMP),
    Column('DiscontinuedDate',           TIMESTAMP),
    Column('rowguid',            String(100)),
    Column('ModifiedDate',       TIMESTAMP),
    # ForeignKeyConstraint(['ProductID'], ['special_offer_product_table.ProductID'],
    #                      name='FK_SpecialOfferProduct_Product_ProductID')
)

metadata.create_all()
Select
    name as Customers
From Customers 
Left join Orders on Orders.customerId = Customers.id 
Where Orders.customerId is Null
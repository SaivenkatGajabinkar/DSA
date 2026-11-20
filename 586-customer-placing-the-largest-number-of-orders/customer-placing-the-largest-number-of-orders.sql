select customer_number from Orders GROUP BY customer_number  Order by count(customer_number) DESC LIMIT 1;

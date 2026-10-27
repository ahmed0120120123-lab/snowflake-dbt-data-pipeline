
  create or replace   view MY_DATABASE.RAW_INTERMEDIATE.int_customer_orders
  
  
  
  
  as (
    WITH orders AS (
    SELECT * FROM MY_DATABASE.RAW_STAGING.stg_orders
)
SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(amount) AS total_spent,
    MAX(order_date) AS most_recent_order_date
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY customer_id
  );


WITH raw_orders AS (
    SELECT * FROM MY_DATABASE.RAW.orders
)
SELECT
    CAST(order_id AS INT) AS order_id,
    CAST(customer_id AS INT) AS customer_id,
    CAST(order_date AS DATE) AS order_date,
    TRIM(status) AS order_status,
    CAST(amount AS DECIMAL(10, 2)) AS amount
FROM raw_orders
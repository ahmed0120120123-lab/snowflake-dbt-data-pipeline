SELECT
    order_id,
    customer_id,
    order_date,
    amount,
    order_status
FROM {{ ref('stg_orders') }}

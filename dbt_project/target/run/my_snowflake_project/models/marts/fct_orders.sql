
  
    

create or replace transient table MY_DATABASE.RAW_MARTS.fct_orders
    
    
    
    
    

    as (SELECT
    order_id,
    customer_id,
    order_date,
    amount,
    order_status
FROM MY_DATABASE.RAW_STAGING.stg_orders
    )
;


  
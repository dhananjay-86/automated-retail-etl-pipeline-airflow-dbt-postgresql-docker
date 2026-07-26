{{ config(
    materialized='incremental',
    unique_key='order_id'
) }}

SELECT
    order_id,
    customer_id,
    product_id,
    quantity,
    order_date
FROM {{ ref('stg_orders') }}

{% if is_incremental() %}

WHERE order_date >
(
    SELECT MAX(order_date)
    FROM {{ this }}
)

{% endif %}
SELECT

    customer_id,
    first_name,
    last_name,
    email,
    city

FROM {{ source('raw', 'customers') }}

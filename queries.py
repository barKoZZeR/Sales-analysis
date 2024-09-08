def sales_report_query(start_date, end_date):
    query = f"""
    SELECT
        sales.date AS sale_date,
        products.name AS product_name,
        SUM(sales.quantity) AS total_quantity,
        SUM(sales.total_price) AS total_sales
    FROM
        sales
    JOIN
        products ON sales.product_id = products.id
    WHERE
        sales.date BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY
        sales.date, products.name
    ORDER BY
        total_sales DESC
    """
    return query
SELECT 
    i.item_code,
    i.item_name,
    COALESCE(SUM(sle.actual_qty), 0) AS total_stock
FROM 
    `tabItem` i
LEFT JOIN 
    `tabStock Ledger Entry` sle ON i.item_code = sle.item_code
GROUP BY 
    i.item_code, i.item_name
ORDER BY 
    total_stock DESC;
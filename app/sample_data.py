LEGACY_INVOICE = {
    "invoice_id": "INV-1001",
    "customer": "Acme Enterprises",
    "invoice_date": "2026-04-01",
    "currency": "USD",
    "items": [
        {
            "description": "Transformation assessment",
            "quantity": 2,
            "unit_price": 500.0,
        }
    ],
    "total_amount": 1000.0,
}

TRANSFORMED_INVOICE = {
    "id": "INV-1001",
    "client_name": "Acme Enterprises",
    "date": "2026-04-01",
    "currency": "USD",
    "line_items": [
        {
            "name": "Transformation assessment",
            "qty": 2,
            "price": 500.0,
        }
    ],
    "amount_due": 1000.0,
}

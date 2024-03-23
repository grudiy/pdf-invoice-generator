# pdf-invoice-generator
Generates PDF invoices from Excel files.

The excel invoices should have the columns.
"Generate" function takes arguments:
(invoices_path, pdfs_path, product_id, product_name, amount_purchased, price_per_unit, total_price)

To publish:
1. delete all files, but the folder "pdfinvoice" and setup.py
2. python setup.py sdist 
3. pip install twine 
4. twine upload --skip-existing dist/*
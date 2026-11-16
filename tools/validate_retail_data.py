#!/usr/bin/env python3
"""Validate core KAY POWER HUB retail dashboard metrics using only Python standard library."""
import csv
from pathlib import Path
from decimal import Decimal

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'retail_sales_synthetic.csv'
if not DATA.exists():
    raise SystemExit('Place the existing repository data folder alongside this validator.')
with DATA.open(newline='', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))

money = lambda field: sum((Decimal(row[field]) for row in rows), Decimal('0'))
sales = money('NetSales')
cost = money('COGS')
profit = money('GrossProfit')
ids = {row['OrderID'] for row in rows}
assert len(rows) == len(ids) == 960
assert sales == Decimal('294773.58')
assert cost == Decimal('182588.00')
assert profit == Decimal('112185.58')
assert sales - cost == profit
print(f'Orders: {len(ids)}')
print(f'Net Sales: RM {sales:,.2f}')
print(f'Gross Profit: RM {profit:,.2f}')
print(f'Gross Margin: {(profit / sales * 100):.2f}%')
print('All checks passed.')

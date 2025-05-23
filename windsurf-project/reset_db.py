from app import app, db, TShirt, Order
import os

# Remove database file if it exists
db_path = 'instance/tshirts.db'
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Removed existing database: {db_path}")

# Create tables
with app.app_context():
    db.create_all()
    print("Created new database tables")
    
    # Add t-shirts with updated prices
    tshirts_data = [
        # Winging It - 13 total - Price: 700
        {'design_name': 'Winging It', 'size': 'S', 'quantity': 2, 'price': 700, 'color': 'Black'},
        {'design_name': 'Winging It', 'size': 'M', 'quantity': 2, 'price': 700, 'color': 'Black'},
        {'design_name': 'Winging It', 'size': 'L', 'quantity': 3, 'price': 700, 'color': 'Black'},
        {'design_name': 'Winging It', 'size': 'XL', 'quantity': 3, 'price': 700, 'color': 'Black'},
        {'design_name': 'Winging It', 'size': '2XL', 'quantity': 3, 'price': 700, 'color': 'Black'},
        
        # Power to the Meeple - 12 total - Price: 700
        {'design_name': 'Power to the Meeple', 'size': 'S', 'quantity': 2, 'price': 700, 'color': 'Navy'},
        {'design_name': 'Power to the Meeple', 'size': 'M', 'quantity': 2, 'price': 700, 'color': 'Navy'},
        {'design_name': 'Power to the Meeple', 'size': 'L', 'quantity': 2, 'price': 700, 'color': 'Navy'},
        {'design_name': 'Power to the Meeple', 'size': 'XL', 'quantity': 3, 'price': 700, 'color': 'Navy'},
        {'design_name': 'Power to the Meeple', 'size': '2XL', 'quantity': 3, 'price': 700, 'color': 'Navy'},
        
        # The Board Gamer - 7 total - Price: 700
        {'design_name': 'The Board Gamer', 'size': 'L', 'quantity': 3, 'price': 700, 'color': 'Black'},
        {'design_name': 'The Board Gamer', 'size': 'XL', 'quantity': 2, 'price': 700, 'color': 'Black'},
        {'design_name': 'The Board Gamer', 'size': '2XL', 'quantity': 2, 'price': 700, 'color': 'Black'},
        
        # I Don't Make the Rules - 15 total - Price: 700
        {'design_name': 'I Don\'t Make the Rules', 'size': 'S', 'quantity': 4, 'price': 700, 'color': 'Black'},
        {'design_name': 'I Don\'t Make the Rules', 'size': 'M', 'quantity': 4, 'price': 700, 'color': 'Black'},
        {'design_name': 'I Don\'t Make the Rules', 'size': 'L', 'quantity': 3, 'price': 700, 'color': 'Black'},
        {'design_name': 'I Don\'t Make the Rules', 'size': 'XL', 'quantity': 1, 'price': 700, 'color': 'Black'},
        {'design_name': 'I Don\'t Make the Rules', 'size': '2XL', 'quantity': 3, 'price': 700, 'color': 'Black'},
        
        # VIRTU Meeple - 15 total - Price: 700
        {'design_name': 'VIRTU Meeple', 'size': 'S', 'quantity': 4, 'price': 700, 'color': 'Navy'},
        {'design_name': 'VIRTU Meeple', 'size': 'M', 'quantity': 4, 'price': 700, 'color': 'Navy'},
        {'design_name': 'VIRTU Meeple', 'size': 'L', 'quantity': 2, 'price': 700, 'color': 'Navy'},
        {'design_name': 'VIRTU Meeple', 'size': 'XL', 'quantity': 3, 'price': 700, 'color': 'Navy'},
        {'design_name': 'VIRTU Meeple', 'size': '2XL', 'quantity': 2, 'price': 700, 'color': 'Navy'},
        
        # Before You Ask - 13 total - Price: 800
        {'design_name': 'Before You Ask', 'size': 'S', 'quantity': 4, 'price': 800, 'color': 'Black'},
        {'design_name': 'Before You Ask', 'size': 'M', 'quantity': 4, 'price': 800, 'color': 'Black'},
        {'design_name': 'Before You Ask', 'size': 'L', 'quantity': 1, 'price': 800, 'color': 'Black'},
        {'design_name': 'Before You Ask', 'size': 'XL', 'quantity': 2, 'price': 800, 'color': 'Black'},
        {'design_name': 'Before You Ask', 'size': '2XL', 'quantity': 2, 'price': 800, 'color': 'Black'},
        
        # Settle Down - 11 total - Price: 700
        {'design_name': 'Settle Down', 'size': 'M', 'quantity': 1, 'price': 700, 'color': 'Navy'},
        {'design_name': 'Settle Down', 'size': 'L', 'quantity': 4, 'price': 700, 'color': 'Navy'},
        {'design_name': 'Settle Down', 'size': 'XL', 'quantity': 2, 'price': 700, 'color': 'Navy'},
        {'design_name': 'Settle Down', 'size': '2XL', 'quantity': 4, 'price': 700, 'color': 'Navy'},
        
        # Game Night - 17 total - Price: 700
        {'design_name': 'Game Night', 'size': 'S', 'quantity': 4, 'price': 700, 'color': 'Black'},
        {'design_name': 'Game Night', 'size': 'M', 'quantity': 4, 'price': 700, 'color': 'Black'},
        {'design_name': 'Game Night', 'size': 'L', 'quantity': 2, 'price': 700, 'color': 'Black'},
        {'design_name': 'Game Night', 'size': 'XL', 'quantity': 2, 'price': 700, 'color': 'Black'},
        {'design_name': 'Game Night', 'size': '2XL', 'quantity': 5, 'price': 700, 'color': 'Black'},
        
        # Board Game components - 16 total - Price: 800
        {'design_name': 'Board Game components', 'size': 'S', 'quantity': 4, 'price': 800, 'color': 'Navy'},
        {'design_name': 'Board Game components', 'size': 'M', 'quantity': 4, 'price': 800, 'color': 'Navy'},
        {'design_name': 'Board Game components', 'size': 'L', 'quantity': 3, 'price': 800, 'color': 'Navy'},
        {'design_name': 'Board Game components', 'size': 'XL', 'quantity': 1, 'price': 800, 'color': 'Navy'},
        {'design_name': 'Board Game components', 'size': '2XL', 'quantity': 4, 'price': 800, 'color': 'Navy'}
    ]
    
    # Create and add tshirts
    tshirts = [TShirt(**data) for data in tshirts_data]
    db.session.add_all(tshirts)
    db.session.commit()
    print(f"Added {len(tshirts)} t-shirts to database with updated prices")
    print("  - 'Before You Ask': ₹800")
    print("  - 'Board Game components': ₹800")
    print("  - All other t-shirts: ₹700")

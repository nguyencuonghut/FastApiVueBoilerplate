#!/usr/bin/env python3
"""
Database management script - Similar to Laravel's artisan commands
Usage:
    python manage.py migrate        # Create all tables
    python manage.py seed           # Seed database with initial data
    python manage.py refresh        # Drop all tables and recreate (migrate:refresh)
    python manage.py reset          # Drop, recreate, and seed (migrate:refresh --seed)
"""

import sys
from sqlalchemy import text
from app.database.database import engine, Base, SessionLocal
from app.database.init_db import init_db


def migrate():
    """Create all tables - Similar to 'php artisan migrate'"""
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Tables created successfully!")


def seed():
    """Seed database with initial data - Similar to 'php artisan db:seed'"""
    print("Seeding database...")
    init_db()
    print("✓ Database seeded successfully!")


def refresh():
    """Drop all tables and recreate - Similar to 'php artisan migrate:refresh'"""
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("✓ All tables dropped!")
    
    print("\nCreating all tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Tables created successfully!")


def reset():
    """Drop all tables, recreate, and seed - Similar to 'php artisan migrate:refresh --seed'"""
    print("=" * 60)
    print("DATABASE RESET - This will DELETE all data!")
    print("=" * 60)
    
    print("\n1. Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("   ✓ All tables dropped!")
    
    print("\n2. Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("   ✓ Tables created successfully!")
    
    print("\n3. Seeding database...")
    init_db()
    print("   ✓ Database seeded successfully!")
    
    print("\n" + "=" * 60)
    print("DATABASE RESET COMPLETED!")
    print("=" * 60)


def drop():
    """Drop all tables - Similar to 'php artisan db:wipe'"""
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("✓ All tables dropped!")


def status():
    """Show database status and tables"""
    db = SessionLocal()
    try:
        # Get all tables
        result = db.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name
        """))
        tables = result.fetchall()
        
        print("\n" + "=" * 60)
        print("DATABASE STATUS")
        print("=" * 60)
        print(f"\nTotal tables: {len(tables)}")
        
        if tables:
            print("\nTables:")
            for table in tables:
                # Get row count
                count_result = db.execute(text(f"SELECT COUNT(*) FROM {table[0]}"))
                count = count_result.scalar()
                print(f"  - {table[0]:<30} ({count} rows)")
        else:
            print("\nNo tables found. Run 'python manage.py migrate' to create tables.")
        
        print("\n" + "=" * 60)
    finally:
        db.close()


def help_text():
    """Show help information"""
    print("""
Database Management Commands (Laravel-style)

Usage: python manage.py [command]

Commands:
  migrate       Create all tables (similar to 'php artisan migrate')
  seed          Seed database with initial data (similar to 'php artisan db:seed')
  refresh       Drop and recreate all tables (similar to 'php artisan migrate:refresh')
  reset         Drop, recreate, and seed (similar to 'php artisan migrate:refresh --seed')
  drop          Drop all tables (similar to 'php artisan db:wipe')
  status        Show database status and table information
  help          Show this help message

Examples:
  python manage.py migrate        # Create all tables
  python manage.py seed           # Seed with demo data
  python manage.py reset          # Fresh start with demo data
  python manage.py status         # Check database status
    """)


if __name__ == "__main__":
    commands = {
        'migrate': migrate,
        'seed': seed,
        'refresh': refresh,
        'reset': reset,
        'drop': drop,
        'status': status,
        'help': help_text
    }
    
    if len(sys.argv) < 2:
        print("Error: No command provided")
        help_text()
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command not in commands:
        print(f"Error: Unknown command '{command}'")
        help_text()
        sys.exit(1)
    
    # Execute command
    try:
        commands[command]()
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        sys.exit(1)

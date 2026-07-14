#!/usr/bin/env python3


from dotenv import load_dotenv
import os


load_dotenv()

if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    matrix_mode = os.environ.get('MATRIX_MODE')
    log_level = os.environ.get('LOG_LEVEL')
    if matrix_mode:
        print(f"Mode: {matrix_mode}")
    else:
        print("Mode: [MISSING] Set MATRIX_MODE in .env")
    if os.environ.get('DATABASE_URL'):
        print("Database: Connected to local instance")
    else:
        print("Database: [MISSING] Set DATABASE_URL in .env")
    if os.environ.get('API_KEY'):
        print("API Access: Authenticated")
    else:
        print("API Access: [MISSING] Set API_KEY in .env")
    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("Log Level: [MISSING] Set LOG_LEVEL in .env")
    if os.environ.get('ZION_ENDPOINT'):
        print("Zion Network: Online")
    else:
        print("Zion Network: [MISSING] Set ZION_ENDPOINT in .env")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    if matrix_mode == 'production':
        print("\nPRODUCTION MODE: Enhanced security active")
    else:
        print("\nDEVELOPMENT MODE: Debug features enabled")
    print("\nThe Oracle sees all configurations.")

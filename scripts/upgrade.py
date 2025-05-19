# scripts/upgrade.py
import subprocess

def main():
    print("⬆️ Aplicando migración...")
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    print("✅ Upgrade completo")

if __name__ == "__main__":
    main()

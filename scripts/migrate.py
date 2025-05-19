# scripts/migrate.py
import subprocess

def main():
    print("🔄 Generando migración...")
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", "auto"], check=True)

    print("⬆️ Aplicando migración...")
    subprocess.run(["alembic", "upgrade", "head"], check=True)

    print("✅ Migración completada")

if __name__ == "__main__":
    main()

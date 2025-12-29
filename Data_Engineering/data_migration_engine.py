import pandas as pd
import sqlite3
import os

# Configuration des chemins
LEGACY_DIR = "Legacy_System"
DB_PATH = "Database_Schema/VSA_Production_Vault.db"

def clean_stamping_data(df):
    """Nettoyage spécifique pour l'atelier Presse"""
    print("--- Nettoyage : Atelier Presse ---")
    
    # 1. Gestion des valeurs manquantes (Remplacement par la moyenne pour ne pas perdre de données)
    if df['Produced_Units'].isnull().any():
        mean_val = df['Produced_Units'].mean()
        df['Produced_Units'] = df['Produced_Units'].fillna(mean_val)
        print("💡 Info : Valeurs manquantes comblées par la moyenne.")
    
    # 2. Calcul du taux de rebut (Scrap Rate)
    df['Scrap_Rate_%'] = (df['Scrap_Count'] / df['Produced_Units']) * 100
    return df

def run_migration():
    """Moteur principal de migration ETL"""
    
    # Création du dossier database s'il n'existe pas
    if not os.path.exists("Database_Schema"):
        os.makedirs("Database_Schema")
        
    # Connexion à la base de données SQL
    conn = sqlite3.connect(DB_PATH)
    print(f"🚀 Connexion établie avec la base de données : {DB_PATH}")

    try:
        # --- TRAITEMENT STAMPING ---
        stamping_df = pd.read_excel(f"{LEGACY_DIR}/Stamping_Daily_Report.xlsx")
        stamping_cleaned = clean_stamping_data(stamping_df)
        
        # Chargement vers SQL
        stamping_cleaned.to_sql('Fact_Stamping', conn, if_exists='replace', index=False)
        print("✅ Table 'Fact_Stamping' créée et alimentée.")

        # --- TRAITEMENT ASSEMBLY ---
        assembly_df = pd.read_excel(f"{LEGACY_DIR}/Assembly_Line_Logs.xlsx")
        
        # Ajout d'une colonne de calcul du Takt Time (Écart par rapport à l'objectif de 60s)
        assembly_df['Takt_Deviation'] = assembly_df['Cycle_Time_Sec'] - 60
        
        # Chargement vers SQL
        assembly_df.to_sql('Fact_Assembly', conn, if_exists='replace', index=False)
        print("✅ Table 'Fact_Assembly' créée et alimentée.")

    except Exception as e:
        print(f"❌ Erreur lors de la migration : {e}")
    finally:
        conn.close()
        print("🔌 Connexion SQL fermée.")

if __name__ == "__main__":
    run_migration()
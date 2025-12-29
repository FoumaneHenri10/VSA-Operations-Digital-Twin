import pandas as pd
import numpy as np
import os

# Création du dossier de sortie s'il n'existe pas
output_dir = "Legacy_System"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_stamping_data():
    """Simule le rapport Excel de l'atelier Presse (Stamping)"""
    records = 100
    data = {
        'Shift_Date': pd.date_range(start='2025-01-01', periods=records, freq='D'),
        'Shift_Type': np.random.choice(['A', 'B', 'C'], records),
        'Line_ID': 'LINE_STAMP_01',
        'Target_Units': 500,
        'Produced_Units': np.random.randint(400, 510, records),
        'Scrap_Count': np.random.randint(0, 20, records)
    }
    df = pd.DataFrame(data)
    
    # Ajout d'une erreur réaliste : quelques lignes vides pour tester ta future rigueur
    df.iloc[5, 4] = np.nan 
    
    df.to_excel(f"{output_dir}/Stamping_Daily_Report.xlsx", index=False)
    print("✅ Rapport Presse (Stamping) généré.")

def generate_assembly_data():
    """Simule les données du Montage (Assembly) avec des modèles spécifiques"""
    records = 150
    data = {
        'Timestamp': pd.date_range(start='2025-01-01', periods=records, freq='h'),
        'Model': np.random.choice(['Yaris Standard', 'Yaris Cross Hybrid'], records),
        'Cycle_Time_Sec': np.random.randint(55, 70, records), # Takt time cible autour de 60s
        'Status': np.random.choice(['OK', 'OK', 'OK', 'REWORK'], records)
    }
    df = pd.DataFrame(data)
    df.to_excel(f"{output_dir}/Assembly_Line_Logs.xlsx", index=False)
    print("✅ Logs de Montage (Assembly) générés.")

if __name__ == "__main__":
    generate_stamping_data()
    generate_assembly_data()
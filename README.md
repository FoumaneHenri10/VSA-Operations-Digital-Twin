🏭 VSA - Operations Digital Twin
🎯 Contexte Métier
Dans un environnement de production automobile (type Toyota), la réactivité est la clé. Ce projet simule la migration d'un système de données "Legacy" (fichiers Excel disparates) vers une architecture de données moderne pour permettre un pilotage en temps réel de la performance (OEE et Takt Time).

🛠️ Architecture Technique (Stack)
Ingénierie des données : Python 3.10+ (Pandas pour le nettoyage, SQLite3 pour le stockage).

Base de données : SQLite (Schéma relationnel structuré en tables de faits).

Business Intelligence : Power BI Desktop (Connecteur ODBC, Mesures DAX avancées).

🚀 Défis Résolus
Extraction & Nettoyage (ETL) : Automatisation du traitement de fichiers Excel contenant des valeurs manquantes. Utilisation de la moyenne glissante pour assurer la continuité des données de production.

Modélisation SQL : Transformation de journaux de bord plats en une base de données relationnelle optimisée pour l'analyse.

Analyse de Cadence (Takt Time) : Création d'un algorithme de calcul de déviation pour identifier visuellement les goulots d'étranglement heure par heure.

📈 Résultats (KPIs Pilotés)
Le dashboard "Tour de Contrôle" permet de monitorer :

Production Efficiency : Comparaison temps réel entre le réalisé et l'objectif de l'atelier Presse.

Scrap Rate (Taux de Rebut) : Système d'alerte visuelle (Vert/Rouge) dès que le rebut dépasse 5%.

Takt Deviation : Analyse précise de la fluidité de la ligne de montage (Yaris Standard vs Hybrid).

📖 Comment exécuter le projet
Cloner le dépôt.

Installer les dépendances : pip install pandas openpyxl.

Lancer la migration : python Data_Engineering/data_migration_engine.py.

Ouvrir le rapport Power BI et rafraîchir les données via la source ODBC.
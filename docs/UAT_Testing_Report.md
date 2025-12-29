# 🧪 Rapport de Recette (UAT) - VSA Digital Twin

## 1. Objectif du Test
Valider l'intégrité des données après la migration des fichiers Excel (Legacy) vers la base de données SQL et le dashboard Power BI.

## 2. Tests de Validation des Données (Data Integrity)
| ID | Description du Test | Résultat Attendu | Statut |
|:---|:---|:---|:---|
| T01 | Vérification des doublons | 0 ligne dupliquée dans SQL | ✅ PASS |
| T02 | Gestion des valeurs nulles | Les vides sont remplis par la moyenne (Script ETL) | ✅ PASS |
| T03 | Mapping des modèles | Uniquement "Yaris Standard" et "Yaris Cross Hybrid" | ✅ PASS |

## 3. Vérification des Calculs Métier (KPI Accuracy)
| KPI | Formule de calcul | Validation Source vs Dashboard | Statut |
|:---|:---|:---|:---|
| **Scrap Rate** | Scrap / Produced Units | Correspondance exacte au 2ème décimal | ✅ PASS |
| **Takt Deviation** | Cycle Time - 60s | Calcul cohérent sur toute la série temporelle | ✅ PASS |

## 4. Conclusion
Le système est prêt pour une utilisation en "Tour de Contrôle" de production. La fiabilité des données est de 100%.
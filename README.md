# 📊 Application Streamlit – Traitement Fichiers Staff

Cette application Streamlit permet de traiter deux fichiers Excel (Staff et Ressource) afin de :

1. **Nettoyer** les identifiants employés.
2. **Filtrer** les ressources présentes dans le fichier Staff.
3. **Enrichir** les données avec des colonnes (Mois, Date, Source fichier).
4. **Afficher** un aperçu du résultat.
5. **Exporter** le fichier final en Excel.

---

## 🚀 Fonctionnement

### 1️⃣ Chargement des fichiers
- L’utilisateur charge deux fichiers via l’interface :
  - **Fichier Staff** (format : `staff MMAAAA.xlsx`)
  - **Fichier Ressource** (avec colonne `Matricule`)

### 2️⃣ Lecture et nettoyage
- Les deux fichiers sont lus avec **pandas** (`pd.read_excel`).
- Les identifiants employés sont **nettoyés** :
  - Suppression des espaces et caractères parasites.
  - Complétion à 5 chiffres (`zfill(5)`).
  - Suppression éventuelle de la lettre `m` dans le fichier Ressource.

### 3️⃣ Filtrage
- On conserve uniquement les lignes du fichier Ressource dont l’ID correspond à un ID du fichier Staff.

### 4️⃣ Enrichissement
- Ajout de colonnes :
  - `Mois` (ex : "Juillet 2025")
  - `Date` (1er jour du mois)
  - `Source fichier` (nom du fichier Staff importé)

### 5️⃣ Affichage et export
- Aperçu des données filtrées avec `st.dataframe`.
- Génération d’un fichier Excel prêt à télécharger (`st.download_button`).




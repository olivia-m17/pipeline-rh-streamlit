import pandas as pd
import streamlit as st
from io import BytesIO

st.title("📊 Traitement des Fichiers RH – Pipeline Automatisé")

# === Upload des fichiers ===
staff_file = st.file_uploader("🧑‍💼 Fichier Staff (format: staff MMAAAA.xlsx)", type=["xlsx"])
resource_file = st.file_uploader("📁 Fichier Ressource", type=["xlsx"])

if staff_file and resource_file:
    # Lire les fichiers
    staff_df = pd.read_excel(staff_file)
    resource_df = pd.read_excel(resource_file)

    # Nettoyage des ID
    staff_ids = staff_df.iloc[:, 0].astype(str).str.strip().str.zfill(5)

    resource_df["clean_id"] = (
        resource_df["Matricule"]
        .astype(str)
        .str.replace("m", "", regex=False)
        .str.strip()
        .str.zfill(5)
    )

    # Filtrage
    filtered_df = resource_df[resource_df["clean_id"].isin(staff_ids)].copy()

    # Enrichissement
    filtered_df["Mois"] = "Mai 2025"
    filtered_df["Date"] = pd.to_datetime("2025-05-01")
    filtered_df["Source fichier"] = staff_file.name
    filtered_df.drop(columns=["clean_id"], inplace=True)

    st.success("✅ Traitement terminé. Aperçu des données filtrées :")
    st.dataframe(filtered_df)

    # Export Excel
    output = BytesIO()
    filtered_df.to_excel(output, index=False, engine='openpyxl')
    st.download_button(
        label="📥 Télécharger le fichier Excel final",
        data=output.getvalue(),
        file_name="staff_mai_2025.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.info("📝 Merci de charger les deux fichiers Excel pour lancer le traitement.")

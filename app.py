import pandas as pd
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Traitement RH", page_icon="📊")

st.title(" Traitement des Fichiers RH – Pipeline Automatisé")

# === Upload des fichiers ===
staff_file = st.file_uploader(" Fichier Staff (format: staff MMAAAA.xlsx)", type=["xlsx"])
resource_file = st.file_uploader(" Fichier Ressource", type=["xlsx"])

if staff_file and resource_file:
    try:
        # Lecture des fichiers
        staff_df = pd.read_excel(staff_file)
        resource_df = pd.read_excel(resource_file)

        # Nettoyage des ID du staff
        staff_ids = staff_df.iloc[:, 0].astype(str).str.strip().str.zfill(5)

        # Nettoyage des ID dans ressource
        resource_df["clean_id"] = (
            resource_df["Matricule"]
            .astype(str)
            .str.replace("m", "", regex=False)
            .str.strip()
            .str.zfill(5)
        )

        # === FILTRAGE : uniquement les employés présents dans le fichier staff ===
        filtered_df = resource_df[resource_df["clean_id"].isin(staff_ids)].copy()

        # === ENRICHISSEMENT ===
        filtered_df["Mois"] = "Juin 2025"
        filtered_df["Date"] = pd.to_datetime("2025-06-01")
        filtered_df["Source fichier"] = staff_file.name
        filtered_df.drop(columns=["clean_id"], inplace=True)

        st.success("✅ Traitement terminé. Aperçu des données filtrées :")
        st.dataframe(filtered_df)

        # === EXPORT Excel ===
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            filtered_df.to_excel(writer, index=False)
        output.seek(0)

        st.download_button(
            label="Télécharger le fichier Excel final",
            data=output,
            file_name="staff_juin_2025.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"❌ Une erreur est survenue : {e}")

else:
    st.info("📝 Merci de charger les deux fichiers Excel pour lancer le traitement.")


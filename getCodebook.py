import pandas as pd
from pathlib import Path


def build_theory_codebook(
    merged_output_path: str = "merged_output.xlsx",
    sixcs_structure_path: str = "SixCsStructure.csv",
    output_path: str = "theory_CodeBook.xlsx"
) -> None:
    """
    Gera um novo arquivo XLSX unindo:
    - merged_output.xlsx
    - SixCsStructure.csv

    Regras:
    - Faz o merge usando:
        merged_output.category == SixCsStructure.Concepts
    - Descarta registros sem category
    - Estrutura final:
        Code, Quotation, Concepts, SubCategory, Six C (Categories), Qtd
    - Qtd = contagem total de quotes por Code
    """

    # -----------------------------
    # 1) Ler arquivos
    # -----------------------------
    merged_df = pd.read_excel(merged_output_path)
    sixcs_df = pd.read_csv(sixcs_structure_path)

    # -----------------------------
    # 2) Padronizar nomes de colunas
    # -----------------------------
    merged_df.columns = [col.strip() for col in merged_df.columns]
    sixcs_df.columns = [col.strip() for col in sixcs_df.columns]

    # Renomear colunas do arquivo merged_output para o formato final desejado
    expected_merged_cols = {
        "document": "Document",
        "quotation": "Quotation",
        "code": "Code",
        "category": "category"
    }

    merged_df = merged_df.rename(columns=expected_merged_cols)

    # -----------------------------
    # 3) Validar colunas obrigatórias
    # -----------------------------
    required_merged = {"Document","Quotation", "Code", "category"}
    required_sixcs = {"Concepts", "SubCategory", "Six C (Categories)"}

    missing_merged = required_merged - set(merged_df.columns)
    missing_sixcs = required_sixcs - set(sixcs_df.columns)

    if missing_merged:
        raise ValueError(
            f"Colunas ausentes em {merged_output_path}: {sorted(missing_merged)}"
        )

    if missing_sixcs:
        raise ValueError(
            f"Colunas ausentes em {sixcs_structure_path}: {sorted(missing_sixcs)}"
        )

    # -----------------------------
    # 4) Limpeza básica
    # -----------------------------
    # Remover linhas sem category
    merged_df = merged_df.dropna(subset=["category"]).copy()

    # Remover espaços extras
    merged_df["Document"] = merged_df["Document"].astype(str).str.strip()
    merged_df["category"] = merged_df["category"].astype(str).str.strip()
    merged_df["Code"] = merged_df["Code"].astype(str).str.strip()
    merged_df["Quotation"] = merged_df["Quotation"].astype(str).str.strip()

    sixcs_df["Concepts"] = sixcs_df["Concepts"].astype(str).str.strip()
    sixcs_df["SubCategory"] = sixcs_df["SubCategory"].astype(str).str.strip()
    sixcs_df["Six C (Categories)"] = sixcs_df["Six C (Categories)"].astype(str).str.strip()

    # Remover categories vazias após strip
    merged_df = merged_df[merged_df["category"] != ""].copy()
    sixcs_df = sixcs_df[sixcs_df["Concepts"] != ""].copy()

    # -----------------------------
    # 5) Merge
    # -----------------------------
    # Usa inner join para manter apenas registros com correspondência
    # Merge por Code
    result_df = merged_df.merge(
        sixcs_df[["Code", "Concepts", "SubCategory", "Six C (Categories)"]],
        on="Code",
        how="inner"
    )

    # -----------------------------
    # 6) Selecionar estrutura final
    # -----------------------------
    final_df = result_df[
        ["Document", "Quotation", "Code", "Concepts", "SubCategory", "Six C (Categories)"]
    ].copy()

    # Opcional: remover duplicatas exatas
    final_df = final_df.drop_duplicates()

    # Ordenação opcional
    final_df = final_df.sort_values(
        by=["Six C (Categories)", "SubCategory", "Concepts", "Code", "Quotation"],
        ascending=True
    ).reset_index(drop=True)

    # -----------------------------
    # 8) Salvar em XLSX
    # -----------------------------
    output_file = Path(output_path)
    final_df.to_excel(output_file, index=False)

    print(f"Arquivo gerado com sucesso: {output_file.resolve()}")
    print(f"Total de linhas no resultado: {len(final_df)}")


if __name__ == "__main__":
    build_theory_codebook()
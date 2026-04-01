#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import argparse
import pandas as pd


def clean_text(value):
    """Normalize text values."""
    if pd.isna(value):
        return ""
    return str(value).strip()


def split_codes(codes_value):
    """
    Split codes separated by comma.
    Example:
      'Improve code understanding, Improve code expressiveness'
    """
    text = clean_text(codes_value)
    if not text:
        return []
    return [c.strip() for c in text.split(",") if c.strip()]


def main():
    parser = argparse.ArgumentParser(
        description="Merge two XLSX files into one row per quote, code, and category."
    )
    parser.add_argument(
        "--codes-xlsx",
        required=True,
        help="Path to the first XLSX (columns: name, comment, codegroup 1).",
    )
    parser.add_argument(
        "--quotes-xlsx",
        required=True,
        help="Path to the second XLSX (columns: document, quotation, codes, comment).",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to output XLSX file.",
    )
    args = parser.parse_args()

    codes_file = Path(args.codes_xlsx)
    quotes_file = Path(args.quotes_xlsx)
    output_file = Path(args.output)

    # Read input files
    df_codes = pd.read_excel(codes_file)
    df_quotes = pd.read_excel(quotes_file)

    # Normalize column names
    df_codes.columns = [str(c).strip().lower() for c in df_codes.columns]
    df_quotes.columns = [str(c).strip().lower() for c in df_quotes.columns]

    # Validate required columns
    required_codes_cols = {"name", "codegroup 1"}
    required_quotes_cols = {"document", "quotation", "codes"}

    missing_codes = required_codes_cols - set(df_codes.columns)
    missing_quotes = required_quotes_cols - set(df_quotes.columns)

    if missing_codes:
        raise ValueError(
            f"Missing columns in first XLSX: {sorted(missing_codes)}"
        )

    if missing_quotes:
        raise ValueError(
            f"Missing columns in second XLSX: {sorted(missing_quotes)}"
        )

    # Keep only relevant columns from first file
    df_codes = df_codes[["name", "codegroup 1"]].copy()
    df_codes["name"] = df_codes["name"].apply(clean_text)
    df_codes["codegroup 1"] = df_codes["codegroup 1"].apply(clean_text)

    # Transform codegroups into one category column
    rows = []
    for _, row in df_codes.iterrows():
        code_name = row["name"]

        for cat_col in ["codegroup 1"]:
            category = row[cat_col]
            if code_name and category:
                rows.append({
                    "code": code_name,
                    "category": category
                })

    df_code_categories = pd.DataFrame(rows).drop_duplicates()

    # Optional normalized key for safer matching
    df_code_categories["code_key"] = df_code_categories["code"].str.strip().str.lower()

    # Prepare second file
    df_quotes = df_quotes[["document", "quotation", "codes"]].copy()
    df_quotes["document"] = df_quotes["document"].apply(clean_text)
    df_quotes["quotation"] = df_quotes["quotation"].apply(clean_text)
    df_quotes["codes"] = df_quotes["codes"].apply(clean_text)

    # Explode codes column
    expanded_rows = []
    for _, row in df_quotes.iterrows():
        document = row["document"]
        quotation = row["quotation"]
        codes_list = split_codes(row["codes"])

        for code in codes_list:
            expanded_rows.append({
                "document": document,
                "quotation": quotation,
                "code": code
            })

    df_quotes_expanded = pd.DataFrame(expanded_rows)

    if df_quotes_expanded.empty:
        raise ValueError("No codes found in the second XLSX after splitting the 'codes' column.")

    df_quotes_expanded["code_key"] = df_quotes_expanded["code"].str.strip().str.lower()

    # Merge quotes/codes with categories
    df_merged = df_quotes_expanded.merge(
        df_code_categories,
        on="code_key",
        how="left",
        suffixes=("_quote", "_catalog")
    )

    # Prefer original code from quotes file
    if "code_quote" in df_merged.columns:
        df_merged["code"] = df_merged["code_quote"]
    elif "code_x" in df_merged.columns:
        df_merged["code"] = df_merged["code_x"]

    # Keep final columns
    final_cols = ["document", "quotation", "code", "category"]
    df_final = df_merged[final_cols].copy()

    # Remove duplicates
    df_final = df_final.drop_duplicates()

    # Save output
    if output_file.suffix.lower() == ".csv":
        df_final.to_csv(output_file, index=False, encoding="utf-8-sig")
    else:
        df_final.to_excel(output_file, index=False)

    print(f"Done. Output written to: {output_file}")
    print(f"Total rows: {len(df_final)}")


if __name__ == "__main__":
    main()
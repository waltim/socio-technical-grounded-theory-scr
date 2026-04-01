import re
import argparse
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud


def normalize_text(text: str) -> str:
    if pd.isna(text):
        return ""

    text = str(text).lower()
    text = text.replace("\n", " ").replace("\r", " ")
    text = re.sub(r"[^\w\s']", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_texts_from_xlsx(file_path: str, sheet_name: str = None, text_column: str = "Quotation") -> list[str]:
    if sheet_name:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    else:
        df = pd.read_excel(file_path)

    df.columns = [str(c).strip() for c in df.columns]

    if text_column not in df.columns:
        raise ValueError(
            f"Column '{text_column}' not found. Available columns: {list(df.columns)}"
        )

    texts = df[text_column].dropna().astype(str).tolist()
    texts = [normalize_text(t) for t in texts if normalize_text(t)]
    return texts


def build_term_counts(
    texts: list[str],
    ngram_range=(1, 1),
    top_n: int = 30,
    min_df: int = 2
) -> pd.DataFrame:
    vectorizer = CountVectorizer(
        ngram_range=ngram_range,
        stop_words="english",
        min_df=min_df
    )

    X = vectorizer.fit_transform(texts)
    terms = vectorizer.get_feature_names_out()
    freqs = X.sum(axis=0).A1

    df = pd.DataFrame({
        "term": terms,
        "count": freqs
    }).sort_values("count", ascending=False)

    return df.head(top_n).reset_index(drop=True), pd.DataFrame({
        "term": terms,
        "count": freqs
    }).sort_values("count", ascending=False).reset_index(drop=True)


def plot_bar_pdf(df: pd.DataFrame, title: str, output_pdf: str) -> None:
    if df.empty:
        raise ValueError(f"No data available to plot for: {title}")

    plot_df = df.sort_values("count", ascending=True)

    plt.figure(figsize=(11, 8.5))
    plt.barh(plot_df["term"], plot_df["count"])
    plt.xlabel("Frequency")
    plt.ylabel("Term")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_pdf, format="pdf", bbox_inches="tight")
    plt.close()


def generate_wordcloud_pdf(freq_df: pd.DataFrame, title: str, output_pdf: str) -> None:
    if freq_df.empty:
        raise ValueError(f"No data available to generate word cloud for: {title}")

    frequencies = dict(zip(freq_df["term"], freq_df["count"]))

    wc = WordCloud(
        width=1600,
        height=900,
        background_color="white",
        collocations=False
    ).generate_from_frequencies(frequencies)

    plt.figure(figsize=(14, 8))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_pdf, format="pdf", bbox_inches="tight")
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Generate unigram and multi-word term charts and word clouds from an XLSX file."
    )
    parser.add_argument("xlsx_file", help="Path to the input XLSX file")
    parser.add_argument("--sheet", default=None, help="Sheet name (optional)")
    parser.add_argument("--column", default="Quotation", help="Text column name")
    parser.add_argument("--top_n", type=int, default=30, help="Top N terms for bar charts")
    parser.add_argument("--min_df", type=int, default=2, help="Minimum document frequency")
    parser.add_argument("--output_dir", default="output_text_analysis", help="Directory to save outputs")

    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    texts = load_texts_from_xlsx(
        file_path=args.xlsx_file,
        sheet_name=args.sheet,
        text_column=args.column
    )

    if not texts:
        raise ValueError("No valid texts found after cleaning.")

    # -------------------------
    # 1) Unigrams
    # -------------------------
    unigram_top_df, unigram_full_df = build_term_counts(
        texts=texts,
        ngram_range=(1, 1),
        top_n=args.top_n,
        min_df=args.min_df
    )

    unigram_csv = output_dir / "unigrams.csv"
    unigram_chart_pdf = output_dir / "unigrams_chart.pdf"
    unigram_wordcloud_pdf = output_dir / "unigrams_wordcloud.pdf"

    unigram_full_df.to_csv(unigram_csv, index=False)
    plot_bar_pdf(
        unigram_top_df,
        title="Most Frequent Unique Words",
        output_pdf=str(unigram_chart_pdf)
    )
    generate_wordcloud_pdf(
        unigram_full_df,
        title="Word Cloud - Unique Words",
        output_pdf=str(unigram_wordcloud_pdf)
    )

    # -------------------------
    # 2) Multi-word terms
    # -------------------------
    multi_top_df, multi_full_df = build_term_counts(
        texts=texts,
        ngram_range=(2, 3),
        top_n=args.top_n,
        min_df=args.min_df
    )

    multi_csv = output_dir / "multiword_terms.csv"
    multi_chart_pdf = output_dir / "multiword_terms_chart.pdf"
    multi_wordcloud_pdf = output_dir / "multiword_terms_wordcloud.pdf"

    multi_full_df.to_csv(multi_csv, index=False)
    plot_bar_pdf(
        multi_top_df,
        title="Most Frequent Multi-word Terms",
        output_pdf=str(multi_chart_pdf)
    )
    generate_wordcloud_pdf(
        multi_full_df,
        title="Word Cloud - Multi-word Terms",
        output_pdf=str(multi_wordcloud_pdf)
    )

    print("Analysis completed successfully.")
    print(f"Saved: {unigram_csv}")
    print(f"Saved: {unigram_chart_pdf}")
    print(f"Saved: {unigram_wordcloud_pdf}")
    print(f"Saved: {multi_csv}")
    print(f"Saved: {multi_chart_pdf}")
    print(f"Saved: {multi_wordcloud_pdf}")


if __name__ == "__main__":
    main()
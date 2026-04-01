# A Socio-Technical Grounded Theory about Source Code Rejuvenation

This repository contains the empirical materials, qualitative artifacts, and supporting scripts used in the study **“A Socio-Technical Grounded Theory about Source Code Rejuvenation.”** It brings together interview transcripts, analytical memos, codebooks, category structures, lexical validation outputs, and utility scripts used to organize and analyze the data.


## Mining Repositories Studies

This section provides links to the empirical mining studies that support the development of the socio-technical grounded theory of source code rejuvenation. Each study includes datasets, scripts, and replication packages available through Zenodo and GitHub repositories.

---

### Modern C++ Feature Adoption in KDE

**Description:**  
Empirical study analyzing the adoption of modern C++ features (e.g., lambda expressions, auto, range-based for) in 272 KDE open-source projects. The study investigates how developers modernize legacy systems and highlights the role of automated tools in supporting rejuvenation efforts.

📄 Paper: *Embracing modern C++ features: An empirical assessment on the KDE community*
🔗 Zenodo: *(https://github.com/PAMunb/cppEvolution)*

---

### Modern JavaScript Feature Adoption

**Description:**  
Large-scale empirical study of 158 JavaScript repositories analyzing the adoption of ES6+ features. The study combines mining software repositories and qualitative analysis of code review discussions to understand adoption trends, motivations, and challenges in source code rejuvenation.

📄 Paper: *Understanding the adoption of modern JavaScript features: An empirical study on open-source systems*
🔗 Zenodo: *(https://doi.org/10.5281/zenodo.14796287)*

---

### Modern Python Feature Adoption and Rejuvenation

**Description:**  
Empirical study of 424 Python open-source projects investigating when and how modern language features are adopted. The study identifies distinct adoption patterns and analyzes motivations (e.g., code comprehension) and challenges (e.g., compatibility constraints) driving rejuvenation efforts.

📄 Paper: *“It Makes the Code Clearer”: Why Developers Adopt Modern Python Features in Open Source Projects*
🔗 Zenodo: *(https://zenodo.org/records/18462376)*

---

## Overview

The repository supports a socio-technical grounded theory (STGT) investigation of **source code rejuvenation (SCR)**, understood as the set of practices through which developers update legacy code to adopt modern language features.

The materials in this repository support:

- qualitative analysis of interview, survey and Pull Request Comments and documentary evidence;
- construction and refinement of codes, concepts, and categories;
- organization of the theory using the Six Cs structure;
- lexical/context validation of selected themes;
- generation of derived codebook artifacts and text-analysis outputs.

## Repository structure

```
.
├── context_validation_outputs/
├── interviews_transcriptions/
├── mining_repository_studies/
├── output_text_analysis/
├── README.md
├── SCRTheoryCodeBook.xlsx
├── SixCsStructure.csv
├── codes_catalog.xlsx
├── getCodebook.py
├── memos.md
├── merge_quotes_codes.py
├── quotations.xlsx
└── text_analysis_xlsx.py
```

## Main contents

### interviews_transcriptions/
Contains interview transcription files in `.docx` format used as primary qualitative evidence.

### memos.md
Analytical memos capturing interpretive insights during grounded theory development.

### SCRTheoryCodeBook.xlsx
Primary theory-oriented codebook consolidating coded quotations and analytical structures.

### codes_catalog.xlsx
Catalog of codes used in the qualitative analysis workflow.

### quotations.xlsx
Dataset containing quotations and assigned codes.

### SixCsStructure.csv
Defines the Six Cs analytical structure used in the theory.

### context_validation_outputs/
Outputs supporting lexical triangulation and context validation.

### output_text_analysis/
Derived outputs such as unigram/multiword frequencies, charts, and word clouds.

### mining_repository_studies/

This directory contains the primary research papers and supporting artifacts from empirical mining studies. It includes published articles (C++, JavaScript, and Python studies), associated codebooks, and raw survey data. These materials provide complementary quantitative and qualitative evidence on the adoption of modern programming language features and source code rejuvenation practices across different environments.

## Scripts

### merge_quotes_codes.py
Merges code catalog and quotations dataset into structured outputs.

### getCodebook.py
Builds a theory-oriented codebook combining merged data and Six Cs structure.

### text_analysis_xlsx.py
Performs lexical analysis and generates frequency outputs and visualizations.

## Suggested workflow

1. Maintain quotations in `quotations.xlsx`
2. Maintain codes in `codes_catalog.xlsx`
3. Merge using `merge_quotes_codes.py`
4. Generate codebook using `getCodebook.py`
5. Run lexical analysis using `text_analysis_xlsx.py`
6. Use `memos.md` for interpretive grounding

## Dependencies

```
pip install pandas matplotlib scikit-learn wordcloud openpyxl
```

## Reproducibility notes

This repository includes both primary qualitative data and derived analytical artifacts. Outputs can be regenerated using the provided scripts.

## Intended use

Supports transparency, traceability, and reproducibility in empirical software engineering research.

## Citation

Please cite the associated thesis or future DOI release.

## License

To be defined (recommended: MIT for scripts + data usage statement).

## Contact

Walter Lucas  
PhD research on source code rejuvenation and socio-technical grounded theory.

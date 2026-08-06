"""
Equivalente Python do "motor" do seu relatório em R Markdown.

Traduz:
    flextable + officer  ->  python-docx (tabelas nativas do Word, formatadas)
    tidyverse            ->  pandas
    stats / vcd          ->  scipy
    ggplot2 / esquisse   ->  matplotlib

A classe `Relatorio` guarda o documento Word e os contadores automáticos (n_tabela, n_grafico, n_cruzamento, n_qq).
Dependências:
    pip install python-docx pandas numpy scipy openpyxl matplotlib
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from scipy import stats
from scipy.special import gammaln

matplotlib.use("Agg")  # backend sem interface gráfica
import matplotlib.pyplot as plt 


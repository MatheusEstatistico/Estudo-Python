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

from shiny import App, render, ui, reactive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gerando dados de exemplo para o dashboard
dados_vendas = pd.DataFrame({
    'data': pd.date_range('2024-01-01', periods=100, freq='D'),
    'produto': np.random.choice(['A', 'B', 'C', 'D'], 100),
    'vendas': np.random.normal(1000, 200, 100).round(2),
    'custo': np.random.normal(700, 150, 100).round(2),
    'satisfacao': np.random.uniform(3, 5, 100).round(1),
    'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 100)
})
dados_vendas['lucro'] = dados_vendas['vendas'] - dados_vendas['custo']

# Criando a interface do usuário (UI)
app_ui = ui.page_fluid(
    # Título principal do dashboard
    ui.h2("📊 Dashboard de Vendas - Exemplo"),
    
    # Painel de controle com filtros interativos
    ui.row(
        # Filtro de região
        ui.column(4,
            ui.input_select(
                "regiao_filtro", 
                "Selecione a Região:",
                choices=["Todas"] + list(dados_vendas['regiao'].unique()),
                selected="Todas"
            )
        ),
        # Filtro de produto
        ui.column(4,
            ui.input_select(
                "produto_filtro",
                "Selecione o Produto:",
                choices=["Todos"] + list(dados_vendas['produto'].unique()),
                selected="Todos"
            )
        ),
        # Seletor de período
        ui.column(4,
            ui.input_date_range(
                "periodo",
                "Selecione o Período:",
                start=dados_vendas['data'].min(),
                end=dados_vendas['data'].max()
            )
        )
    ),
    
    # Linha de cards com métricas principais
    ui.row(
        ui.column(3, ui.card(
            ui.card_header("💰 Vendas Totais"),
            ui.output_text("total_vendas")
        )),
        ui.column(3, ui.card(
            ui.card_header("📈 Lucro Total"),
            ui.output_text("total_lucro")
        )),
        ui.column(3, ui.card(
            ui.card_header("⭐ Satisfação Média"),
            ui.output_text("media_satisfacao")
        )),
        ui.column(3, ui.card(
            ui.card_header("🛒 Nº de Transações"),
            ui.output_text("num_transacoes")
        ))
    ),
    
    # Layout em 2x2 para os 4 gráficos
    # Primeira linha de gráficos
    ui.row(
        # Painel 1: Evolução das vendas (Gráfico de linha)
        ui.column(6,
            ui.card(
                ui.card_header("Painel 1: Evolução de Vendas por Período"),
                ui.output_plot("grafico_evolucao", height="300px"),
                ui.card_footer("Gráfico de linha mostrando a tendência das vendas ao longo do tempo")
            )
        ),
        # Painel 2: Vendas por produto (Gráfico de barras)
        ui.column(6,
            ui.card(
                ui.card_header("Painel 2: Vendas por Produto"),
                ui.output_plot("grafico_barras", height="300px"),
                ui.card_footer("Gráfico de barras comparando o desempenho por produto")
            )
        )
    ),
    
    # Segunda linha de gráficos
    ui.row(
        # Painel 3: Vendas vs Lucro (Gráfico de dispersão)
        ui.column(6,
            ui.card(
                ui.card_header("Painel 3: Relação Vendas vs Lucro"),
                ui.output_plot("grafico_dispersao", height="300px"),
                ui.card_footer("Gráfico de dispersão mostrando a correlação entre vendas e lucro")
            )
        ),
        # Painel 4: Satisfação por região (Boxplot)
        ui.column(6,
            ui.card(
                ui.card_header("Painel 4: Distribuição de Satisfação por Região"),
                ui.output_plot("grafico_boxplot", height="300px"),
                ui.card_footer("Boxplot comparando a satisfação dos clientes entre regiões")
            )
        )
    )
)

# Criando a lógica do servidor
def server(input, output, session):
    """
    Servidor: Define como os dados serão processados e exibidos
    """
    
    # Função reativa para filtrar os dados conforme seleção do usuário
    @reactive.calc()
    def dados_filtrados():
        """Filtra os dados de acordo com as seleções do usuário"""
        df = dados_vendas.copy()
        
        # Filtro de região
        if input.regiao_filtro() != "Todas":
            df = df[df['regiao'] == input.regiao_filtro()]
        
        # Filtro de produto
        if input.produto_filtro() != "Todos":
            df = df[df['produto'] == input.produto_filtro()]
        
        # Filtro de período
        df = df[
            (df['data'] >= pd.to_datetime(input.periodo()[0])) &
            (df['data'] <= pd.to_datetime(input.periodo()[1]))
        ]
        
        return df
    
    # Cards de métricas
    @output
    @render.text
    def total_vendas():
        """Calcula o total de vendas dos dados filtrados"""
        df = dados_filtrados()
        return f"R$ {df['vendas'].sum():,.2f}"
    
    @output
    @render.text
    def total_lucro():
        """Calcula o lucro total"""
        df = dados_filtrados()
        return f"R$ {df['lucro'].sum():,.2f}"
    
    @output
    @render.text
    def media_satisfacao():
        """Calcula a satisfação média"""
        df = dados_filtrados()
        return f"{df['satisfacao'].mean():.1f}/5.0"
    
    @output
    @render.text
    def num_transacoes():
        """Conta o número de transações"""
        df = dados_filtrados()
        return f"{len(df):,.0f}"
    
    # Painel 1: Gráfico de evolução (linha)
    @output
    @render.plot
    def grafico_evolucao():
        """Gráfico de linha mostrando a evolução das vendas no tempo"""
        df = dados_filtrados()
        
        # Agrupando por data e somando as vendas
        vendas_diarias = df.groupby('data')['vendas'].sum().reset_index()
        
        # Criando o gráfico
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(vendas_diarias['data'], vendas_diarias['vendas'], 
                color='#2E86AB', linewidth=2, marker='o', markersize=3)
        
        # Personalizando o gráfico
        ax.set_xlabel('Data', fontsize=10)
        ax.set_ylabel('Vendas (R$)', fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.fill_between(vendas_diarias['data'], vendas_diarias['vendas'], 
                         alpha=0.1, color='#2E86AB')
        
        # Melhorando a legibilidade das datas
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return fig
    
    # Painel 2: Gráfico de barras por produto
    @output
    @render.plot
    def grafico_barras():
        """Gráfico de barras mostrando vendas por produto"""
        df = dados_filtrados()
        
        # Agrupando por produto
        vendas_produto = df.groupby('produto')['vendas'].sum().reset_index()
        
        # Criando o gráfico
        fig, ax = plt.subplots(figsize=(8, 4))
        cores = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
        bars = ax.bar(vendas_produto['produto'], vendas_produto['vendas'], 
                      color=cores, edgecolor='white', linewidth=1.5)
        
        # Adicionando valores sobre as barras
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=9)
        
        ax.set_xlabel('Produto', fontsize=10)
        ax.set_ylabel('Vendas Totais (R$)', fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        
        return fig
    
    # Painel 3: Gráfico de dispersão
    @output
    @render.plot
    def grafico_dispersao():
        """Gráfico de dispersão mostrando relação entre vendas e lucro"""
        df = dados_filtrados()
        
        # Criando o gráfico
        fig, ax = plt.subplots(figsize=(8, 4))
        
        # Plotando pontos coloridos por produto
        produtos = df['produto'].unique()
        cores = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
        
        for produto, cor in zip(produtos, cores):
            dados_produto = df[df['produto'] == produto]
            ax.scatter(dados_produto['vendas'], dados_produto['lucro'], 
                      c=cor, alpha=0.6, label=produto, s=50)
        
        # Adicionando linha de tendência
        z = np.polyfit(df['vendas'], df['lucro'], 1)
        p = np.poly1d(z)
        ax.plot(df['vendas'].sort_values(), p(df['vendas'].sort_values()), 
                "r--", alpha=0.8, linewidth=1)
        
        ax.set_xlabel('Vendas (R$)', fontsize=10)
        ax.set_ylabel('Lucro (R$)', fontsize=10)
        ax.legend(title='Produtos')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        return fig
    
    # Painel 4: Boxplot de satisfação por região
    @output
    @render.plot
    def grafico_boxplot():
        """Boxplot mostrando a distribuição de satisfação por região"""
        df = dados_filtrados()
        
        # Criando o gráfico
        fig, ax = plt.subplots(figsize=(8, 4))
        
        # Boxplot com cores personalizadas
        box_colors = ['#A1D2CE', '#78CAD2', '#62A8AC', '#5497A7']
        bplot = ax.boxplot([df[df['regiao'] == regiao]['satisfacao'].values 
                           for regiao in df['regiao'].unique()],
                          patch_artist=True, labels=df['regiao'].unique())
        
        # Colorindo cada box
        for patch, color in zip(bplot['boxes'], box_colors):
            patch.set_facecolor(color)
        
        ax.set_xlabel('Região', fontsize=10)
        ax.set_ylabel('Satisfação', fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        
        return fig

# Criando a aplicação Shiny
app = App(app_ui, server)
app.run()


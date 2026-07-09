import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class PasseioCavalo:
    def __init__(self, n=8):
        self.n = n
        self.MOVIMENTOS_CAVALO = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1),
        ]
        self.cache_grau = {}
        
    def movimentos_legais(self, pos, visitado):
        """Retorna movimentos válidos a partir da posição atual."""
        linha, coluna = pos
        legais = []
        for dl, dc in self.MOVIMENTOS_CAVALO:
            nl, nc = linha + dl, coluna + dc
            if 0 <= nl < self.n and 0 <= nc < self.n and not visitado[nl][nc]:
                legais.append((nl, nc))
        return legais
    
    def grau(self, pos, visitado):
        """Número de movimentos legais a partir de uma posição (com cache)."""
        # Cache simples baseado na posição e no estado do tabuleiro
        key = (pos, tuple(tuple(row) for row in visitado))
        if key not in self.cache_grau:
            self.cache_grau[key] = len(self.movimentos_legais(pos, visitado))
        return self.cache_grau[key]
    
    def passeio_cavalo(self, posicao_inicial, max_tentativas=5):
        """Tenta encontrar um passeio completo com múltiplas tentativas se necessário."""
        for tentativa in range(max_tentativas):
            if tentativa > 0:
                # Pequena perturbação: tenta começar de outra posição
                posicao_inicial = (posicao_inicial[0], (posicao_inicial[1] + 1) % self.n)
                print(f"Tentativa {tentativa + 1}: posição inicial {posicao_inicial}")
            
            tabuleiro, caminho, completo = self._passeio_single(posicao_inicial)
            if completo:
                return tabuleiro, caminho, completo, tentativa + 1
        
        return tabuleiro, caminho, False, max_tentativas
    
    def _passeio_single(self, posicao_inicial):
        """Executa um único passeio usando heurística de Warnsdorff."""
        tabuleiro = [[None] * self.n for _ in range(self.n)]
        visitado = [[False] * self.n for _ in range(self.n)]
        caminho = [posicao_inicial]
        
        posicao = posicao_inicial
        visitado[posicao[0]][posicao[1]] = True
        tabuleiro[posicao[0]][posicao[1]] = 0
        
        for passo in range(1, self.n * self.n):
            candidatos = self.movimentos_legais(posicao, visitado)
            if not candidatos:
                break
            
            # Heurística de Warnsdorff com desempate
            if len(candidatos) > 1:
                # Escolhe o com menor grau; em caso de empate, o que tem maior distância do centro
                posicao = min(candidatos, 
                            key=lambda p: (self.grau(p, visitado), 
                                         -abs(p[0] - self.n/2) - abs(p[1] - self.n/2)))
            else:
                posicao = candidatos[0]
                
            visitado[posicao[0]][posicao[1]] = True
            tabuleiro[posicao[0]][posicao[1]] = passo
            caminho.append(posicao)
        
        completo = len(caminho) == self.n * self.n
        return tabuleiro, caminho, completo

    def visualizar(self, caminho, intervalo=200, salvar_gif=None, mostrar_numeros=True):
        """Visualização melhorada com mais opções."""
        n = self.n
        
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim(0, n)
        ax.set_ylim(0, n)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect('equal')
        
        cores = ['#eeeed2', '#769656']
        for linha in range(n):
            for coluna in range(n):
                cor = cores[(linha + coluna) % 2]
                ax.add_patch(plt.Rectangle((coluna, n - 1 - linha), 1, 1, color=cor))
        
        for i in range(n):
            ax.text(i + 0.5, -0.08, chr(ord('A') + i), 
                   ha='center', va='top', fontsize=12, fontweight='bold')
            ax.text(-0.08, i + 0.5, str(i + 1),
                   ha='right', va='center', fontsize=12, fontweight='bold')
        
        # Grid sutil
        for i in range(n + 1):
            ax.axhline(y=i, color='black', linewidth=0.5, alpha=0.2)
            ax.axvline(x=i, color='black', linewidth=0.5, alpha=0.2)
        
        def coord(pos):
            linha, coluna = pos
            return coluna + 0.5, n - 1 - linha + 0.5
        
        # Elementos da animação
        trilha, = ax.plot([], [], color='#FF4444', linewidth=2.5, alpha=0.7, zorder=2)
        cavalo, = ax.plot([], [], marker='s', markersize=28, 
                         color='#2C2C2C', zorder=3, markeredgecolor='#666666',
                         markeredgewidth=2)
        
        # Para animação mais suave
        xs, ys = [], []
        textos = []
        
        def atualizar(frame):
            pos = caminho[frame]
            x, y = coord(pos)
            xs.append(x)
            ys.append(y)
            
            # Atualiza trilha com transição suave
            trilha.set_data(xs, ys)
            cavalo.set_data([x], [y])
            
            # Mostra números apenas se solicitado
            if mostrar_numeros and frame % max(1, len(caminho) // 50) == 0:
                # Mostra alguns números para não poluir o tabuleiro
                ax.text(x, y, str(frame), fontsize=9, ha='center', va='center',
                       color='#FFFFFF' if (pos[0] + pos[1]) % 2 == 1 else '#000000',
                       zorder=4, fontweight='bold', alpha=0.8)
            
            # Título informativo
            titulo = f'Passeio do Cavalo - Passo {frame+1}/{len(caminho)}'
            if frame == len(caminho) - 1:
                titulo += ' ✓ Completo!' if len(caminho) == n*n else ' ⚠ Parcial'
            ax.set_title(titulo, fontsize=14, pad=10)
            
            return trilha, cavalo
        
        anim = animation.FuncAnimation(
            fig, atualizar, frames=len(caminho), interval=intervalo,
            repeat=False, blit=False,
        )
        
        plt.tight_layout(pad=2.0)
        plt.subplots_adjust(top=0.92)  # Dá mais espaço para o título
        plt.show()
        return anim


if __name__ == '__main__':
    passeio = PasseioCavalo(n=8)

    posicao_inicial = [(7, 0)] # <--- POSIÇÃO INICIAL DO CAVALO
    
    for inicio in posicao_inicial:
        print(f"\n{'='*50}")
        print(f"Tentando posição inicial: {inicio}")
        
        tabuleiro, caminho, completo, tentativas = passeio.passeio_cavalo(inicio)
        
        if completo:
            print(f'✓ Passeio completo! {len(caminho)} casas visitadas.')
            print(f'  Encontrado na tentativa {tentativas}')
            
            # Exibe tabuleiro formatado
            print("\nTabuleiro numerado (ordem de visita):")
            for linha in tabuleiro:
                print(' '.join(f'{v:3d}' if v is not None else ' . ' for v in linha))
            
            # Visualização
            passeio.visualizar(caminho, intervalo=300, 
                              mostrar_numeros=True)
            break  # Para no primeiro completo
        else:
            print(f'✗ Passeio parcial: {len(caminho)}/{64} casas.')

    


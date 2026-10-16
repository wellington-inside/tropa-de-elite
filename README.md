# Tropa de Elite: estatísticas do clã (Clash of Clans)

Guia para continuar este trabalho em outra conversa ou ferramenta.

## O que existe aqui
- `outubro-2026/ataques.csv`: uma linha por jogador por guerra do mês.
  Colunas: data, tipo, guerra, adversario, jogador, ataques_feitos, ataques_disponiveis,
  estrelas (estrelas reais de cada ataque; 100% = 3), novas_estrelas (desempate),
  destruicao_pct (soma da % dos ataques), observacao.
- `outubro-2026/liga-resumo.csv`: resultado final da Liga de Clãs de outubro (aba Clã).
- `site/template.html` + `site/gerar.py`: geram a página. Rodar `python3 site/gerar.py saida.html`.
- `site/publicar/clashofclans/`: versão da página que funciona fora do Claude (index.html + ícone).
- `marca/`: logo (SVG/PNG) e fotos de perfil do WhatsApp (clã, liderança, comunicados).

## Regras combinadas com o Wellington
- Ranking das guerras: estrelas reais somadas; desempate por novas estrelas, depois destruição.
- Os 15 melhores das guerras do mês vigente vão para a Liga; os demais jogam no clã Union.
- Os prints chegam da aba "Minha equipe > Ataques". As estrelas reais dos ataques abaixo de 100%
  são contadas pelas estrelinhas acesas; o número no quadro amarelo é o de novas estrelas.
- Página publicada: https://claude.ai/artifact/3Da9pqxBDzhMgPt799ojTc

## Pendente
- Publicar no GitHub Pages (repositório `tropa-de-elite`, endereço clash.wellvideo.com.br
  via CNAME para wellington-inside.github.io).
- Decidir se o ranking usa total de estrelas ou média por guerra.

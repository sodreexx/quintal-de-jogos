# Quintal de Jogos

Três jogos digitais simples para estimular a psicomotricidade: **Pega a Fruta**, **Jogo da Memória** e **Acenda as Luzes**, em cenas 3D no estilo maquete (three.js).

No ar: https://quintal-de-jogos.vercel.app

## O que tem

- Jogos 3D com versões simples de reserva para aparelhos sem WebGL.
- Dificuldade adaptativa (o jogo acelera quando a pessoa acerta e fica mais calmo quando ela erra).
- Sistema de jogadores: as partidas contam até alguém tocar em **Novo jogador**; o **resumo** traz uma análise gentil de cada jogo.
- Narração gravada no ElevenLabs (voz Dantas), com reserva na voz do aparelho.
- Modo claro e escuro, abertura com a marca sodree dev., vídeo de apresentação que só carrega ao tocar.
- Aplicativo web instalável (tela cheia, funciona offline) e aviso para girar a tela nos jogos em celular e tablet.

## Estrutura

| Caminho | O que é |
|---|---|
| `src/quintal-de-jogos.html` | Fonte da página (CSS, marcação e JS num arquivo só) |
| `build.py` | Gera o `index.html` final a partir da fonte |
| `index.html` | Página publicada (gerada; não editar à mão) |
| `sw.js`, `manifest.webmanifest` | Aplicativo web: cache offline e instalação |
| `audio/` | Falas da narração |
| `video/` | Vídeo de apresentação (720p) e capa |
| `vercel.json` | Cabeçalhos da Vercel |

## Como atualizar

1. Edite `src/quintal-de-jogos.html`.
2. Gere a página: `python build.py`
3. Ao mudar arquivos guardados offline, aumente a versão em `sw.js` (`quintal-vN`).
4. Publique: `vercel deploy --prod`

Feito por sodree dev.

# Cores no Terminal

- ANSI (Escape sequence), padrão de normalização que será usado para o nosso terminal
- Para colocarmos uma cor com o código ansi, devemos usar:

```python
\033[0:33:44m # \033[style:text:backgroundm
```

- Style:
  - 0 = None
  - 1 = Bold
  - 4 = Underline
  - 7 = Negative
- Text:
  - 30 = White
  - 31 = Red
  - 32 = Green
  - 33 = Yellow
  - 34 = Blue
  - 35 = Violet
  - 36 = Cyan
  - 37 = Grey
- Background:
  - 40 = White
  - 41 = Red
  - 42 = Green
  - 43 = Yellow
  - 44 = Blue
  - 45 = Violet
  - 46 = Cyan
  - 47 = Grey
- 
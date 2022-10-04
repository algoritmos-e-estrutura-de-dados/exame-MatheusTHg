def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
  trocaTotal = 0

  menor = figurinhas_da_maria if len(figurinhas_da_maria) <= len(figurinhas_do_joao) else figurinhas_do_joao
  maior = figurinhas_da_maria if len(figurinhas_da_maria) >= len(figurinhas_do_joao) else figurinhas_do_joao

  for i, n_figurinha in enumerate(menor):
    if not n_figurinha in maior:
      for n in range(i, len(maior)):
        if n_figurinha != maior[n]:
          aux = maior[n]
          maior[n] = n_figurinha
          menor[i] = aux
          trocaTotal = trocaTotal + 1
          break
  return trocaTotal


if __name__ == '__main__':
  A, B = input().split(' ')
  figurinhas_da_maria = input().split(' ')
  figurinhas_da_joao = input().split(' ')
  print(maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao))

something =  input('Digite algo: ')
print('O tipo primitivo desse valor é', type(something))

print('\n---Testes---',
      f'\nO valor só tem espaços?             {something.isspace()}',
      f'\nO valor é um número?                {something.isnumeric()}',
      f'\nO valor é alfabético?               {something.isalpha()}',
      f'\nO valor é alfa-numérico?            {something.isalnum()}',
      f'\nO valor está em maiúsculas?         {something.isupper()}',
      f'\nO valor está em minúsculas?         {something.islower()}',
      f'\nO valor está capitalizado?          {something.istitle()}',
      f'\nO valor é dígito?                   {something.isdigit()}',
      f'\nO valor é decimal?                  {something.isdecimal()}',
      f'\nO valor é imprimível?               {something.isprintable()}',
      f'\nO valor é ascii?                    {something.isascii()}',
      f'\nO valor é um indentificador válido? {something.isidentifier()}')

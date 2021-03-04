# Automatic_Exam_Filler (em manutenção)

Preenchedor automático de Testes, desenvolvido para a disciplina de Álgebra da EMAp - FGV.

[Links para versões executáveis (Windows/Linux)](https://gvmail-my.sharepoint.com/:f:/g/personal/b39398_fgv_edu_br/EoJvqAgni19GrqVXFWxrJMIB4JmN463Ywy1jpFWhLq-7mw?e=UHKXZ0)

## Instruções

1. Baixe do link acima o executável relativo à seu sistema e coloque o arquivo pdf com todos os testes na mesma pasta, é recomendado reservar uma pasta só pra esses arquivos.
> Para Windows baixe 'script_windows.exe'; Para Linux baixe 'script_linux'
2. Execute o arquivo .exe aguarge a identificação do pdf. O programa irá indexar o pdf com data de modificação mais recente, então, não coloque mais nenhum pdf diferente nessa pasta após baixar o teste.
>  Se estiver no Windows, basta clicar duas vezes no executável. 
No Linux, abra um terminal no diretório e execute por lá através de chmod +x script_linux e depois ./script_linux

2. Após a identificação ser feita corretamente, preencha as informações:

  - __Página do seu Gabarito:__ Página do pdf geral referente à página gabarito do seu teste (não é a parte da prova). Para saber qual o seu teste, consulte as intruções do Professor.
  
  - __Matrícula:__ Número da sua matrícula (9 dígitos)
  
  - __Gabarito:__ Alternativas que você marcou, digitadas sequencialmente da questão 1 a 5, sem espaços.
  
  > Exemplo, suponha que você marcou nas questões 1, 2, 3, 4 e 5 as alternativas A, B, C, D e E respectivamente; Você deve digitar então "ABCDE", sem aspas, símbolos ou espaços.
  > Não há distinção entre maiúsculas e minúsculas.
  
  - __Nome e Sobrenome:__ Para fins de identificação e geração do nome do arquivo de saída, vc deve digitar seu nome e sobrenome.
  
4. Na mesma pasta será gerado um arquivo "Gabarito_Nome_Sobrenome.pdf" contendo seu teste devidamente preenchido.

### Cuidados

 - Caso selecione de forma errada a página referente ao seu teste, você deverá repetir o procedimento informando corretamente este dado; Porém, apague o arquivo incorreto do diretório, pois o programa considera o arquivo geral como o mais recente por data de modificação, e ter um arquivo gerado incorretamente no mesmo diretório pode causar erros inesperados.
 
 - Pelo mesmo motivo, após baixar o arquivo geral de testes na mesma pasta, não baixei mais nenhum outro pdf nessa pasta, só volte a usá-la no próximo teste.
 
### Referências
- Executáveis compilados via [pyinstaller](http://www.pyinstaller.org/).

- [Referência do código](https://sigmoidal.io/pdfrw-explained/).
 

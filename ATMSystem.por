programa
{
	
	funcao inicio()
	{
		inteiro totced50=100, totced20=100, totced5=100, totced1=100, totbank=0, passbank[2]
		cadeia userbank[2], user
		inteiro loop=1, pass=0, mnybank[2], cedatual=0


		userbank[0] = "Joao"
		userbank[1] = "Joaquim"
		passbank[0] = 132
		passbank[1] = 132
		mnybank[0] = 2000
		mnybank[1] = 2000
		totbank = (totced50*50)+(totced20*20)+(totced5*5)+totced1
		
		enquanto (loop > 0){
			inteiro saque=0, totced=0
			escreva("Usuário: ")
			leia(user)
			escreva("Senha: ")
			leia(pass)
			limpa()
			para (inteiro i=0;i<2;i++){
				se (user == userbank[i] e pass == passbank[i]){
					escreva("Digite o valor do saque: ")
					leia(saque)
					limpa()
					se (saque <= mnybank[i] e saque <= totbank e saque > 0 e saque <= 1000){
						mnybank[i]-=saque
						cedatual = 50
						enquanto (loop > 0){
							se (saque >= cedatual){
								saque-=cedatual
								totced++
								se (cedatual == 50){
									totced50-=1
								}
								senao se (cedatual == 20){
									totced20-=1
								}
								senao se (cedatual == 5){
									totced5-=1
								}
								senao se (cedatual == 1){
									totced1-=1
								}
							}
							senao{
								se (totced > 0){
									escreva(totced," cédulas de B$", cedatual)
								}
								se (cedatual == 50 ou totced50 == 0){
									cedatual = 20
								}
								senao se (cedatual == 20 ou totced20 == 0){
									cedatual = 5
								}
								senao se (cedatual == 10 ou totced5 == 0){
									
								}
								totced=0
								se (saque == 0){
									pare
								}
							}
						}
						escreva("\n")
						escreva("Saque realzado com sucesso")
					}
					senao{
						escreva("Saque indisponivel")
						limpa()
						pare
					}
					pare
				}
				senao{
					escreva("Usuário ou senha Incorretos!\n")
					pare
				}
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1688; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
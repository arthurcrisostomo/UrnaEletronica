
def verificar_add(numeros: str):
    # > Verifica se tamanho de numeros é menor ou igual a 1
    if len(numeros) <= 1:
        return True

    # > Indica que não permite adicionar um novo numero
    return False

def localizar_candidato(voto: str, dict_candidatos: dict):
    # > Verifica se o voto do usuario é igual a 2 numeros
    if len(voto) == 2:
        # > Caso a chave seja encontrada no dict_candidatos, retorna o valor da chave
        # se nao for encontrado retorna NUMERO ERRADO
        candidato = dict_candidatos.get(voto, 'NUMERO ERRADO')
    else:
        candidato = ''

    return candidato

def verificacao_confirma(voto: str, dict_candidatos: dict):
    # > Verifica se o self._numero voto não está no self.dict_cadidatos
    if voto not in dict_candidatos and voto != 'BRANCO':
        # > Define o self._numero_voto como nulo
        voto = 'NULO'
        print(voto)

    # > Retorna o voto atual para quem o chamou
    return voto

import os, sys

# Verifica o comando
if len(sys.argv) > 2:
    print(
'''Uso:
    python <nome-deste-script.py> [<diretório das respostas>]
Exemplos:
    python corretor.py
    python corretor.py "caminho/para/dir-respostas"
''')
    exit(1)

# Código para testar questões
dir = sys.argv[1] if len(sys.argv) == 2 else '.'
respostas_certas = 0
respostas_erradas = 0


def questao(descricao: str, script: str, subtestes: list):
    # Converte os subtestes em objetos Teste
    testes = []
    for args_script, func_expect, args_expect in subtestes:
        testes += [Teste(script, args_script, func_expect, args_expect)]

    # Executa os testes, conta acertos e exibe erros
    global respostas_certas, respostas_erradas
    for t in testes:
        erro = t.testar()
        if erro:
            respostas_erradas += 1
            print(f'{descricao} errada:')
            print('-', erro)
            return
    print(f'{descricao} certa.')
    respostas_certas += 1


class Teste():
    def __init__(self, script: str, args: str, func_expect, args_expect: list):
        self.script = f'{dir}/{script}' if dir != '.' else script
        self.args = args
        self.func_expect = func_expect
        self.args_expect = args_expect

    @property
    def comando(self):
        return f'php {self.script} {self.args}'

    def testar(self):
        processo = os.popen(self.comando)
        resposta = processo.read()
        codigo = processo.close()
        codigo = 0 if codigo == None else codigo

        if codigo == 0:
            # Arquivo foi executado, verifica resposta.
            ok, erro = self.func_expect(resposta, *self.args_expect)
            if not ok:
                return self._formatar_erro(erro)
            return None
        elif codigo == 256: # File not found.
            return self._formatar_erro(f'Arquivo {self.script} não encontrado.')
        elif codigo == 65280:
            return self._formatar_erro(f'Erro de sintaxe.' +
            f' Execute o arquivo {self.script} para mais detalhes.')
        else:
            return self._formatar_erro(f"Codigo do erro: {codigo}")

    def _formatar_erro(self, erro):
        return f'Comando: {self.comando}\n  {erro}'


def testar_igual(resultado: str, esperado: str, strip="\n ") -> (bool, str):
    resultado = resultado.strip(strip)
    esperado = esperado.strip(strip)
    if resultado != esperado:
        erro = f"Esperava '{esperado}', recebeu '{resultado}'"
        return False, erro
    return True, ''

# Testes
questao('Q1', 'q1.php', [('', testar_igual, ['string(13) "Hello, world!"'])])

questao('Q2', 'q2.php', [('Charlon', testar_igual, ['string(15) "Hello, Charlon!"'])])

questao('Q3', 'q3.php', [('10.5 14.3 35.2', testar_igual, ['float(20)'])])

questao('Q4', 'q4.php', [('3679', testar_igual, ['string(7) "1h1m19s"'])])


questao('Q5', 'q5.php', [
    ('17', testar_igual, ['string(5) "Menor"']),
    ('18', testar_igual, ['string(6) "Adulto"']),
    ('60', testar_igual, ['string(5) "Idoso"']),
    ('59', testar_igual, ['string(6) "Adulto"'])
])

questao('Q6', 'q7.php', [
    ('1 2 3', testar_igual, ['int(3)']),
    ('3 2 1', testar_igual, ['int(3)']),
    ('1 3 2', testar_igual, ['int(3)']),
    ('1 3 3', testar_igual, ['int(3)']),
    ('3 3 2', testar_igual, ['int(3)']),
    ('3 3 3', testar_igual, ['int(3)'])
])

questao('Q7', 'q9.php', [
    ('5', testar_igual, ['string(10) "1 2 3 4 5 "'])
])

total_respostas = respostas_certas + respostas_erradas
print(f'Respostas certas: {respostas_certas} de {total_respostas}')
print(f'Respostas erradas: {respostas_erradas} de {total_respostas}')
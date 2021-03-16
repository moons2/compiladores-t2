'''
titulo:
    Analisador Sintático para a Linguagem Algoritmica(LA)
    TRABALHO 2 - COMPILADORES 1

autores:
    Luan V. Moraes da Silva - 744342
    Guilherme Servidoni - 727339
    Alisson Roberto Gomes - 725721

para compilar:
    > java -jar antlr-4.9.1-complete.jar -Dlanguage=Python3 LA.g4

para executar:
    > [python | python3] main.py input-program.txt output-program.txt
'''

# importacoes
from antlr4 import *
from LALexer import LALexer
from LAParser import LAParser
import sys
import os


'''
Tratamento de erros lexicos em tempo de execucap
'''


class LexicoErroListener(object):
    def syntaxError(recognizer, offendingSymbol, line, column, msg, e):

        token_type = recognizer._input.getType(
            recognizer._tokenStartCharIndex, recognizer._input.index)

        errs = ['ERR_COMENT', 'ERR_CADEIA', 'ERR_SIMBOLO']
        if token_type in errs:
            # se pertencer, entao eu trato o erro de acordo com o especificado
            if token_type == errs[2]:
                raise Exception(
                    f'Linha {line}: {text} - simbolo nao identificado')
            elif token_type == errs[1]:
                raise Exception(f'Linha {line}: cadeia literal nao fechada')
            else:
                raise Exception(f'Linha {line}: comentario nao fechado')


'''
Parser para erros semanticos em tempo de execucao
'''


class ParserErroListener(object):
    def syntaxError(recognizer, offendingSymbol, line, column, msg, e):
        if "EOF" in offendingSymbol.text:
            offendingSymbol.text = "EOF"

        msg = f'Linha {line}: erro sintatico proximo a {offendingSymbol.text}'
        raise Exception(msg)

# funcao principal
# params: argv, uma lista com as entradas obtidas da linha de comando
# return: nao possui return


def main(argv):
    # guarda argumento 1
    input_file = argv[1]

    # guarda argumento 2
    output_file = argv[2]

    # verifica se o arquivo destino output existe
    if os.path.exists(output_file):
        # se existir entao ele eh apagado
        os.remove(output_file)

    # o arquivo onde a saida sera gerada eh entao criado
    target_file = open(output_file, "a")

    # metodo da lib antlr4 que le um arquivo
    input_stream = FileStream(input_file, encoding="utf-8")

    # variavel que sera atribuida ao arquivo destino
    output = ""

    # objeto Lexer criado
    lexer = LALexer(input_stream)

    # por garantia
    lexer.removeErrorListeners()

    lexer.addErrorListener(LexicoErroListener)

    tokens = CommonTokenStream(lexer)
    parser = LAParser(tokens)

    # sobrescrevo o ErroListener default
    parser.addErrorListener(ParserErroListener)

    # o equivalente de parser.programa() em java
    try:
        parser.programa()
    except Exception as err:
        output += f'{str(err)}\n'

    output += f'Fim da compilacao\n'

    # a variavel output eh entao escrita no arquivo destino e fechado
    target_file.write(output)
    target_file.close()


# python assinatura para verificar se este arquivo e o principal
if __name__ == '__main__':
    main(sys.argv)

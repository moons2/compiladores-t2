'''
titulo:
    Analisador Lexico para a Linguagem Algoritmica(LA)
    TRABALHO 1 - COMPILADORES 1

autores:
    Luan V. Moraes da Silva - 744342
    Guilherme Servidoni - 727339
    Alisson Roberto Gomes - 725721

para compilar:
    > java -jar antlr-4.9.1-complete.jar -Dlanguage=Python3 LALexer.g4

para executar:
    > [python | python3] main.py input-program.txt output-program.txt
'''

# importacoes
from antlr4 import *
from LALexer import LALexer
from LAParser import LAParser
# from antlr4.error.ErrorListener import ErrorListener
import sys
import os


class LexicoErroListener(object):
    def syntaxError(recognizer, offendingSymbol, line, column, msg, e):
        # Caso de caractere não reconhecido
        text = recognizer._input.getText(
            recognizer._tokenStartCharIndex, recognizer._input.index)
        text = text.strip().rstrip('\n')
        return_msg = 'simbolo nao identificado'

        # Em caso de comentario não fechado
        if text[0] == '{' and len(text) > 1:
            raise Exception(f'Linha {line}: comentario nao fechado')
        # Em caso de cadeia literal não fechada, de acordo com a definição da gramática
        elif text[0] == '"' and len(text) > 1:
            raise Exception(f'Linha {line}: cadeia literal nao fechada')

        raise Exception(f'Linha {line}: {text} - {return_msg}')


'''
Parser Error Listener
'''


class ParserErroListener(object):
    def syntaxError(recognizer, offendingSymbol, line, column, msg, e):
        if "EOF" in offendingSymbol.text:  # No Python, o ANTLR4 força "<EOF>" e não somente "EOF"
            offendingSymbol.text = "EOF"

        # Em caso de erro sintático encontrado.
        raise Exception(
            f'Linha {line}: erro sintatico proximo a {offendingSymbol.text}')

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

    output = ""

    # objeto Lexer criado
    lexer = LALexer(input_stream)
    # lexer.addErrorListener(LexicoErroListener)

    stream = CommonTokenStream(lexer)
    parser = LAParser(stream)
    parser.addErrorListener(ParserErroListener)
    try:
        parser.programa()
    except Exception as err:
        output += f'{str(err)}\n'
    # variavel que sera atribuida ao arquivo destino

    # token_list guarda todos os tokens encontrados pos
    # analise do arquivo destino pelo analisador lexico
    # token_list = lexer.getAllTokens()

    # list_exceptions = ['PALAVRA_RESERVADA', 'DELIMITADOR', 'DECLARADOR', 'OP_RELACIONAL', 'OP_ARIT', 'OP_UNARIO', 'ATRIBUIDOR', 'OUTRO_OP', 'OP_LOGICO']

    # errs = ['ERR_COMENT', 'ERR_CADEIA', 'ERR_SIMBOLO']

    # loop que percorre a lista de tokens gerados pelo
    # analisador lexico retornado em lexer.getAllTokens()
    # for token in token_list:

        # obtencao do nome da regra do token
        # token_rule_name = LALexer.symbolicNames[token.type]

        # verificacao se a regra pertence a um dos erros
        # if token_rule_name in errs:
        # se pertencer, entao eu trato o erro de acordo com o especificado
        # if token_rule_name == errs[2]:
        #    output += f'Linha {token.line}: {token.text} - simbolo nao identificado\n'
        # elif token_rule_name == errs[1]:
        #    output += f'Linha {token.line}: cadeia literal nao fechada\n'
        # else:
        #    output += f'Linha {token.line}: comentario nao fechado\n'

        # existe_erro_lexico = True
        # break

        # if token_rule_name in list_exceptions:
        #    output += f'<\'{token.text}\',\'{token.text}\'>\n'
        # else:
        #    output += f'<\'{token.text}\',{token_rule_name}>\n'

    output += f'Fim da compilacao\n'

    # a variavel output eh entao escrita no arquivo destino e fechado
    target_file.write(output)
    target_file.close()


# python assinatura para verificar se este arquivo e o principal
if __name__ == '__main__':
    main(sys.argv)

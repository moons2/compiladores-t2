# Generated from LA.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LAParser import LAParser
else:
    from LAParser import LAParser

# This class defines a complete listener for a parse tree produced by LAParser.
class LAListener(ParseTreeListener):

    # Enter a parse tree produced by LAParser#programa.
    def enterPrograma(self, ctx:LAParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LAParser#programa.
    def exitPrograma(self, ctx:LAParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LAParser#declaracoes.
    def enterDeclaracoes(self, ctx:LAParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by LAParser#declaracoes.
    def exitDeclaracoes(self, ctx:LAParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by LAParser#decl_local_global.
    def enterDecl_local_global(self, ctx:LAParser.Decl_local_globalContext):
        pass

    # Exit a parse tree produced by LAParser#decl_local_global.
    def exitDecl_local_global(self, ctx:LAParser.Decl_local_globalContext):
        pass


    # Enter a parse tree produced by LAParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by LAParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by LAParser#variavel.
    def enterVariavel(self, ctx:LAParser.VariavelContext):
        pass

    # Exit a parse tree produced by LAParser#variavel.
    def exitVariavel(self, ctx:LAParser.VariavelContext):
        pass


    # Enter a parse tree produced by LAParser#identificador.
    def enterIdentificador(self, ctx:LAParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by LAParser#identificador.
    def exitIdentificador(self, ctx:LAParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by LAParser#dimensao.
    def enterDimensao(self, ctx:LAParser.DimensaoContext):
        pass

    # Exit a parse tree produced by LAParser#dimensao.
    def exitDimensao(self, ctx:LAParser.DimensaoContext):
        pass


    # Enter a parse tree produced by LAParser#tipo.
    def enterTipo(self, ctx:LAParser.TipoContext):
        pass

    # Exit a parse tree produced by LAParser#tipo.
    def exitTipo(self, ctx:LAParser.TipoContext):
        pass


    # Enter a parse tree produced by LAParser#tipo_basico.
    def enterTipo_basico(self, ctx:LAParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by LAParser#tipo_basico.
    def exitTipo_basico(self, ctx:LAParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by LAParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:LAParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by LAParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:LAParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by LAParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:LAParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by LAParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:LAParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by LAParser#valor_constante.
    def enterValor_constante(self, ctx:LAParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by LAParser#valor_constante.
    def exitValor_constante(self, ctx:LAParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by LAParser#registro.
    def enterRegistro(self, ctx:LAParser.RegistroContext):
        pass

    # Exit a parse tree produced by LAParser#registro.
    def exitRegistro(self, ctx:LAParser.RegistroContext):
        pass


    # Enter a parse tree produced by LAParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:LAParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by LAParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:LAParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by LAParser#parametro.
    def enterParametro(self, ctx:LAParser.ParametroContext):
        pass

    # Exit a parse tree produced by LAParser#parametro.
    def exitParametro(self, ctx:LAParser.ParametroContext):
        pass


    # Enter a parse tree produced by LAParser#parametros.
    def enterParametros(self, ctx:LAParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LAParser#parametros.
    def exitParametros(self, ctx:LAParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LAParser#corpo.
    def enterCorpo(self, ctx:LAParser.CorpoContext):
        pass

    # Exit a parse tree produced by LAParser#corpo.
    def exitCorpo(self, ctx:LAParser.CorpoContext):
        pass


    # Enter a parse tree produced by LAParser#cmd.
    def enterCmd(self, ctx:LAParser.CmdContext):
        pass

    # Exit a parse tree produced by LAParser#cmd.
    def exitCmd(self, ctx:LAParser.CmdContext):
        pass


    # Enter a parse tree produced by LAParser#cmdleia.
    def enterCmdleia(self, ctx:LAParser.CmdleiaContext):
        pass

    # Exit a parse tree produced by LAParser#cmdleia.
    def exitCmdleia(self, ctx:LAParser.CmdleiaContext):
        pass


    # Enter a parse tree produced by LAParser#cmdescreva.
    def enterCmdescreva(self, ctx:LAParser.CmdescrevaContext):
        pass

    # Exit a parse tree produced by LAParser#cmdescreva.
    def exitCmdescreva(self, ctx:LAParser.CmdescrevaContext):
        pass


    # Enter a parse tree produced by LAParser#cmdse.
    def enterCmdse(self, ctx:LAParser.CmdseContext):
        pass

    # Exit a parse tree produced by LAParser#cmdse.
    def exitCmdse(self, ctx:LAParser.CmdseContext):
        pass


    # Enter a parse tree produced by LAParser#cmdcaso.
    def enterCmdcaso(self, ctx:LAParser.CmdcasoContext):
        pass

    # Exit a parse tree produced by LAParser#cmdcaso.
    def exitCmdcaso(self, ctx:LAParser.CmdcasoContext):
        pass


    # Enter a parse tree produced by LAParser#cmdpara.
    def enterCmdpara(self, ctx:LAParser.CmdparaContext):
        pass

    # Exit a parse tree produced by LAParser#cmdpara.
    def exitCmdpara(self, ctx:LAParser.CmdparaContext):
        pass


    # Enter a parse tree produced by LAParser#cmdenquanto.
    def enterCmdenquanto(self, ctx:LAParser.CmdenquantoContext):
        pass

    # Exit a parse tree produced by LAParser#cmdenquanto.
    def exitCmdenquanto(self, ctx:LAParser.CmdenquantoContext):
        pass


    # Enter a parse tree produced by LAParser#cmdfaca.
    def enterCmdfaca(self, ctx:LAParser.CmdfacaContext):
        pass

    # Exit a parse tree produced by LAParser#cmdfaca.
    def exitCmdfaca(self, ctx:LAParser.CmdfacaContext):
        pass


    # Enter a parse tree produced by LAParser#cmdatribuicao.
    def enterCmdatribuicao(self, ctx:LAParser.CmdatribuicaoContext):
        pass

    # Exit a parse tree produced by LAParser#cmdatribuicao.
    def exitCmdatribuicao(self, ctx:LAParser.CmdatribuicaoContext):
        pass


    # Enter a parse tree produced by LAParser#cmdchamada.
    def enterCmdchamada(self, ctx:LAParser.CmdchamadaContext):
        pass

    # Exit a parse tree produced by LAParser#cmdchamada.
    def exitCmdchamada(self, ctx:LAParser.CmdchamadaContext):
        pass


    # Enter a parse tree produced by LAParser#cmdretorne.
    def enterCmdretorne(self, ctx:LAParser.CmdretorneContext):
        pass

    # Exit a parse tree produced by LAParser#cmdretorne.
    def exitCmdretorne(self, ctx:LAParser.CmdretorneContext):
        pass


    # Enter a parse tree produced by LAParser#selecao.
    def enterSelecao(self, ctx:LAParser.SelecaoContext):
        pass

    # Exit a parse tree produced by LAParser#selecao.
    def exitSelecao(self, ctx:LAParser.SelecaoContext):
        pass


    # Enter a parse tree produced by LAParser#item_selecao.
    def enterItem_selecao(self, ctx:LAParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by LAParser#item_selecao.
    def exitItem_selecao(self, ctx:LAParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by LAParser#constantes.
    def enterConstantes(self, ctx:LAParser.ConstantesContext):
        pass

    # Exit a parse tree produced by LAParser#constantes.
    def exitConstantes(self, ctx:LAParser.ConstantesContext):
        pass


    # Enter a parse tree produced by LAParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:LAParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by LAParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:LAParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by LAParser#op_unario.
    def enterOp_unario(self, ctx:LAParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by LAParser#op_unario.
    def exitOp_unario(self, ctx:LAParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by LAParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:LAParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by LAParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:LAParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by LAParser#termo.
    def enterTermo(self, ctx:LAParser.TermoContext):
        pass

    # Exit a parse tree produced by LAParser#termo.
    def exitTermo(self, ctx:LAParser.TermoContext):
        pass


    # Enter a parse tree produced by LAParser#fator.
    def enterFator(self, ctx:LAParser.FatorContext):
        pass

    # Exit a parse tree produced by LAParser#fator.
    def exitFator(self, ctx:LAParser.FatorContext):
        pass


    # Enter a parse tree produced by LAParser#op1.
    def enterOp1(self, ctx:LAParser.Op1Context):
        pass

    # Exit a parse tree produced by LAParser#op1.
    def exitOp1(self, ctx:LAParser.Op1Context):
        pass


    # Enter a parse tree produced by LAParser#op2.
    def enterOp2(self, ctx:LAParser.Op2Context):
        pass

    # Exit a parse tree produced by LAParser#op2.
    def exitOp2(self, ctx:LAParser.Op2Context):
        pass


    # Enter a parse tree produced by LAParser#op3.
    def enterOp3(self, ctx:LAParser.Op3Context):
        pass

    # Exit a parse tree produced by LAParser#op3.
    def exitOp3(self, ctx:LAParser.Op3Context):
        pass


    # Enter a parse tree produced by LAParser#parcela.
    def enterParcela(self, ctx:LAParser.ParcelaContext):
        pass

    # Exit a parse tree produced by LAParser#parcela.
    def exitParcela(self, ctx:LAParser.ParcelaContext):
        pass


    # Enter a parse tree produced by LAParser#parcela_unario.
    def enterParcela_unario(self, ctx:LAParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by LAParser#parcela_unario.
    def exitParcela_unario(self, ctx:LAParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by LAParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:LAParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by LAParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:LAParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by LAParser#exp_relacional.
    def enterExp_relacional(self, ctx:LAParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by LAParser#exp_relacional.
    def exitExp_relacional(self, ctx:LAParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by LAParser#op_relacional.
    def enterOp_relacional(self, ctx:LAParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by LAParser#op_relacional.
    def exitOp_relacional(self, ctx:LAParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by LAParser#expressao.
    def enterExpressao(self, ctx:LAParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LAParser#expressao.
    def exitExpressao(self, ctx:LAParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LAParser#termo_logico.
    def enterTermo_logico(self, ctx:LAParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by LAParser#termo_logico.
    def exitTermo_logico(self, ctx:LAParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by LAParser#fator_logico.
    def enterFator_logico(self, ctx:LAParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by LAParser#fator_logico.
    def exitFator_logico(self, ctx:LAParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by LAParser#parcela_logica.
    def enterParcela_logica(self, ctx:LAParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by LAParser#parcela_logica.
    def exitParcela_logica(self, ctx:LAParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by LAParser#op_logico_1.
    def enterOp_logico_1(self, ctx:LAParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by LAParser#op_logico_1.
    def exitOp_logico_1(self, ctx:LAParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by LAParser#op_logico_2.
    def enterOp_logico_2(self, ctx:LAParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by LAParser#op_logico_2.
    def exitOp_logico_2(self, ctx:LAParser.Op_logico_2Context):
        pass



del LAParser
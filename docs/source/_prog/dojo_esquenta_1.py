#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Intro Python
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

"""*Dojo* Esquenta -

    Desafios muito simples.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    22.05
        Criação dos desafios.

.. versionadded::    22.08
        Correção dos desafios.


.. seealso::

   Página Original na internete: CodingBat_

.. _CodingBat: https://codingbat.com/python/Warmup-2
"""
_SET0_ = {
    "script_name": "dojo_0", "script_div_id": "dojo_0",
    "height": 200, "title": "multiplicar o inicio"
}  # _SEC_
def multiplicar_o_inicio(inicio, n):
    """Multiplica os três primeiros caracteres.
    """
    inicio_len = 3
    return 'resultado'

assert multiplicar_o_inicio('Chocolate', 2) == ('ChoCho')
assert multiplicar_o_inicio('Chocolate', 3) == ('ChoChoCho')


_SET1_ = {
    "script_name": "dojo_1",    "script_div_id": "dojo_1",
    "height": 200, "title": "criando uma nova palavra"
}  # _SEC_

def exclui_letra(palavra):
    """Exclui caracter sim e outro não.
    """
    resultado = ""
    return resultado


assert exclui_letra("Hello") == ('Hlo')
assert exclui_letra('Heeololeo') == ("Hello")

_SET2_ = {
    "script_name": "dojo_2",    "script_div_id": "dojo_2",
    "height": 200, "title": "numero repetido"
}  # _SEC_
def numero_repetido(numero):
    """Verifica se há o número 9 nos quatro primeiro elemento do array.
    """
    return numero


assert numero_repetido([1, 9, 9, 3, 9]) == 3
assert numero_repetido([1, 9, 9]) == 2

_SET3_ = {
    "script_name": "dojo_3",    "script_div_id": "dojo_3",
    "height": 200, "title": "É ou não é"
}  # _SEC_
def verifica_nove(matriz):
    """Retorna True se um dos quatro primeiros números da matriz for nove
    """
    return None

assert verifica_nove([1, 2, 9, 3, 4]) == True
assert verifica_nove([1, 2, 3, 4, 9]) == False

_SET4_ = {
    "script_name": "dojo_4",    "script_div_id": "dojo_4",
    "height": 200, "title": "Sequencia de numero"
}  # _SEC_
def sequencia_numero(matriz):
    """Retorne True caso a sequência de números 1, 2, 3 aparecer na matriz
    """
    return None


assert sequencia_numero([1, 1, 2, 3, 1]) == True
assert sequencia_numero([1, 1, 2, 4, 1]) == False

_SET5_ = {
    "script_name": "dojo_5",    "script_div_id": "dojo_5",
    "height": 200, "title": "Explosão de letras"
}  # _SEC_
def explosao_letras(palavra):
    palavra_final = ""
    return palavra_final


assert explosao_letras('Code') == ('CCoCodCode')
assert explosao_letras('abc') == ('aababc')
assert explosao_letras('ab') == ('aab')

_SET6_ = {
    "script_name": "dojo_6",    "script_div_id": "dojo_6",
    "height": 200, "title": "Posições Iguais"
}  # _SEC_
def verifica_posicao(palavra1, palavra2):
    posicao_igual = 0
    return posicao_igual


assert verifica_posicao('xxcaazz', 'xxbaaz') == 3
assert verifica_posicao('abc', 'abc') == 2
assert verifica_posicao('abc', 'axc') == 0
_SET7_ = {
    "script_name": "dojo_7",    "script_div_id": "dojo_7",
    "height": 200, "title": "Trecho final repetido"
}  # _SEC_
def trecho_repetido(texto):
    """Retorna o número de vezes que a substring final está repetida.
    """
    resultado = 0
    return resultado

assert trecho_repetido('hixxxhi') == 1
assert trecho_repetido('hoxhoho') == 2


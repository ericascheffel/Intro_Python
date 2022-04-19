#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Intro Python
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

"""Programação Esquenta Zero-

    Operações condicionais.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    22.04
        Criação do tutorial.


.. seealso::

   Página Original na internete: `OPERADORES LÓGICOS EM PYTHON`_

.. _`OPERADORES LÓGICOS EM PYTHON`: http://excript.com/python/operadores-logicos-python.html
"""
_SET0_ = {
    "script_name": "code_0", "script_div_id": "code_0",
    "height": 150, "title": "Tipo booleano"
}  # _SEC_
print(type(True))
print(type(False))
print(type(1 == 1))

_SET1_ = {
    "script_name": "code_1",    "script_div_id": "code_1",
    "height": 150, "title": "Operação condicional"
}  # _SEC_
if 1 == 1:
    print("um igual a um")

if 1 != 1:
    print("um difere de um")
else:
    print("um não difere de um")

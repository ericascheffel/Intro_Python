.. include:: special.rst

.. _modulo_esquenta_um:

Problemas para o Dojo de Aquecimento 1
======================================

1. Multiplicando as palavras
----------------------------

Dada uma string e um int n não negativo, diremos que a frente da string são os primeiros 3 caracteres,
ou o que estiver lá se a string for menor que 3. Retorna n cópias da frente;

frente_vezes('Chocolate', 2) → 'ChoCho'
frente_vezes('Chocolate', 3) → 'ChoChoCho'
frente_vezes('Abc', 3) → 'AbcAbcAbc'

.. raw:: html

  <div id="dojo_0"></div>
  <script type="text/python">
      from ScriptWidget import ScriptBuilder
      sw2 = ScriptBuilder("dojo_esquenta_1.py", height=200, title="dojo esquenta 1")
  </script>


2. Criando uma nova palavra
--------------------------------------------------

Dada uma string, retorne uma nova string feita de todos os caracteres alternados (um sim, um não), começando com
o primeiro, então "Hello" produz "Hlo".



.. raw:: html

  <div id="dojo_1"></div>

3. Número Repetido
---------------------------------

Dado um array de ints, retorne a quantidade de números de 9 no array.

.. raw:: html

  <div id="dojo_2"></div>

4. É ou não é
------------------------------------------------------------------
Dado um array de ints, retorne True se um dos primeiros 4 elementos do array for 9.
O comprimento do array pode ser menor que 4.


.. raw:: html

  <div id="dojo_3"></div>

5. Sequência de Números
---------------------------------

Dada uma matriz de ints, retorne True se a sequência de números 1, 2, 3 aparecer
na matriz em algum lugar.

.. raw:: html

  <div id="dojo_4"></div>

6. Explosão de Letras
---------------------------------

Dada uma string não vazia como "Code", retorne uma string como "CCoCodCode".

.. raw:: html

  <div id="dojo_5"></div>

7. Posições Iguais
---------------------------------

Dadas 2 strings, a e b, retorne o número de posições onde elas contêm a mesma substring de comprimento 2.
Portanto, "xxcaazz" e "xxbaaz" resultam em 3, já que as substrings "xx", "aa" e "az" aparecem no mesmo
lugar em ambas as strings.

.. raw:: html

  <div id="dojo_6"></div>


8. Trecho Final repetido
---------------------------------

Dada uma string, retorne a contagem do número de vezes que uma substring
de comprimento 2 aparece na string e também como os últimos 2 caracteres da
string, então "hixxxhi" produz 1 (não contaremos a substring final).

.. raw:: html

  <div id="dojo_7"></div>

#!/bin/bash

#dump da estrutura
pg_dump -h host_base -U nome_usuario -d nome_base -f estrutura.sql -s -c -E utf-8 -F p -O -v -x

#dump dos dados
pg_dump -h host_base -U nome_usuario -d nome_base -f dados.sql -a -b -E utf-8 -F p -O -v -x

# para dump de tabela especifica, adicionar: -t nome_tabela

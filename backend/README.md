# Modelo final de dados:

Pessoa {
    id*,
    nome,
    sobrenome,
    genero,
    pais FK -> Uniao.id (NULL para os patriarcas imigrantes)
}

Uniao {
    id*,
    pai FK -> Pessoa.id,
    mae FK -> Pessoa.id
}

Evento {
    id*,
    tag ENUM (BIRT,
              CHR,
              DEAT,
              MARR,
              DIV,
              IMMI),
    data,
    local,
    descricao,
    -- Chaves Estrangeiras Mutuamente Exclusivas (ou Polimórficas)
    pers_id FK -> Pessoa.id NULL, -- Para BIRT, DEAT, IMMI
    union_id FK -> Uniao.id NULL    -- Para MARR, DIV
}

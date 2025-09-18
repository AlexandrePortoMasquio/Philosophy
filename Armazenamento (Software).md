---
title: Armazenamento (Software)
updated: 2025-09-15
---

## Definição

Armazenamento, em software, é o conjunto de meios e camadas que conservam [[Dados (Software)]] de forma durável e recuperável ao longo do tempo. Inclui dispositivos de blocos (discos rígidos e SSD/flash), sistemas de arquivos e serviços de dados (bancos, filas, objetos), coordenados pelo [[Kernel (Software)]]. Distingue‑se de [[Memória (Software)]], que é volátil e orientada à execução imediata; aqui, o foco é persistir informação além do ciclo de vida do processo.

## Funcionalidade

O sistema operacional expõe dispositivos e monta sistemas de arquivos que organizam nomes, hierarquias, permissões e metadados. Leituras e escritas passam por caches e filas, equilibrando latência e integridade; políticas de sincronização asseguram que alterações cheguem ao meio físico quando necessário. Camadas superiores (bancos de dados, formatos de arquivo) acrescentam esquemas, transações e controles de concorrência para garantir consistência e recuperação após falhas.

## Casos de Uso

Registros de aplicação (logs), arquivos de usuário (documentos, mídia), bases de dados operacionais e backups. Exemplo cotidiano: ao salvar um texto, o conteúdo sai da memória do editor e é registrado no armazenamento; após reiniciar o dispositivo, o arquivo permanece disponível. Em dispositivos móveis, espaço limitado e desgaste de flash pedem parcimônia e políticas de retenção; em servidores, desempenho e confiabilidade motivam redundância e verificação periódica.

## Em Android e KMP

Em [[Android]], o armazenamento segue o modelo de escopo: dados privados residem em diretórios específicos do [[Aplicativo (Android)]]; conteúdo partilhado (mídia) passa por provedores como o MediaStore. Prefere‑se evitar permissões amplas, usar APIs de conteúdo e sincronizar gravações importantes (fsync/journaling) quando a integridade é crítica. Em segundo plano, tarefas de compactação/rotação de logs e limpeza de cache devem respeitar políticas de energia e cotas, preservando responsividade.

Em [[KMP]], a persistência entra por contratos no código comum e implementações nas bordas. Repositórios e esquemas vivem no shared; drivers e detalhes de I/O são injetados por plataforma (ex.: [[SQLDelight]] com drivers Android/Native). Políticas como [[TTL]] e migrações de esquema mantêm consistência entre versões; operações de arquivo e criptografia ficam específicas por plataforma. Essa separação reduz acoplamento e permite evoluir detalhes sem comprometer o domínio.

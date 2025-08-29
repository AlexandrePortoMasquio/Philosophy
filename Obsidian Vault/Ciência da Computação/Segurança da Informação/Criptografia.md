---
title: Criptografia
tags: [segurança, criptografia]
created: 2025-08-29
updated: 2025-08-29
---

## Definição (Cosmologia Informacional)
- Mecanismos formais para restringir, verificar e autenticar a transmissão de informação (formas) sob um canal ruidoso, preservando invariantes desejados (sigilo, integridade e autoria). Independente de tecnologia específica ou de sujeitos.

## Componentes
- Simétrica: AES/GCM para cifrar/decifrar com a mesma chave (rápida, gestão de chaves essencial).
- Assimétrica: RSA/EC para troca de chaves/assinaturas (mais lenta, adequada a identidade/negociação).
- Hashes: SHA‑2/SHA‑3 para impressão digital; HMAC para integridade com segredo.

## Práticas
- Use primitivas de alto nível (AEAD, libs consolidadas); não invente criptografia.
- Chaves em cofres/OS (Keystore/Secure Enclave); rotação e escopo mínimos.

## Ligações
- [[Blockchain]] (assinaturas, chaves públicas, imutabilidade via hash)
- [[Segurança da Informação]] · [[Protocolos]]

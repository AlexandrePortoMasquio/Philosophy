---
title: Criptografia
tags: [segurança, criptografia]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Técnicas para confidencialidade, integridade e autenticidade de informações.
- Base de muitos protocolos modernos (TLS, assinaturas, KMS, carteiras digitais).
- TODO definir criptografia de forma objetiva, dentro da cosmologia informacional, de forma independente da tecnologia.


## Componentes
- Simétrica: AES/GCM para cifrar/decifrar com a mesma chave (rápida, exige gestão de chaves).
- Assimétrica: RSA/EC para troca de chaves/assinaturas (mais lenta, útil para identidade).
- Hashes: SHA‑2/SHA‑3 para impressão digital; HMAC para integridade com segredo.

## Práticas
- Use primitivas de alto nível (AEAD, libs consolidadas); nunca “invente” criptografia.
- Chaves em cofres/OS (Keystore/Secure Enclave); rotação e escopo mínimos.

## Ligações
- [[Blockchain]] (assinaturas, chaves públicas, imutabilidade via hash)
- [[Segurança da Informação]] · [[Protocolos]]

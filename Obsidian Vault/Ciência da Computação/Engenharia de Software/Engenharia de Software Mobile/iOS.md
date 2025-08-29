---
title: iOS (no KMP)
tags: [ios, kmp]
created: 2025-08-29
updated: 2025-08-29
---

## Como o KMP usa o iOS
- O módulo Shared (KMP) é empacotado como XCFramework (binaries/framework) e consumido pelo app iOS em Swift.
- A interoperabilidade converte tipos Kotlin para Swift/ObjC de forma transparente na maioria dos casos; para `Flow/StateFlow`, usar adaptadores (Combine/closures) no boundary.
- DI/composição: criar Composition Root em Swift, injetando `SqlDriver` nativo e instâncias do shared (repositórios, use cases).

## SwiftUI vs UIKit
- SwiftUI (recomendado): declarativo, integra bem com Combine e tem melhor sinergia com o modelo reativo do shared (Flow→Publisher).
- UIKit: imperativo e maduro; útil se o projeto exigir APIs legadas específicas; mais verboso para estados reativos.

## Ligações
- [[KMP]] · [[SwiftUI]] · [[UIKit]] · [[SQLDelight]] · [[Ktor]]

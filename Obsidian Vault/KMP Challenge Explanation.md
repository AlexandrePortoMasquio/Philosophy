---
title: KMP Challenge — Explanation
tags: [kmp, interview, architecture]
created: 2025-08-31
updated: 2025-08-31
---

## Objective
- Prepare the technical defense of the take‑home challenge (sake shop list/detail) implemented with [[Kotlin]] Multiplatform: architecture, decisions, trade‑offs, and how to run/validate.
- Requirements: see [[Desafio Técnico KMP - Requisitos|KMP Technical Challenge — Requirements]].

## Architecture (overview)
- Ports/Adapters (DIP): contracts in the domain; implementations in data/feature. Improves testability and data‑source swapping.
- Layers (shared):
  - Domain: entities (CatalogItem), `AppResult`/`DomainError` (typed state/errors), repository contract, and use cases.
  - Data: `RemoteDataSource` (Ktor) + `LocalDataSource` (SQLDelight); `CatalogRepositoryImpl` (offline‑first) with mappers.
  - Simple DI (factories) exposes `HttpClient`, DB, and repository construction. No framework (less friction, faster builds).
- UI/Platforms:
  - Android: Compose (MVVM), consumes the shared repository; Kamel for image loading.
  - iOS: SwiftUI (MVVM), consumes a KMP Facade (Swift‑friendly bridge) that encapsulates coroutines/Flow.

## Decisions and Why
- [[Ktor]] + kotlinx.serialization: lightweight, multiplatform, reflection‑free; great fit for shared.
- [[SQLDelight]]: single schema and typed queries; ideal for Android/iOS offline‑first.
- Typed Result/Error: `AppResult/DomainError` avoid throwing across boundaries/interop, standardizing Loading/Empty/Error/Content.
- Factory‑based DI: simplicity over frameworks (challenge timebox); keeps shared isolated.
- Facade for iOS: a clean API surface for SwiftUI without leaking coroutine details.
- Native platforms: [[Kotlin]] (Android) and [[SwiftUI|Swift]] (iOS) to meet native‑app requirements while demonstrating practical [[KMP]] (shared domain/data).

## Tooling
- Languages/UI: [[Kotlin]] (+ Compose Multiplatform/Android), [[SwiftUI]] (iOS).
- Networking/JSON: [[Ktor]] + kotlinx.serialization (MPP, lightweight, reflection‑free).
- Persistence: [[SQLDelight]] (single schema, typed queries, KMP‑friendly).
- Images (Android): Kamel (Compose Multiplatform) for image loading.
- Build: Gradle (KTS), Android/iOS targets; modules `shared`, `composeApp`, `iosApp`.
- Tests (planned): unit tests in domain and mappers; fakes for data sources.
- DI: no Koin/Hilt in shared; factories/constructors instead. Koin can be added later at the app layer.

## Dependency Injection
- Approach: constructor/factory DI in shared (no container). The shared module exposes `Providers` (factories) to create `HttpClient`, `CatalogDatabase`, data sources, and `CatalogRepository`. Apps (Android/iOS) call pure functions — no framework coupling.
- Why not [[Koin]]/Hilt here:
  - Time/complexity: take‑home; avoid setup/plugins/initialization overhead.
  - KMP boundaries: DI containers in KMP work, but can complicate iOS interop (lifecycles/scopes). Simple factories make [[SwiftUI]] bridging trivial (via Facade).
  - Testability: constructors take interfaces (ports), making fakes easy without a container.
- Trade‑offs:
  - Pros: faster builds, explicit/legible wiring, fewer dependencies.
  - Cons: a bit more wiring in apps, fewer dynamic scopes.
- When to add Koin:
  - As features/modules grow and you need scopes (feature/viewModel), especially on Android. Keep shared neutral; add Koin in app layers.
- Example (factory):
  - `createCatalogRepository(driver, baseUrl): CatalogRepository`
  - `createHttpClient(): HttpClient`
  - Apps call these at startup and pass instances to ViewModels/facade.

## Development Organization
- Vertical slices: implement list → details end‑to‑end (domain, data, UI) to validate the architecture early.
- Contracts first: define entities/UseCases/Repo in domain before adapters (minimizes UI rework).
- Short iterations: start with local mock JSON (same contract), then switch to Ktor keeping domain stable.
- Local CI sanity: `:shared:check` and `:composeApp:assembleDebug` for fast feedback; run iOS in Xcode after each increment.

## Commits and Branches
- Small, descriptive commits: one reason per commit (e.g., "domain: add CatalogRepository contract", "data: implement SQLDelight schema").
- Scoped messages: layer prefixes (domain/data/ui/di/docs/chore) for quick history scanning.
- Logical sequence: contracts → mocks → real adapters → UI; each step builds.
- Branching: work on `main` for the challenge scope; in teams, use short‑lived feature branches + PRs.

## Data Flow (offline‑first)
- UI → Use Case → Repository → Local (SQLDelight) and, when available, Remote (Ktor).
- Cache‑first reads; coordinated refresh updates cache and emits new state.
- Images: Kamel (Compose MPP) on Android; iOS displays via SwiftUI side.

## Topology, Attractors, Intensities (conceptual note)
- Do not attempt deep philosophical grounding here; keep the explanation technical.

## Requirements Coverage
- List: title, address, rating; tapping navigates to details.
- Details: title, image, description, rating; “Open in Maps” and “Visit Website” actions per platform.
- Reuse: shared domain/repository; a web UI could reuse entities and use cases later.

## How to Run (quick)
- Gradle sanity: `./gradlew help` and `:shared:check` (generates SQLDelight code).
- Android: `./gradlew :composeApp:assembleDebug` (or Android Studio).
- iOS: open `iosApp/iosApp.xcodeproj` in Xcode and run (optional `BASE_URL` in Info.plist; mock JSON by default).

## Tests and Quality
- Unit (planned/outlined in README): use cases with fakes; mappers; validation of `AppResult/DomainError` paths.
- Stable contracts enable deterministic repository tests (Remote/Local fakes).

## Trade‑offs and Next Steps
- No DI framework in shared: less over‑engineering; later add Koin/Hilt in apps if needed.
- Cache TTL/incremental hydration: hooks in place; implement expiry/refresh policies.
- Observability: minimal logs now; add light tracing and latency/error metrics.
- Accessibility/UX: polish navigation, focus, and sizes (Material / iOS HIG).

## Likely Questions (and Answers)
- Why KMP here? To share domain/data and accelerate multi‑platform delivery while keeping native UIs.
- How do you handle errors? `DomainError` maps Network/Timeout/NotFound/Unknown; UI shows clear states and actions (retry/open offline).
- What if the API changes? Adapt the remote adapter/mappers; domain contracts remain.
- How to switch mock → real API? Set `baseUrl` and use the real `HttpClient`; UI/domain unchanged.

## Quick References
- Code and decisions: see the submodule README.
- [[Desafio Técnico KMP - Requisitos|KMP Technical Challenge — Requirements]] · [[Kotlin]] · [[Compose Multiplatform]] · [[SwiftUI]] · [[Ktor]] · [[SQLDelight]] · [[Koin]] · [[MVVM]]

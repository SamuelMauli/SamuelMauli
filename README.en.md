<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./.github/assets/header-en-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./.github/assets/header-en-light.svg">
  <img alt="Samuel Mauli — full-stack, platform architecture, SRE" src="./.github/assets/header-en-dark.svg" width="100%">
</picture>

[Português](./README.md) · **English** · [Español](./README.es.md)

**[Portfolio](https://samuelmauli.github.io/portifolio/)** · [LinkedIn](https://www.linkedin.com/in/samuelmauli/) · [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com) · Curitiba, Brazil

<p>
  <img alt="22 systems in production" src="https://img.shields.io/badge/22-systems_in_production-E8FF47?style=flat-square&labelColor=080808">
  <img alt="6 apps on both stores" src="https://img.shields.io/badge/6-apps_·_2_stores-E8FF47?style=flat-square&labelColor=080808">
  <img alt="8 businesses, 3 countries" src="https://img.shields.io/badge/8_businesses-3_countries-E8FF47?style=flat-square&labelColor=080808">
  <img alt="measured RTO 38 minutes" src="https://img.shields.io/badge/measured_RTO-38_min_·_proven_PITR-E8FF47?style=flat-square&labelColor=080808">
</p>

---

I take a product from design to production — and then keep it running. I pick the language for the problem: **Go** where idempotency and concurrency matter (payment, billing), **Python** where data and ML govern (PostGIS, XGBoost, vLLM), **Node/TypeScript** where front and back share types. AI only where it moves a number — and preferably **inside the client's perimeter** (ONNX in the process, vLLM on-premise, BYOK). And I'm the SRE of my own operation: EC2 → VPS, ~20 processes behind Caddy, full observability and tested restore, not assumed.

## Results I delivered

| Delivery | Metric |
|---|---|
| Rural environmental compliance (9 federal databases) → signed certificate | **weeks → < 5 min** |
| Document extraction with LLM in banking ERP | **8 min → 10 s** per document |
| Production restore with proven PITR | **1.2 s from target · RTO 38 min** |
| Apps published and maintained on both stores | **6 apps · iOS + Android** |
| Energy invoice capture with contingency integration | **3 sources · zero billing gap** |
| Batch payment with idempotency and immutable trail | **0 duplicate payments** |

---

## Sectors I deliver into

I don't write generic software: every product carries the regulation, the authority and the vocabulary of its sector.

| Sector | Domain | Regulation and official source |
|---|---|---|
| **Agribusiness / ESG** | Environmental certification of rural property, supply-chain traceability | Law 12.651/12 · CAR · PRODES/DETER · IBAMA · INCRA · FUNAI · EUDR |
| **Public sector** | Public tendering, government contracting, funding | Law 14.133/21 · PNCP · Comprasnet · TCU |
| **Financial** | Payment orchestration at scale, reconciliation | PIX (Central Bank) · CNAB 240 · mTLS per bank · immutable trail |
| **Legal / accounting** | Litigation risk provisioning, judicial deposits | CPC 25 / IAS 37 · DataJud/CNJ · PROJUDI · ICP-Brasil A1 |
| **Energy** | Distributed generation by subscription, condominium cost sharing | Utility invoice · tariff flag · individual metering |
| **Occupational health** | Psychosocial risk and HR action plan | NR-01 · COPSOQ III · LGPD with sensitive data |
| **Mobility** | School transport: guardian, driver, route | LGPD with minors · versioned consent in backend |
| **Industry / logistics** | Gatehouse, freight scheduling, access control | NF-e validation · visitor audit trail |

---

## In production

**22 systems live** — the proprietary Doublethree catalogue and the platforms I lead at Grupo Negócios Públicos. The main ones:

**Agribusiness/ESG · Terra-fy** — crosses CAR geometry against 9 federal databases and issues a certificate signed with ICP-Brasil A1, verifiable by QR and hash. Unlocks rural credit, M&A and the European requirement (EUDR).
`FastAPI` `PostGIS` `MapLibre` `pyHanko`

**Public sector · Licitaqui** — reads every tender published in Brazil, surfaces only the winnable ones and **cites the literal passage** that proves each requirement. Go/no-go decision in minutes.
`Next.js` `pgvector` `Playwright` `on-prem LLM`

**Public sector · Aportia** — monitors capital sources and funding and returns an **explainable fit score, criterion by criterion**. BYOK: the analysis never leaves the client's account.
`Next.js` `Prisma` `BM25 + embeddings`

**Financial · PaymentsHub** — ingests the batch from the ERP, pre-validates against the bank's API, **requires human approval with RBAC authority**, and pays via PIX REST or CNAB 240 over SFTP. Per-payment idempotency, immutable trail.
`Go` `PostgreSQL` `River` `MinIO`

**Legal · Lexis Predict** — classifies litigation risk under CPC 25 / IAS 37 with **mandatory per-feature explanation (SHAP)**, 100% on-premise. Below `0.70` confidence, a human decides.
`Python` `XGBoost` `vLLM` `k3s`

**Legal · Lexis Vault** — ties judicial deposits and cases through CNAB 240, DataJud/CNJ and PROJUDI, and **recovers idle funds and unclaimed writs**.
`FastAPI` `Airflow` `Kubernetes`

**Energy · Wave** — **3 integrations in contingency** guarantee invoice capture, with batch reconciliation and utility PDF reading. App on both stores + operation API.
`React Native` `Node.js` `AWS`

**Energy · AmperCondo** — individual metering and **per-unit billing with automatic settlement** (bank slip/PIX). Multi-tenant by schema, idempotent billing.
`Go (hexagonal)` `PostgreSQL` `Asaas`

**Health · OnMe** — measures psychosocial risk via **COPSOQ III** and delivers the action plan in NR-01 hierarchy. Sensitive data stays in-house: embeddings in ONNX inside the Node process.
`NestJS` `React Native` `ONNX Runtime`

**Mobility · Vanlink** — 2 Flutter apps on the stores with **real-time tracking and versioned LGPD consent** for minors.
`Flutter` `APNs` `FCM`

**Industry · LogiSentry** — gatehouse, freight scheduling and visitor in one flow, with **kiosk PWA** and auditable trail. Multi-tenant, 5 languages.
`Turborepo` `NestJS` `Next.js` `Stripe`

**Agencies · Cadência** — white-label mobile **CRM**: each agency on its own subdomain and brand. Pipeline updated in front of the client.
`React Native` `Expo Router` `NestJS`

> **Infrastructure behind it all:** 8 vCPU / 32 GB VPS · ~20 processes across 8 businesses behind Caddy (wildcard DNS-01) · Prometheus/Grafana/Loki · proven PITR.

---

## Principles

- **Sensitive data does not leave the perimeter** — local model (ONNX, vLLM) or BYOK. Privacy is architecture, not a clause.
- **Money demands idempotency and trail** — no reading billed twice, no batch paid twice.
- **Automated decision is auditable** — SHAP on feature, literal quote from tender, offline-verifiable hash. Below threshold, human decides.
- **Backup without tested restore is not backup** — PITR with `recovery_target_time`, RTO measured.
- **Publishing an app is the full cycle** — bump, signed build, upload via ASC API / Play Developer API, without managed pipeline in between.

---

## Stack

| Layer | Tools |
|---|---|
| **Languages** | Go · TypeScript · Python · Java · PHP · Dart · Rust · C++ · Kotlin · Swift · SQL |
| **Backend** | NestJS · Node · FastAPI · Flask · Spring Boot · Hibernate/JPA · Laravel · Slim · Go (hexagonal, River) |
| **Front end** | Next.js · React · Vue · Tailwind · Turborepo · PWA · Vite |
| **Mobile** | React Native (bare + Expo Router) · Flutter · SwiftUI · Jetpack Compose · APNs · FCM · ASC API + Play Developer API |
| **Data** | PostgreSQL · PostGIS · pgvector · MySQL · MongoDB · Redis · DuckDB · Redshift · Prisma · Drizzle · Airflow |
| **AI / ML** | XGBoost · LightGBM · SHAP · scikit-learn · TensorFlow · PyTorch · OpenCV · ONNX Runtime · vLLM · Ollama · BGE-M3 · RAG (BM25 + embeddings) · Claude / GPT / Gemini / Groq |
| **Infra / SRE** | Docker · Kubernetes / k3s · Caddy · Nginx · PM2 · GitHub Actions · AWS · Cloudflare · Prometheus · Grafana · Loki · Alertmanager · PITR |
| **Integrations** | PIX · CNAB 240 · mTLS · SFTP · Asaas · Stripe · Banco Inter · RabbitMQ · WebSocket · ICP-Brasil A1 · DataJud/CNJ · PNCP/Comprasnet |
| **Quality** | Playwright · Jest · Vitest · pytest · JUnit |

---

## On GitHub

| Repository | |
|---|---|
| [**GreenChain**](https://github.com/SamuelMauli/GreenChain-Backend) | Supply-chain traceability on Hyperledger Fabric + geoprocessing for EUDR compliance ([front](https://github.com/SamuelMauli/GreenChain-Frontend)) |
| [**Quimera**](https://github.com/SamuelMauli/Quimera) | Chess engine in C++ with opponent predictive modeling |
| [**Rust-LavaLamp**](https://github.com/SamuelMauli/Rust-LavaLamp) | Cryptographic entropy from images, in the vein of Cloudflare's LavaRand |
| [**Curitiba-Verde**](https://github.com/SamuelMauli/Curitiba-Verde) | Deforestation mapping through computer vision and NDVI |
| [**LibrasNow**](https://github.com/SamuelMauli/LibrasNow) | Real-time sign language translation at the edge |
| [**wselect-pro**](https://github.com/SamuelMauli/wselect-pro) | LMS in production, deployed via GitHub Actions |
| [**EBANX Take-Home**](https://github.com/SamuelMauli/EBANX-Take-Home-API) | Banking API in PHP 8.2 + Slim 4 |

---

## Career

```
2025 →      Mid-level Developer · Grupo Negócios Públicos (Vanlink)
            SGI + CRM, 2 Flutter apps on the stores, payment orchestration,
            LLM document extraction: 8 min → 10 s per document

2024 →      Developer & Consultant · Doublethree
            22 systems in production, 6 apps on the stores,
            AWS → VPS migration and the entire operation kept running

2024–2025   Java & PHP Developer · Meisters Solutions
            Spring Boot and Laravel, ETL/ELT for pharma,
            BlauSight (generative AI) and Ballesol CareAI (Spain)

2023–2024   IT Support Agent · Positivo Tecnologia — ITIL, SLA, IMC backlog
2023        Oracle Consultant · TRI CS Inc. — OIC, BI Publisher, REST/SOAP
2022–2023   N1 Support · ICI Curitiba — City of Curitiba, NOC and field
```

Trilingual (Portuguese · English · Spanish), with software in production in Brazil, Spain and Mexico.

---

Open to challenging projects and partnerships — [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com)

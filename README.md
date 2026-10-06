<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./.github/assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./.github/assets/header-light.svg">
  <img alt="Samuel Mauli — full-stack, arquitetura de plataforma, SRE" src="./.github/assets/header-dark.svg" width="100%">
</picture>

**Português** · [English](./README.en.md) · [Español](./README.es.md)

**[Portfólio](https://samuelmauli.github.io/portifolio/)** · [LinkedIn](https://www.linkedin.com/in/samuelmauli/) · [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com) · Curitiba, PR

<p>
  <img alt="22 sistemas em produção" src="https://img.shields.io/badge/22-sistemas_em_produção-E8FF47?style=flat-square&labelColor=080808">
  <img alt="6 apps em duas lojas" src="https://img.shields.io/badge/6-apps_·_2_lojas-E8FF47?style=flat-square&labelColor=080808">
  <img alt="8 negócios, 3 países" src="https://img.shields.io/badge/8_negócios-3_países-E8FF47?style=flat-square&labelColor=080808">
  <img alt="RTO medido 38 minutos" src="https://img.shields.io/badge/RTO-38min_·_PITR_provado-E8FF47?style=flat-square&labelColor=080808">
</p>

---

Levo produto do desenho à produção — e mantenho no ar. Escolho a linguagem pelo problema: **Go** onde idempotência e concorrência pesam (pagamento, faturamento), **Python** onde dados e ML mandam (PostGIS, XGBoost, vLLM), **Node/TypeScript** onde front e back compartilham tipo. IA só onde move número — e de preferência **dentro do perímetro do cliente** (ONNX no processo, vLLM on-premise, BYOK). E sou o SRE da própria operação: EC2 → VPS, ~20 processos atrás de Caddy, observabilidade completa e restore testado, não presumido.

## Resultados que entreguei

| Entrega | Número |
|---|---|
| Conformidade ambiental rural (9 bases federais) → certificado assinado | **semanas → < 5 min** |
| Extração documental com LLM no ERP bancário | **8 min → 10 s** por documento |
| Restore de produção com PITR provado | **a 1,2 s do alvo · RTO 38 min** |
| Apps publicados e mantidos nas duas lojas | **6 apps · iOS + Android** |
| Captura de fatura de energia com integração em contingência | **3 fontes · zero gap de faturamento** |
| Pagamento em lote com idempotência e trilha imutável | **0 pagamento em duplicidade** |

---

## Setores em que entrego

Não escrevo software genérico: cada produto carrega a norma, o órgão e o vocabulário do seu setor.

| Setor | Domínio | Regulação / fonte oficial |
|---|---|---|
| **Agro / ESG** | Certificação socioambiental rural, rastreabilidade de cadeia | Lei 12.651/12 · CAR · PRODES/DETER · IBAMA · INCRA · FUNAI · EUDR |
| **Setor público** | Licitação, contratação pública, fomento | Lei 14.133/21 · PNCP · Comprasnet · TCU |
| **Financeiro** | Orquestração de pagamento em escala, conciliação | PIX (Bacen) · CNAB 240 · mTLS por banco · trilha imutável |
| **Jurídico/contábil** | Provisão de risco processual, depósito judicial | CPC 25 / IAS 37 · DataJud/CNJ · PROJUDI · ICP-Brasil A1 |
| **Energia** | Geração distribuída por assinatura, rateio em condomínio | Fatura de distribuidora · bandeira tarifária · medição individual |
| **Saúde ocupacional** | Risco psicossocial e plano de ação de RH | NR-01 · COPSOQ III · LGPD com dado sensível |
| **Mobilidade** | Transporte escolar: responsável, condutor, rota | LGPD com menor · consentimento versionado no backend |
| **Indústria/logística** | Portaria, agendamento de carga, controle de acesso | Validação de NF-e · trilha de visitante |

---

## Em produção

**22 sistemas no ar** — o catálogo proprietário da **Doublethree** e as plataformas que lidero no Grupo Negócios Públicos. Os principais:

**Agro/ESG · Terra-fy** — cruza a geometria do CAR contra 9 bases federais e emite certificado assinado com ICP-Brasil A1, verificável por QR e hash. Destrava crédito rural, M&A e a exigência europeia (EUDR).
`FastAPI` `PostGIS` `MapLibre` `pyHanko`

**Setor público · Licitaqui** — lê todo edital publicado no Brasil, entrega só o que a empresa pode vencer e **cita o trecho literal** que prova cada exigência. Decisão de participar em minutos.
`Next.js` `pgvector` `Playwright` `LLM on-prem`

**Setor público · Aportia** — monitora fontes de capital e fomento e devolve **score de fit explicável, critério a critério**. BYOK: a análise nunca sai da conta do cliente.
`Next.js` `Prisma` `BM25 + embeddings`

**Financeiro · PaymentsHub** — recebe o lote do ERP, pré-valida na API do banco, **exige aprovação humana com alçada (RBAC)** e paga por PIX REST ou CNAB 240 via SFTP. Idempotência por pagamento, trilha imutável.
`Go` `PostgreSQL` `River` `MinIO`

**Jurídico · Lexis Predict** — classifica risco processual sob CPC 25 / IAS 37 com **explicação obrigatória por feature (SHAP)**, 100% on-premise. Abaixo de `0,70` de confiança, decide humano.
`Python` `XGBoost` `vLLM` `k3s`

**Jurídico · Lexis Vault** — amarra depósito judicial e processo via CNAB 240, DataJud/CNJ e PROJUDI, e **recupera valor parado e alvará não sacado**.
`FastAPI` `Airflow` `Kubernetes`

**Energia · Wave** — **3 integrações em contingência** garantem a captura da fatura, com reconciliação em lote e leitura de PDF de concessionária. App nas duas lojas + API da operação.
`React Native` `Node.js` `AWS`

**Energia · AmperCondo** — medição individualizada e **cobrança por unidade com baixa automática** (boleto/PIX). Multi-tenant por schema, faturamento idempotente.
`Go (hexagonal)` `PostgreSQL` `Asaas`

**Saúde · OnMe** — mede risco psicossocial pela **COPSOQ III** e entrega o plano de ação na hierarquia da NR-01. Dado sensível nunca sai: embeddings em ONNX no próprio processo Node.
`NestJS` `React Native` `ONNX Runtime`

**Mobilidade · Vanlink** — 2 apps Flutter nas lojas com **tracking em tempo real e consentimento de LGPD versionado** para menor de idade.
`Flutter` `APNs` `FCM`

**Indústria · LogiSentry** — portaria, agendamento de carga e visitante num só fluxo, com **PWA de totem** e trilha auditável. Multi-tenant, 5 idiomas.
`Turborepo` `NestJS` `Next.js` `Stripe`

**Agências · Cadência** — CRM móvel **white-label**: cada agência pelo próprio subdomínio e marca. Pipeline atualizado na frente do cliente.
`React Native` `Expo Router` `NestJS`

> **Infra que sustenta tudo:** VPS 8 vCPU / 32 GB · ~20 processos de 8 negócios atrás de Caddy (wildcard DNS-01) · Prometheus/Grafana/Loki · PITR provado.

---

## Princípios

- **Dado sensível não sai do perímetro** — modelo local (ONNX, vLLM) ou BYOK. Privacidade é arquitetura, não cláusula.
- **Dinheiro exige idempotência e trilha** — nenhuma leitura cobrada duas vezes, nenhum lote pago duas vezes.
- **Decisão automatizada é auditável** — SHAP na feature, citação literal do edital, hash offline. Abaixo do limiar, decide humano.
- **Backup sem restore testado não é backup** — PITR com `recovery_target_time`, RTO medido.
- **Publicar app é ciclo completo** — bump, build assinado, upload por ASC API / Play Developer API, sem pipeline gerenciado no meio.

---

## Stack

| Camada | Ferramentas |
|---|---|
| **Linguagens** | Go · TypeScript · Python · Java · PHP · Dart · Rust · C++ · Kotlin · Swift · SQL |
| **Backend** | NestJS · Node · FastAPI · Flask · Spring Boot · Hibernate/JPA · Laravel · Slim · Go (hexagonal, River) |
| **Front** | Next.js · React · Vue · Tailwind · Turborepo · PWA · Vite |
| **Mobile** | React Native (bare + Expo Router) · Flutter · SwiftUI · Jetpack Compose · APNs · FCM · ASC + Play Developer API |
| **Dados** | PostgreSQL · PostGIS · pgvector · MySQL · MongoDB · Redis · DuckDB · Redshift · Prisma · Drizzle · Airflow |
| **IA / ML** | XGBoost · LightGBM · SHAP · scikit-learn · TensorFlow · PyTorch · OpenCV · ONNX Runtime · vLLM · Ollama · BGE-M3 · RAG (BM25 + embeddings) · Claude / GPT / Gemini / Groq |
| **Infra / SRE** | Docker · Kubernetes / k3s · Caddy · Nginx · PM2 · GitHub Actions · AWS · Cloudflare · Prometheus · Grafana · Loki · Alertmanager · PITR |
| **Integrações** | PIX · CNAB 240 · mTLS · SFTP · Asaas · Stripe · Banco Inter · RabbitMQ · WebSocket · ICP-Brasil A1 · DataJud/CNJ · PNCP/Comprasnet |
| **Qualidade** | Playwright · Jest · Vitest · pytest · JUnit |

---

## No GitHub

| Repositório | |
|---|---|
| [**GreenChain**](https://github.com/SamuelMauli/GreenChain-Backend) | Rastreabilidade em Hyperledger Fabric + geoprocessamento para conformidade EUDR ([front](https://github.com/SamuelMauli/GreenChain-Frontend)) |
| [**Quimera**](https://github.com/SamuelMauli/Quimera) | Engine de xadrez em C++ com modelagem preditiva do oponente |
| [**Rust-LavaLamp**](https://github.com/SamuelMauli/Rust-LavaLamp) | Entropia criptográfica por imagem, na linha do LavaRand da Cloudflare |
| [**Curitiba-Verde**](https://github.com/SamuelMauli/Curitiba-Verde) | Mapeamento de desmatamento por visão computacional e NDVI |
| [**LibrasNow**](https://github.com/SamuelMauli/LibrasNow) | Tradução de língua de sinais em tempo real na borda |
| [**wselect-pro**](https://github.com/SamuelMauli/wselect-pro) | LMS em produção, deploy por GitHub Actions |
| [**EBANX Take-Home**](https://github.com/SamuelMauli/EBANX-Take-Home-API) | API bancária em PHP 8.2 + Slim 4 |

---

## Trajetória

```
2025 →      Desenvolvedor Pleno · Grupo Negócios Públicos (Vanlink)
            SGI + CRM, 2 apps Flutter nas lojas, orquestração de pagamento,
            extração documental com LLM: 8 min → 10 s por documento

2024 →      Developer & Consultor · Doublethree
            22 sistemas em produção, 6 apps nas lojas,
            migração AWS → VPS e a operação inteira em pé

2024–2025   Java & PHP Developer · Meisters Solutions
            Spring Boot e Laravel, ETL/ELT para farmacêutica,
            BlauSight (IA generativa) e Ballesol CareAI (Espanha)

2023–2024   Agente de Suporte TI · Positivo Tecnologia — ITIL, SLA, backlog da IMC
2023        Consultor Oracle · TRI CS Inc. — OIC, BI Publisher, REST/SOAP
2022–2023   Suporte N1 · ICI Curitiba — Prefeitura de Curitiba, NOC e campo
```

Trilíngue (PT · EN · ES), com software em produção no Brasil, na Espanha e no México.

---

Aberto a projeto desafiador e parceria — [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com)

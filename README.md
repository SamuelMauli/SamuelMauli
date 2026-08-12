<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./.github/assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./.github/assets/header-light.svg">
  <img alt="Samuel Mauli — full-stack, arquitetura de plataforma, SRE" src="./.github/assets/header-dark.svg" width="100%">
</picture>

**[Portfólio](https://samuelmauli.github.io/portifolio/)** · [LinkedIn](https://www.linkedin.com/in/samuelmauli/) · [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com) · Curitiba, PR · PT / EN / ES

---

Levo produto do desenho à produção — e depois mantenho no ar.

Escolho a linguagem pelo problema, não pela moda: **Go** onde idempotência e concorrência importam (orquestração bancária, faturamento), **Python** onde o ecossistema de dados e ML manda (PostGIS, XGBoost, vLLM), **Node/TypeScript** onde o time inteiro compartilha tipo com o front. No mobile, **React Native** e **Flutter**, com seis apps publicados nas duas lojas — incluindo os casos difíceis: APNs direto quando o Firebase corrompeu no iOS, build assinado sem pipeline gerenciado.

Aplico IA onde ela resolve algo mensurável, e de preferência **dentro do perímetro do cliente**: embeddings multilíngues em ONNX Runtime no próprio processo Node, LLM servido por vLLM on-premise, XGBoost com SHAP obrigatório quando a decisão vai para auditoria.

Também sou o SRE da própria operação: migrei tudo de EC2 para VPS, hoje ~20 processos de oito negócios atrás de Caddy, com Prometheus/Grafana/Loki e **PITR provado** — restore parou a `1,2s` do alvo, RTO medido em `38min`. Backup sem restore testado eu não chamo de backup.

---

## Stack

| Camada | Ferramentas |
|---|---|
| **Linguagens** | Go · TypeScript · Python · Java · PHP · Dart · Rust · C++ · Kotlin · Swift · SQL |
| **Backend** | NestJS · Node · FastAPI · Flask · Spring Boot · Hibernate/JPA · Laravel · Slim · Go (hexagonal, River) |
| **Front-end** | Next.js · React · Vue · Tailwind · Turborepo · PWA · Vite |
| **Mobile** | React Native (bare + Expo Router) · Flutter · SwiftUI · Jetpack Compose · APNs · FCM · ASC API + Play Developer API |
| **Dados** | PostgreSQL · PostGIS · pgvector · MySQL · MongoDB · Redis · DuckDB · Redshift · Prisma · Drizzle · Airflow |
| **IA / ML** | XGBoost · LightGBM · SHAP · scikit-learn · TensorFlow · PyTorch · OpenCV · ONNX Runtime · vLLM · Ollama · BGE-M3 · RAG (BM25 + embeddings) · Claude / GPT / Gemini / Groq |
| **Infra / SRE** | Docker · Kubernetes e k3s · Caddy · Nginx · PM2 · GitHub Actions · AWS · Cloudflare · Prometheus · Grafana · Loki · Alertmanager · PITR |
| **Integrações** | PIX · CNAB 240 · mTLS · SFTP · Asaas · Stripe · Banco Inter · RabbitMQ · WebSocket · ICP-Brasil A1 · DataJud/CNJ · PNCP / Comprasnet |
| **Qualidade** | Playwright · Jest · Vitest · pytest · JUnit |

---

## Em produção

Dez produtos proprietários que arquitetei, construí e mantenho no ar.

| Produto | O que resolve | Stack | Escala |
|---|---|---|---|
| **Terra-fy** | Certificado socioambiental de imóvel rural cruzando a geometria do CAR contra nove bases federais. PDF assinado com ICP-Brasil A1, QR e hash verificáveis, em menos de 5 min após o pagamento. | FastAPI · PostGIS · MapLibre · pyHanko | `65k` linhas · cobertura nacional |
| **Licitaqui** | Agente que lê os editais publicados no Brasil e entrega só os que a empresa pode ganhar, citando o trecho literal que prova cada afirmação. Análise jurídica multi-passe e jurisprudência do TCU. | Next.js · pgvector · Playwright · LLM on-prem | `79k` linhas · 51 entidades · 68 rotas |
| **Wave Energia** | Energia por assinatura: app nas duas lojas mais a API da operação. Três integrações de distribuidora capturando fatura por contingência. | React Native · Node.js · AWS | `184k` linhas · iOS + Android |
| **OnMe** | Saúde mental corporativa em três superfícies sobre um backend só. Embeddings rodam em ONNX dentro do processo Node — nenhuma chamada a IA de terceiro. COPSOQ III, plano de ação na NR-01. | NestJS · React Native · ONNX Runtime | `96k` linhas · 4 peças |
| **PaymentsHub** | Orquestrador de pagamento bancário em escala: pré-validação no banco, aprovação humana com RBAC, PIX REST ou lote CNAB 240 por SFTP auditado. Idempotência por pagamento, mTLS por conexão. | Go · PostgreSQL · River · MinIO | 21 tabelas · 50 rotas |
| **Lexis Predict** | Risco processual para provisão contábil sob CPC 25 / IAS 37 com IA 100% on-premise. SHAP obrigatório; confiança abaixo de `0,70` vai para revisão humana. | Python · XGBoost · vLLM · k3s | `50k` linhas |
| **Lexis Vault** | O extrato fala em ID de depósito, o tribunal fala em nº de processo — o Vault amarra os dois. CNAB 240 por SFTP, DataJud/CNJ e PROJUDI, motor de conciliação em quatro camadas. | FastAPI · Airflow · Kubernetes | 21 tabelas |
| **Aportia** | Monitora fontes de capital e fomento e calcula score de fit explicável critério a critério. BYOK: a chave de LLM é do cliente, a análise nunca sai da conta dele. | Next.js · Prisma · BM25 + embeddings | 28 entidades · 50 rotas |
| **LogiSentry** | Agendamento de caminhão, visitante e sala numa portaria só, com PWA de totem no tablet da recepção. | Turborepo · NestJS · Next.js · Stripe | 20 entidades · 35 telas · 5 idiomas |
| **AmperCondo** | Acaba com rateio de energia por fração ideal: medidor por unidade, cobrança individual com baixa automática. Multi-tenant por schema, faturamento idempotente. | Go (hexagonal) · PostgreSQL · Asaas | 15 tabelas · event bus |
| **Cadência** | CRM móvel white-label nas duas lojas: cada agência entra pelo próprio subdomínio, com a própria marca. | React Native · Expo Router · NestJS | 29 telas · 9 domínios |
| **Vanlink** | Dois apps Flutter de transporte escolar em produção — pais e condutores. Tracking em tempo real, gate de consentimento LGPD servido pelo backend, geocoding com validação cruzada. | Flutter · APNs · FCM | 2 apps · App Store + Play |

**Infra que sustenta tudo:** um VPS de 8 vCPU / 32 GB, ~20 processos de oito negócios atrás de Caddy com wildcard por DNS-01, observabilidade completa e PITR provado.

---

## No GitHub

| Repositório | |
|---|---|
| [**Quimera**](https://github.com/SamuelMauli/Quimera) | Engine de xadrez em C++ com modelagem preditiva do oponente |
| [**Rust-LavaLamp**](https://github.com/SamuelMauli/Rust-LavaLamp) | Entropia criptográfica por imagem, na linha do LavaRand da Cloudflare |
| [**GreenChain**](https://github.com/SamuelMauli/GreenChain-Backend) | Rastreabilidade blockchain + geoprocessamento para conformidade EUDR ([front](https://github.com/SamuelMauli/GreenChain-Frontend)) |
| [**Curitiba-Verde**](https://github.com/SamuelMauli/Curitiba-Verde) | Mapeamento de desmatamento por visão computacional e NDVI |
| [**LibrasNow**](https://github.com/SamuelMauli/LibrasNow) | Tradução de língua de sinais em tempo real na borda |
| [**wselect-pro**](https://github.com/SamuelMauli/wselect-pro) | LMS em produção, `106k` linhas, deploy por GitHub Actions |
| [**EBANX Take-Home**](https://github.com/SamuelMauli/EBANX-Take-Home-API) | API bancária em PHP 8.2 + Slim 4 |

---

## Trajetória

```
2025 →      Desenvolvedor Pleno · Grupo Negócios Públicos (Vanlink)
            SGI + CRM, dois apps Flutter nas lojas, orquestração de pagamento,
            extração documental com LLM: 8 min → 10 s por documento

2024 →      Developer & Consultor · Doublethree
            Dez produtos proprietários do desenho à produção, seis apps nas lojas,
            migração AWS → VPS e a operação inteira em pé

2024–2025   Java & PHP Developer · Meisters Solutions
            Spring Boot e Laravel, pipelines ETL/ELT para farmacêutica,
            BlauSight (IA generativa) e Ballesol CareAI

2023–2024   Agente de Suporte TI · Positivo Tecnologia — ITIL, SLA, backlog da IMC
2023        Consultor Oracle · TRI CS Inc. — OIC, BI Publisher, REST/SOAP
2022–2023   Suporte N1 · ICI Curitiba — Prefeitura de Curitiba, NOC e campo
```

---

<div align="center">
<img height="150" alt="" src="https://github-readme-stats.vercel.app/api?username=SamuelMauli&show_icons=true&hide_border=true&hide_title=true&bg_color=00000000&icon_color=9FB300&text_color=8A8A8A&ring_color=9FB300&count_private=true&include_all_commits=true"/>
<img height="150" alt="" src="https://github-readme-stats.vercel.app/api/top-langs/?username=SamuelMauli&layout=compact&hide_border=true&hide_title=true&bg_color=00000000&text_color=8A8A8A&langs_count=8"/>
</div>

---

Aberto a projeto desafiador e parceria — [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com)

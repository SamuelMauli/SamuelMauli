<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./.github/assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./.github/assets/header-light.svg">
  <img alt="Samuel Mauli — full-stack, arquitetura de plataforma, SRE" src="./.github/assets/header-dark.svg" width="100%">
</picture>

**Português** · [English](./README.en.md) · [Español](./README.es.md)

**[Portfólio](https://samuelmauli.github.io/portifolio/)** · [LinkedIn](https://www.linkedin.com/in/samuelmauli/) · [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com) · Curitiba, PR

---

Levo produto do desenho à produção — e depois mantenho no ar.

Escolho a linguagem pelo problema, não pela moda: **Go** onde idempotência e concorrência importam (orquestração bancária, faturamento), **Python** onde o ecossistema de dados e ML manda (PostGIS, XGBoost, vLLM), **Node/TypeScript** onde o time inteiro compartilha tipo com o front. No mobile, **React Native** e **Flutter**, com seis apps publicados nas duas lojas — incluindo os casos difíceis: APNs direto quando o Firebase corrompeu no iOS, build assinado sem pipeline gerenciado.

Aplico IA onde ela resolve algo mensurável, e de preferência **dentro do perímetro do cliente**: embeddings multilíngues em ONNX Runtime no próprio processo Node, LLM servido por vLLM on-premise, XGBoost com SHAP obrigatório quando a decisão vai para auditoria.

Também sou o SRE da própria operação: migrei tudo de EC2 para VPS, hoje ~20 processos de oito negócios atrás de Caddy, com Prometheus/Grafana/Loki e **PITR provado** — restore parou a `1,2s` do alvo, RTO medido em `38min`. Backup sem restore testado eu não chamo de backup.

---

## Setores em que entrego

Não escrevo software genérico: cada produto abaixo carrega a norma, o órgão e o vocabulário do seu setor.

| Setor | Domínio de negócio | Regulação e fonte oficial com que lido |
|---|---|---|
| **Agronegócio / ESG** | Certificação socioambiental de imóvel rural, rastreabilidade de cadeia | Código Florestal (Lei 12.651/12) · CAR · PRODES / DETER · IBAMA · INCRA · FUNAI · ICMBio · EUDR |
| **Setor público** | Licitação, contratação pública, capital e fomento | Lei 14.133/21 · PNCP · Comprasnet · jurisprudência do TCU |
| **Financeiro** | Orquestração de pagamento em escala, conciliação bancária | PIX (Bacen) · CNAB 240 · mTLS por conexão bancária · trilha de auditoria imutável |
| **Jurídico e contábil** | Provisão de risco processual, depósito judicial e alvará | CPC 25 / IAS 37 · DataJud/CNJ · PROJUDI · assinatura ICP-Brasil A1 |
| **Energia** | Geração distribuída por assinatura, rateio em condomínio | Fatura de distribuidora · bandeira tarifária · crédito de energia · medição individualizada |
| **Saúde ocupacional** | Risco psicossocial e plano de ação de RH | NR-01 · taxonomia COPSOQ III · LGPD com dado sensível |
| **Mobilidade** | Transporte escolar: responsável, condutor e rota | LGPD com menor de idade · consentimento versionado servido pelo backend |
| **Indústria e logística** | Portaria, agendamento de carga e controle de acesso | Validação de NF-e · credenciamento e trilha de visitante |

---

## Em produção

Vinte e dois sistemas em produção hoje: o catálogo proprietário da Doublethree mais as plataformas que lidero no Grupo Negócios Públicos. Doze deles em detalhe abaixo.

### Agronegócio e ESG

**Terra-fy** — Produtor rural e trading precisam **provar conformidade ambiental para vender, financiar e exportar**, e hoje isso custa semanas de consultoria. A plataforma cruza a geometria oficial do CAR contra nove bases federais e emite o certificado em menos de 5 minutos após o pagamento, assinado com ICP-Brasil A1 e verificável por QR e hash. Destrava crédito rural, due diligence de M&A e a exigência de rastreabilidade do mercado europeu.
`FastAPI` `PostGIS` `MapLibre` `pyHanko`

### Setor público

**Licitaqui** — Empresa que vende para o governo queima hora cara de equipe lendo edital que não tem chance de ganhar. O agente lê continuamente o que é publicado no Brasil, entrega só o que a empresa pode vencer e **cita o trecho literal que prova cada exigência** — decisão de participar em minutos, menos inabilitação por detalhe de habilitação e risco de impugnação mapeado antes da proposta.
`Next.js` `pgvector` `Playwright` `LLM on-prem`

**Aportia** — Quem busca capital ou fomento não sabe onde tem chance real e perde prazo em edital errado. A plataforma monitora as fontes oficiais e devolve um **score de fit explicável critério a critério**. A chave de LLM é do próprio cliente (BYOK): a análise do plano de negócio nunca sai da conta dele.
`Next.js` `Prisma` `BM25 + embeddings`

### Financeiro

**PaymentsHub** — Empresa que paga centenas de fornecedores por dia opera em planilha e internet banking, e um pagamento em duplicidade vira prejuízo direto. O orquestrador recebe o lote do ERP, pré-valida contra a API do banco, **exige aprovação humana com alçada (RBAC)** e executa por PIX REST ou lote CNAB 240 via SFTP auditado. Idempotência por pagamento e trilha imutável de ponta a ponta.
`Go` `PostgreSQL` `River` `MinIO`

### Jurídico e contábil

**Lexis Predict** — Provisão de contingência costuma sair do feeling do jurídico, e o auditor cobra critério. O modelo classifica risco processual sob CPC 25 / IAS 37 com **explicação obrigatória por feature (SHAP)** e roda 100% on-premise: nenhuma peça processual sai para IA de terceiro. Abaixo de `0,70` de confiança, quem decide é humano.
`Python` `XGBoost` `vLLM` `k3s`

**Lexis Vault** — Depósito judicial some entre o banco e o tribunal: o extrato fala em ID de depósito, o processo fala em número. O Vault amarra os dois com CNAB 240 por SFTP, DataJud/CNJ e PROJUDI, e **recupera valor parado e alvará não sacado** — fechamento de mês sem garimpo manual.
`FastAPI` `Airflow` `Kubernetes`

### Energia

**Wave Energia** — Assinante quer o desconto na conta e a operadora precisa faturar certo, mas o dado depende de distribuidora que cai. **Três integrações em contingência** garantem a captura da fatura, com reconciliação em lote, leitura de PDF de concessionária, bandeira tarifária e crédito de energia. App nas duas lojas mais a API da operação.
`React Native` `Node.js` `AWS`

**AmperCondo** — Rateio por fração ideal faz quem consome pouco pagar pelo vizinho, e a discussão volta toda assembleia. Medição individualizada, tarifa configurável e **cobrança por unidade com baixa automática** por boleto ou PIX. Multi-tenant por schema e faturamento idempotente: a mesma leitura nunca é cobrada duas vezes.
`Go (hexagonal)` `PostgreSQL` `Asaas`

### Saúde ocupacional

**OnMe** — A NR-01 passou a exigir gestão de risco psicossocial e o RH não tem instrumento para isso. A plataforma mede pela taxonomia **COPSOQ III**, entrega o plano de ação na hierarquia da norma e mantém o dado sensível dentro do servidor: os embeddings rodam em ONNX no próprio processo Node, sem nenhuma chamada a IA de terceiro. App do colaborador, painel do RH e motor de ML sobre um backend só.
`NestJS` `React Native` `ONNX Runtime`

### Mobilidade

**Vanlink** — O responsável quer saber onde a van está agora, e a empresa precisa provar consentimento de LGPD envolvendo menor de idade. Dois apps Flutter em produção nas duas lojas com **tracking em tempo real, consentimento versionado servido pelo backend** e geocoding com validação cruzada de endereço de escola. Menos ligação para o escritório, menos risco jurídico.
`Flutter` `APNs` `FCM`

### Indústria, logística e agências

**LogiSentry** — Portaria industrial trava caminhão na fila e anota visitante em papel. Agendamento de carga, visitante e sala numa portaria só, com **PWA de totem no tablet da recepção** e trilha auditável de quem entrou. Multi-tenant, cinco idiomas.
`Turborepo` `NestJS` `Next.js` `Stripe`

**Cadência** — Agência opera fora do escritório e perde follow-up até voltar para o CRM. CRM móvel nas duas lojas, **white-label**: cada agência entra pelo próprio subdomínio, com a própria marca. Pipeline atualizado na frente do cliente, não no fim do dia.
`React Native` `Expo Router` `NestJS`

**Infra que sustenta tudo:** um VPS de 8 vCPU / 32 GB, ~20 processos de oito negócios atrás de Caddy com wildcard por DNS-01, observabilidade completa e PITR provado.

---

## Como eu trabalho

- **Dado sensível não sai do perímetro.** Saúde ocupacional, provisão contábil e análise de edital rodam com modelo local — ONNX no próprio processo, vLLM on-premise, ou BYOK com a chave do cliente. Privacidade como arquitetura, não como cláusula de contrato.
- **Dinheiro exige idempotência e trilha.** Nenhuma leitura é cobrada duas vezes, nenhum lote é pago duas vezes: chave de idempotência por pagamento, aprovação humana com RBAC e evento imutável do início ao fim.
- **Decisão automatizada precisa ser auditável.** Se a saída vai para uma auditoria, ela vem com explicação — SHAP nas features, citação literal do trecho do edital, hash verificável offline. Abaixo do limiar de confiança, quem decide é humano.
- **Backup sem restore testado não é backup.** PITR provado com `recovery_target_time`, RTO medido, não presumido.
- **Publicar app é ciclo completo.** Bump de versão, build assinado, upload por ASC API e Play Developer API, submissão à revisão — sem pipeline gerenciado no meio.

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

## No GitHub

| Repositório | |
|---|---|
| [**Quimera**](https://github.com/SamuelMauli/Quimera) | Engine de xadrez em C++ com modelagem preditiva do oponente |
| [**Rust-LavaLamp**](https://github.com/SamuelMauli/Rust-LavaLamp) | Entropia criptográfica por imagem, na linha do LavaRand da Cloudflare |
| [**GreenChain**](https://github.com/SamuelMauli/GreenChain-Backend) | Rastreabilidade blockchain + geoprocessamento para conformidade EUDR ([front](https://github.com/SamuelMauli/GreenChain-Frontend)) |
| [**Curitiba-Verde**](https://github.com/SamuelMauli/Curitiba-Verde) | Mapeamento de desmatamento por visão computacional e NDVI |
| [**LibrasNow**](https://github.com/SamuelMauli/LibrasNow) | Tradução de língua de sinais em tempo real na borda |
| [**wselect-pro**](https://github.com/SamuelMauli/wselect-pro) | LMS em produção, deploy por GitHub Actions |
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
            BlauSight (IA generativa) e Ballesol CareAI (Espanha)

2023–2024   Agente de Suporte TI · Positivo Tecnologia — ITIL, SLA, backlog da IMC
2023        Consultor Oracle · TRI CS Inc. — OIC, BI Publisher, REST/SOAP
2022–2023   Suporte N1 · ICI Curitiba — Prefeitura de Curitiba, NOC e campo
```

Trilíngue: português, inglês e espanhol — com software em produção no Brasil, na Espanha e no México.

---

Aberto a projeto desafiador e parceria — [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com)

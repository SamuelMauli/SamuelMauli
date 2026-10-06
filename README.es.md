<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./.github/assets/header-es-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./.github/assets/header-es-light.svg">
  <img alt="Samuel Mauli — full-stack, arquitectura de plataforma, SRE" src="./.github/assets/header-es-dark.svg" width="100%">
</picture>

[Português](./README.md) · [English](./README.en.md) · **Español**

**[Portafolio](https://samuelmauli.github.io/portifolio/)** · [LinkedIn](https://www.linkedin.com/in/samuelmauli/) · [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com) · Curitiba, Brasil

<p>
  <img alt="22 sistemas en producción" src="https://img.shields.io/badge/22-sistemas_en_producción-E8FF47?style=flat-square&labelColor=080808">
  <img alt="6 apps en dos tiendas" src="https://img.shields.io/badge/6-apps_·_2_tiendas-E8FF47?style=flat-square&labelColor=080808">
  <img alt="8 negocios, 3 países" src="https://img.shields.io/badge/8_negocios-3_países-E8FF47?style=flat-square&labelColor=080808">
  <img alt="RTO medido 38 minutos" src="https://img.shields.io/badge/RTO-38min_·_PITR_probado-E8FF47?style=flat-square&labelColor=080808">
</p>

---

Llevo producto del diseño a producción — y después lo mantengo en pie. Elijo lenguaje por el problema: **Go** donde la idempotencia y concurrencia pesan (pago, facturación), **Python** donde mandan datos y ML (PostGIS, XGBoost, vLLM), **Node/TypeScript** donde front y back comparten tipo. IA sólo donde mueve número — y de preferencia **dentro del perímetro del cliente** (ONNX en proceso, vLLM on-premise, BYOK). Y soy el SRE de la propia operación: EC2 → VPS, ~20 procesos detrás de Caddy, observabilidad completa y restore probado, no presumido.

## Resultados que entregué

| Entrega | Número |
|---|---|
| Conformidad ambiental rural (9 bases federales) → certificado firmado | **semanas → < 5 min** |
| Extracción documental con LLM en ERP bancario | **8 min → 10 s** por documento |
| Restore de producción con PITR probado | **a 1,2 s del objetivo · RTO 38 min** |
| Apps publicadas y mantenidas en las dos tiendas | **6 apps · iOS + Android** |
| Captura de factura de energía con integración en contingencia | **3 fuentes · cero gap de facturación** |
| Pago en lote con idempotencia y trilha inmutable | **0 pago en duplicidad** |

---

## Sectores en los que entrego

No escribo software genérico: cada producto carga la norma, el órgano y el vocabulario de su sector.

| Sector | Dominio | Regulación / fuente oficial |
|---|---|---|
| **Agro / ESG** | Certificación socioambiental rural, trazabilidad de cadena | Ley 12.651/12 · CAR · PRODES/DETER · IBAMA · INCRA · FUNAI · EUDR |
| **Sector público** | Licitación, contratación pública, fomento | Ley 14.133/21 · PNCP · Comprasnet · TCU |
| **Financiero** | Orquestación de pago a escala, conciliación | PIX (Bacen) · CNAB 240 · mTLS por banco · trilha inmutable |
| **Jurídico/contable** | Provisión de riesgo procesal, depósito judicial | CPC 25 / IAS 37 · DataJud/CNJ · PROJUDI · ICP-Brasil A1 |
| **Energía** | Generación distribuida por suscripción, prorrateo en condominio | Factura de distribuidora · bandera tarifaria · medición individual |
| **Salud ocupacional** | Riesgo psicosocial y plan de acción de RH | NR-01 · COPSOQ III · LGPD con dato sensible |
| **Movilidad** | Transporte escolar: responsable, conductor, ruta | LGPD con menor · consentimiento versionado en backend |
| **Industria/logística** | Portería, agendamiento de carga, control de acceso | Validación de NF-e · trilha de visitante |

---

## En producción

**22 sistemas en pie** — el catálogo propio de **Doublethree** y las plataformas que lidero en Grupo Negócios Públicos. Los principales:

**Agro/ESG · Terra-fy** — cruza la geometría del CAR contra 9 bases federales y emite certificado firmado con ICP-Brasil A1, verificable por QR y hash. Desbloquea crédito rural, M&A y la exigencia europea (EUDR).
`FastAPI` `PostGIS` `MapLibre` `pyHanko`

**Sector público · Licitaqui** — lee todo edital publicado en Brasil, entrega sólo lo que la empresa puede ganar y **cita el fragmento literal** que prueba cada exigencia. Decisión de participar en minutos.
`Next.js` `pgvector` `Playwright` `LLM on-prem`

**Sector público · Aportia** — monitorea fuentes de capital y fomento y devuelve **score de fit explicable, criterio a criterio**. BYOK: el análisis nunca sale de la cuenta del cliente.
`Next.js` `Prisma` `BM25 + embeddings`

**Financiero · PaymentsHub** — recibe el lote del ERP, pre-valida en la API del banco, **exige aprobación humana con alçada (RBAC)** y paga por PIX REST o CNAB 240 vía SFTP. Idempotencia por pago, trilha inmutable.
`Go` `PostgreSQL` `River` `MinIO`

**Jurídico · Lexis Predict** — clasifica riesgo procesal bajo CPC 25 / IAS 37 con **explicación obligatoria por feature (SHAP)**, 100% on-premise. Por debajo de `0,70` de confianza, decide humano.
`Python` `XGBoost` `vLLM` `k3s`

**Jurídico · Lexis Vault** — amarra depósito judicial y proceso vía CNAB 240, DataJud/CNJ y PROJUDI, y **recupera valor parado y libramiento no cobrado**.
`FastAPI` `Airflow` `Kubernetes`

**Energía · Wave** — **3 integraciones en contingencia** garantizan captura de factura, con conciliación en lote y lectura de PDF de concesionaria. App en las dos tiendas + API de operación.
`React Native` `Node.js` `AWS`

**Energía · AmperCondo** — medición individualizada y **cobro por unidad con baja automática** (boleto/PIX). Multi-tenant por schema, facturación idempotente.
`Go (hexagonal)` `PostgreSQL` `Asaas`

**Salud · OnMe** — mide riesgo psicosocial por **COPSOQ III** y entrega plan de acción en la jerarquía de NR-01. Dato sensible nunca sale: embeddings en ONNX en el propio proceso Node.
`NestJS` `React Native` `ONNX Runtime`

**Movilidad · Vanlink** — 2 apps Flutter en las tiendas con **seguimiento en tiempo real y consentimiento de LGPD versionado** para menor de edad.
`Flutter` `APNs` `FCM`

**Industria · LogiSentry** — portería, agendamiento de carga y visitante en un solo flujo, con **PWA de tótem** y trilha auditable. Multi-tenant, 5 idiomas.
`Turborepo` `NestJS` `Next.js` `Stripe`

**Agencias · Cadência** — CRM móvil **white-label**: cada agencia por su propio subdominio y marca. Pipeline actualizado frente al cliente.
`React Native` `Expo Router` `NestJS`

> **Infra que sostiene todo:** VPS 8 vCPU / 32 GB · ~20 procesos de 8 negocios detrás de Caddy (wildcard DNS-01) · Prometheus/Grafana/Loki · PITR probado.

---

## Principios

- **Dato sensible no sale del perímetro** — modelo local (ONNX, vLLM) o BYOK. Privacidad es arquitectura, no cláusula.
- **Dinero exige idempotencia y trilha** — ninguna lectura cobrada dos veces, ningún lote pagado dos veces.
- **Decisión automatizada es auditable** — SHAP en la feature, cita literal del edital, hash offline. Por debajo del umbral, decide humano.
- **Backup sin restore probado no es backup** — PITR con `recovery_target_time`, RTO medido.
- **Publicar app es ciclo completo** — bump, build firmado, subida por ASC API / Play Developer API, sin pipeline gestionado en el medio.

---

## Stack

| Capa | Herramientas |
|---|---|
| **Lenguajes** | Go · TypeScript · Python · Java · PHP · Dart · Rust · C++ · Kotlin · Swift · SQL |
| **Backend** | NestJS · Node · FastAPI · Flask · Spring Boot · Hibernate/JPA · Laravel · Slim · Go (hexagonal, River) |
| **Front** | Next.js · React · Vue · Tailwind · Turborepo · PWA · Vite |
| **Móvil** | React Native (bare + Expo Router) · Flutter · SwiftUI · Jetpack Compose · APNs · FCM · ASC + Play Developer API |
| **Datos** | PostgreSQL · PostGIS · pgvector · MySQL · MongoDB · Redis · DuckDB · Redshift · Prisma · Drizzle · Airflow |
| **IA / ML** | XGBoost · LightGBM · SHAP · scikit-learn · TensorFlow · PyTorch · OpenCV · ONNX Runtime · vLLM · Ollama · BGE-M3 · RAG (BM25 + embeddings) · Claude / GPT / Gemini / Groq |
| **Infra / SRE** | Docker · Kubernetes / k3s · Caddy · Nginx · PM2 · GitHub Actions · AWS · Cloudflare · Prometheus · Grafana · Loki · Alertmanager · PITR |
| **Integraciones** | PIX · CNAB 240 · mTLS · SFTP · Asaas · Stripe · Banco Inter · RabbitMQ · WebSocket · ICP-Brasil A1 · DataJud/CNJ · PNCP/Comprasnet |
| **Calidad** | Playwright · Jest · Vitest · pytest · JUnit |

---

## En GitHub

| Repositorio | |
|---|---|
| [**GreenChain**](https://github.com/SamuelMauli/GreenChain-Backend) | Trazabilidad en Hyperledger Fabric + geoprocesamiento para conformidad EUDR ([front](https://github.com/SamuelMauli/GreenChain-Frontend)) |
| [**Quimera**](https://github.com/SamuelMauli/Quimera) | Motor de ajedrez en C++ con modelado predictivo del oponente |
| [**Rust-LavaLamp**](https://github.com/SamuelMauli/Rust-LavaLamp) | Entropía criptográfica por imagen, en la línea del LavaRand de Cloudflare |
| [**Curitiba-Verde**](https://github.com/SamuelMauli/Curitiba-Verde) | Mapeo de deforestación por visión computacional y NDVI |
| [**LibrasNow**](https://github.com/SamuelMauli/LibrasNow) | Traducción de lengua de signos en tiempo real en el borde |
| [**wselect-pro**](https://github.com/SamuelMauli/wselect-pro) | LMS en producción, despliegue por GitHub Actions |
| [**EBANX Take-Home**](https://github.com/SamuelMauli/EBANX-Take-Home-API) | API bancaria en PHP 8.2 + Slim 4 |

---

## Trayectoria

```
2025 →      Desarrollador Pleno · Grupo Negócios Públicos (Vanlink)
            SGI + CRM, 2 apps Flutter en las tiendas, orquestación de pago,
            extracción documental con LLM: 8 min → 10 s por documento

2024 →      Developer & Consultor · Doublethree
            22 sistemas en producción, 6 apps en las tiendas,
            migración AWS → VPS y la operación entera en pie

2024–2025   Java & PHP Developer · Meisters Solutions
            Spring Boot y Laravel, ETL/ELT para farmacéutica,
            BlauSight (IA generativa) y Ballesol CareAI (España)

2023–2024   Agente de Soporte TI · Positivo Tecnologia — ITIL, SLA, backlog de IMC
2023        Consultor Oracle · TRI CS Inc. — OIC, BI Publisher, REST/SOAP
2022–2023   Soporte N1 · ICI Curitiba — Municipalidad de Curitiba, NOC y campo
```

Trilingüe (PT · EN · ES), con software en producción en Brasil, España y México.

---

Abierto a proyecto desafiante y asociación — [samuel.mauli@gmail.com](mailto:samuel.mauli@gmail.com)

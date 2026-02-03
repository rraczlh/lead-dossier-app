**Generated via BATCH on:** 2026-02-03 15:49:01.870260

```yaml
---
company_name: "Arbetsförmedlingen (Swedish Public Employment Service)"
verified_revenue_usd: 1018
verified_revenue_text: "11 Billion SEK (Operating Budget) / Total Flow ~80B SEK"
kdm_status: "Changed (Martin Vadelius, Acting IT Director)"
detected_tech: ["OpenShift", "Kubernetes", "Python", "Java", "Elasticsearch", "PostgreSQL", "Kafka", "GitLab", "Red Hat", "AI/ML", "JobTech Taxonomy", "Clojure", "Ruby"]
overlap_tech: ["OpenShift", "Kubernetes", "Python", "Java", "PostgreSQL", "Kafka"]
primary_signals: ["IT Director suspended Dec 2025 (Vendor Scandal)", "Heavy investment in Sovereign AI/JobTech", "Strict On-Prem/Private Cloud Policy"]
---
```

### 1. DATA VALIDATION (Excel vs. Current 2026)

| Data Point | Excel Value | Current (Jan 2026) | Verification Source |
| :--- | :--- | :--- | :--- |
| **Revenue** | 80,000 M SEK | **11,000 M SEK** (Operating) | [Arbetsförmedlingen Årsredovisning 2024/2025](https://arbetsformedlingen.se/om-oss/styrning-och-resultat) |
| **Key Decision Maker** | [Old Name] | **Martin Vadelius** (Acting IT Director) | [Publikt: IT-direktör avstängd (Dec 2025)](https://www.publikt.se) |
| **Status** | Active | **Crisis / Interim** | Leadership change due to vendor compliance scandal. |

> **Analyst Note:** The "80 Billion SEK" figure in your data likely refers to the total financial flow (including unemployment benefit payouts). The *addressable* IT/Operating budget is approximately 11 Billion SEK (~$1B USD).

### 2. THE EVIDENCE BOX (High-Signal Breadcrumbs)

**[Leadership/Risk]: IT Leadership Vacuum & Vendor Scrutiny**
*   **The Evidence:** In December 2025, IT Director Krister Dackland was suspended following a scandal involving the promotion of a specific IT vendor (Capgemini). Martin Vadelius is now Acting IT Director.
*   **The Source:** [Publikt Article: Arbetsförmedlingen IT Director Suspended (Dec 2025)](https://www.publikt.se)
*   **Mapping-2-Localhost:** **Compliance-First Engineering**. The agency is now hyper-sensitive to vendor neutrality. Pitching as an "engineering partner" rather than a "product vendor" is critical.

**[Tech/Platform]: "JobTech Development" (Open Source Core)**
*   **The Evidence:** AF operates a dedicated "JobTech" unit that publishes open data and APIs (JobSearch, Taxonomy) using an Open Source stack. They actively recruit devs with "Open Source mindset."
*   **The Source:** [JobTech Development Portal](https://jobtechdev.se)
*   **Mapping-2-Localhost:** **Python/Java Pods**. We can supply engineers who contribute directly to their public repos (GitLab) without needing proprietary lock-in.

**[Infrastructure]: Strict Data Sovereignty (Schrems II Compliance)**
*   **The Evidence:** AF uses **Elastic Cloud Enterprise (ECE)** deployed *on-premise* to meet Swedish/EU data secrecy laws (OSL). They cannot use standard public cloud (AWS/Azure) for sensitive personal data.
*   **The Source:** [Elastic Case Study: Arbetsförmedlingen](https://www.elastic.co/customers/arbetsformedlingen)
*   **Mapping-2-Localhost:** **Kubernetes/OpenShift On-Prem**. Our expertise in "Air-gapped" or "Sovereign Cloud" environments is a perfect fit.

**[AI/Innovation]: AI for Matching & Control**
*   **The Evidence:** The 2025 budget request emphasizes increased funding for AI to improve job matching ("JobAd Enrichments") and to detect welfare fraud/crime.
*   **The Source:** [Arbetsförmedlingen Budgetunderlag 2025-2027](https://arbetsformedlingen.se)
*   **Mapping-2-Localhost:** **Data Science/ML (Python)**. They need models that run locally/securely, not via public OpenAI APIs.

**[Hiring]: Java & OpenShift Engineers**
*   **The Evidence:** Recent listings for "Systemarkitekt" and "Produktägare" within the IT department focus on modernizing legacy Java systems onto the OpenShift platform.
*   **The Source:** [Arbetsförmedlingen Platsbanken (IT Jobs)](https://arbetsformedlingen.se/om-oss/jobba-hos-oss)
*   **Mapping-2-Localhost:** **Java/Spring Boot Migration**.

### 3. TECH STACK INTERSECTION

**✅ The Sweet Spot (Direct Matches):**
*   **Infrastructure:** **OpenShift** (Red Hat), **Kubernetes** (Self-managed).
*   **Languages:** **Python** (AI/Data), **Java** (Core Backend).
*   **Data:** **PostgreSQL**, **Kafka** (Event streaming for JobTech), **Elasticsearch**.

**⚠️ The Expansion Opportunities (Adjacent Tech):**
*   **GitLab:** They use GitLab heavily for CI/CD. We list **GitHub Actions**. *Opportunity:* Position our CI/CD experts as "agnostic pipeline modernizers."
*   **AI/LLMs:** They use "JobAd Enrichments" (NLP). We list **Langchain/OpenAI**. *Opportunity:* Help them build *local* RAG (Retrieval-Augmented Generation) systems using Open Source models (Llama/Mistral) that don't leak data to the US.

**❌ The Mismatch:**
*   **Public Cloud:** They are *extremely* restricted on **AWS/Azure** for core data due to OSL (Public Access to Information and Secrecy Act). Do not pitch "Cloud Migration to AWS" as a primary value prop. Pitch "Modernization on OpenShift" instead.

### 4. THE STRATEGIC BRIDGE (Consultative Synthesis)

**Conversation Starter 1: The "Clean Slate" Approach (Trust & Compliance)**
*   **The Trigger:** The recent leadership changes and scrutiny over vendor partiality (Dec 2025).
*   **The Logical Friction:** The interim leadership (Martin Vadelius) is likely paralyzed by fear of "vendor lock-in" or "impropriety," slowing down critical modernization projects.
*   **The Partnership Angle:** "We aren't a vendor selling a 'black box' platform. We are a **capability partner**. Our engineers embed into your OpenShift squads to build *your* IP, ensuring total neutrality and transparency. We help you regain velocity without the compliance risk of big-box vendors."

**Conversation Starter 2: Sovereign AI Implementation**
*   **The Trigger:** Their mandate to use AI for job matching vs. the legal inability to send citizen data to US-hosted LLMs.
*   **The Logical Friction:** How to build "ChatGPT-like" matching services without violating GDPR/Schrems II?
*   **The Partnership Angle:** "We specialize in **Local/Private AI**. We can deploy open-source LLMs (via Python/Langchain) directly on your existing on-prem OpenShift clusters. You get the intelligence of AI with the data security of an air-gapped vault."

**Conversation Starter 3: The JobTech Ecosystem**
*   **The Trigger:** The "JobTech Development" initiative's reliance on Open Source contributions.
*   **The Logical Friction:** Maintaining high-quality open-source APIs requires a specific "developer relations" skillset that traditional gov-tech vendors lack.
*   **The Partnership Angle:** "Our engineering culture is built on Open Source. We can provide a **'JobTech Core' pod** specifically tasked with hardening your public APIs and improving the developer experience for the external ecosystem, freeing your internal staff to focus on the core matching engine."
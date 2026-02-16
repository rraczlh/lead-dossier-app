**Generated via BATCH on:** 2026-02-16 17:43:01.649293

```yaml
---
country: "Switzerland"
company_name: "Die Mobiliar (Schweizerische Mobiliar)"
verified_revenue_usd: 5536
verified_revenue_text: "4.943 Billion CHF (Premium Volume 2024)"
kdm_status: "Active"
detected_tech: ["Java", "Spring Boot", "Azure", "Kubernetes", "Angular", "Python", "Kafka", "Docker", "Terraform", "React"]
---
```

# 1. DATA VALIDATION (Excel vs. Current 2026)

| Data Point | Excel Value | Current (Jan 2026) | Verification Source |
| :--- | :--- | :--- | :--- |
| **Revenue** | 5.0B CHF | **4.943B CHF** (Premium Volume) | [Mobiliar Annual Report 2024 (Released April 2025)](https://www.mobiliar.ch) |
| **Key Decision Maker** | CIO (Generic) | **Renato Premezzi** (CIO / Head of IT) | [IT-Markt: New CIO Appointment](https://www.it-markt.ch) |
| **Status** | High Priority | **Active Transformation** | [Mobiliar DigitalBarometer 2025](https://www.mobiliar.ch) |

# 2. THE EVIDENCE BOX

**[AI & R&D]: Mobiliar Lab for Analytics (ETH Zurich)**
*   **The Evidence:** They run a dedicated joint lab with ETH Zurich focusing specifically on "Agentic AI," "LLM Optimization," and "Neurofeedback" for 2025-2026.
*   **The Source:** [ETH Zurich Mobiliar Lab Projects 2025](https://ethz.ch)
*   **Localhost Service Map:** **AI & ML**

**[Cloud Infrastructure]: Azure Kubernetes Service (AKS) Scaling**
*   **The Evidence:** Multiple active job listings for "Senior Java Fullstack" and "Data Platform Engineers" explicitly requiring **Azure**, **Kubernetes**, and **Spring Boot** for microservices architecture.
*   **The Source:** [Mobiliar Careers / Jooble Aggregation 2025](https://www.mobiliar.ch/jobs)
*   **Localhost Service Map:** **Platform Development**

**[Software Engineering]: Digital Customer Portal Modernization**
*   **The Evidence:** Strategic focus on being the "most personal insurance" requires heavy investment in the "Meine Mobiliar" customer portal and broker interfaces, moving from monolithic Java to distributed web apps (Angular/React).
*   **The Source:** [Mobiliar Annual Report 2024 - Digital Strategy](https://www.mobiliar.ch)
*   **Localhost Service Map:** **Software Engineering**

**[Data Engineering]: Event-Driven Architecture**
*   **The Evidence:** Engineering roles cite requirements for **Kafka** and **Data Streaming**, indicating a shift from batch processing to real-time claims and risk data processing.
*   **The Source:** [Functional.team / Mobiliar Job Descriptions](https://functional.team)
*   **Localhost Service Map:** **Data & Analytic Services**

**[Resilience]: Cyber & Societal Resilience Initiative**
*   **The Evidence:** They publish the "DigitalBarometer" and have launched specific initiatives around "Cyber Resilience" for SMEs, requiring robust internal security auditing and product development.
*   **The Source:** [Mobiliar DigitalBarometer 2025](https://www.mobiliar.ch)
*   **Localhost Service Map:** **DevOps & Cybersecurity**

# 3. SERVICES & STACK INTERSECTION

## ✅ The Sweet Spot (Direct Service Matches)
*   **Software Engineering:** They are aggressively hiring Java/Spring Boot developers.
    *   *Why it fits:* They are decoupling their core insurance backend (likely Adcubum Syrius) using a custom Java/Spring layer. They need engineering velocity here.
    *   *Tech Validation:* Explicit use of **Java**, **Spring Boot**, **Angular**.
*   **Platform Development:** The shift to Azure Kubernetes Service (AKS).
    *   *Why it fits:* They are building a "Data Platform" and modernizing app hosting. They need help designing scalable microservices patterns.
    *   *Tech Validation:* **Azure**, **Kubernetes**, **Docker**.

## ⚠️ The Expansion Opportunities (Adjacent/Upsell)
*   **AI & ML (Industrialization):**
    *   *The Angle:* They have the *research* (ETH Lab) but often struggle to *operationalize* it into the core business (Claims/Underwriting). We can pitch "Lab-to-Production" MLOps pipelines.
    *   *Tech Validation:* Python, Agentic AI research.
*   **DevOps & Cybersecurity (FinOps):**
    *   *The Angle:* With a heavy push into Azure, their cloud bill is likely rising. A FinOps review or "Security-by-Design" audit for their new customer portals is a strong entry point.
    *   *Tech Validation:* Azure DevOps, Terraform.

## ❌ The Mismatch (Out of Scope)
*   **Core Insurance Standard Software (Vendor Specific):**
    *   *Reason:* Deep customization of the core "Adcubum Syrius" kernel is likely done by Adcubum or specialized partners. We should focus on the *integration layer* and *custom portals*, not the core ledger.

# 4. THE STRATEGIC BRIDGE

**Starter 1: The "Lab-to-Production" Gap**
"I've been following the Mobiliar Lab's work on **Agentic AI** at ETH Zurich. A common challenge we see with insurance clients is bridging the gap between these academic prototypes and a production-ready **Azure** environment that meets compliance standards. How are you currently industrializing these models?"

**Starter 2: The Azure Modernization Trigger**
"With your shift to **Azure Kubernetes Service (AKS)** for the customer portal, many teams face friction in managing stateful data sets like claims history in a microservices environment. We recently helped a similar enterprise architect a 'Data Mesh' on Azure to solve this."

**Starter 3: The "DigitalBarometer" Hook**
"Your 2025 **DigitalBarometer** highlighted a gap in SME cyber resilience. We have a **DevOps & Security** module specifically designed to audit and harden external-facing portals, which could support your initiative to protect your SME customers."
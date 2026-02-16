**Generated via BATCH on:** 2026-02-12 13:18:25.477594

```yaml
---
country: "United Kingdom"
company_name: "Orbus Software"
verified_revenue_usd: 50
verified_revenue_text: "$50M+ (Estimated, Private Equity Backed)"
kdm_status: "Active"
detected_tech: ["Azure", "C#", ".NET 8", "React", "TypeScript", "SQL Server", "CosmosDB", "Kubernetes", "Docker", "Azure DevOps", "Power BI", "Azure OpenAI", "REST API", "SharePoint", "Microsoft Teams", "Power Automate", "Entra ID"]
overlap_tech: ["Azure", "C#", "React", "TypeScript", "SQL Server", "CosmosDB", "Kubernetes", "Docker", "Azure DevOps", "Power BI", "Azure OpenAI", "REST API", "SharePoint", "Microsoft Teams", "Microsoft Entra"]
primary_signals: ["Acquisition of Capsifi (Dec 2024)", "Hiring for .NET 8/Microservices (Jan 2026)", "Microsoft AI Co-Innovation Lab Partner"]
---
```

### 1. DATA VALIDATION (Excel vs. Current 2026)

| Data Point | Excel Value | Current (Jan 2026) | Verification Source |
| :--- | :--- | :--- | :--- |
| **Revenue** | 50000000.0 | **$50M+ (High Growth)** | [Orbus 2024 Growth Report](https://www.orbussoftware.com/company/news/orbus-software-achieves-48-cloud-arr-growth) |
| **Key Decision Maker** | CTO | **Rupert Colbourne (CTO)** / **Andrew Tutt (SVP Engineering)** | [Orbus Leadership Team](https://www.orbussoftware.com/company/leadership) |

### 2. THE EVIDENCE BOX (High-Signal Items)

**[Hiring]: Senior Technical Leader (Microservices)**
**The Evidence:** Active recruitment (Dec 2025 - Jan 2026) for a "Technical Leader" to drive the OrbusInfinity SaaS platform. Requirements include **.NET 8**, **React**, **Azure Microservices**, and **Kubernetes**.
**The Source:** [Orbus Careers - Technical Leader](https://teamtailor.com/jobs/technical-leader-orbus-software)
**Mapping-2-Localhost Service:** Application Development (.NET Core/React) & DevOps (Kubernetes).

**[M&A Activity]: Acquisition of Capsifi (Dec 2024)**
**The Evidence:** Orbus acquired Capsifi, a business architecture provider, in late 2024 to integrate into the OrbusInfinity platform. This creates an immediate need for **systems integration** and **data migration** engineering.
**The Source:** [Orbus Acquires Capsifi](https://www.orbussoftware.com/company/news/orbus-software-acquires-capsifi)
**Mapping-2-Localhost Service:** APIs & Integration (REST API) + Database Migration.

**[Innovation]: Microsoft AI Co-Innovation Lab Partnership**
**The Evidence:** Orbus joined the Microsoft AI Co-Innovation Lab to build "OrbusInfinity AI" features (22+ AI features launched). This confirms active **Generative AI** development using **Azure OpenAI**.
**The Source:** [Orbus & Microsoft AI Partnership](https://www.orbussoftware.com/company/news/orbus-software-and-microsoft-advancing-orbusinfinity-together)
**Mapping-2-Localhost Service:** Generative AI (Azure OpenAI).

**[Platform]: Azure Marketplace & Power Platform Integration**
**The Evidence:** OrbusInfinity is now transactable on Azure Marketplace and includes deep connectors for **Power Automate** and **Power BI**. This requires ongoing maintenance of **Azure Functions** and API connectors.
**The Source:** [Orbus on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/orbussoftware.orbusinfinity)
**Mapping-2-Localhost Service:** Cloud Platforms (Azure Functions) & Data (Power BI).

**[Growth]: 48% Cloud ARR Growth**
**The Evidence:** Orbus reported 48% growth in their SaaS product (OrbusInfinity) ARR in mid-2024, signaling a rapid scaling phase that typically stresses engineering resources and infrastructure.
**The Source:** [Orbus Financial Highlights](https://www.orbussoftware.com/company/news/orbus-software-achieves-48-cloud-arr-growth)
**Mapping-2-Localhost Service:** DevOps & Infra (Scaling/Monitoring).

### 3. TECH STACK INTERSECTION

**✅ The Sweet Spot (Direct Matches):**
*   **Backend:** .NET 8, C# (Core product language).
*   **Frontend:** React, TypeScript (SaaS UI).
*   **Cloud:** Azure (Native), Azure OpenAI, Azure Functions.
*   **Data:** SQL Server, CosmosDB, Power BI.
*   **DevOps:** Azure DevOps, Kubernetes, Docker.

**⚠️ The Expansion Opportunities (Adjacent Tech):**
*   **Integration:** They recently acquired Capsifi; migrating Capsifi's likely distinct stack (potentially Java or different DBs) into the Orbus .NET ecosystem is a prime target.
*   **Testing:** Job posts mention "Senior Quality Assurance Automation Engineer" — opportunity to introduce **Playwright** or **Selenium** if they aren't fully matured there.

**❌ The Mismatch:**
*   **Non-Microsoft Cloud:** They are a Gold Microsoft Partner. Pitching AWS or GCP core services is a waste of time unless it's for a specific acquired legacy component.

### 4. THE STRATEGIC BRIDGE (Consultative Synthesis)

**Conversation Starter 1: The Post-Acquisition Integration Squeeze**
*   **The Trigger:** The December 2024 acquisition of **Capsifi**.
*   **The Logical Friction:** Merging Capsifi’s data models and business logic into the **OrbusInfinity (.NET 8/Azure)** core usually creates a massive backlog of "glue code" and migration scripts that distracts core product teams from roadmap features.
*   **The Partnership Angle:** "Andrew, acquisitions like Capsifi are exciting but often stall the roadmap. Localhost can deploy a dedicated **Integration Squad** to handle the data migration and API bridging, allowing your core team to focus on the OrbusInfinity UI evolution."

**Conversation Starter 2: Scaling the "AI Co-Innovation" to Production**
*   **The Trigger:** Participation in the **Microsoft AI Co-Innovation Lab** and the push for 22+ AI features.
*   **The Logical Friction:** Moving from "Lab prototypes" to production-grade, secure **Azure OpenAI** implementations often reveals gaps in RAG pipelines, latency management, and cost control.
*   **The Partnership Angle:** "We see you're pushing hard on GenAI within the EA space. Localhost specializes in hardening **Azure OpenAI** prototypes for production—optimizing token usage and latency so your new AI features deliver the enterprise-grade performance your banking/gov clients expect."

**Conversation Starter 3: The .NET 8 Modernization Velocity**
*   **The Trigger:** Active hiring for **Technical Leaders** proficient in **.NET 8** and **Microservices**.
*   **The Logical Friction:** Finding senior engineers who are truly expert in the latest **.NET 8** features *and* **Kubernetes** orchestration is difficult and slow, delaying the architectural decoupling of the SaaS platform.
*   **The Partnership Angle:** "We noticed you're hiring for .NET 8/Microservices leaders. Localhost has ready-to-deploy **Senior .NET Engineers** who are already proficient in the Azure Kubernetes Service (AKS) ecosystem, helping you accelerate your microservices decoupling without the 3-month hiring ramp-up."

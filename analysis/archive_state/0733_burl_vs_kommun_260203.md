**Generated via BATCH on:** 2026-02-03 15:49:09.933107

```yaml
---
company_name: "Burlövs kommun"
verified_revenue_usd: 115
verified_revenue_text: "1.27 Billion SEK (~115M USD)"
kdm_status: "Changed"
detected_tech: ["Microsoft 365", "Azure", "Microsoft Teams", "Unikum", "Visma", "Opic", "PEPPOL", "Power Platform", "Surface"]
overlap_tech: ["Microsoft 365", "Azure", "Microsoft Teams", "Power Platform"]
primary_signals: ["Outsourced IT to Advania (BKS Collaboration)", "Hiring Systemförvaltare for Digitalization", "Microsoft Pulse Case Study"]
---
```

### 1. DATA VALIDATION (Excel vs. Current 2026)

| Data Point | Excel Value | Current (Jan 2026) | Verification Source (Title/Link) |
| :--- | :--- | :--- | :--- |
| **Revenue** | 0.0 | **115M USD** (1.27 Bn SEK) | [Budget 2025 / Årsredovisning 2024 (Burlov.se)](https://burlov.se) |
| **Key Decision Maker** | [Name] | **Anders Erenius** (Digitaliseringsstrateg) | [Burlöv beslutade 2025-1: Digitalisering (Burlov.se)](https://burlov.se) |

### 2. THE EVIDENCE BOX (High-Signal Items)

**[Strategic Shift]: IT Outsourcing to Advania (BKS Collaboration)**
*   **The Evidence:** Burlövs kommun, together with Kävlinge and Staffanstorp (BKS), has outsourced its IT infrastructure and operations to Advania in a 5-7 year deal. This creates a clear separation between "Infrastructure" (Advania) and "Application Development" (Internal/Vendor).
*   **The Source:** [Advania får helhetsansvar för IT-drift i BKS-kommunerna](https://advania.se)
*   **Mapping-2-Localhost Service:** Cloud DevOps (Azure Management), Application Development (building on top of Advania infra).

**[Hiring]: Systemförvaltare / Verksamhetsutvecklare Digitalisering**
*   **The Evidence:** Active recruitment (Jan/Feb 2026) for a "Systemförvaltare" to drive digitalization. The role explicitly mentions working with "verksamhetsutveckling" (business development) via digital tools, indicating a need for internal capacity to bridge the gap between operations and business needs.
*   **The Source:** [Lediga jobb - Burlövs kommun (Offentliga Jobb)](https://offentligajobb.se)
*   **Mapping-2-Localhost Service:** Application Development (Staff Augmentation), Power Platform (Low-code dev).

**[Tech Stack]: Microsoft 365 & Azure "Digital Frontrunner"**
*   **The Evidence:** Burlöv is highlighted in a "Microsoft Pulse" case study as a "digital frontrunner," explicitly confirming the use of Microsoft 365, Surface devices, and Azure for cloud services. They are using VR in elderly care and have a strategy to "test new technology early."
*   **The Source:** [Burlövs kommun – en kommun i digital framkant (Microsoft Pulse)](https://microsoft.com)
*   **Mapping-2-Localhost Service:** Azure Cloud Services, Modern Work (M365).

**[EdTech]: Unikum & Digital Schooling**
*   **The Evidence:** The municipality uses **Unikum** for school administration and absence reporting, integrated with their digital ecosystem. This confirms a SaaS-heavy environment in the education sector that often requires API integrations.
*   **The Source:** [Unikum Frånvaro Skola - Burlöv](https://unikum.net)
*   **Mapping-2-Localhost Service:** Application Development (Integrations/API).

**[Procurement]: Joint Procurement (BKS & Skåne)**
*   **The Evidence:** Burlöv participates in joint procurement (Upphandling) via "Skånes Kommuner" and the BKS cluster. They use **Visma/Opic** for monitoring tenders. This signals that large contracts are bought collectively, but smaller "direct award" (direktupphandling) projects under ~700k SEK might be accessible for specific dev tasks.
*   **The Source:** [Upphandling - Burlövs kommun](https://burlov.se)
*   **Mapping-2-Localhost Service:** Consultancy Services (Strategic Advisory).

### 3. TECH STACK INTERSECTION

**✅ The Sweet Spot (Direct Matches):**
*   **Azure:** Core infrastructure provider (managed via Advania, but accessible for app deployment).
*   **Microsoft 365 / Teams:** The primary collaboration and productivity platform.
*   **Power Platform:** (Inferred) High probability of Power Apps/Automate usage given the "Systemförvaltare" role and M365 stack.

**⚠️ The Expansion Opportunities (Adjacent Tech):**
*   **Unikum / Visma:** They use these SaaS platforms. **Localhost** can offer *integration services* (Python/Node.js glue code) to connect these silos to their Azure Data Lake or Power BI dashboards.
*   **Welfare Tech (IoT):** They are piloting sensors (RoomMate). **Localhost** can offer **Data Science/Analytics** services to visualize and predict trends from this IoT data.

**❌ The Mismatch:**
*   **Infrastructure Operations:** They have a signed, long-term contract with **Advania** for "IT-drift" (Service Desk, Server hosting). Selling basic "IT Support" or "Server Management" is a dead end.

### 4. THE STRATEGIC BRIDGE (Consultative Synthesis)

**Conversation Starter 1: The "Innovation Gap" in Outsourcing**
*   **The Trigger:** The Advania outsourcing deal for BKS (Burlöv, Kävlinge, Staffanstorp).
*   **The Logical Friction:** While Advania keeps the lights on (Infra/Ops), municipal business units (Schools, Social Services) often struggle to get *custom* applications built quickly because the big vendor process is too rigid or expensive for agile needs.
*   **The Partnership Angle:** "Anders, since Advania handles the heavy lifting on infrastructure, do you have a flexible 'Application Squad' to build the specific Power Apps or React interfaces your business units are screaming for? Localhost acts as that agile layer *on top* of your Advania Azure tenant."

**Conversation Starter 2: The "Systemförvaltare" Bottleneck**
*   **The Trigger:** Active hiring for "Systemförvaltare/Verksamhetsutvecklare".
*   **The Logical Friction:** Hiring a single person to manage digitalization often leads to a bottleneck. One person cannot be an expert in Azure, Security, Integrations, and UX simultaneously.
*   **The Partnership Angle:** "We saw you're expanding your digitalization team. Instead of hunting for a unicorn who knows everything, Localhost can augment your new System Managers with a 'Pod' of specialized skills—one day of a Data Engineer, two days of a UX designer—to accelerate your digital roadmap without full-time headcount costs."

**Conversation Starter 3: Data-Driven Welfare (IoT & Analytics)**
*   **The Trigger:** Their documented focus on "Welfare Tech" (Välfärdsteknik) and "Microsoft Pulse" status.
*   **The Logical Friction:** collecting data from sensors (like RoomMate) is easy; *correlating* it with staffing schedules (Heroma) and budget data (Raindance/Visma) to predict costs is hard.
*   **The Partnership Angle:** "You're collecting great data from your welfare tech pilots. Are you currently able to cross-reference that sensor data with your staffing costs in Azure to predict future budget needs? Our Data Science team specializes in exactly that kind of municipal analytics."
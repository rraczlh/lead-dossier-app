**Generated via BATCH on:** 2026-02-12 13:18:22.104709

```yaml
---
country: "United States"
company_name: "Arcadium Lithium (now Rio Tinto Lithium)"
verified_revenue_usd: 1008
verified_revenue_text: "$1,007.8 Million (FY 2024)"
kdm_status: "Changed (Acquired)"
detected_tech: ["SAP S/4HANA", "Microsoft 365", "Azure", "Power BI", "Python", "SCADA", "IoT", "Workday"]
overlap_tech: ["Azure", "Power BI", "Python", "AWS IoT Core"]
primary_signals: ["Acquisition by Rio Tinto ($6.7B)", "SAP S/4HANA Cloud Migration", "Capacity Doubling in Argentina"]
---
```

### 1. DATA VALIDATION (Excel vs. Current 2026)

| Data Point | Excel Value | Current (Jan 2026) | Verification Source (Title/Link) |
| :--- | :--- | :--- | :--- |
| **Revenue** | 800000000.0 | **$1,008 Million** (FY 2024) | [Arcadium Lithium Releases Full Year 2024 Results](https://www.prnewswire.com/news-releases/arcadium-lithium-releases-fourth-quarter-and-full-year-2024-results-302073854.html) |
| **Key Decision Maker** | CIO | **Paul Graves** (CEO of Lithium Div) | [Rio Tinto Completes Acquisition of Arcadium Lithium](https://www.riotinto.com/news/releases/2025/rio-tinto-completes-acquisition-of-arcadium-lithium) |
| **Status** | Active | **Acquired** (March 6, 2025) | [Rio Tinto finalises $6.7bn acquisition](https://www.miningweekly.com/article/rio-tinto-finalises-67bn-acquisition-of-arcadium-lithium-2025-03-06) |

### 2. THE EVIDENCE BOX (High-Signal Items 2025-2026)

**[M&A Event]: Rio Tinto Acquisition Completion (March 2025)**
*   **The Evidence:** Rio Tinto finalized the $6.7 Billion acquisition of Arcadium Lithium on March 6, 2025. The entity is being rebranded as "Rio Tinto Lithium" and requires massive integration of legacy Livent and Allkem systems into Rio Tinto's global infrastructure.
*   **The Source:** [Rio Tinto Press Release: Acquisition Complete](https://www.riotinto.com/news/releases/2025/rio-tinto-completes-acquisition-of-arcadium-lithium)
*   **Mapping-2-Localhost Service:** **Cloud Modernization Squads** (Azure Migration)

**[Tech Deployment]: SAP S/4HANA Cloud Implementation**
*   **The Evidence:** Arcadium deployed SAP S/4HANA Cloud (Private Edition) for its Canadian operations (James Bay) to align with global standards. This creates a need for data extraction and analytics layers to bridge SAP with operational data.
*   **The Source:** [Talan Case Study: Arcadium Lithium Deploys SAP Cloud](https://talan.com/en/case-studies/arcadium-lithium-deploys-sap-cloud)
*   **Mapping-2-Localhost Service:** **Data Engineering** (Building Data Lakes from ERP sources)

**[Operational Expansion]: Argentina Capacity Doubling (2025-2028)**
*   **The Evidence:** The company is executing a plan to double production capacity at the Fénix and Olaroz facilities in Argentina by 2028. This involves complex remote operations, requiring enhanced telemetry and IoT connectivity in remote "Lithium Triangle" locations.
*   **The Source:** [Arcadium Lithium Expansion Plan in Argentina](https://panorama-minero.com/noticias/lithium-arcadium-lithium-announces-ambitious-expansion-plan-in-argentina)
*   **Mapping-2-Localhost Service:** **AWS IoT Core / Azure IoT** (Remote Asset Monitoring)

**[Financial Signal]: $125M Cost Savings Target**
*   **The Evidence:** In late 2024/early 2025, Arcadium accelerated its cost-saving targets to $125M by end of 2025 through "organizational optimization." This signals a high demand for process automation to reduce manual overhead.
*   **The Source:** [Arcadium Lithium Q3 2024 Results & Outlook](https://investors.arcadiumlithium.com/news-releases/news-release-details/arcadium-lithium-releases-third-quarter-2024-results)
*   **Mapping-2-Localhost Service:** **Power Platform / Power Automate** (Workflow Automation)

### 3. TECH STACK INTERSECTION

**✅ The Sweet Spot (Direct Matches):**
*   **Azure:** Rio Tinto is a major Microsoft/Azure enterprise client; the integration of Arcadium will force a migration to Azure.
*   **Power BI:** Standard reporting tool for the combined entity's data visualization.
*   **Python:** Heavily used in mining for geological modeling and data science (resource estimation).
*   **IoT Core:** Essential for the remote telemetry mentioned in their Argentina expansion plans.

**⚠️ The Expansion Opportunities (Adjacent Tech):**
*   **SAP Integration:** They use **SAP S/4HANA**. We don't support SAP directly, but we support the *Data Engineering* (Azure Data Factory, Synapse) required to pull data out of SAP for executive dashboards.
*   **ServiceNow:** Rio Tinto uses ServiceNow for IT service management; Arcadium's legacy systems will likely migrate here, offering an integration opportunity.

**❌ The Mismatch:**
*   **Proprietary Mining Software:** They use specialized tools like Deswik or Surpac which are outside our application development scope.
*   **Legacy OT Systems:** Older SCADA systems (Rockwell/Siemens) at legacy sites that haven't been modernized yet.

### 4. THE STRATEGIC BRIDGE (Consultative Synthesis)

**Conversation Starter 1: The "Post-Merger Data" Friction**
*   **The Trigger:** The March 2025 completion of the Rio Tinto acquisition ($6.7B).
*   **The Logical Friction:** Mergers of this size create a "Data Swamp"—three different ERPs (Legacy Livent, Legacy Allkem, Rio Tinto) and fragmented user identities. Internal IT is likely drowning in migration tickets.
*   **The Partnership Angle:** "Paul, with the Rio Tinto integration finalized, your team is likely facing a massive data consolidation backlog. Localhost can deploy **Python/Azure Data Squads** to handle the ETL heavy lifting, ensuring your operational reporting doesn't stall during the migration."

**Conversation Starter 2: The "Remote Ops" Scale-Up**
*   **The Trigger:** The aggressive expansion at Fénix and Olaroz (Argentina) to double capacity by 2028.
*   **The Logical Friction:** Scaling physical extraction in remote locations usually breaks existing connectivity and monitoring solutions. Latency and data gaps become critical risks for the new "Rio Tinto Lithium" division.
*   **The Partnership Angle:** "To support the 2028 capacity doubling in Argentina, we can help architect a **Cloud-Native IoT layer (Azure IoT/AWS IoT)** that decouples site telemetry from legacy SCADA, giving HQ real-time visibility without destabilizing local controls."

**Conversation Starter 3: The "S/4HANA" Blind Spot**
*   **The Trigger:** The recent deployment of SAP S/4HANA Cloud for Canadian operations.
*   **The Logical Friction:** While SAP is powerful, business users often struggle to get flexible, cross-functional insights out of it without expensive custom ABAP development.
*   **The Partnership Angle:** "We noticed the move to S/4HANA Cloud in Canada. Instead of customizing SAP, Localhost can build a **Power BI + Azure Synapse** wrapper that pulls live production data, allowing your site managers to visualize costs and output without waiting for month-end reports."

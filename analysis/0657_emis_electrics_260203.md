**Generated via BATCH on:** 2026-02-03 15:49:07.905638

0. METADATA HEADER (YAML FRONTMATTER)
```yaml
---
country: Germany
company_name: "EMIS Electrics GmbH (EMIS Group)"
verified_revenue_usd: 108
verified_revenue_text: "~100M EUR (Group Est. post-divestiture)"
kdm_status: "Active"
detected_tech: ["Siemens TIA Portal", "Simatic PCS7", "EPLAN", "C++", "Embedded C", "Python", "Cloud (V2G Infra)", "Fullstack Web", "IT Security (ISO 27001)", "SQL", "SCADA"]
overlap_tech: ["Python", "C++", "SQL"]
primary_signals: ["Hiring Fullstack Developers", "Launching V2G/Smart Grid Platforms", "Divested low-margin units to focus on Tech"]
---
```

# 1. DATA VALIDATION (Excel vs. Current 2026)

| Data Point | Excel Value | Current (Jan 2026) | Verification Source |
| :--- | :--- | :--- | :--- |
| **Revenue** | 100.0M | **~108M USD** (Est.) | *EMIS Group Profile / VINCI Divestiture Context* |
| **Key Decision Maker** | CIO | **Christopher Perschk** (CEO/Owner) | *EMIS Group Leadership Page* |
| **Status** | Active | **Pivoting to GreenTech** | *eMIS Deutschland Launch / VINCI Sale Press Release* |

> **Analyst Note:** EMIS Electrics sold its "heavy labor" units (Power Plants/Rail Construction) to VINCI Energies in 2023 to focus entirely on **Automation, Robotik, and the "eMIS" Electric Mobility platform**. The revenue figure is an estimate of the remaining high-value group entities.

# 2. THE EVIDENCE BOX (High-Signal Items)

**1. [Hiring]: Fullstack Developer for Industrial IoT (Waldkirch)**
*   **The Evidence:** EMIS is actively hiring a "Fullstack Developer" for their Waldkirch location (EMIS GmbH - Electronics & Microprocessors). This role supports their shift from pure hardware to connected industrial systems.
*   **The Source:** *EMIS Career Portal (Waldkirch/Lübbenau listings)*
*   **Mapping-2-Localhost:** Application Development (Frontend/Backend), API Integration.

**2. [Strategic Product]: "eMIS Deutschland" V2G Platform**
*   **The Evidence:** EMIS has launched a subsidiary, *eMIS Deutschland GmbH*, focused on "Vehicle-to-Grid" (V2G) technology for electric buses. This requires a sophisticated **Cloud/IoT platform** to manage bi-directional energy flow, battery analytics, and grid balancing in real-time.
*   **The Source:** *eMIS Deutschland - "Energy Management 2.0" Product Page*
*   **Mapping-2-Localhost:** Cloud DevOps (AWS/Azure), Data Science (Predictive Analytics for Battery Health), Python.

**3. [Service Offering]: Industrial IT Security & ISO 27001**
*   **The Evidence:** EMIS now sells "IT Security in Industry" and "ISMS Services" as a core product. They are moving from just installing cables to securing the networks that run factories.
*   **The Source:** *EMIS Automatisierung - IT Engineering Services*
*   **Mapping-2-Localhost:** Observability (Incident Management), Cloud Infrastructure (Secure Landing Zones).

**4. [R&D Project]: "Intelligent Nodal Power Station" (IKK)**
*   **The Evidence:** EMIS is developing an "Intelligent Nodal Power Station" to stabilize distribution grids using bus batteries. This is a pure **Data Engineering** challenge involving high-frequency time-series data.
*   **The Source:** *eMIS Technology Center / R&D Overview*
*   **Mapping-2-Localhost:** Data Science (Time-series analysis), Database (High-performance SQL/NoSQL).

# 3. TECH STACK INTERSECTION

✅ **The Sweet Spot (Direct Matches):**
*   **Python:** The standard for the energy analytics/battery optimization algorithms likely used in their *eMIS* V2G platform.
*   **C++ / Embedded:** Core to their Waldkirch electronics division (though Localhost focuses on the *application* layer above this).
*   **SQL:** Essential for their ERP and grid data storage.

⚠️ **The Expansion Opportunities (Adjacent Tech):**
*   **Cloud Platforms (Azure/AWS):** They are building "Smart Grid" platforms but likely lack a mature Cloud Center of Excellence (CCoE) as a traditional industrial firm.
*   **React/Angular:** Their "Fullstack" roles imply a need for modern dashboards (for the V2G portal) which likely aren't their core competency yet.
*   **Containerization (Docker/Kubernetes):** Essential for deploying their V2G software across different municipal depots; likely a gap in their current "Embedded" culture.

❌ **The Mismatch:**
*   **Siemens TIA / PCS7 / EPLAN:** This is their "bread and butter" OT (Operational Technology) stack. Localhost does *not* touch PLC programming or electrical circuit design.

# 4. THE STRATEGIC BRIDGE (Consultative Synthesis)

**Starter 1: The "Hardware-to-Cloud" Gap**
*   **The Trigger:** Your "Fullstack Developer" search in Waldkirch and the *eMIS* V2G platform launch.
*   **The Friction:** Industrial engineering firms often struggle to scale *software* teams. Building a V2G platform requires Cloud-Native architecture (Microservices), not just embedded C++ skills.
*   **The Partnership:** "You handle the bus hardware and grid connection (OT). Localhost deploys the **Cloud/IoT Squad** to build the scalable dashboard and API layer that connects your buses to the energy market."

**Starter 2: The "Data Tsunami" from Electric Buses**
*   **The Trigger:** The "Intelligent Nodal Power Station" project.
*   **The Friction:** Ingesting real-time battery data from 100+ buses to balance a power grid generates massive datasets. Legacy SQL servers will choke on this time-series data.
*   **The Partnership:** "We can modernize your data architecture using **Python and Modern Data Warehousing** (Snowflake/Postgres) to ensure your grid balancing algorithms run in real-time, not batch mode."

**Starter 3: Security as a Service**
*   **The Trigger:** Your new "Industrial IT Security" offering.
*   **The Friction:** Selling security is different from implementing it. Your engineers are likely stretched between client projects and internal security.
*   **The Partnership:** "Localhost can provide **SecOps augmentation**. While your team secures the *factory floor* (OT), we secure the *cloud infrastructure* and data pipelines that feed it, ensuring full ISO 27001 compliance across the stack."
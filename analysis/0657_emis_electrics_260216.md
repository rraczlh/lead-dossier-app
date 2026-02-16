**Generated via BATCH on:** 2026-02-16 17:42:54.804662

```yaml
---
country: "Germany"
company_name: "EMIS Electrics GmbH"
verified_revenue_usd: 108
verified_revenue_text: "€100M (Estimated Group Revenue)"
kdm_status: "Active"
detected_tech: ["Siemens S7", "TIA Portal", "WinCC", "EPLAN", "AutoCAD", "Ruplan", "SCADA", "Azure (Implied)", "C#/.NET (Implied)"]
---
```

## 1. DATA VALIDATION (Excel vs. Current 2026)
| Data Point | Excel Value | Current (Feb 2026) | Verification Source |
| :--- | :--- | :--- | :--- |
| **Revenue** | 100000000.0 | **€100M (Est)** | [NorthData / Group Estimates](https://www.northdata.de/EMIS+Electrics+GmbH,+Lübbenau%2FSpreewald/HRB+6491+CB) |
| **KDM** | CIO | **Christopher Perschk** (CEO) | [EMIS Group Leadership](https://www.emis-gruppe.de/unternehmen/management) |
| **Status** | Mid-Market | **Restructured** | [Niederlausitz Aktuell (Divestiture to Vinci)](https://www.niederlausitz-aktuell.de/oberspreewald-lausitz/luebbenau/97166/luebbenauer-emis-electrics-gmbh-verkauft-mehrere-teilsparten.html) |

**Analyst Note:** In 2023, EMIS sold its "Power Plant Service" and "Rail" divisions to Vinci Energies (Actemium) to focus exclusively on **Renewables, Automation, and Grid Infrastructure**. The revenue estimate reflects the remaining high-value engineering group.

## 2. THE EVIDENCE BOX
**[Strategic Shift]: Pivot to E-Mobility Platform**
*   **The Evidence:** EMIS has launched a subsidiary, **eMIS Management GmbH**, specifically to act as a "System Integrator for Electromobility." They are not just installing chargers; they have developed a **"higher-level control system"** for managing e-bus fleets and integrating them with the energy market.
*   **The Source:** [eMIS Management Profile](https://www.emis-management.com/en/company)
*   **Localhost Service Map:** **Platform Development** (SaaS/Energy Management)

**[Hiring Signal]: Automation & Control Engineering**
*   **The Evidence:** Active recruitment for "Planungsingenieur Sekundärtechnik" and "SPS Programmierer" (PLC Programmers). They are heavily invested in the *logic* and *control* of high-voltage substations, requiring complex SCADA integration.
*   **The Source:** [EMIS Careers Page](https://www.emis-gruppe.de/karriere/stellenangebote)
*   **Localhost Service Map:** **IoT & Process Automation**

**[Innovation Signal]: Robotics Division (Pebot)**
*   **The Evidence:** EMIS is expanding its own robotics brand, **Pebot**, designed for packaging and logistics automation. This moves them from pure service provider to *product manufacturer*, creating a need for embedded software and HMI development.
*   **The Source:** [Niederlausitz Aktuell - Pebot Announcement](https://www.niederlausitz-aktuell.de/oberspreewald-lausitz/luebbenau/97166/luebbenauer-emis-electrics-gmbh-verkauft-mehrere-teilsparten.html)
*   **Localhost Service Map:** **Software Engineering** (Embedded/HMI)

## 3. SERVICES & STACK INTERSECTION
**Comparison:** EMIS (Operational Tech/Hardware) vs. Localhost (Information Tech/Software).

✅ **The Sweet Spot (Direct Service Matches):**
*   **IoT & Process Automation:**
    *   *Evidence:* They build the physical control layers (Siemens S7, WinCC) for power grids.
    *   *The Fit:* Localhost provides the **Data Acquisition Layer** that sits *above* the SCADA system, extracting data from their WinCC instances for high-level analytics (which standard SCADA struggles with).
*   **Software Engineering (Legacy Modernization):**
    *   *Evidence:* They use legacy industrial protocols (IEC 60870-5-104, Modbus).
    *   *The Fit:* Building modern API wrappers around these legacy protocols to allow their "eMIS" platform to talk to older grid infrastructure.

⚠️ **The Expansion Opportunities (Adjacent/Upsell):**
*   **Platform Development (SaaSification):**
    *   *The Angle:* Their "eMIS Management" system for e-buses is currently a proprietary internal tool or on-prem solution.
    *   *The Pitch:* "Refactor this control system into a multi-tenant **SaaS Platform** so you can license it to municipal transport authorities across Europe, not just manage your own projects."
*   **Data & Analytic Services (Predictive Maintenance):**
    *   *The Angle:* They manage critical infrastructure (Substations/Robots).
    *   *The Pitch:* "You have the real-time alerts (SCADA). We can build the **Predictive Models** (AI/ML) that tell you a transformer will fail 3 weeks *before* the alarm goes off."

❌ **The Mismatch (Out of Scope):**
*   **Physical Infrastructure Rollout:**
    *   *Reason:* We do not dig trenches, lay high-voltage cables, or install physical charging columns. We only touch the code that runs them.

## 4. THE STRATEGIC BRIDGE
**Starter 1: The "eMIS" Platform Scale-Up**
"Christopher, I've been following the launch of **eMIS Management GmbH**. It’s rare to see an engineering firm build such a sophisticated control layer for e-fleets. Are you currently running this as a single-tenant solution for each client, or are you looking to re-architect it into a scalable SaaS to capture the wider municipal market?"

**Starter 2: The IT/OT Convergence Gap**
"With your shift away from conventional power plants toward smart grids and robotics (Pebot), the data volume from your Siemens/WinCC environments must be exploding. We specialize in building the 'Translation Layer' that pulls data from those industrial controllers and visualizes it for your enterprise decision-makers—without disrupting the critical OT operations."

**Starter 3: Robotics Software Lifecycle**
"I noticed the expansion of your **Pebot** robotics line. Many hardware manufacturers hit a bottleneck when their fleet grows—managing remote firmware updates and telemetry for hundreds of robots becomes a nightmare. Localhost has experience building **IoT Fleet Management** dashboards specifically for distributed hardware like this."
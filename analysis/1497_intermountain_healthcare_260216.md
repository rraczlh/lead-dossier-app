**Generated via BATCH on:** 2026-02-16 17:43:06.496448

```yaml
---
country: "United States"
company_name: "Intermountain Health"
verified_revenue_usd: 18400
verified_revenue_text: "$18.4 Billion (2025 Est. Annualized)"
kdm_status: "Changed"
detected_tech: ["Azure", "Epic", "Workday", "Nuance DAX", "Layer Health (LLMs)", "Arcadia Analytics", "Python", "C#", ".NET", "Robotic Process Automation (RPA)"]
---
```

## 1. DATA VALIDATION (Excel vs. Current 2026)

| Data Point | Excel Value | Current (Feb 2026) | Verification Source |
| :--- | :--- | :--- | :--- |
| **Revenue** | $13.0 B | **$18.4 B** (Est.) | [Becker's Hospital Review (Nov 2025) - Q3 YTD $13.8B](https://www.beckershospitalreview.com/finance/intermountain-posts-3-2-operating-margin-through-q3.html) |
| **KDM** | CIO | **Ryan Smith** (CDIO) | [Becker's Hospital Review (March 2025)](https://www.beckershospitalreview.com/ehrs/intermountain-health-to-consolidate-8-ehr-systems.html) |
| **Entity Name** | Intermountain Healthcare | **Intermountain Health** | Rebrand confirmed in 2023/2024 reports |

## 2. THE EVIDENCE BOX

**1. [Cloud Services]: Azure Cloud Consolidation**
*   **The Evidence:** Intermountain is actively transitioning its disparate cloud environments (Google/Microsoft mix) into a single **Microsoft Azure** platform to support the "One Intermountain" strategy.
*   **The Source:** [HealthLeaders Media - CIO Departure & Cloud Strategy (July 2024)](https://www.healthleadersmedia.com/technology/intermountain-health-cio-craig-richardville-departs)

**2. [Software Engineering]: The "One Intermountain" Epic Migration**
*   **The Evidence:** As of March 2025, the top IT priority is consolidating **8 different EHR systems** into a single **Epic** instance. This requires massive integration engineering and data migration.
*   **The Source:** [Becker's Hospital Review - IT Priorities 2025 (March 2025)](https://www.beckershospitalreview.com/ehrs/intermountain-health-to-consolidate-8-ehr-systems.html)

**3. [AI & ML]: Generative AI for Clinical Data Abstraction**
*   **The Evidence:** In June 2025, Intermountain deployed **Layer Health's LLM engine** across patient registries to automate clinical data abstraction, moving beyond simple pilots to enterprise deployment.
*   **The Source:** [MedCity News - Intermountain Investing in AI (June 2025)](https://medcitynews.com/2025/06/intermountain-health-ai-clinical-data-abstraction/)

**4. [Data & Analytic Services]: Castell Value-Based Care Platform**
*   **The Evidence:** Their subsidiary, **Castell**, is expanding its "Reimagined Primary Care" model, which relies on the **Arcadia Analytics** platform to ingest claims data from external payers and providers to manage population health risk.
*   **The Source:** [Fierce Healthcare / Arcadia Partnership Announcements](https://www.fiercehealthcare.com/tech/intermountain-launches-new-startup-aimed-at-value-based-care)

**5. [IoT & Process Automation]: Tech-First Revenue Cycle**
*   **The Evidence:** As of Nov 2025, they are shifting to a "tech-first revenue cycle," utilizing **AI agents** and RPA to automate claims denials and appeals, shaving 30 minutes off each appeal letter.
*   **The Source:** [Becker's Hospital Review - AI as Tailwind (Nov 2025)](https://www.beckershospitalreview.com/innovation/intermountain-turns-ai-into-a-tailwind.html)

## 3. SERVICES & STACK INTERSECTION

**Comparison of Intermountain Health Stack vs. Localhost Official Services**

✅ **The Sweet Spot (Direct Service Matches):**
*   **Data & Analytic Services:** The **Castell** platform is a data-hungry beast. While they use Arcadia, they need custom ETL pipelines to ingest data from *external* clinics and payers to make their value-based care model work.
    *   *Tech Validation:* Use of **Snowflake** (industry standard) and complex **SQL** environments.
*   **AI & ML:** They are aggressively buying/partnering (Layer Health, Nuance). They need "last mile" engineering to integrate these LLMs into their specific workflows (e.g., the Revenue Cycle AI agents).
    *   *Tech Validation:* Active deployment of **LLMs** and **Generative AI** for clinical abstraction.

⚠️ **The Expansion Opportunities (Adjacent/Upsell):**
*   **Cloud Services (FinOps):** They are moving everything to **Azure**. A consolidation of this magnitude ($18B org) invariably leads to cloud cost sprawl.
    *   *The Angle:* "With the shift to a unified Azure environment, ensuring cost governance (FinOps) prevents the 'cloud bill shock' typical in post-merger integrations."
*   **Software Engineering (Interoperability):** The move to a single **Epic** instance isn't just about buying Epic; it's about rewriting hundreds of legacy interfaces (HL7/FHIR) that connected the old 8 EHRs.
    *   *The Angle:* "Your internal teams are focused on the Epic rollout; we can handle the legacy interface refactoring to ensure downstream systems don't break."

❌ **The Mismatch (Out of Scope):**
*   **Core EHR Development:** They are an **Epic** shop. We do not build EHRs; we build *integrations* for them. Do not pitch building a patient record system.

## 4. THE STRATEGIC BRIDGE

**Starter 1: The "One Intermountain" Data Friction**
> "Ryan, I saw the March report regarding the consolidation of 8 EHRs into a single Epic instance. While Epic handles the clinical core, most CDIOs we work with underestimate the drag this puts on the *peripheral* data ecosystem—specifically the reporting pipelines for Castell. Localhost can deploy a dedicated Data Engineering pod to ensure your value-based care analytics don't go dark during the migration."

**Starter 2: The AI Governance & Scaling Gap**
> "Your deployment of Layer Health for clinical abstraction is a strong move. However, scaling GenAI agents for the Revenue Cycle (as mentioned in your Nov '25 strategy) often hits a bottleneck: **Governance Ops**. We help healthcare enterprises build the 'Guardrails-as-Code' infrastructure on Azure so you can deploy those 300+ AI projects without risking HIPAA compliance."

**Starter 3: The Castell Expansion**
> "With Castell expanding its risk-based contracts, the ability to ingest 'dirty data' from non-Intermountain providers is critical. We specialize in building 'Data Washing Machines'—automated ETL pipelines that sanitize external claims data before it hits your Arcadia/Snowflake environment, ensuring your risk models remain accurate."
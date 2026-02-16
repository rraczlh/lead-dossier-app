**Generated via BATCH on:** 2026-02-16 17:42:43.018858

```yaml
---
country: "Slovakia"
company_name: "AQUA PRO EUROPE, a.s."
verified_revenue_usd: 6
verified_revenue_text: "€6.13M (EUR)"
kdm_status: "Active"
detected_tech: ["Microsoft 365", "PHP (Web)", "PDA Software (Logistics)", "Google Analytics", "E-shop (Custom/CMS)"]
---
```

## 1. DATA VALIDATION (Excel vs. Current 2026)
| Data Point | Excel Value | Current (Feb 2026) | Verification Source |
| :--- | :--- | :--- | :--- |
| **Revenue** | €6,137,266 | **€6.1M - €6.5M** | [Valida.sk / Finstat (2024/2025 Data)](https://valida.sk/50886771) |
| **Key Decision Maker** | [Name] | **Ing. Radoslav Liker** (Chairman) | [ORSR.sk (Official Register)](https://www.orsr.sk/vypis.asp?ID=427063&SID=4&P=1) |
| **Status** | Active | **Hiring (Feb 2026)** | [Profesia.sk Job Listings](https://www.profesia.sk/praca/aqua-pro-europe/C42066) |

## 2. THE EVIDENCE BOX
**[Hiring]: Logistics & Mobile Workforce Signals**
*   **The Evidence:** Active recruitment for "Vodič" (Driver) positions as of Feb 5, 2026, explicitly requiring "práca s PDA" (work with PDA devices).
*   **The Source:** [Profesia.sk Job Listing (Feb 2026)](https://www.profesia.sk/praca/aqua-pro-europe/O42066)
*   **Localhost Service Map:** **Software Engineering** (Mobile Workforce Apps)

**[Product]: Internal R&D (SaniBox)**
*   **The Evidence:** The company developed "SaniBox," a mobile sanitation unit, internally. This demonstrates a willingness to invest in hardware/process innovation, creating an opening for IoT/Digital Twins.
*   **The Source:** [Aqua Pro Europe - History & Projects](https://aquapro.sk/o-nas/)
*   **Localhost Service Map:** **IoT & Process Automation**

**[Scale]: Distribution Network Complexity**
*   **The Evidence:** They operate **5 distribution centers** serving **3,000+ corporate clients** across Slovakia. This scale creates a specific data challenge regarding route optimization and inventory prediction.
*   **The Source:** [Aqua Pro Europe - Distribution Network](https://aquapro.sk/distribucia/)
*   **Localhost Service Map:** **Data & Analytic Services**

## 3. SERVICES & STACK INTERSECTION
Comparison of **AQUA PRO EUROPE** Stack vs. Localhost Official Services.

✅ **The Sweet Spot (Direct Service Matches):**
*   **Software Engineering (Mobile/Web):**
    *   *Why it fits:* They rely on a B2B Customer Portal and E-shop for orders. However, there is **no dedicated mobile app** for customers to manage water delivery or sanitation schedules.
    *   *Tech Validation:* Drivers use PDAs, implying an existing API/Backend that a modern Customer App could hook into.

⚠️ **The Expansion Opportunities (Adjacent/Upsell):**
*   **Data & Analytic Services (Logistics):**
    *   *The Angle:* With 5 depots and thousands of delivery points, they have a "Traveling Salesman Problem." We can pitch **Predictive Analytics** to optimize routes based on historical consumption data, reducing fuel costs.
*   **IoT & Process Automation:**
    *   *The Angle:* Their "Dolphin" water coolers are currently "dumb" devices. A strategic roadmap could involve retrofitting them with simple IoT telemetry to trigger auto-refills, locking in customers and automating the "Order -> Delivery" loop.

❌ **The Mismatch (Out of Scope):**
*   **Cloud Services (FinOps/Native):**
    *   *Reason:* Their revenue (~$6M) and likely on-prem/hybrid ERP setup suggest they are not ready for complex Cloud Native refactoring or FinOps. Basic "Lift & Shift" is the maximum scope here.

## 4. THE STRATEGIC BRIDGE
**Starter 1: The "Uber for Water" Trigger (Software Engineering)**
"Mr. Liker, I noticed your drivers use PDAs for logistics, but your 3,000+ corporate clients still likely order via web or phone. Localhost could build a 'My Dolphin' mobile app that allows office managers to scan a QR code on the cooler to instantly request a refill or sanitation, integrating directly with your existing logistics backend."

**Starter 2: The Efficiency Bottleneck (Data & Analytics)**
"Managing 5 distribution centers across Slovakia creates massive routing complexity. We've helped logistics companies use their historical delivery data to predict exactly *when* a client will run out of water before they even call. This reduces 'emergency runs' and optimizes your fuel spend."

**Starter 3: The Innovation Play (IoT)**
"I read about your internal development of the SaniBox unit—it shows you aren't afraid of R&D. Have you considered a pilot project to add low-cost telemetry to your premium water coolers? It would give you real-time consumption data and completely automate the re-ordering process."
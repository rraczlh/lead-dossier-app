**Generated via BATCH on:** 2026-02-03 15:49:05.017032

0. METADATA HEADER (YAML FRONTMATTER)
```yaml
---
company_name: "MAG (Manchester Airports Group)"
verified_revenue_usd: 1650
verified_revenue_text: "£1.3 Billion GBP"
kdm_status: "Active"
detected_tech: ["AWS", "Azure", "Java", "Spring Boot", "C#", ".NET", "Python", "Angular", "Databricks", "Terraform", "Docker", "ECS", "Xamarin", "MAUI", "PHP"]
overlap_tech: ["AWS", "Azure", "Java", "C#", "Python", "Angular", "Docker"]
primary_signals: ["Hiring Head of Data Engineering for CAVU", "Migration to Event-Based Architecture", "SaaS Product Expansion (Propel)"]
---
```

1. DATA VALIDATION (Excel vs. Current 2026)
| Data Point | Excel Value | Current (Jan 2026) | Verification Source (Title/Link) |
| :--- | :--- | :--- | :--- |
| **Revenue** | 1000000000.0 | **£1.3 Billion (FY25)** | [MAG delivers record year as investment plans continue (July 2025)](https://marketingstockport.co.uk/news/manchester-airports-group-delivers-record-year-as-investment-plans-continue/) |
| **Key Decision Maker** | CIO | **Nicholas Woods (CIO)** | [In conversation with Nicholas Woods, CIO at MAG](https://www.internationalairportreview.com/article/179839/in-conversation-with-nicholas-woods-cio-at-manchester-airports-group/) |
| **Digital Arm** | N/A | **CAVU** | [About CAVU - MAG's Global Travel Services Business](https://magairports.com/company/cavu) |

2. THE EVIDENCE BOX (High-Signal Items 2025-2026)

**[Hiring]: Head of Data Engineering (CAVU)**
*   **The Evidence:** MAG's digital division, CAVU, is hiring a Head of Data Engineering to build a "centralised data engineering function" using **AWS** and **Databricks**. The role explicitly demands "Medallion Architecture" and moving to a "fully event-based architecture."
*   **The Source:** [MAG Careers - Head of Data Engineering Job Description](https://careers.magairports.com/jobs) (Verified via Snippet 1.20)
*   **Mapping-2-Localhost Service:** Data Science & ML (Core: Python/Pandas) + Cloud DevOps (AWS Infrastructure).

**[Architecture]: Technical Solutions Architect (AWS/SaaS)**
*   **The Evidence:** Hiring architects to oversee the **Propel** platform (SaaS booking engine). Requirements include **AWS** (EC2, ECS, Fargate), **Docker**, and **PHP/.NET** modernization. The role focuses on scaling the platform to support "onboarding hundreds of new airports."
*   **The Source:** [Parking.net - Technical Solutions Architect Job Listing](https://www.parking.net/job/technical-solutions-architect-manchester-hybrid-uk) (Verified via Snippet 1.24)
*   **Mapping-2-Localhost Service:** Cloud DevOps (AWS, Docker) + Application Development (Backend: .NET Core).

**[Modernization]: Legacy .NET to Cloud-Native**
*   **The Evidence:** Recruitment for "Lead Software Engineers" to re-platform legacy systems. Specific mentions of **C#**, **.NET**, and integrating with **Azure** environments, moving away from monolithic structures to microservices.
*   **The Source:** [TotalJobs - Senior Software Engineer (.NET/Azure)](https://www.totaljobs.com/jobs/software-engineering/in-manchester) (Verified via Snippet 1.9)
*   **Mapping-2-Localhost Service:** Application Development (Backend: .NET Core) + Cloud DevOps (Azure).

3. TECH STACK INTERSECTION

✅ **The Sweet Spot (Direct Matches):**
*   **Cloud Infrastructure:** **AWS** (Primary for CAVU/Digital) and **Azure** (Corporate/Legacy).
*   **Backend Engineering:** **Java (Spring Boot)** and **C# (.NET Core)** are the core languages for their booking and operational systems.
*   **Frontend:** **Angular** is explicitly cited in developer roles, aligning with our Frontend capability.
*   **Containerization:** **Docker** and **ECS** are standard in their new architecture.

⚠️ **The Expansion Opportunities (Adjacent Tech):**
*   **Databricks:** They are heavily investing in Databricks for their data lake. While not in our "Core" list, our **Python/Pandas** expertise allows us to staff the *pipelines* and *analytics* layers running on top of their Databricks infrastructure.
*   **Terraform:** They use Terraform for IaC. We list **CDK/CloudFormation**. This is a prime opportunity to either adapt to Terraform (low lift) or pitch CDK for their AWS-native "Propel" SaaS product for better integration.

❌ **The Mismatch:**
*   **Mobile Frameworks:** They are currently using **Xamarin** and **.NET MAUI** for mobile apps (e.g., fuel delivery platforms). Localhost specializes in **React Native** and **Flutter**. This is a specific "Rewrite/Modernization" pitch opportunity, as Xamarin is nearing end-of-life/legacy status compared to React Native.
*   **PHP:** They still have significant PHP legacy code in the CAVU booking engine. We support PHP, but the strategic value is likely migrating this to **Node.js** or **.NET Core**.

4. THE STRATEGIC BRIDGE (Consultative Synthesis)

**Conversation Starter 1: The "Propel" SaaS Scaling Friction**
*   **The Trigger:** CAVU is aggressively selling its "Propel" booking platform to 300+ other airports, requiring massive multi-tenant scalability (evidenced by the "Technical Solutions Architect" search).
*   **The Logical Friction:** Onboarding "hundreds of new airports" onto a single platform often breaks legacy CI/CD pipelines and creates data isolation nightmares. They are likely struggling with tenant provisioning speed.
*   **The Partnership Angle:** Localhost's **Cloud DevOps** pods can deploy a "Tenant-per-Container" strategy using **AWS ECS** and **GitHub Actions**, decoupling their deployment logic to allow rapid onboarding without destabilizing the core platform.

**Conversation Starter 2: The Databricks "Medallion" Gap**
*   **The Trigger:** The search for a "Head of Data Engineering" to implement a "Medallion Architecture" (Bronze/Silver/Gold data layers) on Databricks.
*   **The Logical Friction:** Finding a single leader is hard; building the *team* to execute the cleaning, transformation, and governance of that data is harder. They likely have a backlog of raw data (Bronze) that isn't making it to analytics (Gold) fast enough.
*   **The Partnership Angle:** We can deploy a **Python/Pandas** data squad immediately to build the ETL pipelines feeding their Databricks Silver/Gold layers, unblocking their Data Science team to focus on passenger flow prediction models.

**Conversation Starter 3: The Mobile Modernization (Xamarin to React Native)**
*   **The Trigger:** Their reliance on **Xamarin/MAUI** for operational apps (Fuel Delivery, etc.).
*   **The Logical Friction:** Microsoft's support for Xamarin has ended/shifted, and the developer pool is shrinking. Maintaining these apps is becoming a technical debt liability, and user experience likely lags behind modern consumer standards.
*   **The Partnership Angle:** Localhost can execute a "Strangler Fig" migration, rewriting high-impact mobile modules in **React Native** (which we support) to improve field-staff efficiency, while slowly retiring the .NET mobile codebase.
# Research topic: literature map and revised shortlist (5 October 2026)

Kristiyan's brief: a topic that hasn't been researched yet, with enough adjacent research to support analysis and conclusions. He prefers **B**, AI in investment-committee and underwriting decisions (the investment context), and **D**, AI, price discovery and heterogeneous assets (the technical angle).

The novelty checks below come from web searches in October 2026. Before submitting, re-check them in Google Scholar or Scopus through iDiscover, Cambridge's library catalogue.

## The key source: the gap is stated in the literature
**Seagraves, Seiler and Sirmans (2026), "The Agentic Frontier: Artificial Intelligence in Commercial Real Estate", *Journal of Real Estate Research*.**
- They classify 66 CRE AI papers by four market frictions (opacity, search costs, illiquidity, **heterogeneity**) and by method. **Half of the friction-by-method cells are empty.**
- There is "strong evidence that AI improves prediction but **almost none that better prediction reduces frictions or changes market outcomes**."
- Anthropic Economic Index data on 324 tasks in 16 CRE occupations show AI use on information-processing tasks, but **none on tasks that need professional judgement**. The authors call this boundary the "agentic frontier".

This paper serves as the research-context paragraph: the most recent review says plainly that the question is unanswered.

## Literature map (the existing research to build on)

**1. AI prediction in CRE (well established)**
- Deppner, von Ahlefeldt-Dehn, Beracha and Schaefers (2023/2025), *JREFE*: ML finds structured error in NCREIF office, retail and industrial appraisals, improves accuracy and removes bias. The first ML study beyond residential and multifamily.
- Francke and van de Minne (2024), *Real Estate Economics* 52(5): hybrid ML and econometrics gives an out-of-sample MAPE below 11% on CRE transactions, competitive with appraisals.
- Lorenz, Willwersch, Cajias and **Fuerst** (2023), *REE*: interpretable ML for real estate market analysis. Fuerst is at Land Economy.
- **Wan and Lindenthal** (2023), *REE* 51(3): the "accountability gap" in ML models; cross-validation is not enough in regulated settings. Lindenthal is at Land Economy.
- Leow and **Lindenthal** (2025), *REE*: ML forecasts of REIT returns.

**2. The limits of algorithms in heterogeneous assets (emerging)**
- Buchak, Matvos, Piskorski and Seru (forthcoming, *JPE*; NBER WP 28252), on iBuyers: algorithmic pricing is profitable only for **liquid, easy-to-value** houses. Hard-to-code attributes cause adverse selection. This is housing only, and no CRE equivalent exists.
- AVM accuracy research (Rossini and Kershaw; Matysiak for TEGoVA): error rises with heterogeneity and omitted "soft" attributes.
- Garmaise and Moskowitz (2004), *RFS* 17(2): information asymmetry in CRE.
- Stein (2002), *JF*; Liberti and Petersen (2019), *RCFS*: **hard versus soft information**. Hierarchical organisations rely on hard information. This is the theoretical lens.

**3. How people use algorithmic advice (established in psychology, thin in CRE)**
- Anchoring in valuation: Northcraft and Neale (1987); Diaz and Hansz; Diaz and Wolverton (1998).
- Dietvorst, Simmons and Massey (2015), algorithm aversion; Logg, Minson and Moore (2019), algorithm appreciation.
- Kmen, Navratil, Kattenbeck and Giannopoulos (2026), *Scientific Reports*: 13 experts valuing Vienna **residential** apartments; the human–ML hybrid was most accurate. **This is the closest prior experiment.**
- Jaklis (2025), MIT Sloan thesis: a US survey in which 44% say their investment committees distrust AI analysis and 27% trust it. Descriptive only.

**4. Systemic risk and governance**
- Danielsson, Macrae and Uthemann (2022), *JBF*: AI and systemic risk, monoculture and procyclicality. Kleinberg and Raghavan (2021), *PNAS*: algorithmic monoculture.
- Calder-Wang and Kim (2024): algorithmic rent pricing improves efficiency **and** coordinates prices (US multifamily).
- Bank of England and FCA (2024), *AI in UK financial services*: 75% of firms use AI and a third of use cases are third-party. Only 34% fully understand the models they use. The Bank flags herding and concentration risk.
- RICS (effective 9 March 2026), *Responsible use of AI in surveying practice*: a named surveyor must take responsibility for AI output. PRA SS1/23 on model risk management is a governance benchmark.

**5. The real estate investment decision process (established, but predates AI)**
- Roberts and Henneberry (2007), *JPIF*: a ten-stage normative decision model covering France, Germany and the UK. Parker (2016): Australian unlisted funds. Gallimore et al.: behavioural factors.

## Revised shortlist

| # | Topic | Gap (not yet studied) | Base to build on | Method and data | Feasibility |
|---|---|---|---|---|---|
| **1 (recommended)** | **"Where the algorithm stops": asset heterogeneity and how judgement is split between AI and people in CRE investment committees** (B + D) | No study of how **CRE** investment committees accept, adjust or override AI underwriting inputs, or whether heterogeneity sets that boundary. Seagraves et al. name the judgement frontier as untested. | Groups 1, 2, 3 and 5; governance from group 4 | Vignette experiment with 40–60 UK investment professionals in a 3 × 2 design (no AI / AI point estimate / AI estimate with uncertainty band and explanation × low or high heterogeneity asset), plus 10–12 interviews with committee members, leading to a **governance framework** | High. No proprietary data needed. Needs ethics approval and network access. |
| 2 | **A heterogeneity penalty for AI valuation?** Does ML error in UK CRE rise measurably with asset heterogeneity? (pure D) | No study measures how ML error changes with heterogeneity in CRE, or in the UK. | Groups 1 and 2 | Quantitative: build a heterogeneity index and test how error varies with it, using transaction data (CoStar, MSCI/RCA or EGi) | Medium. **Depends on data access and Python or R skills.** |
| 3 | **Algorithmic monoculture in CRE**: do shared data platforms and AI tools make underwriting assumptions converge? | No real estate study. Regulators raise the herding risk in general. | Groups 4 and 2, plus valuation smoothing (MSCI valuation versus sale price) | Experiment measuring the spread of ERV and exit-yield assumptions with and without shared AI output, plus interviews | Medium-high. **Can be folded into option 1 as a second outcome.** |
| 4 | **Accountability for AI-informed investment decisions** under the RICS 2026 standard (governance and law) | The standard is new. No study of how responsibility is shared between valuer, committee, vendor and investor. | Group 4 and professional negligence case law | Doctrinal and qualitative analysis with interviews | High, but less technical |

Dropped from the first list:
- **C (algorithmic rent-setting):** the US is now well covered (Calder-Wang and Kim, the RealPage litigation), and it fits B and D less well.
- **E (due diligence):** there is too little academic literature to build on.
- **A (valuation liability):** merged into option 4.
- **F (retail distress):** kept apart from the AI theme.

## Recommendation
Option 1, with option 3's measure of how far assumptions spread included as a second outcome. It combines the investment context (B) with the technical heterogeneity angle (D). It answers a gap that a 2026 review states directly. It gives a framework, which is what the template asks for, and it's feasible within an MSt. Supervisor fit: Lindenthal (ML accountability and testing) and Fuerst (interpretable ML).

## Open questions for Kristiyan
1. Data access at Hay Wain or Modella: CoStar, MSCI/RCA, EGi/Radius, LonRes? (Decides whether option 2 is viable.)
2. Python, R or statistics skill level?
3. Could you realistically recruit 40–60 UK investment professionals for a 15-minute online experiment?
4. Does Hay Wain or Modella already use AI in underwriting or committee papers? Did you lead any of it? (This is also strong material for the personal statement.)

## Kristiyan's answers (6 October 2026)
1. Data access (CoStar, MSCI and similar): yes, or will have it by the time the course starts.
2. Python and R: none yet.
3. Recruiting 40–60 professionals for an experiment: very achievable.
4. **Hay Wain used no AI before he joined. He led the work that built AI into Hay Wain's processes across several workflows.** (Leadership material for the personal statement.)
- He likes option 1 but wants it **more technical**, and asked for several variants.

## More technical variants of option 1 (6 October 2026)
More novelty checks: LLM valuation studies are almost all residential, e.g. "On the performance of LLMs for real estate appraisal" (2025) and "Incorporating LLMs in automated real estate valuation" (*JRER* 2025). One non-UK CRE paper uses features derived from language models (the HSE multimodal model). Shen and Ross (2021, *JUE*) measured the value of soft information in **housing** descriptions. Conformal prediction for AVMs has only been applied to residential (e.g. Hjort et al. 2022; spatially weighted CP 2023; *JREFE* 2024). **Nobody has tested any of these on UK CRE, or as a function of heterogeneity.**

- **1A, mapping the frontier (recommended):** build a heterogeneity index for UK CRE deals. Value a hold-out set of transactions three ways: a gradient-boosted model, an LLM or agent underwriter, and human professionals (the experiment). Estimate how error changes with heterogeneity for each, and find the crossover point where humans add value. The output is a delegation framework for investment committees.
- **1B, LLM underwriter benchmark:** test frontier LLMs and agents against human underwriting on real anonymised UK deals with known outcomes, stratified by heterogeneity. Measure accuracy, calibration and hallucinated assumptions. Low coding, high novelty.
- **1C, soft information:** use LLMs to measure the soft information in CRE marketing brochures, IC papers and leases (the Shen and Ross method applied to CRE). Test whether it explains the pricing residual left by hard data, and whether that effect grows with heterogeneity.
- **1D, calibrated uncertainty in decisions:** add conformal prediction intervals to an ML valuation model for UK CRE. Test experimentally whether showing calibrated uncertainty, rather than a point estimate, reduces anchoring and improves committee decisions, and whether intervals widen with heterogeneity.

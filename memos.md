**Memo on “Accepting automated small syntactic changes”**

The participant in this code (n=1; P22) discussed automated transformations with a clear distinction between small syntactic updates and deeper structural refactoring. The emphasis does not lie on automation as a general good, but on the conditions under which it becomes acceptable and safe.

P22 explicitly framed automation as dependent on strong testing guarantees. They stated that “you have to have full coverage of the tests” and that after refactoring, “you have to be certain that the behavior does not change.” The participant directly connected this requirement to regression testing and almost complete test coverage. In their view, this is rarely achieved in industrial projects. This observation introduces a practical constraint. Even if tools exist, organizational and technical preconditions often limit their safe use.

Within this context, P22 differentiated between types of changes. They considered “small syntactic changes” acceptable when they are mechanically verifiable and low risk. The example of adding the override keyword in C++ 11 illustrates this point. According to P22, inserting such a keyword with an automatic tool is “almost trivial” and “you hardly can mess up anything with that.” Here, the participant explicitly tied acceptability to trivial detectability and minimal semantic risk. The justification is efficiency. Doing this manually would be “a waste of time.”

However, the participant drew a firm boundary when discussing higher-level refactorings. Changes such as reorganizing inheritance structures or replacing raw pointers with smart pointers require a “very high-level understanding of the code.” P22 clearly stated that “no tool can do this at the moment.” This does not reject automation entirely. Instead, it introduces a distinction between surface-level syntactic augmentation and semantic restructuring. The former is positioned as safe and pragmatic under test coverage, while the latter demands human judgment.

Interestingly, P22 also reflected on technological evolution. They mentioned static analyzers and symbolic execution as examples of advances once considered impossible. They speculated that stronger automation may become feasible in the future. Still, they remained cautious about short-term expectations, stating that in the next five to ten years they do not foresee widespread applicability of such advanced automated refactoring tools.

This code therefore captures a nuanced acceptance stance. P22 does not reject automation. They accept it when changes are syntactically bounded, low risk, and verifiable through tests. They reject or question it when changes alter structural or semantic aspects that require contextual reasoning about the program. The central analytic tension in this code concerns risk control versus efficiency. Automation is acceptable when it reduces manual effort without threatening behavioral stability.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P22

**Memo on “Analyse costs/benefits before rejuvenate”**

This code aggregates 38 quotations from 22 participants. Across interviews, survey responses, and pull request discussions, participants consistently described rejuvenation as a decision that requires deliberate evaluation rather than automatic adoption of new versions or features.

A central theme concerns weighing effort against benefit. Several participants explicitly stated that migration or refactoring only makes sense when there is a clear and meaningful gain. P02 emphasized the need to analyze “whether an evolution is worthwhile,” considering performance, readability, or potential issues. P12 similarly argued that one cannot update “because this version is new,” but must evaluate the impact on project stability. P25 described concrete trade-offs, noting that spending two days refactoring for marginal improvement may conflict with sprint demands. P29 framed evolution in terms of “cost and time,” highlighting that management may resist paying for changes that do not immediately solve visible problems.

Time constraints emerged as a recurring constraint. P21 directly identified time as the “main issue,” especially when handling multiple demands alone. P03 discussed balancing new functionality requests with language evolution, often giving lower priority to upgrades. C++ Surveys responses reinforced this pattern by noting the difficulty of securing budget and time for modernization unless code quality has significantly degraded. Together, these statements show that rejuvenation competes with feature delivery and operational continuity.

Risk perception also played a prominent role. Participants frequently mentioned instability, regression, and unintended bugs. P18 warned that updates may introduce new defects into previously stable code. P07 and P04 stressed that large or widely used code bases require careful validation because revalidation can be costly and disruptive. P17 highlighted situations in which deprecations accumulate and force large, non-incremental migrations. Pull request data reflects similar caution. The JavaScript PR discussions quote described avoiding ES6 features due to transpilation overhead, while the Python PR discussions quote warned that certain changes could make tests “onerous.” These excerpts illustrate how developers consider tooling overhead and maintenance burden as part of the cost calculus.

Dependencies and compatibility further shape the evaluation process. P23 and P26 described challenges in aligning third-party libraries with new language versions. Migration often requires checking whether each dependency supports the target version. P25 mentioned fear that production servers may not support a newer Java version, creating operational risk. These statements indicate that rejuvenation decisions extend beyond source code and involve infrastructure and deployment constraints.

However, participants did not describe the decision process as purely defensive. Some emphasized proactive reasoning. P08 argued that delaying migration increases long-term cost and advocated incremental updates. P22 identified specific triggers that justify change, such as improved safety, reduced external dependencies, or measurable performance gains. P20 noted that certain constructs, like compile-time improvements, provide tangible benefits. P13 and P26 suggested that when a feature clearly solves a problem or reduces code complexity, adoption becomes more attractive, though still subject to contextual judgment.

Project maturity and organizational culture also influence decisions. P13 compared an older Python 2 system with a newer Kotlin project, observing that younger projects offer greater flexibility for updates. P03 contrasted companies with structured technical debt allocation against those that require detailed planning for any migration. These observations indicate that cost–benefit analysis occurs within organizational processes, not only at the technical level.

Across these quotations, the code captures rejuvenation as a negotiated decision shaped by time, risk, expected benefit, project scale, dependency constraints, and organizational priorities. Participants consistently described a reflective process. They evaluate gains such as safety, performance, readability, and reduced dependency burden against costs including regression testing, instability, team coordination, infrastructure compatibility, and opportunity cost. The decision to rejuvenate rarely appears automatic. Instead, it depends on thresholds that vary by language, project type, and business context.

This code therefore represents a core decision mechanism within source code rejuvenation. Before acting, developers calculate effort, risk, and value. Adoption occurs when perceived benefit clearly outweighs cost under the specific constraints of the project.

**Memo metrics**

* Total quotations in this code: 38

* Total participants in this code: 22

* Participants: C++ Surveys, JavaScript PR discussions, Python PR discussions, P02, P03, P04, P05, P07, P08, P09, P12, P13, P14, P17, P18, P20, P21, P22, P23, P25, P26, P29

**Memo on “application domain may influence SCR efforts”**

This code includes 2 quotations from a single participant (P12). In both excerpts, P12 explicitly linked rejuvenation decisions to the nature of the application domain, particularly low-level and critical systems.

P12 emphasized that working at a low level changes the tolerance for change. They stated that “when there are low-level programming difficulties, that disturbs the chain of a whole product,” and used the example of a flaw in the Linux kernel that “destroys everything from there.” In this framing, low-level components propagate impact upward. A small defect can affect the entire product line. As a result, adoption of new functionality occurs only if it is “advantageous and if its impact is not big.”

In the second quotation, P12 reinforced this caution through an analogy with mechanical engineering. They mentioned car engines or gears used for 40 or 50 years because they are already tested and reliable. They clarified that the issue is not that new functionality is inherently unreliable. Rather, reliability must be demonstrated over time before adoption in critical layers. Until that reliability is proven, implementation at the low level is unlikely.

Across these quotations, the participant did not describe cost, time, or fashion as primary drivers. Instead, reliability and system-wide impact dominate the reasoning. The application domain shapes thresholds. In low-level and critical systems, stability outweighs novelty. Even beneficial features must pass a stricter filter.

This code therefore captures how technical criticality constrains rejuvenation. The same feature that might be easily adopted in a less critical layer faces stronger scrutiny in foundational components. The domain defines acceptable risk and directly influences whether rejuvenation occurs.

**Memo metrics**

* Total quotations in this code: 2

* Total participants in this code: 1

* Participants: P12

**Memo on “Avoiding system obsolescence”**

This code includes 14 quotations from 11 participants. Across these excerpts, participants framed rejuvenation as a way to prevent systems from becoming outdated, unsupported, or progressively harder to maintain.

Several participants explicitly linked modernization to long-term maintainability. P19 described modernization as “a process of evolution” and connected it to preventing degradation over time. They highlighted that newer versions, together with unit tests and coverage, help counter code decay. P23 similarly noted that legacy code written years ago often requires adaptation to support new language features, especially when deprecated constructs remain in use.

Support discontinuation emerged as a recurring concern. P03 and P01 pointed out that providers discontinue support for older versions, including security and bug maintenance. P01 emphasized that keeping an unsupported version has “no meaning” once security maintenance ceases. P05 stressed migrating to long-term support versions to guarantee stability for future years. P06 introduced a concrete example from the Google Play platform, where outdated libraries can lead to rejection or banning. These quotations show that obsolescence is not only technical but also institutional. External policies and vendor schedules can force updates.

Participants also described reputational and practical consequences of falling behind. P01 mentioned the desire not to appear obsolete and to remain aligned with current standards. P26 stated that migration helps reduce the burden of legacy code and keeps the system “on par with what is done in software in general.” The C++ Surveys excerpt was particularly explicit, noting that if periodic updates are not performed, “the software will get old and will die.” This language indicates a perception that stagnation threatens project survival.

Performance and security improvements also intersect with obsolescence concerns. P11 discussed evolving code to gain new features, performance gains, and security bug fixes, and to avoid the “trauma of migration” after falling several versions behind. The example of Ruby’s garbage collector improvement illustrates how performance evolution can justify staying updated. In this sense, avoiding obsolescence is not merely reactive. It is also preventive. Regular updates reduce the accumulated cost of large migrations.

At the same time, participants did not present rejuvenation as automatic. The quotations imply that teams assess version maturity, support status, and long-term viability. However, once a version becomes unsupported or too outdated, inaction is framed as risky.

This code therefore captures a longitudinal concern. Developers and teams modernize not only to gain immediate benefits, but to prevent progressive decay, loss of support, incompatibility with platforms, and increasing migration cost. Avoiding obsolescence functions as a strategic motive that extends beyond single feature adoption.

**Memo metrics**

* Total quotations in this code: 14

* Total participants in this code: 11

* Participants: C++ Surveys, P01, P03, P05, P06, P11, P19, P22, P23, P24, P26

**Memo on “CI pipeline incompatibility with modern features”**

This code contains a single quotation from one source (Python PR discussions). Although brief, the statement captures a concrete tension between adopting a modern language feature and the constraints imposed by the integration environment.

The quotation states: “CI is unhappy about type hints.” In this excerpt, the participant directly attributed resistance to the continuous integration pipeline rather than to the developer’s personal preference. The wording suggests that the introduction of type hints triggered a failure, warning, or incompatibility within the automated validation process. The phrase “is unhappy” reflects a pragmatic obstacle: the pipeline does not accept or correctly process the new construct.

This quotation does not elaborate on the specific technical cause. It does not clarify whether the issue relates to tooling configuration, Python version support, static analysis rules, or linting constraints. However, it clearly shows that modern features may face institutional or tooling barriers. Even when a feature is available in the language, its adoption depends on alignment with build scripts, test runners, and validation rules embedded in CI workflows.

In this code, the decision point does not revolve around readability, performance, or developer preference. Instead, the constraint lies in automated infrastructure. The CI pipeline acts as a gatekeeper. If it rejects or flags the feature, developers must either adjust the pipeline, revert the feature, or postpone adoption.

This code therefore highlights a procedural dimension of source code rejuvenation. Adoption of modern features requires compatibility not only at the language level but also at the integration and validation level. Infrastructure readiness becomes a prerequisite for change.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: Python PR discussions

**Memo on “Backward compatibility constraints hindering SCR”**

This code aggregates 29 quotations from four sources: C++ Surveys, JavaScript PR discussions, Python PR discussions, and P25. Across these excerpts, participants described backward compatibility as a concrete constraint that limits or postpones the adoption of modern language features.

A dominant pattern appears in the JavaScript pull request discussions. Contributors repeatedly rejected or reverted ES6 and later constructs because the project explicitly supports ES5 or older browser environments. Statements such as “we don't yet support ES2015,” “let is ES6 syntax so this needs to be var,” and “we can’t use arrow syntax because that’s only in ES6” show that modern syntax is consciously avoided. The reason is not aesthetic preference but platform support. Older browsers, legacy environments, or tools such as PhantomJS, Node 4, or Internet Explorer constrain available syntax. In several excerpts, developers even reference compatibility tables or issue numbers to justify reverting to older constructs.

Similarly, Python PR discussions excerpts show constraints tied to supported Python versions. Developers explicitly postponed using f-strings, union syntax with X | Y, yield from, or newer annotation styles until older Python versions such as 3.5 or 3.6 are dropped. One participant stated, “I’d rather do that when we drop Python 3.5 support.” This phrasing indicates a staged strategy. Adoption becomes possible only after official support for older versions ends.

The C++ Surveys excerpt reinforces this pattern at the library level. A project maintained compatibility with older Qt versions because a known user depended on Qt 5.6. This decision “prohibited some new constructions from being used.” Here, backward compatibility extends beyond language syntax and includes third-party library ecosystems and user bases.

P25 framed the issue more generally, noting that moving from Java 8 to Java 21 may cause code to break due to changes in behavior or removed constructs. The participant identified compatibility as “the biggest point,” suggesting that version jumps may produce widespread breakage.

Across all quotations, backward compatibility appears as an explicit boundary condition. Developers do not reject modern features in principle. Instead, they describe a project-level obligation to maintain support for older runtimes, browsers, or dependent clients. As long as such obligations remain, rejuvenation is either limited, deferred, or implemented through workarounds.

This code therefore captures a structural tension. Language evolution introduces new constructs, but project commitments to existing platforms restrict their immediate adoption. Rejuvenation becomes feasible only when support policies change, older environments are phased out, or compatibility layers are removed.

**Memo metrics**

* Total quotations in this code: 29

* Total participants in this code: 4

* Participants: C++ Surveys, JavaScript PR discussions, Python PR discussions, P25

**Memo on “bug fixes in the language implementation”**

This code contains a single quotation from one participant (P11). Although brief, the statement positions bug fixes in the language or platform as a direct motivation for updating applications.

P11 stated: “I'm always updating my application for several reasons, among them: bug fixes, and other problems arising from the aging of the code, and the lack of technical support over time.” In this excerpt, updating is not framed as optional enhancement but as routine maintenance. Bug fixes are listed alongside aging and loss of support, suggesting that defects and maintenance gaps accumulate over time.

The participant did not differentiate between bugs in user code and bugs in the language implementation itself. However, the wording implies that newer versions address known issues and that staying on older versions may expose the application to unresolved defects. Updating therefore becomes a preventive action.

In this code, rejuvenation is linked to reliability and continuity. The driver is not novelty or new functionality. Instead, it is the need to correct errors and maintain alignment with supported versions. The participant presents updating as a recurring practice rather than a one-time event.

This code highlights a maintenance-oriented motive within source code rejuvenation. Language-level bug fixes act as a trigger for upgrading, especially when older versions no longer receive technical support.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P11

**Memo on “code standards might prevent source code rejuvenation efforts”**

This code contains 5 quotations from JavaScript PR discussions. Across these excerpts, contributors described how established coding standards and project conventions restrict the introduction of modern constructs.

In several quotations, reviewers requested replacing ES6 arrow functions with traditional function syntax. The reasons include consistency with the existing codebase and alignment with project style. One contributor stated they “always try to follow the pattern of existing code” and therefore used var instead of modern constructs. Another explicitly emphasized that pull requests “should be concise” and avoid unrelated stylistic modernization.

Beyond stylistic consistency, contributors raised concerns about contributor accessibility and readability. One reviewer questioned whether shortened arrow syntax justifies “upping the JavaScript reading level for contributors,” especially when many contributors may not use JavaScript as their primary language. The concern centers on inclusiveness and shared understanding rather than purely technical correctness.

Compatibility and tooling implications also appeared. A reviewer noted that arrow functions may be transpiled into additional code and could create issues in older environments such as IE8. Even when acknowledging potential benefits of arrow functions in certain contexts, contributors questioned whether isolated modernization makes sense if hundreds of other anonymous functions remain unchanged.

Across these quotations, coding standards function as stabilizing constraints. Contributors prioritize consistency, readability for the current contributor base, and avoidance of unnecessary stylistic divergence. Modern features are not rejected outright, but their adoption requires alignment with established conventions and project-wide agreement.

This code therefore illustrates how local governance and stylistic norms can limit rejuvenation. Even when a language feature is technically available, standards and contributor expectations may delay or prevent its use.

**Memo metrics**

* Total quotations in this code: 5

* Total participants in this code: 1

* Participants: JavaScript PR discussions

### **Memo on “Companies may not consider SCR efforts Relevant”**

This code includes 2 quotations from P23 and P25. Both participants framed source code rejuvenation as potentially undervalued within company settings.

P23 described situations in which companies question why they should “pay you a month’s salary for doing practically nothing other than enhancing your code.” In this view, modernization is not easily monetizable. The company “cannot resell it just because it's written in the newer language.” The participant also noted structural constraints, such as deprecated dependencies with no newer alternatives, which further limit change.

P25 reinforced this delivery-oriented framing. They explained that in a company scenario, “you need to deliver,” and that improvements not explicitly requested may delay visible progress. Showing that a demand is completed can be more valued than internal improvements.

Across both quotations, rejuvenation is positioned as secondary to business deliverables. The issue is not technical feasibility but perceived business relevance. If modernization does not clearly translate into customer-visible value or revenue, it may be deprioritized.

**Memo metrics**

* Total quotations in this code: 2

* Total participants in this code: 2

* Participants: P23, P25

### **Memo on “Company Restrictions may hinder SCR efforts”**

This code includes 2 quotations from P23 and P25. The excerpts describe explicit organizational and regulatory constraints that prevent language evolution.

P23 provided an example from the automotive industry. They described formally validated compilers and industrial regulations that restricted moving from C++ 2003 to C++ 11\. Some clients “cannot purchase or order code that has C++ 11 features.” In this case, language evolution conflicts with certification requirements and external contractual obligations.

P25 described internal process restrictions. In sprint-based workflows, developers “don’t change things that are not related to a specific demand.” Modernization outside the defined task scope is not permitted. This reflects procedural limitation rather than technical impossibility.

Together, these quotations show that constraints may stem from legal standards, certification processes, or internal development policies. Even when developers see technical advantages, organizational rules can block adoption.

**Memo metrics**

* Total quotations in this code: 2

* Total participants in this code: 2

* Participants: P23, P25

### **Memo on “Company/Team decision-making”**

This code contains 12 quotations from 7 participants. The excerpts consistently describe language evolution as a collective decision rather than an individual action.

P20 stated they have “never seen” external executives mandate language feature adoption. Instead, initiative typically comes from developers who follow language evolution and propose improvements. The team evaluates and decides collectively.

P01 emphasized that updates usually follow “corporate criteria” and that teams may not have full freedom to change language versions independently. P03 compared companies with structured allocation for technical debt against those requiring detailed planning for any migration. C++ Surveys responses described project-level autonomy, but also coordination through mailing lists and shared standards across related projects.

P29 mentioned that a boss or president may make final decisions, even if teams manage technical discussions.

Across these quotations, decision-making appears multi-layered. Developers propose, teams deliberate, maintainers or management approve, and processes mediate change. Rejuvenation depends on governance structures, project maturity, and internal alignment.

**Memo metrics**

* Total quotations in this code: 12

* Total participants in this code: 7

* Participants: C++ Surveys, P01, P03, P05, P07, P20, P29

### **Memo on “Core-driven rejuvenation”**

This code contains 1 quotation from C++ Study. The excerpt reports that 63.63% of responding developers were among top contributors in KDE projects and that top developers were responsible for 63.2% of rejuvenation commits.

The data indicates concentration of rejuvenation efforts among highly active contributors. Rather than evenly distributed modernization, core developers appear to lead such changes. The quotation does not speculate on motivations but quantitatively associates rejuvenation with central contributors.

This suggests that influence, experience, or commit authority may correlate with modernization activity. The excerpt presents rejuvenation as disproportionately driven by top developers within the project structure.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: C++ Study

### **Memo on “Delayed adoption of new versions”**

This code includes 19 quotations from 13 participants and study excerpts. The dominant pattern is time lag between release and adoption.

P20 described intentionally staying behind newer C++ standards to ensure stability. P22 explicitly mentioned “three, four years delays” before using new C++ features. P11 stated preference for mature LTS versions in mission-critical systems. P26 reported waiting until versions become consolidated and standardized before migration.

P01 and P03 linked delays to time constraints and workload. P24 mentioned team resistance and infrastructure constraints when proposing migration to Java 21\. JavaScript PR discussions included reluctance to use “optional chaining because it is too new.”

Empirical study excerpts (JavaScript Study and Python Study) quantified multi-year delays between feature release and generalized adoption. Python 3.0 features showed delays of several years, and JavaScript features exhibited gradual integration after release.

Across qualitative and quantitative evidence, delay emerges as a pattern tied to stability, maturity, tooling support, and organizational readiness. Adoption often follows consolidation rather than immediate release.

**Memo metrics**

* Total quotations in this code: 19

* Total participants in this code: 13

* Participants: C++ Surveys, JavaScript PR discussions, JavaScript Study, Python Study, P01, P09, P11, P13, P20, P22, P24, P26, P27

**Memo on “Developer expertise mediates the impact of LLMs on development practices”**

This code includes one quotation from P29. The participant described the usefulness of AI and LLM tools as dependent on the developer’s level of expertise. Rather than presenting AI as inherently beneficial or harmful, the participant framed its value as conditional on how developers use it.

P29 suggested that excessive reliance on AI tools may lead developers to remain at an average or “mediocre” level of practice. In contrast, developers who understand the limitations of these tools and use them selectively can extract meaningful benefits from them.

The quotation indicates that expertise functions as a moderating factor in the interaction between developers and AI-assisted programming tools. The impact of these tools is therefore not uniform. Instead, their usefulness depends on the developer’s ability to critically evaluate generated outputs and decide when and how to apply them.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P29

### **Memo on “Difficulty in following language evolution”**

This code contains 5 quotations from 4 participants. The excerpts consistently describe the challenge of keeping up with rapid language change.

P23 cited lack of time to investigate new features and difficulty adapting them to existing systems, especially when dependencies evolve simultaneously. P22 described exponential growth in language specification size and interaction complexity between features, noting that feature interactions can introduce unforeseen side effects.

P03 linked difficulty to balancing new feature demands with modernization tasks. P01 described annual or semiannual version releases as overwhelming, especially when working across multiple languages.

Across these quotations, difficulty arises from rapid release cycles, expanding language scope, dependency changes, and competing work priorities. Following language evolution requires continuous learning and experimentation, which participants described as hard to sustain in daily work contexts.

**Memo metrics**

* Total quotations in this code: 5

* Total participants in this code: 4

* Participants: P01, P03, P22, P23

### **Memo on “Disabling warnings to keep systems compiling”**

This code contains 1 quotation from P20. The participant described migrating to C++ 17 and needing to disable compiler warnings.

They explained that constructs accepted in earlier versions became flagged in newer compilers. The updated standard required warnings for incorrect usage patterns that previously went unnoticed. As a result, warnings appeared during migration.

Instead of immediately correcting all issues, the team disabled warnings to maintain compilation. This suggests a tension between stricter standards enforcement and legacy code compatibility. New standards reveal previously tolerated misuse, creating friction during upgrades.

The quotation highlights how compiler evolution can expose latent issues and force short-term compromises to maintain build continuity.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P20

### **Memo on “discussions of developers community influences the adoption of modern features”**

This code includes 4 quotations from C++ Surveys. The excerpts describe informal community influence on modernization.

The participant stated there is “no organized modernization effort in KDE,” yet talks at Akademy and blog posts on Planet KDE help spread awareness of modern C++ features. Mailing list discussions weigh pros and cons before updating standard settings in build configurations.

The quotations indicate decentralized but communicative influence. Conferences, blogs, and mailing lists function as channels where new ideas circulate. While no central mandate exists, discussion spaces shape awareness and eventual adoption.

Community discourse therefore operates as a soft coordination mechanism. Modernization spreads through shared conversations rather than formal directives.

**Memo metrics**

* Total quotations in this code: 4

* Total participants in this code: 1

* Participants: C++ Surveys

### **Memo on “earlier adoption of modern features (even before their official release)”**

This code includes 6 quotations from 4 sources: C++ Study, JavaScript Study, Python Study, and P13. The excerpts describe cases in which developers adopted language features before their formal stable release.

P13 reported using features in experimental versions and adapting code as these features progressed from experimental to stable APIs. The participant framed this as an effort to keep up with the latest tool versions rather than reacting after official release.

The C++ Study excerpt shows that auto-typed variables, lambda expressions, and decltype appeared in KDE projects months before the formal release of C++11. This indicates usage aligned with draft or pre-release implementations.

The JavaScript Study excerpts report that several ES6 and later features were used years before their official ECMAScript release versions. Examples include const, let, arrow functions, async declarations, optional chaining, and others. The text links early usage to browser support that preceded formal standard publication.

The Python Study excerpt identified negative time differences between feature release and first appearance in repositories. Formatted string literals and yield from appeared in datasets during alpha releases of Python 3.6 and 3.3, respectively.

Across these sources, early adoption does not appear accidental. Developers integrated features during alpha or beta stages or when partial platform support existed. This reflects proactive experimentation and willingness to work with evolving implementations prior to final standardization.

**Memo metrics**

* Total quotations in this code: 6

* Total participants in this code: 4

* Participants: C++ Study, JavaScript Study, Python Study, P13

### **Memo on “environment configurations might hinder SCR efforts”**

This code includes 4 quotations from 4 participants: P06, P09, P12, and P25. The excerpts describe how infrastructure and environment constraints limit modernization.

P12 explained that in low-level programming contexts, they use the language version defined by the toolchain or hardware producer. They stated that they are often “locked by the producer,” and that basic language functions rarely change enough to justify version switching. This reflects vendor-imposed constraints.

P09 emphasized compatibility issues in client-facing software. Because many clients depend on the system, introducing new features risks breaking external code. The need to avoid crashing client systems limits feature adoption.

P06 described mixed environments with validation, development, and production stages. Updating requires coordinated downtime, which is not always feasible. This introduces operational barriers to upgrading language versions or refactoring.

P25 noted that server configurations may need to change during migration. Deploy environments can create unforeseen complications, turning simple changes into extended troubleshooting processes.

Across all quotations, environment constraints emerge at multiple layers: hardware vendors, client systems, deployment servers, and multi-stage environments. Rejuvenation depends not only on code changes but also on synchronized configuration updates. Infrastructure readiness becomes a limiting factor.

**Memo metrics**

* Total quotations in this code: 4

* Total participants in this code: 4

* Participants: P06, P09, P12, P25

### **Memo on “Experience-shaped trust in AI tools”**

This code contains 1 quotation from P27. The participant explicitly linked trust in AI tools to personal background and professional trajectory.

P27 associated their lower level of trust with age and prior experience. They stated they are “used to breaking my head,” which suggests a habit of solving problems manually. In contrast, they described younger team members as trusting AI tools “totally,” using them without hesitation.

The participant positioned themselves as someone who uses AI with “human intervention.” This indicates conditional trust rather than full delegation. The contrast between generations is not framed as technical superiority, but as difference in formative experience. One group learned through manual problem solving, while another group entered the field with AI assistance already available.

This code highlights how prior professional experience shapes attitudes toward AI. Trust is not uniform. It varies according to background, age, and established working habits.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P27

### **Memo on “Expert context influencing adoption behavior”**

**This code contains 1 quotation from P22. The participant described how expertise level influences the frequency and confidence of adopting new language features.**

**P22 reported that when they modify code, they “almost always try to use the new features.” However, they clarified that they do not modify code solely for modernization. Adoption occurs when there is an existing trigger for change. This indicates opportunistic integration rather than proactive rewriting.**

**The participant also contrasted their own context with that of an “average programmer.” They described their group, which includes advanced Ph.D. students and language developers, as more sensitive to new features. They estimated that their group would score higher on a frequency scale compared to the average developer.**

**In the same quotation, P22 rated the difficulty of staying updated as high. They described the expansion of the C++ standard and emphasized the interaction complexity between features. Even for someone deeply involved in language development and teaching, keeping up is described as hard.**

**This code shows that expertise operates in two directions. It increases willingness and ability to apply modern features when touching code, but it also exposes the depth and complexity of language evolution. Adoption behavior depends on context, role, and technical immersion.**

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P22

### **Memo on “Fear of exposing confidential code to AI tools”**

This code includes 2 quotations from P28 and P29. Both participants raised concerns related to confidentiality and risk when using AI tools.

P28 explicitly stated that they do not use AI tools at work and do not know colleagues who openly use them. They linked this to confidentiality, noting that “the code and bank data are confidential” and expressing concern that LLMs collect data. They concluded that “there could be a problem.”

P29, in a broader reflection on AI, mentioned that when you “put code there and it's not business,” there is “a chance of failing your code,” because it is used to train models. Although P29 focused more on quality and mediocrity, this remark directly references exposure risk.

Across these quotations, fear centers on data privacy and loss of control over proprietary information. The concern is not limited to code correctness but extends to how AI systems process and potentially reuse submitted content. Confidentiality constraints therefore influence whether AI tools can be used in professional environments.

**Memo metrics**

* Total quotations in this code: 2

* Total participants in this code: 2

* Participants: P28, P29

### **Memo on “Fear of overreliance inhibiting foundational skill development”**

This code contains 1 quotation from P29. The participant expressed concern that excessive reliance on AI may weaken fundamental programming skills.

P29 stated that “Junior shouldn't use it” and claimed to have seen juniors who “don’t know how to code anymore.” They described cases where developers perceived as mid-level or senior cannot perform minimal tasks without AI assistance. In their view, such developers may deliver code that contains many bugs while overestimating their competence.

The participant compared AI to “Stack Overflow, but faster,” suggesting that copying solutions without deep understanding remains a risk. They argued that many applications may work initially but later fail in production, requiring patching.

This quotation frames AI as a tool that can mask lack of understanding. The concern is not only about code quality but about long-term skill erosion. Overreliance may produce superficial productivity while undermining foundational knowledge.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P29

### **Memo on “Fear / risk aversion about upgrading”**

This code contains 10 quotations from 9 participants: JavaScript PR discussions, P01, P02, P08, P09, P12, P24, P25, and P29. Across these excerpts, upgrading is consistently framed as a risky activity that requires careful evaluation.

P12 described adopting a newer technique in an Android application that resulted in a memory leak due to poorly implemented bindings. This experience reinforced the need to “weigh these newer, more versatile features carefully.” The quotation explicitly associates novelty with potential instability.

P08 connected risk to poorly tested code. They described fear of crashing production systems during migration and mitigated this fear by writing automated tests before changing the language version. Here, risk aversion translates into preparatory safeguards.

P02 emphasized the need to understand what changed in a new version and to perform regression testing. The participant framed upgrading as a decision that must account for testing costs and potential drawbacks.

P24 and P25 reported resistance from colleagues and managers. P24 noted fear of unfamiliarity and infrastructure incompatibility. P25 described managerial reluctance rooted in concern about delaying demands or introducing production issues. Server compatibility was cited as an additional fear.

P29 explained that resistance depends on the magnitude of change. Incremental evolution was described as “calm,” whereas large version jumps were associated with breakage. JavaScript PR discussions highlighted compatibility concerns with older runtimes, which also reflect risk awareness.

Across participants, upgrading is not rejected outright. Instead, it is treated as a decision that involves weighing stability, infrastructure readiness, testing capacity, and delivery timelines. Fear operates as a moderating factor in adoption decisions.

**Memo metrics**

* Total quotations in this code: 10

* Total participants in this code: 9

* Participants: JavaScript PR discussions, P01, P02, P08, P09, P12, P24, P25, P29

### **Memo on “Feature interactions create unexpected side effects”**

This code contains 1 quotation from P22. The participant discussed the rapid expansion of the C++ standard and the complexity introduced by interacting features.

P22 described the growth of the standard from approximately 800 pages to around 1600 pages. They emphasized that new features do not simply accumulate in isolation. Instead, “these two new language features sometimes interact,” and complexity becomes “multiplicative” rather than additive.

The participant stressed that even when developers understand individual features, combinations may produce side effects. They noted that interactions can generate behaviors not anticipated by standardization committees. This requires experimentation and practical application, not only theoretical knowledge.

This code frames side effects as emergent from feature interaction. The risk does not stem solely from a single new construct but from the way multiple constructs combine in real systems. Complexity arises from interaction patterns rather than isolated novelty.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P22

### **Memo on “Framework/libraries dependencies motivate SCR efforts”**

This code includes 7 quotations from 4 sources: C++ Surveys, Python Study, P11, and P25. The excerpts consistently describe external dependencies as triggers for modernization.

P11 provided a detailed account of legacy Ruby systems that lost support from monitoring and integration tools. When New Relic and LivePerson ended support, migration became unavoidable. The participant described intense effort and compressed timelines, showing that external dependency decisions can force urgent upgrades.

P25 noted that needing a specific library compatible only with a newer Java version required updating the language version. Here, dependency compatibility directly dictated migration.

The Python Study excerpt linked adoption curves to major events such as Python 2 end-of-life and the release of Django 2.0, which required Python 3\. The text described pressure resulting from discontinued support and toolchain maturation. These shifts reduced inertia and encouraged broader rejuvenation.

C++ Surveys responses highlighted Qt upgrades as catalysts for adopting more modern C++. Transitioning between Qt versions often required newer language standards. The modernization of KDE frameworks was described as occurring alongside major Qt transitions.

Across these quotations, framework and library evolution acts as an external driver. When dependencies drop support, introduce incompatible changes, or require newer language standards, projects must adapt. Modernization becomes reactive to upstream changes rather than internally initiated.

**Memo metrics**

* Total quotations in this code: 7

* Total participants in this code: 4

* Participants: C++ Surveys, Python Study, P11, P25

### 

### **Memo on “Framework/library dependencies hinder SCR efforts”**

This code contains 19 quotations from 7 participants: C++ Surveys, P05, P13, P20, P21, P23, and P26. Across these excerpts, dependencies appear as structural constraints that slow down or block source code rejuvenation.

Several participants described third-party libraries that do not evolve in sync with the language. P13 stated that updating the codebase is not enough if third-party dependencies are not updated. They gave the example of migrating from Vue 2 to Vue 3, where internal code may be easy to migrate, but external libraries prevent full migration.

P05 reported compatibility issues between Java versions and plugins such as Lombok. They emphasized that dependencies often do not align 100% with new language versions, and that framework constraints may curb language evolution. They also mentioned that modules introduced in Java 9 require structural reorganization.

P21 described frameworks and compilers as bottlenecks. Even when a new language feature exists, developers must wait until the framework version used across applications is updated. P20 reinforced this by noting that compiler updates and upstream binary compatibility issues must propagate through the entire dependency chain before local upgrades are possible.

P23 highlighted deprecated or legacy dependencies that block language updates, requiring replacement or adaptation of each outdated component. P26 described manual step-by-step upgrades across versions due to compatibility concerns with front-end libraries.

C++ Surveys responses showed that Qt provides its own concurrency primitives and abstractions, reducing incentives to adopt equivalent C++ standard features. In some cases, compatibility with older Qt versions used by known users prevented adoption of newer C++ constructs.

Across all quotations, dependencies act as gating mechanisms. Language evolution does not occur in isolation. It is mediated by frameworks, libraries, compilers, and upstream compatibility chains. When these elements lag or diverge, rejuvenation becomes constrained.

**Memo metrics**

* Total quotations in this code: 17

* Total participants in this code: 7

* Participants: C++ Surveys, P05, P13, P20, P21, P23, P26

### **Memo on “Gradual experimentation before adoption”**

This code contains 1 quotation from P22. The participant described a deliberate delay and staged experimentation before adopting new language features.

P22 stated that they typically wait three to four years after feature release before using it widely. They mentioned that C++ 20 was already one year old but still in early experimentation within their context. This reflects a conscious delay strategy rather than immediate adoption.

The participant differentiated between language features and libraries. When migrating from Boost filesystem to the standard library equivalent, the change occurred quickly because behavior and syntax were already known. In contrast, genuinely new features require time to gain familiarity and practical confidence.

This quotation describes a phased model: initial release, observation and experimentation, internal trials, and eventual broader adoption. The delay is not passive avoidance but structured learning and risk reduction.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P22

### **Memo on “Help on bug prevention”**

This code contains 17 quotations from 11 participants: C++ Surveys, Python PR discussions, P03, P05, P08, P10, P16, P19, P20, P21, and P22. Across these excerpts, modern language features are framed as mechanisms for reducing errors and preventing defects.

Participants highlighted features such as smart pointers, enhanced for loops, lambda expressions, final and override markers, and null safety systems. P22 explicitly linked smart pointers to reducing memory leaks and described them as a trigger for modernization. P21 associated evolution with data protection and memory safety.

P08 described null safety as preventing null pointer exceptions at compile time. P05 discussed Java’s try-with-resources mechanism as preventing resource leaks. P16 emphasized type-restricted collections that prevent inserting incorrect object types and allow compile-time error detection.

Python PR discussions excerpts showed reviewers recommending keyword-only arguments, async/await, type annotations, and yield from to prevent incorrect calls, improve exception handling, and enforce type checking.

P03 and C++ Surveys mentioned improved readability and conciseness as factors that reduce mistakes. P20 described range-based loops as preventing incorrect index usage.

Across participants and repositories, prevention operates at different levels: memory safety, type safety, resource management, concurrency handling, and API misuse. Modern features are perceived as structural safeguards that detect or avoid common classes of bugs before runtime.

**Memo metrics**

* Total quotations in this code: 17

* Total participants in this code: 11

* Participants: C++ Surveys, Python PR discussions, P03, P05, P08, P10, P16, P19, P20, P21, P22

### **Memo on “Heterogeneous Rejuvenation Dynamics”**

This code contains 6 quotations from 3 study sources: C++ Study, JavaScript Study, and Python Study. The excerpts present quantitative evidence of uneven adoption patterns across projects and features.

C++ Study reported that lambda expressions, auto-typed variables, and range-based for are widely used but not uniformly distributed. One project alone accounted for a large proportion of occurrences, indicating concentration rather than homogeneous spread.

JavaScript Study showed variation in adoption rates across features. Some features appear in more than 75% of projects, while others remain below 15%. Occurrence counts also vary significantly between projects, with specific repositories contributing disproportionate shares.

Python Study revealed large differences in median usage across features. Many features show median values of zero, while others have concentrated usage in specific repositories. Adoption timelines also differ substantially. Some features appear shortly after release, while others show multi-year delays before generalized growth.

Across languages, rejuvenation does not follow a single uniform curve. Adoption varies by feature, project, and time. Some features spread rapidly and broadly, while others remain localized or delayed. This heterogeneity indicates that modernization unfolds unevenly across ecosystems and repositories.

**Memo metrics**

* Total quotations in this code: 6

* Total participants in this code: 3

* Participants: C++ Study, JavaScript Study, Python Study

### 

### **Memo on “Human-curated AI-generated code”**

This code contains 1 quotation from P27. The participant described routine use of AI tools for generating new code, but not for refactoring.

P27 stated that AI tools such as Copilot are “used routinely, by all the team developers” when creating new code. However, when revisiting or refactoring existing code, they do not rely heavily on tools. They emphasized that AI-generated code still requires improvement to make it “a little more legible” and “a little more like us.”

The quotation frames AI output as a draft rather than a final artifact. Human intervention remains necessary to align code with team standards and readability expectations. The participant values legibility over raw generation speed and sees editing as part of the workflow.

This code shows that AI use is integrated into development practice, but developers maintain responsibility for reviewing and shaping the final code.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P27

### **Memo on “implementation of a new language version may introduce bugs”**

This code contains 1 quotation from P12. The participant provided a concrete example of unintended consequences during adoption of a newer technique.

P12 described developing an Android application in C\#. A specific technique required unsafe memory access. The bindings for Android were not well implemented, which resulted in a memory leak that damaged several components. The participant concluded that newer and more versatile features must be “closely watched.”

The example illustrates that upgrading or using new language features can expose defects in bindings or implementations. The risk does not arise from misuse alone but from immature or poorly implemented integrations.

This code highlights that modernization can introduce instability when the surrounding tooling or platform support is not robust.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P12

### **Memo on “Improve code expressiveness”**

This code contains 76 quotations from 27 participants and study sources: C++ Study, C++ Surveys, JavaScript PR discussions, JavaScript Study, Python PR discussions, and P01, P04, P05, P06, P07, P08, P10, P11, P12, P13, P14, P16, P17, P18, P19, P20, P24, P25, P26, P27, P28, P29.

Across interviews and repository excerpts, participants consistently linked language evolution to reduced verbosity, clearer structure, and more concise representations of intent. Common examples include lambda expressions, range-based loops, auto type inference, annotations, records, async/await, coroutines, f-strings, arrow functions, and import statements.

Participants such as P19, P20, P01, and P18 emphasized that newer constructs reduce boilerplate and make reading smoother. P11 and P27 highlighted that writing fewer lines to achieve the same functionality increases clarity and lowers cognitive effort. C++ Surveys repeatedly associated lambdas and auto with less repetition and more readable code.

JavaScript PR discussions and Python PR discussions excerpts show reviewers recommending arrow functions, destructuring, default parameters, f-strings, and async constructs to make code “cleaner,” “more concise,” or “more elegant.” These suggestions focus on improving how intent is expressed within the code.

Some participants also noted trade-offs. P16 and P05 warned that certain features can harm readability if misused. P14 observed that async/await may feel more intuitive to write but not always simpler to understand. These remarks indicate that expressiveness depends on careful application.

Empirical excerpts from C++ Study and JavaScript Study illustrate large-scale refactorings that replaced older constructs with more modern ones to achieve conciseness and clarity.

Overall, this code captures expressiveness as a central motivation for rejuvenation. Developers value constructs that allow them to express the same logic with fewer lines, clearer semantics, and reduced syntactic noise.

**Memo metrics**

* Total quotations in this code: 76

* Total participants in this code: 27

* Participants: C++ Study, C++ Surveys, JavaScript PR discussions, JavaScript Study, Python PR discussions, P01, P04, P05, P06, P07, P08, P10, P11, P12, P13, P14, P16, P17, P18, P19, P20, P24, P25, P26, P27, P28, P29

### **Memo on “Improve code maintenance”**

This code contains 18 quotations from 12 participants: C++ Surveys, P01, P07, P11, P12, P14, P16, P19, P24, P25, P27, and P29.

Participants frequently linked modernization to long-term maintainability. P19 noted that markers such as final and override make code easier for future maintainers to understand. P16 described annotations as reducing manual boilerplate and making code easier to maintain.

P11 explicitly stated that the code written today becomes legacy tomorrow, and that new features facilitate rebuilding older code in a more maintainable way. They also connected modernization to easier function extraction and test building.

P07 and P01 emphasized that updates aim to improve long-term maintenance and problem resolution. P24 described how annotations replaced XML configuration, reducing complexity and simplifying system evolution. P27 stressed that readable code prevents future rewrites due to misunderstanding.

C++ Surveys participants described auto and lambdas as tools that enhance maintainability through conciseness and improved readability.

Across participants, maintenance is framed as future-oriented. Modern features reduce verbosity, clarify intent, and ease refactoring. Participants consistently view these improvements as investments in code longevity and stability.

**Memo metrics**

* Total quotations in this code: 18

* Total participants in this code: 12

* Participants: C++ Surveys, P01, P07, P11, P12, P14, P16, P19, P24, P25, P27, P29

### **Memo on “Improve code performance”**

This code contains 18 quotations from 13 participants: C++ Surveys, JavaScript Study, Python PR discussions, P02, P03, P11, P12, P17, P20, P23, P25, P27, and P29.

Participants frequently associated language evolution with measurable performance gains. P23 explicitly referred to C++11 move constructors as reducing memory consumption in large projects. C++ Surveys respondents mentioned range-for loops generating better machine code and removing unnecessary copy constructions. Python PR discussions noted that f-strings are marginally faster than older formatting approaches.

P11 described substantial runtime improvements between Ruby versions after a garbage collector rewrite. P03 and P25 connected newer Java versions with garbage collector improvements and other optimizations. P27 highlighted performance improvements in both Java and JavaScript, particularly in asynchronous execution.

Some participants framed performance as one of several decision pillars. P20 stated that adoption depends on whether a feature makes code simpler, safer, or faster. P12 linked performance to readability and maintenance benefits, indicating that these concerns often appear together.

Performance here is not described abstractly. Participants referenced concrete constructs, runtime behavior, memory usage, garbage collection, asynchronous execution, and version-level improvements.

**Memo metrics**

* Total quotations in this code: 18

* Total participants in this code: 13

* Participants: C++ Surveys, JavaScript Study, Python PR discussions, P02, P03, P11, P12, P17, P20, P23, P25, P27, P29

### **Memo on “Improve code security”**

This code contains 16 quotations from 12 participants: C++ Surveys, P01, P03, P11, P12, P17, P20, P21, P22, P23, P25, and P27.

Security appears as a strong and often decisive motivation for modernization. P21 described memory corruption and concurrency problems as “time bombs.” P17 and P03 emphasized that unsupported versions expose systems to security breaches. P01 noted that unsupported Java versions no longer receive security maintenance.

P22 discussed reducing third-party dependencies as a safety measure. They highlighted risks associated with outdated or unsupported libraries. C++ Surveys referred to compile-time safety improvements in Qt enabled by C++11 features.

P12 and P20 placed safety alongside performance and readability as central criteria. P27 described advances in authentication, encryption, and privacy mechanisms over recent years.

Participants consistently framed security as non-negotiable. Even when other improvements were optional, security updates were described as necessary.

**Memo metrics**

* Total quotations in this code: 16

* Total participants in this code: 12

* Participants: C++ Surveys, P01, P03, P11, P12, P17, P20, P21, P22, P23, P25, P27

### **Memo on “Improve code standardization”**

This code contains 3 quotations from 3 participants: Python PR discussions, P03, and P24.

Participants associated modern language features with more consistent coding patterns. P03 linked newer constructs such as optional and streams to preventing common mistakes and promoting standardized practices. P24 described legacy systems that mix older and newer styles, arguing that standardization would ease onboarding.

Python PR discussions referred to adding type annotations and updating return types to align with modern typing practices. This change was described as positive and consistent with current standards.

Standardization here concerns reducing variation across codebases and aligning with updated conventions. Participants emphasized clarity and fewer recurring mistakes.

**Memo metrics**

* Total quotations in this code: 3

* Total participants in this code: 3

* Participants: Python PR discussions, P03, P24

### **Memo on “Improve code testability”**

This code contains 1 quotation from P11.

P11 described how newer language features facilitate smaller methods, reduced coupling, and improved design. They explicitly stated that these improvements support building tests and extracting functions from legacy code.

The participant connected language constructs such as lambda expressions with cleaner and more maintainable code. They emphasized that today’s code becomes tomorrow’s legacy and must support future testing and restructuring.

Testability emerges here as a downstream benefit of clearer structure and reduced verbosity.

**Memo metrics**

* Total quotations in this code: 1

* Total participants in this code: 1

* Participants: P11

### **Memo on “Improve code understanding”**

This code contains 47 quotations from 24 participants: C++ Study, C++ Surveys, JavaScript PR discussions, Python PR discussions, P01, P02, P03, P04, P05, P07, P10, P11, P12, P13, P14, P16, P17, P18, P19, P22, P23, P26, P27, and P29.

Participants repeatedly emphasized readability and clarity. P19 described language evolution as reducing syntactic friction and improving reading fluidity. P18 and P14 explicitly connected new constructs with simplified learning curves and elimination of problematic patterns such as callback nesting.

C++ Surveys respondents frequently referenced lambdas, auto, and range-based loops as reducing boilerplate and making intent clearer. C++ Study described automated refactoring that introduced auto to improve readability across many files. Python PR discussions highlighted f-strings, type hints, and yield from as clearer alternatives.

Some participants acknowledged trade-offs. P16 and P05 noted that certain constructs can harm readability if misused. This indicates awareness that clarity depends on proper application.

Across participants, understanding is described in practical terms: fewer lines, less repetition, clearer semantics, reduced indirection, improved naming, and simplified iteration patterns.

**Memo metrics**

* Total quotations in this code: 47

* Total participants in this code: 24

* Participants: C++ Study, C++ Surveys, JavaScript PR discussions, Python PR discussions, P01, P02, P03, P04, P05, P07, P10, P11, P12, P13, P14, P16, P17, P18, P19, P22, P23, P26, P27, P29

## **Memo on “Improve concurrency/asyncronous programming”**

This code contains 7 quotations from 6 participants: P13, P14, P21, P22, P24, and P27.

Participants consistently framed language evolution as an enabler of safer and more manageable concurrency models. P21 described the migration from C to C++ as necessary to mitigate parallelism issues and to gain access to object-oriented concurrency control and frameworks. Concurrency was associated with risk reduction in systems handling simultaneous data and production-level load.

P22 emphasized the historical absence of standardized multi-threading support in pre-C++11 environments. The introduction of standardized threading libraries reduced dependency on third-party solutions and long-term maintenance burdens. Concurrency modernization was therefore not only about performance, but also about stability and portability.

P13 and P08 (through Kotlin coroutines and async/await discussions) connected asynchronous constructs with expressive and maintainable concurrency. P14 described async/await as making asynchronous code appear structurally synchronous, improving clarity while preserving non-blocking semantics. P24 associated newer APIs with easier thread management compared to older Java versions. P27 linked asynchronous constructs to both performance and developer facilitation.

Concurrency is described concretely: threading APIs, coroutines, async/await syntax, parallel execution, platform dependence, and third-party libraries. It appears as both a technical necessity and a productivity facilitator.

### **Memo metrics**

Total quotations in this code: 7  
Total participants in this code: 6  
Participants: P13, P14, P21, P22, P24, P27

## 

## **Memo on “Improve development productivity”**

This code contains 21 quotations from 15 participants: C++ Surveys, Python PR discussions, P03, P04, P08, P11, P12, P14, P16, P19, P20, P24, P25, P26, and P27.

Participants repeatedly associated modern language features with reduced verbosity, syntactic simplification, and faster development cycles. P04 and P19 emphasized writing fewer lines of code to achieve equivalent functionality. P16 and P25 discussed annotations and records eliminating boilerplate code such as getters, setters, constructors, and DTO implementations.

Lambda expressions (C++ Surveys, P04, P16) were frequently cited as improving conciseness and local reasoning, although some participants noted potential readability trade-offs. Python PR discussions highlighted type annotations enabling IDE inference and smoother workflows.

P11 and P20 described productivity as multidimensional: faster implementation, easier maintenance, and improved design modularity. P08 connected frequent upgrades with access to new features and faster bug fixes. P26 referenced framework evolution (Vue 2 to Vue 3\) as enhancing ease of learning and development flow.

Productivity is articulated through concrete constructs: lambda expressions, annotations, records, async/await, coroutines, auto typing, and IDE integration. The discourse emphasizes reduced manual effort, improved legibility, and acceleration of routine development tasks.

### **Memo metrics**

Total quotations in this code: 21  
Total participants in this code: 15  
Participants: C++ Surveys, Python PR discussions, P03, P04, P08, P11, P12, P14, P16, P19, P20, P24, P25, P26, P27

## **Memo on “Incremental SCR effort”**

This code contains 30 quotations from 17 participants: C++ Study, C++ Surveys, JavaScript PR discussions, JavaScript Study, Python PR discussions, Python Study, P03, P04, P07, P08, P09, P14, P20, P21, P22, P23, and P27.

Participants described source code rejuvenation as predominantly incremental rather than disruptive. P23 articulated selective refactoring at the method or class level during ongoing tasks. P20 and P22 emphasized that modernization is rarely the primary trigger; it typically occurs during maintenance, redesign, or feature implementation.

Gradual migration strategies were prominent. P07 and P08 described progressive upgrades, avoiding large-scale rewrites. P27 detailed microservice duplication and phased replacement of legacy components. JavaScript PR discussions and Python PR discussions illustrated small-scale refactorings such as var-to-let transitions or gradual addition of type annotations.

C++ Surveys respondents characterized modernization as continuous and low-intensity, often occurring opportunistically when touching relevant code. Large empirical studies (C++ Study, JavaScript Study, Python Study) reinforced this pattern by showing gradual increases in feature adoption over time rather than abrupt shifts.

Incrementality appears as a risk mitigation strategy. Participants avoid rewriting stable code unless triggered by substantial advantages (e.g., memory safety improvements, null safety, typing guarantees). Modernization is embedded in daily work rather than framed as a standalone initiative.

### **Memo metrics**

Total quotations in this code: 30  
Total participants in this code: 17  
Participants: C++ Study, C++ Surveys, JavaScript PR discussions, JavaScript Study, Python PR discussions, Python Study, P03, P04, P07, P08, P09, P14, P20, P21, P22, P23, P27

## **Memo on “Keep the systems running and evolutive maintenances are more important than SCR efforts”**

This code contains 35 quotations from 21 participants: C++ Surveys, P01, P03, P04, P06, P08, P09, P10, P11, P12, P13, P14, P16, P18, P20, P22, P23, P25, P27, P28, and P29.

Participants consistently prioritized system stability, production reliability, and business continuity over proactive rejuvenation. P20 emphasized that one should not evolve code merely to adopt new features; stable systems should remain stable. P12 and P14 stressed testing and regression assurance as prerequisites for any modernization.

Mission-critical contexts (P06, P11) were associated with preference for LTS versions and mature releases. P23 described regulatory and industrial constraints preventing language upgrades. P25 and P29 highlighted managerial resistance driven by cost, time, and risk concerns.

Several participants (P03, P09, P28) described evolution being deprioritized due to client demands and feature pressure. Migration is often reactive—triggered by deprecation, loss of support, or external constraints (P11’s New Relic case). Rewrites are viewed as financially and operationally risky.

Modernization is framed as subordinate to maintaining functionality. Even when benefits are recognized, participants repeatedly describe the necessity of preserving uptime, preventing regressions, and meeting delivery timelines. SCR competes with feature development and business priorities.

### **Memo metrics**

Total quotations in this code: 35  
Total participants in this code: 21  
Participants: C++ Surveys, P01, P03, P04, P06, P08, P09, P10, P11, P12, P13, P14, P16, P18, P20, P22, P23, P25, P27, P28, P29

## **Memo on “Lack of code internal quality might hinder SCR efforts”**

This code contains 2 quotations from 2 participants: C++ Surveys and P08.

Participants associated low internal code quality with increased difficulty in performing source code rejuvenation. P08 described a migration to Dart’s null safety in which the existing code was “probably badly written,” making migration harder. In this account, rejuvenation becomes intertwined with refactoring; modernization exposes structural weaknesses that complicate adoption of new features.

C++ Surveys described organizational contexts where modernization is postponed until the code quality has already degraded significantly. Modernization is then triggered reactively, when developers become “too annoyed” with the legacy codebase. Here, poor internal quality not only complicates SCR, but also delays it until the cost and frustration are higher.

Internal quality appears as a precondition for smooth rejuvenation. When absent, it transforms SCR from a feature adoption effort into a broader restructuring process.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 2  
Participants: C++ Surveys, P08

## **Memo on “Lack of documentation about new language features might hinder SCR efforts”**

This code contains 1 quotation from 1 participant: P19.

P19 highlighted disparities between communities in the availability and maturity of documentation and literature about modern language features. Python was described as having extensive and rapidly updated literature, whereas C++ documentation on modern constructs was characterized as less consolidated.

Adoption is framed not as mere enthusiasm for novelty, but as requiring a theoretical and practical basis. The lack of documentation becomes a barrier to informed adoption, particularly when teams seek justification grounded in established knowledge.

Documentation is therefore positioned as a legitimizing and enabling mechanism for SCR. Without adequate documentation and community consolidation, modernization efforts may be delayed or avoided.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P19

## **Memo on “Lack of retrocompatibility might hinder SCR efforts”**

This code contains 5 quotations from 4 participants: P07, P08, P20, and P26.

Participants described retrocompatibility as a critical structural condition for feasible rejuvenation. P20 emphasized compiler constraints and upstream dependency chains: migration is contingent upon ecosystem-level compatibility. Without alignment across compilers and libraries, upgrades are blocked.

P08 contrasted traumatic migrations (e.g., Python 2 to 3\) with smoother transitions (e.g., TypeScript 3 to 4). Migration difficulty is strongly associated with breaking changes and ecosystem coordination. Languages that maintain compatibility lower the barrier to SCR.

P07 noted that excessive concern for retrocompatibility may accumulate semantic complexity, but absence of compatibility creates disruptive migrations. Automated migration tools and guides were described as especially important when compatibility breaks cannot be resolved algorithmically.

P26 emphasized service dependencies and stability concerns in large systems. Migration is constrained by compatibility across interconnected components.

Retrocompatibility emerges as a structural facilitator of incremental SCR. Its absence amplifies technical and organizational friction.

### **Memo metrics**

Total quotations in this code: 5  
Total participants in this code: 4  
Participants: P07, P08, P20, P26

## **Memo on “Lack of SCR may introduce technical debt”**

This code contains 5 quotations from 4 participants: P08, P09, P11, and P13.

Participants consistently framed delayed modernization as increasing future migration cost. P13 contrasted proactive updating with leaving legacy systems unchanged due to high current cost. The decision to postpone is explicitly linked to accumulated future burden.

P11 emphasized that failing to track language evolution leads to painful and energy-intensive migrations. The cost of skipping versions accumulates, particularly in ecosystems with aggressive deprecation policies (e.g., Scala). Modernization is described as a preventive strategy to avoid “trauma of migration.”

P08 stressed that postponing updates makes change progressively harder. P09 described client-driven prioritization of feature demands over systematic code reevaluation, reinforcing how technical debt accumulates through neglect.

Technical debt here is not abstract; it is temporal. Delayed SCR increases migration cost, complexity, and risk over time.

### **Memo metrics**

Total quotations in this code: 5  
Total participants in this code: 4  
Participants: P08, P09, P11, P13

## **Memo on “Lack of tool to help SCR efforts”**

This code contains 2 quotations from 2 participants: P03 and P20.

Participants expressed both skepticism and interest regarding automated tools for SCR. P20 highlighted the complexity of C++ as an obstacle to generic migration tooling and expressed caution about letting tools modify code without oversight. Tools were associated with refactoring assistance but not necessarily full language evolution.

P03 reported manual updates as the norm but expressed interest in automated tools that could help track changes and assess impact. The potential value of tooling lies in traceability and impact analysis rather than blind automation.

Tool absence is therefore framed as both a technical limitation and a trust issue. SCR tooling must balance automation with developer control, particularly in complex languages and mission-critical systems.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 2  
Participants: P03, P20

## **Memo on “Lack of trust in programming transformation tools”**

This code contains 13 quotations from 8 participants: C++ Surveys, P01, P04, P05, P07, P20, P23, and P27.

Participants consistently expressed skepticism toward fully automated transformation tools. P23 questioned the scalability and robustness of Clang-based tools when applied to millions of lines of code, emphasizing implementation limitations and algorithmic weakness. Trust appears contingent on tool maturity, active maintenance, and demonstrated reliability.

P20 and C++ Surveys highlighted the structural complexity of C++, noting pointer hierarchies, compiler extensions, and multi-paradigm semantics as obstacles to safe automation. Tools that provide suggestions (e.g., Clang-Tidy, IDE hints) were perceived positively, whereas tools that automatically modify code without granular oversight were considered risky.

P04 and P07 articulated a preference for advisory tooling rather than full automation. Suggestions, linters, and version-control traceability were framed as acceptable safeguards. Automated semantic transformations were treated with caution, particularly when potential behavioral changes are involved.

P01 emphasized manual intervention in mission-critical systems, reinforcing that runtime risk constrains automation. P27 differentiated between AI-assisted code generation and refactoring, noting continued need for human validation to preserve legibility and intent.

Trust in transformation tools emerges as conditional: dependent on test coverage, semantic transparency, ecosystem maturity, and developer control. Full automation is associated with risk amplification in complex systems.

### **Memo metrics**

Total quotations in this code: 13  
Total participants in this code: 8  
Participants: C++ Surveys, P01, P04, P05, P07, P20, P23, P27

## **Memo on “Language evolution evaluated through perceived benefit”**

This code contains 4 quotations from 4 participants: C++ Surveys, Python PR discussions, P23, and P28.

Participants framed language evolution as worthy of adoption only when perceived benefits are substantial. P23 described the transition to C++11 as a “big relief,” positioning certain versions as milestone improvements rather than incremental upgrades. Later versions were described as beneficial but less essential.

P28 indicated that frequent Java releases do not necessarily justify migration unless they introduce meaningful constructs, such as lambda expressions. C++ Surveys explicitly stated that paradigm shifts or concurrency changes would only justify rewriting if the advantages were substantial.

Python PR discussions suggested that type annotations could be compelling enough to accelerate migration to Python 3.6, demonstrating how specific features can act as decisive triggers.

Perceived benefit appears as a decision filter. Adoption is not continuous but contingent on feature significance, ergonomic gains, or architectural relief.

### **Memo metrics**

Total quotations in this code: 4  
Total participants in this code: 4  
Participants: C++ Surveys, Python PR discussions, P23, P28

## **Memo on “Language evolution introducing silent behavior changes”**

This code contains 1 quotation from 1 participant: P22.

P22 described scenarios in which identical C++ code compiles without warnings across language versions but exhibits different runtime behavior. These “silent” behavioral shifts were presented as particularly concerning in large codebases, where even rare occurrences scale into significant risk.

The example of compiling the same syntax under different standard flags (e.g., C++98 vs. C++11) producing divergent outputs illustrates semantic drift without syntactic breakage. This phenomenon challenges static verification and complicates automated detection.

Attempts to compare abstract syntax trees across compiler configurations were described as technically complex and limited in effectiveness, due to non-semantic structural differences.

Silent behavior changes are framed as high-risk contingencies in SCR. They undermine confidence in version upgrades and amplify uncertainty in large-scale systems.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P22

## **Memo on “Language evolution is not that relevant to motivate maintenance efforts”**

This code contains 2 quotations from 1 participant: P18.

P18 explicitly stated that language evolution is “not a concern” when deciding whether to evolve code. Maintenance efforts were instead driven primarily by changing requirements. Refactoring was associated with adapting to new functional demands rather than adopting language features.

Language changes were described as occasionally forcing compatibility adjustments, but not as proactive motivators. New features are adopted in newly written code as a natural progression, rather than as drivers for revisiting stable legacy modules.

Here, language evolution is positioned as peripheral to maintenance priorities. Requirement volatility and functional evolution outweigh technological modernization in shaping refactoring decisions.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 1  
Participants: P18

## **Memo on “Language evolution might introduce breaking changes”**

This code contains 4 quotations from 3 participants: P05, P12, and P22.

Participants described language evolution as potentially introducing breaking changes at multiple levels. P12 emphasized the practical risk of breaking existing code when function prototypes or signatures change. The concern is not theoretical. It is operational. Code that previously compiled and worked may fail after migration. This requires regression testing and verification to ensure no unintended side effects.

P05 framed breaking changes in relation to structural adjustments, such as the introduction of modules in Java 9\. Migration may require reorganizing projects and adapting configuration files. Dependencies were described as a central challenge. When external libraries do not align immediately with new language versions, they may stop working, even if the core language upgrade itself is manageable.

P22 highlighted more subtle breakage, where identical code compiled under different C++ standards behaves differently at runtime. The issue is not always visible during compilation. It can manifest only during execution, increasing uncertainty.

Breaking changes are therefore described as technical, structural, and dependency-driven. They require testing, coordination, and sometimes partial redesign.

### **Memo metrics**

Total quotations in this code: 4  
Total participants in this code: 3  
Participants: P05, P12, P22

## **Memo on “Language evolution triggering hidden regressions”**

This code contains 1 quotation from 1 participant: P22.

P22 described hidden regressions occurring when the same code produces different runtime behavior across language versions, despite compiling without warnings. The example of compiling identical C++ code under C++98 and C++11 and obtaining different outputs illustrates a form of regression that is not syntactically visible.

The participant emphasized scale. In large codebases with millions of lines, even rare behavioral differences can accumulate into significant risk. Attempts to automatically detect such divergences through abstract syntax tree comparison were described as technically challenging, particularly because syntactic differences do not always imply semantic changes.

Hidden regressions are presented as difficult to predict and hard to detect automatically. They amplify the perceived risk of upgrading and increase reliance on comprehensive testing strategies.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P22

## **Memo on “language version support discontinuity”**

This code contains 9 quotations from 7 participants: Python Study, P07, P08, P11, P13, P17, and P29.

Participants consistently described discontinuation of language support as a strong trigger for rejuvenation. P17 linked end-of-life status with security risks and corporate pressure. P07 and P08 referenced Python 2 discontinuation as a direct motivation to migrate to Python 3\.

P11 described real-world consequences of prolonged delay, including loss of monitoring support and urgent forced migration within short timeframes. These episodes were characterized as stressful and risky, with partial rewrites and limited testing.

P13 described a trade-off context. Although aware of the risks of using discontinued versions, resource constraints and project maturity influenced prioritization. Migration was delayed when the effort to update dependencies was high.

P29 referred to vendor warranty and cloud service warnings as institutional pressure points. Once support ends, organizations may lose coverage or compliance guarantees, forcing action.

Python Study connected adoption acceleration with Python 2 end-of-life and the phase-out of support by major libraries. Discontinuity reduced inertia and increased migration pressure.

Support discontinuity emerges as an external structural force. It shifts modernization from optional improvement to mandatory action.

### **Memo metrics**

Total quotations in this code: 9  
Total participants in this code: 7  
Participants: Python Study, P07, P08, P11, P13, P17, P29

## **Memo on “Large SCR efforts”**

This code contains 12 quotations from 5 participants: C++ Study, C++ Surveys, JavaScript Study, P20, and P27.

Participants described large-scale rejuvenation efforts affecting dozens of files and thousands of code occurrences. C++ Study provided examples of commits introducing hundreds of range-based for loops, auto-typed variables, and lambda expressions across many files. Some transformations were supported by tools such as clang-tidy.

JavaScript Study documented similar large efforts, such as replacing var declarations with const and let across thousands of instances, or introducing dozens of arrow functions and async constructs. These transformations preserved functionality while modernizing syntax.

P27 described an architectural strategy involving duplication of functions and gradual replacement via microservices. Rather than modifying the existing system directly, the team created new components in updated versions and deprecated the legacy ones incrementally.

P20 noted that repeated patterns across codebases may justify radical or coordinated changes rather than isolated refactorings.

Large SCR efforts are characterized by scale, coordination, and systematic transformation. They often combine automation, architectural restructuring, and incremental rollout strategies.

### **Memo metrics**

Total quotations in this code: 12  
Total participants in this code: 5  
Participants: C++ Study, C++ Surveys, JavaScript Study, P20, P27

## **Memo on “learning through static analysis SCR recommendations”**

This code contains 2 quotations from 1 participant: P05.

P05 described static analysis recommendations as a learning mechanism rather than merely an enforcement mechanism. Tool-generated warnings about lambda expressions prompted curiosity and further investigation. The participant emphasized that seeing a suggested transformation helped them understand how the feature works and why it produces a more concise expression.

Static analysis is framed as an educational scaffold. It exposes developers to modern constructs that they might not have actively searched for. The suggestion acts as a trigger for inquiry. The participant associated this process with improved legibility and better code quality, but consistently highlighted learning as the primary benefit.

Challenges were described as mostly related to compatibility rather than conceptual difficulty. The learning benefit appears to precede full adoption and confidence in using the feature independently.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 1  
Participants: P05

## **Memo on “Legacy constraint removal enabling SCR”**

This code contains 2 quotations from 1 participant: JavaScript PR discussions.

The quotations describe modernization being enabled by the removal of legacy platform constraints. In the first excerpt, dropping support for Internet Explorer allowed broader adoption of ES6 features such as arrow functions, spread operators, and classes. The absence of backward compatibility requirements reduced the need for transpilation with Babel and opened the door to native feature usage.

In the second excerpt, un-transpiled ES6 classes required adaptation of existing extension mechanisms. The decision to drop support for older platforms is explicitly linked to encouraging the use of native language constructs and deprecating legacy extension methods.

Legacy constraint removal appears as a structural enabler. Once outdated platforms are no longer supported, modernization becomes technically simpler and architecturally cleaner. Adoption is not purely developer-driven; it is conditioned by platform policy decisions.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 1  
Participants: JavaScript PR discussions

## **Memo on “Limited trust in AI for complex development work”**

This code contains 1 quotation from 1 participant: P29.

P29 described artificial intelligence tools as useful within limits but unreliable for complex development tasks. The participant differentiated between trivial tasks, such as CSS or simple front-end features, and more complex logic. AI-generated code was characterized as often mediocre and requiring improvement.

The participant emphasized that developers who lack expertise may over-rely on AI and produce lower-quality outcomes. Expertise mediates the benefit. Skilled developers can extract value from AI, whereas others may stagnate.

Security and confidentiality concerns were also mentioned. Submitting code to AI systems may expose internal logic to external training processes, introducing risk.

AI is therefore framed as a productivity aid for simple tasks but not as a reliable substitute for complex reasoning and architectural design.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P29

## **Memo on “LLM-driven productivity gains”**

This code contains 1 quotation from 1 participant: P27.

P27 described a substantial productivity increase associated with LLM usage. The participant estimated that a developer using LLMs could produce output equivalent to multiple developers without such tools. The focus was on ticket resolution speed, feature delivery, and overall throughput.

The statement framed productivity gains in quantitative and team-level terms. LLM usage was associated with increased velocity and reduced staffing needs for the same amount of functionality.

Unlike the previous code on limited trust, this quotation presents LLMs as transformative in terms of delivery capacity. No explicit concerns were raised in this excerpt regarding quality degradation or risk.

LLM usage is therefore framed here as a force multiplier in development productivity.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P27

## **Memo on “LLMs enabling role shift from manual implementation to business-focused orchestration”**

This code contains 1 quotation from 1 participant: P27.

P27 described a perceived shift in the developer’s role due to LLM usage. The participant stated that LLMs assist with automated test creation, pipeline execution, and structural aspects of development. As a result, manual implementation work decreases.

The developer is portrayed less as a manual coder and more as a consultant who understands business needs and selects appropriate technologies. The participant emphasized that LLMs act as a foundation that supports punctual interventions by the developer, rather than replacing strategic reasoning.

Automation in deployment, environment configuration, and test generation was compared to cloud infrastructure abstractions. The focus moves toward business intelligence and optimization decisions. According to the participant, LLMs handle repetitive tasks, while developers remain responsible for higher-level decisions.

The quotation frames LLM adoption not as replacement, but as role transformation toward orchestration and business alignment.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P27

## **Memo on “LLM-supported program comprehension”**

This code contains 1 quotation from 1 participant: P27.

P27 described using LLMs to understand legacy or confusing code. The participant reported submitting legacy code to an LLM and asking for explanations of what the code does. The primary purpose was comprehension rather than automated refactoring.

The participant expressed belief in the potential of such tools, while acknowledging limited personal use in full refactoring scenarios. The tool was framed as providing contextual reading of entire folders and suggesting improvements, although the participant did not report using it to automatically upgrade code versions.

LLM support here is positioned as an interpretive assistant. It aids understanding and clarifies intent, particularly in legacy contexts. Adoption remains partial and exploratory.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P27

## **Memo on “Management approval required”**

This code contains 1 quotation from 1 participant: P01.

P01 described modernization decisions as contingent on managerial approval. The team may evaluate language benefits and bundle arguments for change, but final permission rests with a superior.

The participant indicated that modernization requires organizational endorsement beyond technical justification. Even if the team recognizes advantages, a decision authority determines whether the effort proceeds.

Modernization is therefore framed as a governance decision. Technical evaluation alone does not guarantee execution. Approval structures mediate SCR initiatives.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P01

## **Memo on “Manual SCR effort”**

This code contains 13 quotations from 9 participants: C++ Surveys, P01, P02, P03, P11, P12, P23, P28, and P29.

Participants consistently described performing source code rejuvenation manually. Several participants (P02, P03, P01) stated that upgrades between language versions were conducted by hand. Automated tools were rarely used for version-level evolution.

P12 emphasized reliability concerns in critical systems, arguing that manual evaluation is necessary when runtime stability is essential. P23 reported testing tools but frequently reverting to manual changes when dissatisfied with tool output. P28 preferred manual implementation due to unsatisfactory tool results.

C++ Surveys respondents indicated that modernization often occurs incrementally during maintenance rather than through dedicated tooling. Even when clang-tidy was used to assist identification of changes, further manual adjustments followed.

Manual effort is framed as safer, more controllable, and more precise. Tool usage remains selective and supplementary rather than central.

### **Memo metrics**

Total quotations in this code: 13  
Total participants in this code: 9  
Participants: C++ Surveys, P01, P02, P03, P11, P12, P23, P28, P29

## **Memo on “Market-driven upgrade timing”**

This code contains 3 quotations from 3 participants: JavaScript PR discussions, P24, and P26.

Participants described upgrade timing as influenced by market adoption rather than immediate feature availability. P24 stated that updates are not immediate upon release. Adoption depends on whether the broader market has consolidated around a version and whether its features are likely to be used.

P26 emphasized waiting until a version stabilizes and becomes widely adopted before migrating. The decision is framed as pragmatic rather than innovation-driven.

JavaScript PR discussions described delaying certain feature usage, such as ES7 constructs, until browser support becomes widespread. Temporary workarounds are maintained until adoption thresholds are reached.

Market-driven timing appears as a strategic pacing mechanism. Teams monitor adoption curves and update when versions mature and achieve widespread support.

### **Memo metrics**

Total quotations in this code: 3  
Total participants in this code: 3  
Participants: JavaScript PR discussions, P24, P26

## **Memo on “New language features might hinder debugging”**

This code contains 1 quotation from 1 participant: P11.

P11 distinguished between simple and complex language features in terms of debugging impact. Functional constructs such as map were adopted immediately and described as straightforward improvements over traditional loops. In contrast, features related to concurrency, threading, and parallel computation were approached with caution.

The participant emphasized that debugging concurrent or metaprogramming-related features can be difficult. Runtime errors may appear without clear traceability, and debugging tools may provide limited assistance. The example of Ruby metaprogramming illustrates this concern. Although described as powerful and attractive, it was also characterized as difficult to debug when issues arise.

Here, hesitation toward certain features is directly tied to diagnosability. Adoption decisions are influenced by the ability to trace and isolate problems. Debugging complexity acts as a moderating factor in feature uptake.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P11

## **Memo on “Non active communities might hinder SCR efforts”**

This code contains 1 quotation from 1 participant: P19.

P19 compared Python and C++ communities in terms of documentation and knowledge dissemination. Python was described as having extensive literature and rapid community activity. In contrast, C++ was characterized as having slower consolidation of modern knowledge.

Adoption was framed as requiring a theoretical basis and community support. Modernization is not described as merely following trends. It depends on available documentation, shared understanding, and practical examples that justify change within the work context.

Community vitality appears as an enabling condition for SCR. When modern practices are well-documented and widely discussed, adoption becomes more justifiable and accessible. When literature lags behind language evolution, hesitation increases.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P19

## **Memo on “Non modular architecture might hinder SCR efforts”**

This code contains 1 quotation from 1 participant: P17.

P17 described system architecture as influencing the feasibility of incremental rejuvenation. In monolithic systems with extensive coupling, migration from very old versions to newer ones may require a large, coordinated effort. When the period of deprecation warnings has already passed, piecemeal migration may no longer be possible.

The participant emphasized that architectural structure determines whether change can occur gradually or must be executed as a comprehensive operation. A monolithic system increases the dimension and impact of change.

Non-modular architecture is therefore framed as a structural barrier to incremental SCR. It raises the scope and risk of modernization efforts.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P17

## **Memo on “Operational and Legal Risk Avoidance”**

This code contains 2 quotations from 2 participants: P22 and P29.

P22 emphasized reducing third-party dependencies as a key modernization goal. Replacing external libraries with standard language features reduces distribution complexity, licensing concerns, and integration risks. The participant explicitly mentioned build systems, dependency management, and licensing constraints as operational considerations.

P29 described language and framework evolution as improving maintainability and project stability. Although not framed explicitly in legal terms, the quotation highlighted how modernization contributes to keeping projects running and simplifying structural elements.

Operational and legal risk avoidance appears as a motivation for adopting standard constructs and minimizing external dependencies. Modern language features can reduce exposure to licensing, deployment, and maintenance issues.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 2  
Participants: P22, P29

## **Memo on “Organizational Influence SCR efforts”**

This code contains 9 quotations from 4 participants: C++ Surveys, P20, P24, and P25.

Participants consistently framed source code rejuvenation as conditioned by organizational context rather than purely technical judgment. P20 explicitly linked modernization capacity to organizational culture. In environments that value internal software quality, developers may allocate time for maintenance and modernization. In delivery-driven contexts, internal improvement must be embedded opportunistically within other maintenance activities. Culture shapes timing and feasibility.

P24 described both personal and organizational pressures. Professional competitiveness motivates updating skills and language usage. The company also supports adoption of new features, which facilitates modernization. Staying updated enables participation in code reviews and collaboration. Here, organizational alignment promotes SCR.

P25 presented a contrasting scenario. Meetings emphasized stability over change. If the system works, stakeholders question the need to evolve. Fear of infrastructure incompatibility, such as server support for newer Java versions, introduces hesitation. Production environment risks are central. Migration decisions require weighing operational risk against perceived benefit.

C++ Surveys responses highlighted collective governance structures. In large communities such as KDE, compiler versions and minimal requirements are coordinated across projects to ensure consistency. Mailing lists and project maintainers mediate decisions. Smaller projects retain autonomy, while flagship projects follow agreed constraints tied to supported operating systems and compilers. In some cases, less central projects provide more freedom for modernization.

Across quotations, organizational influence operates through culture, governance, infrastructure constraints, community agreements, and perceived risk. SCR is not an isolated developer decision. It emerges from negotiated policies and collective standards.

### **Memo metrics**

Total quotations in this code: 9  
Total participants in this code: 4  
Participants: C++ Surveys, P20, P24, P25

## **Memo on “Perceived low reliability of LLM-generated output”**

This code contains 2 quotations from 2 participants: P28 and P29.

Participants described skepticism regarding the reliability and precision of LLM-generated code. P29 emphasized that most current AI systems are generic rather than specialized. According to this participant, generic systems cannot reach the same performance level as tools tailored to a specific language or domain. The concern is that broad models increase the probability of failure when attempting language-specific upgrades or code evolution tasks. The participant suggested that improvements would require specialization and targeted refinement rather than general-purpose generation.

P28 described practical dissatisfaction with generated results. Although viewing LLMs positively, the participant reported that outputs often required significant modification during implementation. This repeated need for adjustment led to a preference for manual implementation. Despite this hesitation, the participant acknowledged that LLM usage may increase in the future.

Across both quotations, reliability concerns focus on precision and contextual adequacy. Generated outputs are described as requiring revision or as lacking domain-specific specialization. Adoption is therefore conditional and cautious.

### **Memo metrics**

Total quotations in this code: 2  
 Total participants in this code: 2  
 Participants: P28, P29

## **Memo on “Preferring decision support over full automation”**

This code contains 1 quotation from 1 participant: P22.

P22 described the development of a tool focused on strong typing refactoring. The example illustrates replacing generic types, such as double or string, with semantically meaningful domain-specific types, such as hostname or family name. The goal is to prevent accidental misuse of interchangeable primitive types and increase code safety.

The participant emphasized that fully automatic transformation is not always feasible or desirable. Introducing stronger types requires addressing multiple consequences, such as implementing concatenation behavior, adjusting output functions, and resolving function signatures that previously accepted interchangeable parameters. These changes create branching decisions that cannot be resolved purely algorithmically.

The tool under development is described as detecting opportunities and offering choices rather than enforcing automatic modifications. The participant explicitly stated that human judgment remains essential. In some situations, automatic decisions are considered impossible, unreliable, or not worth the investment. The role of the tool is to support the human developer in making informed decisions.

The quotation frames automation as advisory rather than authoritative. Decision support is preferred over full automation, particularly in complex refactoring scenarios where semantic interpretation and design intent matter.

### **Memo metrics**

Total quotations in this code: 1  
 Total participants in this code: 1  
 Participants: P22

## **Memo on “Preferring warnings over automatic changes”**

This code contains 1 quotation from 1 participant: P22.

P22 described practical experience with static analysis and refactoring tools, particularly Clang and Clang-Tidy. The participant explained that such tools offer two operational modes. One mode issues warnings, informing the developer that an older construct can be replaced by a newer one. The other mode performs automatic source code modification.

The participant emphasized that, in practice, warning-based usage is preferred. Automatic refactoring is available, but it is typically limited to relatively simple transformations. For more substantial changes, manual rewriting remains the dominant practice. The participant explicitly stated that large-scale or complex transformations are not well supported by current tools in industrial contexts.

Clang-Tidy is described as a pluggable infrastructure that allows detection of modernization opportunities. However, the decision to apply changes often remains manual. Automatic modification is seen as appropriate for trivial refactorings, while significant changes require human oversight.

The quotation frames static analysis as a detection and advisory mechanism rather than a fully autonomous transformation engine. Warnings provide visibility and guidance, while developers retain control over implementation.

### **Memo metrics**

Total quotations in this code: 1  
 Total participants in this code: 1  
 Participants: P22

## **Memo on “Pressure to modernize legacy constructs”**

This code contains 3 quotations from 3 participants: C++ Surveys, Python Study, and P20.

Participants described modernization pressure as emerging from compiler evolution, ecosystem transitions, and framework-level upgrades. P20 focused on compiler behavior in C++. Migration to C++17 introduced new warnings for patterns that previously compiled without notice in C++14. The standard began requiring compilers to report situations previously tolerated. As a result, legacy constructs that once passed silently began triggering warnings or rejection. The pressure here originates from stricter enforcement of language rules. Developers may respond by fixing code or temporarily disabling warnings, but the change signals that older practices are no longer acceptable.

Python Study described ecosystem-level pressure in the Python community. The end-of-life of Python 2 removed long-term support, including security patches. Frameworks such as Django and major scientific libraries dropped Python 2 support. These coordinated decisions reduced the viability of remaining on older versions. The quotation emphasized temporal alignment between these events and acceleration in feature adoption. Tooling improvements, including static type checking support, lowered adoption cost and reinforced migration momentum. The pressure here is institutional and community-driven.

C++ Surveys linked modernization to major framework upgrades, particularly Qt transitions. Moving from Qt4 to Qt5 or Qt6 often requires more modern C++ standards. In some projects, adoption depends on distribution-level compiler support. Modern features become usable once compilers in common distributions can handle them.

Across quotations, pressure to modernize legacy constructs does not arise from individual preference alone. It stems from evolving compiler diagnostics, framework requirements, end-of-life policies, and broader toolchain alignment. Legacy usage becomes progressively harder to sustain as standards, frameworks, and community practices advance.

### **Memo metrics**

Total quotations in this code: 3  
 Total participants in this code: 3  
 Participants: C++ Surveys, Python Study, P20

## **Memo on “Prior knowledge reduces adoption effort”**

This code contains 2 quotations from 2 participants: C++ Surveys and P22.

Participants described prior familiarity as a factor that lowers the effort required to adopt new language features. P22 explained that adoption of new C++ standards often occurs with a delay of several years. The delay allows developers to accumulate knowledge and observe maturity before practical use. However, when a new standard feature closely resembles previously used third-party libraries, the transition becomes faster. The example of migrating from Boost filesystem to the standard filesystem library illustrates this point. Because syntax and behavior were already known, adoption required minimal conceptual effort. The change involved adjusting references rather than learning a new paradigm.

C++ Surveys reinforced this idea by comparing new C++ constructs to existing practices. Range-based for loops were described as similar to Qt’s Q\_FOREACH, which developers had already used. Lambda expressions were positioned as simplifying existing patterns, particularly in Qt signals and slots. The similarity between old and new constructs reduces the cognitive burden of transition.

Across both quotations, prior exposure and conceptual overlap reduce friction. When new features align with existing knowledge or mirror familiar libraries, adoption becomes an incremental adjustment rather than a disruptive change.

### **Memo metrics**

Total quotations in this code: 2  
 Total participants in this code: 2  
 Participants: C++ Surveys, P22

## **Memo on “Programming language complexity might hinder SCR efforts”**

This code contains 4 quotations from 4 participants: C++ Surveys, P20, P22, and P29.

Participants consistently associated language complexity, particularly in C++, with limitations in automated support for source code rejuvenation. P20 described C++ as a “pretty complex language,” making it difficult to design a generic evolution tool. While acknowledging that tools help, the participant expressed skepticism about allowing automated tools to modify code without close control. The comparison with simpler migration scenarios in other languages illustrates the perceived difficulty of building reliable transformation tools for C++.

P22 reinforced this view by highlighting semantic complexity. The participant explained that many transformations require semantic decisions rather than purely syntactic replacements. C++ analysis was described as more complex than languages such as Java or C\#. Detecting all side effects and avoiding unintended consequences was considered nearly impossible at industrial scale with current tools. The risk of subtle issues reduces confidence in automatic refactoring.

C++ Surveys echoed concerns about tool trust. Although IDEs provide automated functions, the participant stated reluctance to rely on them in C++. Pointer hierarchies and static analysis limitations were cited as complicating factors. In contrast, the participant indicated more willingness to trust automation in less complex languages.

P29 approached complexity from a cost perspective. Updating legacy systems was described as sometimes too expensive, leading to architectural alternatives such as microservice-based replacement instead of incremental modernization. This suggests that complexity and migration cost may redirect effort toward system redesign rather than feature-level rejuvenation.

Across all quotations, complexity operates as a structural constraint. It limits tool maturity, increases risk of unintended side effects, reduces trust in automation, and may raise the cost of incremental modernization to the point that replacement strategies become preferable.

### **Memo metrics**

Total quotations in this code: 4  
 Total participants in this code: 4  
 Participants: C++ Surveys, P20, P22, P29

## **Memo on “Programming language flexibility”**

This code contains 4 quotations from 1 participant: P01.

P01 contrasted older and newer languages in terms of flexibility and openness to change. Older languages were described as inflexible, with long periods in which version upgrades did not occur. The example of a C++ project remaining effectively tied to older standards for many years illustrates this stability, or inertia. According to the participant, newer languages appear more flexible, and the developers who work with them also tend to accept change more readily.

The participant also linked flexibility to usage context. Java systems, especially smaller ones, were described as more susceptible to evolution. However, this susceptibility does not necessarily imply low effort. Framework dependencies can still constrain change. Flexibility here refers more to openness and frequency of evolution rather than simplicity of migration.

In another excerpt, P01 associated flexibility with developer culture. Developers working with C, Fortran, or Assembly were portrayed as more attached to low-level control and less receptive to tools or automation. In contrast, developers working with JavaScript and TypeScript were described as highly tool-oriented and quick to adopt new releases.

Across the quotations, flexibility is framed as a socio-technical characteristic. It involves language design, community habits, and developer attitudes toward tools and change. Older languages and their communities are described as more conservative, while newer technologies encourage faster and more frequent adoption.

### **Memo metrics**

Total quotations in this code: 4  
 Total participants in this code: 1  
 Participants: P01

## **Memo on “Programming language migration”**

This code contains 11 quotations from 4 participants: P07, P08, P11, and P21.

Participants described programming language migration as motivated by structural limitations, safety concerns, typing systems, concurrency control, and long-term maintainability. P21 provided the most detailed account. Migration from C to C++ was framed as necessary to handle concurrency, encapsulation, and data protection. Pure C was associated with memory corruption, lack of object control, and difficulty managing parallelism. Migration was presented as a structural solution to recurring defects such as memory leaks and unsafe data access.

P21 also emphasized constraints such as time and documentation. Legacy systems with limited documentation required guessing code behavior. Migration demanded substantial effort, particularly when one person handled multiple responsibilities. Framework and compiler versions were described as bottlenecks that could prevent use of new features unless the entire ecosystem was updated.

P11 contextualized migration within broader language evolution, referring to the coexistence of Python 2 and Python 3\. Evolution was described as crucial for long-term competitiveness. Delayed migration could impact business positioning, as illustrated by references to Java being pressured by Scala and C\# innovations.

P08 described multiple migration strategies. One Python 2.7 system was considered too obsolete to migrate incrementally and was instead replaced by a new Kotlin system. In another case, migration from JavaScript to TypeScript occurred gradually to introduce typing and reduce bugs. Kotlin was chosen over Java due to null safety guarantees. Migration decisions were explicitly tied to defect prevention and robustness.

P07 also linked migration to typing needs. The lack of a robust type system in Python motivated transition to a statically typed language. However, scheduling constraints and parallel replacement efforts influenced the decision not to migrate to Python 3 first.

Across quotations, programming language migration is framed as a structural response to safety, typing, concurrency, and maintainability issues. It involves technical drivers, organizational constraints, and strategic replacement decisions. Migration may occur incrementally, gradually, or through full system replacement depending on context.

### **Memo metrics**

Total quotations in this code: 11  
 Total participants in this code: 4  
 Participants: P07, P08, P11, P21

## **Memo on “programming languages are currently evolving in a fast pace”**

This code contains 5 quotations from 4 participants: P01, P13, P20, and P22.

Participants described contemporary language evolution as faster and more frequent than in the past. P20 characterized C++11 as a major turning point, introducing substantial features such as lambdas, type deduction, range-based loops, and template improvements. After that, release cycles became more regular, approximately every three years. The participant framed this cadence as enabling gradual incorporation of useful constructs into daily work.

P22 emphasized the expansion of the C++ standard over time, noting that its size roughly doubled from earlier versions to more recent ones. This growth was associated with increased complexity. The participant highlighted that following evolution requires more than reading documentation. Developers must apply new features in practice and understand how they interact. Interaction effects between features were described as multiplicative rather than additive, making it harder to anticipate side effects. Even experienced developers find it difficult to keep up, particularly when language features interact in unexpected ways.

P13 described Kotlin as intentionally evolving at a faster cadence than Java historically did. The language was portrayed as under active development, with community feedback leading to rapid incorporation of new features. In this account, faster evolution was seen as responsive and aligned with developer needs. The participant perceived frequent updates as part of normal day-to-day practice.

P01 provided a more critical perspective. Earlier language versions remained stable for many years, while current ecosystems release updates yearly or even more frequently. This rapid cadence makes it difficult for teams to keep up. Adoption tends to occur only when driven by security concerns or market pressure. Writing code, testing, and adapting to new versions require time that teams often lack. The participant also distinguished between compiler evolution and language-level changes, suggesting that compiler updates are easier to follow than structural language modifications.

Across the quotations, rapid evolution is described as both enabling and burdensome. Frequent releases introduce useful features and community responsiveness, but also increase cognitive load, interaction complexity, and organizational strain. Keeping pace requires continuous learning and practical experimentation, which many teams struggle to maintain.

### **Memo metrics**

Total quotations in this code: 5  
 Total participants in this code: 4  
 Participants: P01, P13, P20, P22

## **Memo on “Project complexity might hinder SCR efforts”**

This code contains 17 quotations from 14 participants: P05, P06, P07, P08, P10, P11, P13, P14, P17, P20, P21, P22, P26, and P27.

Participants consistently described project complexity as a central constraint on source code rejuvenation. Complexity was associated with code base size, system criticality, architectural structure, documentation gaps, and dependency chains.

Several participants emphasized scale. P07, P05, P26, and P22 explicitly linked code base size with migration difficulty. Large systems require extensive testing and validation. P22 noted that while small projects are manageable, projects with millions of lines of code significantly increase risk. Even rare side effects become meaningful at scale. P07 highlighted that stable systems demand revalidation of everything before migration, which raises cost and effort.

System criticality emerged as another factor. P06 described mission-critical systems that cannot fail and must maintain continuous availability and data integrity. P20 similarly noted that production systems cannot “crash” or “stop working,” making risk tolerance low. In these contexts, SCR is constrained by operational requirements.

Legacy characteristics were also central. P21 explained that poor documentation forces developers to guess what the code does, making evolution risky. P27 described old, critical code paths that, if modified, could break the product with financial consequences. P11 indicated that some legacy systems become so entrenched that migration is impractical, and rewriting from scratch becomes extremely costly.

Architectural structure influences feasibility. P17 noted that monolithic systems may require full, coordinated operations rather than incremental updates, especially if the deprecation window has passed. P14 observed that in large shared codebases, old and new patterns coexist, reducing consistency and complicating maintenance.

Testing and quality assurance overhead also appear repeatedly. P10 described the need to refactor tests, rerun QA, and ensure no degradation occurs. CI/CD pipelines help, but do not eliminate the effort. P13 described trade-offs in older Python 2 systems, where dependency upgrades would demand substantial work, leading to postponement.

Some participants framed incremental migration as a mitigation strategy. P08 advocated updating early and gradually to avoid accumulating migration debt. However, when systems become too obsolete, full replacement may occur, as described in Python-to-Kotlin transitions.

Across all quotations, project complexity is multi-dimensional. It includes size, age, architectural coupling, documentation quality, system criticality, dependency maturity, and validation cost. These factors collectively increase risk, extend timelines, and often shift decisions toward postponement, gradual evolution, or full system replacement rather than straightforward rejuvenation.

### **Memo metrics**

Total quotations in this code: 17  
 Total participants in this code: 14  
 Participants: P05, P06, P07, P08, P10, P11, P13, P14, P17, P20, P21, P22, P26, P27

## **Memo on “Reactive approach”**

This code contains 7 quotations from 5 participants: C++ Surveys, Python PR discussions, P01, P22, and P25.

Participants consistently described source code rejuvenation as reactive rather than proactive. Modernization tends to occur when triggered by other activities such as bug fixing, feature implementation, security concerns, or external discontinuation events.

P22 explicitly stated that new features are almost always applied when code is already being modified. However, the team does not change code solely for modernization purposes. A trigger is required. The participant also emphasized the difficulty of keeping up with rapid language evolution, reinforcing that systematic modernization demands effort beyond daily responsibilities.

P01 characterized modernization as reactive to discontinuation, security issues, or community abandonment. Language evolution was described as fast, but adoption often occurs only when external pressure arises.

P25 described a sprint-driven workflow in which developers focus strictly on assigned demands. Changes unrelated to the specific task are typically avoided. This reinforces the idea that modernization is embedded within task-driven activity rather than planned independently.

C++ Surveys responses reflected similar patterns. Modernization of existing code occurs when rewriting is already necessary or when substantial benefits justify the change. Otherwise, older code remains unchanged. New code tends to use modern features, while legacy sections are updated only when required.

Python PR discussions illustrated incremental modernization during refactoring. Type annotations may be introduced when functions are already being extracted, demonstrating opportunistic adoption rather than dedicated migration campaigns.

Across quotations, modernization is not framed as a standalone objective. It is integrated into existing workflows and often triggered by maintenance tasks, defect correction, feature implementation, or external pressures. The reactive approach minimizes unnecessary risk but may delay systematic adoption.

### **Memo metrics**

Total quotations in this code: 7  
 Total participants in this code: 5  
 Participants: C++ Surveys, Python PR discussions, P01, P22, P25

## **Memo on “Reason for programming language evolution”**

This code contains 1 quotation from 1 participant: P14.

P14 framed programming language evolution as a response to unmet needs identified by the community. According to the participant, as a language evolves, it becomes evident that certain features or constructs are missing. These gaps motivate the introduction of new elements that make coding more convenient and productive.

The quotation emphasizes convenience and productivity as driving forces. Language evolution is not described as arbitrary or purely technical. It emerges from practical experience, where developers recognize recurring patterns or limitations and seek constructs that simplify implementation.

In this account, evolution is community-informed. The development community identifies missing constructs and influences the direction of change. Language evolution is therefore presented as an adaptive process driven by practical shortcomings and productivity concerns.

### **Memo metrics**

Total quotations in this code: 1  
 Total participants in this code: 1  
 Participants: P14

## **Memo on “Recommendation to stick with LTS versions for complex systems”**

This code contains 2 quotations from 2 participants: P11 and P25.

Participants described long-term support (LTS) versions as preferable for mission-critical or complex systems. P11 explicitly stated using Java 11 LTS for mission-critical projects. The participant contrasted LTS versions with recently released versions that introduce new features but may still accumulate bug fixes over time. Mature versions were described as more robust and suitable for sensitive systems.

P25 reinforced this view by recommending that Java migrations target LTS versions. Although many projects remain on older versions such as Java 8, upgrading to the latest LTS release was described as more advantageous than adopting non-LTS releases.

Across both quotations, LTS versions are framed as stable, mature, and supported for extended periods. Stability and long-term maintenance guarantees outweigh access to the newest features in high-risk or mission-critical contexts.

### **Memo metrics**

Total quotations in this code: 2  
 Total participants in this code: 2  
 Participants: P11, P25

## **Memo on “Reduce technical debt”**

This code contains 4 quotations from 2 participants: P03 and P09.

Participants described reducing technical debt as closely tied to modernization practices. P03 presented two contrasting approaches. In one, systems remain operational without following language and framework evolution. New features are added while core dependencies remain outdated, increasing future migration impact. In the other approach, modernization occurs gradually during maintenance, updating frameworks and addressing technical debt incrementally.

P03 emphasized the influence of organizational process and maturity. In one company, detailed planning was required before any migration due to outdated technology stacks. In another, a structured 80/20 allocation allowed continuous attention to technical debt, including framework updates and performance improvements.

P09 described code reevaluation as demand-driven. Modernization and reassessment occur when client requirements expose limitations in the current system. Technical debt reduction is therefore reactive and aligned with business needs.

Across quotations, reducing technical debt is framed as a strategic and process-dependent decision. Continuous modernization distributes effort over time, while postponement accumulates cost. Organizational maturity and allocation of time directly influence the feasibility of systematic debt reduction.

### **Memo metrics**

Total quotations in this code: 4  
 Total participants in this code: 2  
 Participants: P03, P09

## **Memo on “Reducing cognitive load for newcomers”**

This code contains 2 quotations from 2 participants: C++ Surveys and P19.

Participants framed modernization as a way to make code more accessible to new developers. P19 described modernization as a continuous evolution process. According to the participant, code written in more recent language versions is more comfortable for newcomers to read and maintain. The quotation also linked modernization to preventing degradation. Over time, code degrades, but adopting newer versions, along with unit tests and coverage practices, helps maintain clarity and structure. Modernization is therefore associated with ongoing maintenance that benefits future maintainers.

C++ Surveys reinforced this perspective by stating that using modern C++ features makes software more attractive to new contributors. The emphasis is not only on readability but also on perceived modernity as a factor in attracting participation.

Across both quotations, modernization is connected to onboarding and contributor experience. Updated constructs and conventions reduce friction for newcomers who are trained in more recent language standards. Modernization thus supports long-term maintainability by aligning code with current developer expectations.

### **Memo metrics**

Total quotations in this code: 2  
 Total participants in this code: 2  
 Participants: C++ Surveys, P19

## **Memo on “Relevance of adopting new technologies”**

This code contains 1 quotation from 1 participant: P10.

P10 described a deliberate preference for adopting bleeding-edge technologies and always using the latest version. The rationale provided was uncertainty about future needs. By staying on the latest version, the team avoids being blocked if a new feature becomes necessary. If something breaks, the team resolves it immediately rather than postponing adjustment.

The quotation presents early adoption as a preventive strategy. Instead of delaying upgrades and accumulating migration challenges, the team chooses to confront incompatibilities as soon as they arise. Adoption is framed as pragmatic risk management rather than experimentation for its own sake.

Here, adopting new technologies is considered relevant because it maintains readiness for future requirements and reduces the likelihood of large, delayed migration efforts.

### **Memo metrics**

Total quotations in this code: 1  
 Total participants in this code: 1  
 Participants: P10

# **Memo on “Relevance of CI/CD to SCR efforts”**

This code contains 3 quotations from 2 participants: P10 and P27.

Participants described CI/CD and automated pipelines as important mechanisms that support source code rejuvenation and refactoring activities.

P10 emphasized that legacy code modernization often requires extensive testing. Refactoring may require revisiting unit tests and sometimes repeating the entire QA process. According to the participant, CI/CD pipelines help mitigate this effort because automated tests are executed whenever code changes are submitted. The merge process depends on successful pipeline execution, which helps ensure that modernization changes do not degrade the software.

The same participant also explained that when new language versions or refactoring changes are introduced, the pipeline typically fails initially until tests are updated. This indicates that modernization and testing evolve together, reinforcing the dependency between them.

P27 described broader automation trends in development environments. Automated testing, integration pipelines, and infrastructure automation were portrayed as reducing manual work and enabling developers to focus more on higher-level decision-making. These automated processes make it easier to detect errors and maintain code quality during evolution activities.

Across quotations, CI/CD pipelines appear as infrastructural support for safe modernization. Automated testing and pipeline validation reduce the risk of introducing defects during refactoring and enable developers to modify code more confidently.

### **Memo metrics**

Total quotations in this code: 3  
Total participants in this code: 2  
Participants: P10, P27

# **Memo on “Relevance of keeping the programs updated with language evolution”**

This code contains 3 quotations from 3 participants: P13, P25, and P29.

Participants described maintaining updated language and dependency versions as an important practice for security, support, and maintainability.

P13 reported regularly updating dependencies in actively maintained projects. Updates occur periodically, sometimes every few weeks or months. However, the participant also acknowledged the existence of legacy projects still using Python 2, indicating that modernization practices vary depending on project context.

P25 emphasized the importance of choosing long-term support (LTS) versions when migrating Java systems. According to the participant, LTS releases offer advantages to organizations due to extended maintenance and stability.

P29 highlighted security and reliability as motivations for updates. The participant explained that outdated frameworks or languages may expose systems to security vulnerabilities that are corrected in newer versions. Using supported frameworks also provides guarantees and support from vendors such as Microsoft in the .NET ecosystem.

Across quotations, keeping systems updated is framed as a protective strategy. It reduces exposure to vulnerabilities, ensures vendor support, and helps maintain the reliability of software systems.

### **Memo metrics**

Total quotations in this code: 3  
Total participants in this code: 3  
Participants: P13, P25, P29

# **Memo on “Relevance of Language implementation / frameworks / library evolution”**

This code contains 23 quotations from 11 participants: C++ Surveys, P06, P07, P08, P13, P15, P16, P17, P20, P27, and P29.

Participants frequently described ecosystem evolution—particularly frameworks and libraries—as a major driver of source code rejuvenation.

Several participants distinguished between language evolution and ecosystem evolution. P07 explicitly stated that framework evolution is often the primary reason for code evolution. Similarly, P16 emphasized that language changes alone rarely require modifications to existing code because backward compatibility often preserves functionality. Instead, updates to libraries frequently demand adaptation because interfaces or usage patterns change.

Framework releases were described as introducing new requirements or behaviors. P17 illustrated this through changes in Rails, where newer framework versions require developers to modify how sessions or parameters are handled. These updates can improve security or simplify implementation, but they also force developers to adapt existing systems.

Some participants highlighted the role of ecosystem investments and industry support. P29 noted that languages with strong corporate backing and active ecosystems, such as C\# and .NET, evolve continuously and remain viable platforms.

Several quotations also described modernization triggered by toolkit or framework requirements. For example, C++ Surveys explained that framework requirements such as Qt versions determine which language standards projects must support. When frameworks migrate to newer standards, applications often follow.

Participants also described performance improvements, usability gains, and code simplification as benefits of evolving frameworks and libraries. P06 explained that technological advances in frameworks simplify implementation and facilitate refactoring.

Overall, the quotations frame ecosystem evolution—frameworks, libraries, toolkits, and runtime environments—as a central force shaping code evolution. Language evolution alone is often insufficient to trigger modernization, but ecosystem changes frequently require developers to update code.

### **Memo metrics**

Total quotations in this code: 23  
Total participants in this code: 11  
Participants: C++ Surveys, P06, P07, P08, P13, P15, P16, P17, P20, P27, P29

# **Memo on “Relevance of regression / automated testing”**

This code contains 23 quotations from 15 participants: JavaScript PR discussions, P01, P02, P03, P04, P07, P08, P10, P12, P14, P15, P20, P22, P23, and P27.

Participants consistently described automated testing and regression testing as essential mechanisms for enabling safe code evolution.

Many quotations framed testing as a prerequisite for refactoring. P20 emphasized that without tests, modifications become risky reengineering rather than safe refactoring. The participant described an example where a single-line change caused a system failure despite passing initial tests, illustrating the risk of insufficient coverage.

Other participants reinforced this perspective. P14 stated that testing must come first before code modification begins, even when the goal is only to improve readability. Testing ensures that observable behavior remains unchanged during refactoring.

Regression testing also appeared as a key safeguard during migrations. P12 explained that language changes can affect function prototypes or low-level behavior, requiring extensive regression testing to confirm that no defects were introduced.

Several participants linked testing directly to modernization feasibility. P08 described writing automated tests before migrating parts of an application to gain confidence that failures would be detected immediately. P07 noted that higher test coverage significantly increases confidence during migration and enables tools to be used more safely.

Testing practices were also connected to architectural strategies. P04 described isolating system components and migrating them gradually to reduce testing scope. Similarly, P27 described duplicating functionality and testing new implementations before replacing older components.

Across quotations, automated testing serves as both a risk mitigation mechanism and an enabler of modernization. High test coverage increases confidence in refactoring, facilitates migration to newer versions, and allows developers to detect behavioral changes quickly.

### **Memo metrics**

Total quotations in this code: 23  
Total participants in this code: 15  
Participants: JavaScript PR discussions, P01, P02, P03, P04, P07, P08, P10, P12, P14, P15, P20, P22, P23, P27

# **Memo on “Relevance of SCR perception”**

This code contains 4 quotations from 3 participants: JavaScript PR discussions, P13, and P24.

Participants described how perceptions of language evolution influence modernization practices.

P13 described Kotlin as a language designed for faster evolution compared to Java. The participant highlighted the rapid introduction of new features driven by community feedback and ecosystem development. In this context, evolving code alongside the language was perceived as natural and beneficial.

The same participant also illustrated how language evolution can improve expressiveness and semantics. Kotlin features such as stronger type representations and coroutine support encouraged developers to adapt their code in order to take advantage of clearer abstractions and improved concurrency models.

P24 emphasized that modernization and standardization help reduce inconsistencies in legacy systems. When older and newer coding styles coexist, the system becomes harder for developers to understand. Standardizing code through modernization can simplify onboarding and comprehension.

JavaScript PR discussions showed a practical perspective from pull request discussions. Developers proposed adopting newer constructs such as arrow functions, promises, and modern variable declarations in order to improve code clarity and structure.

Across quotations, perceptions of language evolution influence how developers interpret modernization. When language evolution is perceived as beneficial for expressiveness, readability, or standardization, developers are more inclined to adapt their code to newer constructs.

### **Memo metrics**

Total quotations in this code: 4  
Total participants in this code: 3  
Participants: JavaScript PR discussions, P13, P24

# **Memo on “Reliance on static analysis to detect source code rejuvenation opportunities”**

This code contains 2 quotations from 2 participants: P03 and P10.

Participants described static analysis tools such as linters and IDE diagnostics as mechanisms that help identify problems introduced during modernization or version upgrades.

P10 emphasized the role of linters integrated into development pipelines. According to the participant, linters encode community-recommended practices and can enforce these practices automatically during development. In the described workflow, linting rules are treated as build errors rather than warnings, meaning that code that violates these rules cannot pass the build process. This practice encourages developers to align their code with updated language practices and helps detect issues when new language features or standards are introduced.

P03 described a different but related mechanism. When upgrading language versions, compilation errors may emerge due to newly introduced keywords or changes in language constructs. The participant explained that IDE analysis tools such as Eclipse help developers detect these issues and guide the refactoring process. However, the participant also noted that modernization is still largely performed manually and requires extensive system retesting after version upgrades.

Across quotations, static analysis tools appear as diagnostic support mechanisms. They help developers detect problems that arise when languages evolve, but they do not eliminate the need for manual refactoring and testing.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 2  
Participants: P03, P10

# **Memo on “Reliance on static analysis to detect SCR opportunities”**

This code contains 14 quotations from 7 participants: C++ Surveys, Python PR discussions, P04, P05, P10, P11, and P20.

Participants frequently described static analysis tools and linters as mechanisms that help identify opportunities for code modernization.

Several participants mentioned tools such as **Clang-Tidy, Clazy, Sonar, IntelliJ inspections, and language-specific linters**. These tools analyze code and provide suggestions indicating that certain constructs could be replaced by newer language features or improved idioms. For example, P20 described how Clang-Tidy suggests modern C++ practices, such as replacing older constructs with more efficient alternatives.

Participants also described how these tools support incremental modernization. P04 explained that linters integrated into development workflows can indicate that certain constructs are obsolete and recommend replacements using newer language features. The participant emphasized that tools providing suggestions rather than automatic transformations are considered safer because developers retain control over the final decision.

P05 described how IDE suggestions helped developers learn new language constructs, such as lambda expressions. These suggestions can trigger curiosity and learning, allowing developers to understand modern constructs while improving code readability.

Similarly, P10 explained that linters often include auto-fix capabilities that help update legacy code to better practices, although the participant acknowledged that human review remains necessary because automated changes may alter behavior.

Pull request discussions and survey responses also showed practical examples of these suggestions being followed, such as replacing string formatting with **f-strings** in Python projects.

Across quotations, static analysis tools serve two complementary roles: they identify outdated constructs and suggest modernization opportunities, while also supporting learning and gradual adoption of newer language features.

### **Memo metrics**

Total quotations in this code: 14  
Total participants in this code: 7  
Participants: C++ Surveys, Python PR discussions, P04, P05, P10, P11, P20

### **Memo on “Using tooling to support and partially automate SCR”**

This code contains **11 quotations from 4 participants**: C++ Survey, P07, P08, P23, and P26). Participants consistently framed tooling as a mechanism to **support and partially automate SCR**, rather than fully replace manual effort. P07 and P08 argued that tools are useful to **accelerate repetitive and large-scale transformations**, particularly by identifying refactoring opportunities and reducing manual workload.

P23 emphasized that tooling should be treated as an **assistive layer**, requiring developers to actively review and guide changes. Similarly, P26 highlighted that automation is typically limited to **low-risk and well-understood transformations**, reinforcing that developers retain control over critical decisions.

Across multiple quotations (including recurring evidence from 31-JSEP-CodeBook), tooling is positioned as a **complement to developer expertise**, not a substitute. Automation is leveraged to improve efficiency, but developers consistently validate, adjust, or reject tool-generated outputs.

A clear pattern emerges where developers adopt a **hybrid execution model**, combining automation with manual oversight. Tooling is selectively applied based on the nature of the task, being preferred for deterministic and localized changes while avoided in complex or semantically sensitive scenarios.

Partial automation in SCR is therefore not about replacing developers, but about **augmenting their capabilities**, enabling more scalable and efficient rejuvenation while maintaining human control.

### **Memo metrics**

**Total quotations in this code:** 11  
 **Total participants in this code:** 4  
 **Participants:** P07, P08, P23, P26

# **Memo on “Resistance to change”**

This code contains 7 quotations from 5 participants: C++ Surveys, JavaScript PR discussions, P20, P24, and P29.

Participants described various forms of resistance to adopting new language constructs or evolving coding practices.

One recurring explanation concerns **habit and familiarity**. P20 referred to the “don’t move my cheese” phenomenon, where developers resist changing established practices even when new constructs become available. Similarly, C++ Surveys described situations where long-standing frameworks or patterns remain dominant because developers are accustomed to them.

Participants also described resistance emerging from **cognitive disruption** caused by new constructs. P24 reported that when lambda expressions were introduced in Java, developers initially resisted adopting them because they changed familiar programming patterns such as loops.

Another form of resistance involves **concerns about complexity or readability**. Pull-request discussions showed contributors questioning whether adopting new syntax (e.g., arrow functions in JavaScript) would increase the learning burden for contributors who are less familiar with the language.

Finally, participants noted **organizational and economic resistance**. P29 explained that modernization often requires time and resources, and organizations sometimes prioritize immediate problem resolution over long-term modernization efforts.

Across quotations, resistance appears as a socio-technical phenomenon involving habits, perceived complexity, organizational priorities, and developer familiarity with existing constructs.

### **Memo metrics**

Total quotations in this code: 7  
Total participants in this code: 5  
Participants: C++ Surveys, JavaScript PR discussions, P20, P24, P29

# **Memo on “Retrocompatibility disobligates developers to conduct SCR”**

This code contains 1 quotation from 1 participant: P16.

The participant described how backward compatibility in programming languages can reduce the necessity of performing explicit source code rejuvenation.

According to P16, many programming languages maintain strong backward compatibility guarantees. As a result, older code can often be compiled with newer compilers without requiring significant modifications. In such cases, developers may continue using existing code structures even when the language evolves.

The participant contrasted this situation with changes in supporting libraries. When libraries such as Hibernate evolve, the changes may require substantial refactoring because library APIs or supporting classes change. In contrast, language-level evolution may not force developers to modify existing code if compatibility is preserved.

This quotation suggests that backward compatibility can delay or reduce modernization efforts. Developers may adopt newer constructs primarily in newly written code while allowing older code to remain unchanged as long as it continues to compile and function correctly.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P16

# **Memo on “SCR automated tools may introduce bugs”**

This code contains 2 quotations from 2 participants: P09 and P11.

Participants described risks associated with automated tools that modify source code during modernization or migration processes.

P11 reported past experiences where automated tools directly modified code instead of only suggesting improvements. According to the participant, this behavior sometimes generated undesirable modifications that affected the structure of the program. The participant explained that such tools could alter large portions of the codebase automatically, making it difficult to understand what was changed and potentially introducing faults. Although tools have evolved over time, the participant emphasized that they should still be used cautiously.

P09 described a similar situation in which a migration tool modified many files automatically without clearly informing developers about the changes that were made. In that case, the modification introduced a failure that only became visible during execution. Developers had to rely on version control diffs to identify what had changed in the code. The participant highlighted the importance of transparency in automated transformations so that developers can understand and validate the modifications performed by the tool.

Across quotations, automated transformation tools are portrayed as useful but potentially risky. When tools modify code without clearly communicating the changes, developers may struggle to identify the source of introduced defects.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 2  
Participants: P09, P11

# **Memo on “SCR efforts may introduce bugs”**

This code contains 8 quotations from 5 participants: JavaScript PR discussions, P12, P18, P22, and P24.

Participants described how modernization or refactoring activities may introduce defects into previously stable systems.

Several participants emphasized that modifying existing code can produce unintended side effects. P18 explained that when developers update code due to external changes, such as language updates, the modification process itself may introduce new bugs. This can occur when developers are unfamiliar with the new constructs or when changes are performed quickly without sufficient planning.

P12 described situations where modifications to function prototypes or low-level components caused unexpected conflicts in other parts of the system. These changes often require extensive regression testing to verify that basic system behavior has not been altered.

Other quotations illustrate similar issues in pull request discussions. Developers highlighted potential failures related to optional chaining, function contexts, or event listeners that could cause runtime errors if the modernization is not carefully implemented.

Participants also explained that automated refactoring tools may struggle to perform transformations safely because many changes involve semantic decisions that cannot be fully automated.

Across quotations, modernization activities are perceived as risky operations. Even when the goal is to improve code quality or adopt new features, the process may introduce defects if changes are not carefully validated.

### **Memo metrics**

Total quotations in this code: 8  
Total participants in this code: 5  
Participants: JavaScript PR discussions, P12, P18, P22, P24

# **Memo on “SCR is a non-trivial effort”**

This code contains 17 quotations from 13 participants: P01, P04, P05, P06, P07, P08, P09, P11, P22, P25, P26, P27, and P29.

Participants consistently described source code rejuvenation as a complex and resource-intensive activity.

Many participants highlighted the technical challenges associated with migrating large codebases. P05 explained that upgrading between language versions becomes difficult when the project is large. Similarly, P07 noted that large codebases require extensive testing because changes can affect many components.

Participants also described organizational and operational constraints. P06 emphasized that updating systems can be difficult when multiple environments and users depend on the software being continuously available. In such contexts, stopping systems for refactoring or migration may not be feasible.

Several quotations described modernization as an incremental and manual process. P26 explained that version migration often requires updating dependencies and libraries step by step, verifying compatibility after each change. This process can involve significant manual work.

Participants also highlighted strategic considerations when deciding whether to modernize. P27 described a case where developers duplicated functionality in microservices using newer language versions instead of modifying the existing system directly. This strategy allowed the team to gradually transition to a modern architecture while minimizing risks to production systems.

Across quotations, source code rejuvenation is portrayed as a demanding activity that requires significant effort, coordination, and careful decision-making. The complexity arises from technical dependencies, large codebases, testing requirements, and organizational constraints.

### **Memo metrics**

Total quotations in this code: 17  
Total participants in this code: 13  
Participants: P01, P04, P05, P06, P07, P08, P09, P11, P22, P25, P26, P27, P29

# **Memo on “SCR might difficult code understanding”**

This code contains 7 quotations from 5 participants: C++ Surveys, JavaScript PR discussions, Python PR discussions, P16, and P24.

Participants described situations where adopting modern language constructs may complicate code comprehension for some developers.

Several quotations highlighted the tension between expressiveness and readability. P16 explained that certain constructs such as lambda expressions simplify implementation but may also make code harder to read, especially for developers unfamiliar with the syntax.

P24 similarly reported that developers sometimes struggle to understand code written using newer constructs. When some team members adopt modern patterns while others are unfamiliar with them, disagreements may emerge regarding code readability.

Participants from survey and pull-request discussions expressed comparable concerns. For example, some developers considered certain modern features, such as the auto keyword in C++, confusing because the type of variables becomes less explicit.

Pull request discussions also showed hesitation toward adopting constructs such as arrow functions when contributors believed they might increase the cognitive burden for developers unfamiliar with the syntax.

Across quotations, modern language constructs are viewed as having both advantages and drawbacks. While they can simplify implementation or reduce verbosity, they may also increase the difficulty of understanding code for developers who are not yet familiar with them.

### **Memo metrics**

Total quotations in this code: 7  
Total participants in this code: 5  
Participants: C++ Surveys, JavaScript PR discussions, Python PR discussions, P16, P24

# **Memo on “SCR requires careful planning”**

This code contains 18 quotations from 14 participants: P03, P06, P07, P08, P11, P12, P13, P19, P20, P22, P23, P25, P26, and P27.

Participants frequently emphasized that modernization efforts require careful planning and evaluation before implementation.

Several participants described the importance of analyzing the impact of adopting new features. P12 explained that developers must assess whether changes may destabilize the system or introduce operational risks. Similarly, P25 noted that teams often conduct detailed studies to understand how modifications will affect existing code, tests, and dependencies.

Participants also highlighted the need to understand new language features before adopting them. P19 described a process of studying language updates and evaluating whether they fit the current maintenance task. P23 explained that learning new features and adapting them to existing systems can be challenging, especially when dependencies or deprecated libraries are involved.

Compatibility and dependency management were also recurring themes. P26 described how upgrading frameworks or libraries requires verifying compatibility with other components of the system.

Several quotations illustrated strategic approaches to modernization. For example, P27 described a gradual migration strategy where new implementations were developed alongside existing functionality. This allowed the team to test and stabilize the new version before replacing the old one.

Across quotations, planning emerges as a central element in modernization activities. Developers often evaluate technical risks, dependency constraints, and organizational priorities before deciding whether and how to adopt new language features.

### **Memo metrics**

Total quotations in this code: 18  
Total participants in this code: 14  
Participants: P03, P06, P07, P08, P11, P12, P13, P19, P20, P22, P23, P25, P26, P27

# **Memo on “Service oriented computing favors SCR efforts”**

This code contains 1 quotation from 1 participant: P04.

The participant described how the structure of software systems can influence the feasibility of performing source code rejuvenation activities.

P04 explained that developers often avoid modifying features that are already stable in production unless the change is strictly necessary. Revalidating a production feature can require significant effort, including testing and verification processes. For this reason, teams frequently limit modernization efforts to specific parts of the system rather than applying changes across the entire codebase.

The participant emphasized that modern software architectures make this selective evolution easier. By decomposing systems into services or smaller components, developers can modernize individual parts of the system without affecting the whole application. This architectural structure reduces the risk associated with modernization and enables gradual evolution of the code.

Across this quotation, system architecture appears as an enabling factor. Modular or service-based structures allow developers to introduce new features or migrate parts of the system more safely while maintaining stability in other components.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P04

# **Memo on “Sources of language-evolution knowledge”**

This code contains 10 quotations from 8 participants: P01, P04, P07, P08, P09, P11, P12, and P27.

Participants described several channels through which they stay informed about the evolution of programming languages and related technologies.

One recurring source involves **online communities and technical media**. Participants reported following blogs, forums, and discussion platforms where developers and language maintainers share updates about new language versions and features.

Another frequently mentioned source is **GitHub repositories and project discussions**. Participants explained that observing repositories, following development discussions, and reading changelogs helps them track ongoing changes in programming languages and frameworks.

Participants also described **newsletters and curated technology reports** as important sources of information. For example, some developers follow newsletters such as InfoQ or technology radar publications to monitor emerging technologies and trends.

In addition, **social media and professional networks** play a role. Participants reported following influential developers and language maintainers on platforms such as LinkedIn or Twitter to stay informed about new releases or discussions around language evolution.

Some participants also mentioned **books and formal documentation** as sources of knowledge, although they noted that books are often slower to reflect recent language updates.

Across quotations, language-evolution knowledge appears to be obtained through a combination of formal and informal sources. Developers combine documentation, community discussions, online media, and peer exchange to stay updated on evolving language ecosystems.

### **Memo metrics**

Total quotations in this code: 10  
Total participants in this code: 8  
Participants: P01, P04, P07, P08, P09, P11, P12, P27

# **Memo on “Team cohesion”**

This code contains 4 quotations from 4 participants: P01, P14, P20, and P24.

Participants described how team dynamics influence decisions related to adopting new language features or upgrading language versions.

One recurring observation is that modernization initiatives often originate from developers who actively follow language evolution. According to P20, proposals to adopt new language features typically emerge internally from developers who recognize potential improvements in the code.

However, adoption decisions are not made individually. P14 explained that disagreements can arise in larger teams when some members prefer adopting newer language versions while others prefer maintaining existing practices.

Participants also emphasized that team capability must be considered. P01 explained that updating language versions may create difficulties if other team members are not familiar with the new constructs or features introduced by the update.

Finally, P24 described situations in which developers advocate for modernization during project planning, proposing upgrades when they see potential improvements in maintainability or development efficiency.

Across quotations, modernization decisions appear as collaborative processes influenced by team consensus, knowledge distribution, and internal discussions about the benefits and risks of adopting new technologies.

### **Memo metrics**

Total quotations in this code: 4  
Total participants in this code: 4  
Participants: P01, P14, P20, P24

# **Memo on “Tool configurability influencing source code rejuvenation adoption and control”**

This code contains 7 quotations from 6 participants: P01, P02, P05, P11, P22, and P23.

Participants discussed how development tools support modernization efforts and how their configuration affects their usefulness.

Several participants described using **static analysis tools, linters, or IDE assistants** that detect outdated constructs and suggest improvements. These tools often highlight parts of the code that could be updated to use newer language features or more modern idioms.

However, participants emphasized that developers often prefer tools that **suggest changes rather than automatically applying them**. P11 explained that automated tools that modify code without explicit confirmation may introduce confusion or unexpected changes. For this reason, tools that present suggestions and allow developers to manually confirm modifications are often preferred.

Participants also mentioned the importance of **tool configurability**. P01 explained that tools become more useful when developers can configure their behavior, disable certain checks, or control which transformations should be applied automatically.

Some participants described advanced uses of tools, such as developing custom plugins or static analysis extensions to detect modernization opportunities in specific codebases.

Across quotations, development tools are viewed as supportive mechanisms that help identify modernization opportunities. However, participants emphasize that tools should assist developers rather than fully automate complex code transformations.

### **Memo metrics**

Total quotations in this code: 7  
Total participants in this code: 6  
Participants: P01, P02, P05, P11, P22, P23

# **Memo on “tools should explain about code changes”**

This code contains 1 quotation from 1 participant: P09.

The participant described the importance of transparency when automated tools modify source code during migration or modernization tasks.

P09 reported an experience where a tool automatically changed multiple files during a migration process but did not provide clear information about the modifications performed. As a result, a defect introduced by the tool was only discovered when the system was executed. Developers had to inspect the Git diff to identify what had changed in the codebase.

The participant emphasized that tools should communicate clearly what transformations were applied and which parts of the code were affected. Providing this information helps developers understand the consequences of automated changes and reduces the risk of unexpected failures.

Across this quotation, transparency and traceability emerge as key expectations for automated code transformation tools. Developers prefer tools that explicitly explain their modifications rather than silently rewriting code.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P09

# **Memo on “Tools suggesting changes without enforcing automation”**

This code contains 4 quotations from 2 participants: P22 and P23.

Participants described a preference for development tools that suggest improvements instead of automatically enforcing code transformations.

P23 explained that IDE assistants often recommend simplified constructs or newer language features. However, the participant prefers tools that highlight potential improvements rather than directly modifying the code. This approach allows developers to review suggested changes and decide whether they are appropriate for the current context.

Participants also noted that automated transformations may produce noisy outputs or unnecessary modifications. For this reason, developers sometimes test such tools but avoid adopting them fully in real projects.

P22 described ongoing research on semi-automated tools that detect possible improvements while leaving final decisions to developers. The participant explained that some refactorings require semantic understanding and cannot always be performed safely by automated tools. Human judgment is therefore required to determine the appropriate transformation.

Across quotations, developers appear to favor **assistive tools** rather than fully automated transformation systems. Tools that identify opportunities for improvement and leave the final decision to developers are considered more reliable and acceptable in practice.

### **Memo metrics**

Total quotations in this code: 4  
Total participants in this code: 2  
Participants: P22, P23

# **Memo on “Tool-supported problem diagnosis”**

This code contains 1 quotation from 1 participant: P29.

The participant described using tools primarily for diagnosing problems in existing systems rather than for automatically performing modernization tasks.

P29 explained that a custom tool was developed to analyze issues in a transactional payment system. The tool was used to inspect how certain components were implemented and identify problems that occurred during system execution.

However, the participant reported not using automated tools to perform code evolution or modernization tasks. Instead, they preferred manually modifying the codebase when changes were required.

Across this quotation, tools appear as diagnostic instruments that support understanding and troubleshooting system behavior. Their role is primarily analytical rather than transformational.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P29

# **Memo on “tool support for SCR efforts”**

This code contains 11 quotations from 6 participants: C++ Study, C++ Surveys, P07, P08, P23, and P26.

Participants described several ways in which tools support source code rejuvenation activities.

One recurring example involves **migration tools provided by language ecosystems**. Participants reported using tools designed to assist with transitions between language versions, such as scripts used to migrate code from Python 2 to Python 3 or migration tools for framework updates.

Participants also mentioned **static analysis and refactoring tools** such as clang-tidy and other Clang-based utilities. These tools can detect outdated constructs and automatically transform certain patterns into modern equivalents.

Some quotations highlighted **command-line migration utilities** released alongside language updates. These tools can scan codebases and identify parts that require modification during version transitions.

Participants also explained that migration tools rarely perform complete transformations automatically. Instead, they often automate simple transformations and indicate where manual adjustments are required.

Across quotations, tools are portrayed as helpful facilitators of modernization tasks. They reduce the effort required to update codebases by identifying modernization opportunities and performing limited automated transformations.

### **Memo metrics**

Total quotations in this code: 11  
Total participants in this code: 6  
Participants: C++ Study, C++ Surveys, P07, P08, P23, P26

# **Memo on “Tool support limited to trivial SCR”**

This code contains 2 quotations from 2 participants: C++ Surveys and P22.

Participants described limitations in the current capabilities of automated tools for supporting source code rejuvenation.

P22 explained that tools such as clang-tidy can detect outdated constructs and automatically apply some refactorings. However, these transformations are typically limited to straightforward syntactic changes. More complex transformations often require manual rewriting and developer intervention.

Similarly, survey responses reported that scripts can assist with specific migration tasks, such as updating certain syntactic patterns. However, adopting more advanced language features often requires modifications to the program logic, which cannot be performed automatically.

Across quotations, tools are described as useful for **mechanical or repetitive transformations**, but insufficient for handling complex modernization tasks that involve deeper semantic or architectural changes.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 2  
Participants: C++ Surveys, P22

# **Memo on “Transpilation overhead constraining adoption”**

This code contains 1 quotation from 1 participant: JavaScript PR discussions.

The participant described how technical overhead introduced by build tools can discourage the adoption of newer language features.

In this case, the developer reported using ES6 modules but intentionally restricting the use of ES6 features outside the module boundaries. The reason was the additional overhead generated by the transpilation process required to convert ES6 code into ES5 for compatibility with older environments. According to the participant, using Babel to transpile even a small number of ES6 constructs significantly increased the amount of generated code.

As a result, the developer limited the use of modern features to avoid unnecessary complexity and performance overhead in the compiled output.

Across this quotation, build tooling constraints appear as a practical barrier to modernization. Even when developers are interested in using newer language features, the costs associated with transpilation or compatibility layers may discourage their broader adoption.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: JavaScript PR discussions

# **Memo on “trustness and reliability in legacy systems may hinder SCR efforts”**

This code contains 2 quotations from 1 participant: P12.

The participant emphasized that reliability considerations often discourage modernization efforts in critical or low-level systems.

P12 compared software evolution decisions to engineering practices in other domains, such as mechanical systems, where components remain unchanged for decades once they prove reliable. Similarly, in critical software components that are already stable and heavily used, developers may prefer not to introduce modifications unless there is a clear reliability benefit.

The participant also explained that this concern influences the adoption of automated code transformation tools. While such tools might be acceptable in higher-level applications, they are considered risky in low-level or mission-critical components where system behavior must remain stable.

Across quotations, reliability appears as a dominant decision criterion. When legacy code has already demonstrated long-term stability, developers may avoid modernization efforts that could potentially introduce unexpected behavior.

### **Memo metrics**

Total quotations in this code: 2  
Total participants in this code: 1  
Participants: P12

# **Memo on “Uniform knowledge”**

This code contains 11 quotations from 9 participants: P01, P02, P05, P09, P11, P13, P24, P26, and P28.

Participants frequently emphasized the importance of shared knowledge across development teams when adopting new language features.

Several participants explained that introducing advanced language constructs may create difficulties if other team members are not familiar with them. P01 noted that developers sometimes avoid adopting advanced features until knowledge about them is widely shared within the team. This helps ensure that future maintenance tasks can be performed by any team member.

Participants also described the role of **training, knowledge sharing, and internal communication** in enabling modernization. P02 suggested that teams should explicitly communicate language evolution decisions and ensure that developers understand how new features will be used within the project.

Other quotations illustrated how differences in knowledge levels can generate disagreements during adoption discussions. For example, P24 described situations where some developers supported the use of modern constructs while others resisted them because they were unfamiliar with the new syntax.

Across quotations, knowledge alignment within teams appears as a key factor influencing adoption decisions. Modernization is more likely to occur when developers share a common understanding of new language features and their benefits.

### **Memo metrics**

Total quotations in this code: 11  
Total participants in this code: 9  
Participants: P01, P02, P05, P09, P11, P13, P24, P26, P28

# **Memo on “Upgrading language implementation (compiler) might compromise performance”**

This code contains 4 quotations from 2 participants: JavaScript PR discussions and P20.

Participants discussed concerns that upgrading compilers or adopting newer language constructs may negatively affect system performance.

P20 described a case where migrating to a newer compiler version resulted in unexpected performance degradation. Although compiler upgrades typically improve performance or security, the participant reported a situation where the new compiler introduced slower execution in certain workloads. The cause remained unclear, but the experience reinforced the need for careful performance testing during upgrades.

Similarly, pull request discussions highlighted concerns that certain modern language constructs might introduce performance overhead. Developers mentioned examples such as arrow functions, rest syntax, and other modern JavaScript constructs that may increase memory allocations or garbage collection activity.

Across quotations, performance considerations emerge as an important constraint when adopting new language implementations or features. Developers may postpone modernization when performance regressions are suspected or when the runtime impact of new constructs is uncertain.

### **Memo metrics**

Total quotations in this code: 4  
Total participants in this code: 2  
Participants: JavaScript PR discussions, P20

# **Memo on “Use code review to recommend adoption of modern features”**

This code contains 12 quotations from 3 participants: JavaScript PR discussions, Python PR discussions, and P19.

Participants described code review processes as an important mechanism for encouraging the adoption of modern language features.

P19 explained that modernization often occurs through decentralized discussions during code review. Developers who are familiar with newer language features may suggest alternative implementations when reviewing colleagues’ code. These suggestions help disseminate knowledge about language evolution across the team.

Pull request discussions provided multiple examples of this practice. Reviewers recommended replacing older constructs with modern alternatives such as optional chaining in JavaScript or type annotations in Python.

These suggestions typically appear as informal comments rather than mandatory requirements. Developers may propose improvements such as adopting type hints, f-strings, or newer language constructs that make code clearer or more expressive.

Across quotations, code review functions as a social mechanism for modernization. Through review comments and discussions, developers share knowledge about language evolution and gradually introduce modern constructs into the codebase.

### **Memo metrics**

Total quotations in this code: 12  
Total participants in this code: 3  
Participants: JavaScript PR discussions, Python PR discussions, P19

# **Memo on “Minimizing dependency on third-party libraries”**

This code contains 6 quotations from 3 participants: C++ Study, P13, and P22.

Participants frequently described modernization as a way to reduce reliance on third-party libraries by replacing them with language-native or standard library features.

Several quotations from P22 illustrate this pattern in the context of C++. Before C++11, developers often relied on external libraries for capabilities such as multithreading or regular expressions. With the introduction of these features in the language standard, teams began replacing third-party solutions with standard implementations. According to the participant, this change reduces long-term maintenance problems, compatibility issues, and dependency management complexity.

Participants also emphasized practical operational advantages of reducing external dependencies. For example, removing third-party libraries simplifies build processes, distribution, and deployment environments, especially in ecosystems where dependency management tools are less mature.

Similarly, P13 described adopting Kotlin’s built-in serialization functionality instead of relying on widely used external libraries such as Jackson. In this case, the decision was influenced by the availability of a stable language-supported alternative and the perceived reliability of the official implementation.

Across quotations, the reduction of external dependencies appears as a recurring motivation for adopting modern language features. Developers frame language evolution as an opportunity to simplify system architecture and reduce long-term maintenance risks.

### **Memo metrics**

Total quotations in this code: 6  
Total participants in this code: 3  
Participants: C++ Study, P13, P22

# **Memo on “Using LLMs to understand language evolution”**

This code contains 1 quotation from 1 participant: P26.

The participant described using large language models as a support tool to understand differences between language versions.

P26 explained that LLMs were used primarily to explore how older constructs could be rewritten using newer language features. In the example discussed, the participant compared older JavaScript patterns with newer constructs such as arrow functions and React hooks. Instead of automatically migrating entire codebases, the participant used the tool to analyze small fragments of code and understand how language constructs had changed.

According to the participant, this exploratory use helped clarify how the new version of the language worked and how certain constructs should be applied in practice. After understanding the transformation, the participant manually replicated the changes in other parts of the system.

Across this quotation, LLMs appear as a learning and exploration mechanism rather than an automated migration tool. Developers use them to understand language evolution and guide manual modernization decisions.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P26

# **Memo on “Using transpilers to maintain compatibility”**

This code contains 1 quotation from 1 participant: JavaScript PR discussions.

The participant discussed the use of transpilation tools as a strategy to adopt modern language constructs while maintaining compatibility with older execution environments.

In this quotation, the developer explained that certain JavaScript constructs introduced in newer language versions require transpilation to ensure compatibility across different browsers. As a result, developers sometimes structure their code in ways that facilitate future transitions once the newer language feature becomes widely supported.

The participant illustrated this by describing how variable declarations were intentionally organized so that they could be easily modified once browser support for the newer feature improved.

Across this quotation, transpilation is presented as a transitional mechanism that enables developers to experiment with newer language constructs while preserving compatibility with older platforms.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: JavaScript PR discussions

# **Memo on “Using static analysis recommendations to guide SCR”**

This code contains 1 quotation from 1 participant: P22.

The participant described how static analysis tools can identify opportunities to modernize source code by detecting outdated constructs and recommending replacements.

In this case, P22 referred to Clang-based tools, particularly clang-tidy, which provide automated checks that detect older programming patterns and suggest modern alternatives. These tools can either generate warnings recommending improvements or automatically apply refactoring transformations depending on configuration settings.

However, the participant also emphasized that automated transformations are typically limited to relatively simple modifications. More substantial modernization changes often still require manual intervention by developers.

Across this quotation, static analysis tools appear as mechanisms that help identify modernization opportunities and guide rejuvenation efforts, while developers retain control over whether and how the recommended changes are applied.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: P22

# **Memo on “Version gap increases rejuvenation cost”**

This code contains 4 quotations from 2 participants: P17 and P29.

Participants described how large gaps between language versions can significantly increase the complexity and cost of modernization efforts.

P17 explained that when a system remains on very old versions of a language, developers may lose the opportunity to gradually address deprecations and incremental changes. As a result, migrating to a much newer version may require a large and disruptive update rather than a series of small adjustments.

Similarly, P29 discussed situations where modernization becomes so complex that organizations consider rewriting the system instead of performing an incremental migration. According to the participant, migration costs increase substantially when systems remain outdated for long periods.

Participants also emphasized that gradual evolution tends to reduce migration complexity. When upgrades are performed incrementally between consecutive versions, the required changes are often manageable and can be implemented quickly.

Across quotations, the size of the version gap emerges as a key factor influencing the feasibility and cost of rejuvenation efforts.

### **Memo metrics**

Total quotations in this code: 4  
Total participants in this code: 2  
Participants: P17, P29

# **Memo on “Volunteer-driven rejuvenation”**

This code contains 1 quotation from 1 participant: C++ Surveys.

The participant described modernization activities that occur through voluntary contributions across multiple projects.

In this example, developers reported running automated modernization tools across several repositories and submitting merge requests with the resulting improvements. According to the participant, the process is relatively inexpensive when automated tools are available, requiring mainly the effort of someone willing to perform the task and verify the results.

This quotation highlights how modernization efforts in open-source ecosystems may sometimes depend on individual contributors who proactively modernize code across multiple projects.

Across this quotation, rejuvenation appears as an activity occasionally driven by volunteer initiative rather than by formal project planning.

### **Memo metrics**

Total quotations in this code: 1  
Total participants in this code: 1  
Participants: C++ Surveys
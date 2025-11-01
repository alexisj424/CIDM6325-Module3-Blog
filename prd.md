# Product Requirements Document (PRD)

## 1. Document Information

- Product/Feature Name: Baby-Led Weaning (BLW) Tracker  
- Author(s): Alexis Lopez 
- Date Created: 2025-09-21  
- Last Updated: 2025-09-21  
- Version: 0.1 (Draft)  

---

## 2. Overview

- **Summary:**  
  The BLW Tracker is a web application that helps caregivers introduce solid foods to infants safely and confidently. It consolidates professional, evidence-based guidance into an accessible interface and provides a logging system for tracking food introductions and allergy notes.  

- **Problem Statement:**  
  Parents face confusion due to fragmented and inconsistent BLW information from blogs, social media, and informal sources. They need a centralized, reliable, and interactive resource to reduce anxiety and improve safety.  

- **Goals & Objectives:**  
  - Provide evidence-backed BLW food introduction guidance.  
  - Enable tracking of foods introduced, dates, and reactions.  
  - Increase caregiver confidence in food prep and allergy management.  
  - Lay groundwork for future scalability (meal planning, sharing).  

- **Non-Goals:**  
  - No personalized nutrition plans.  
  - No medical advice or diagnosis.  
  - No community/social features in MVP.  
  - No gamification at this stage.  

---

## 3. Context & Background

- **Business Context:**  
  This project demonstrates a socially relevant, usable digital artifact for portfolio development, showcasing how digital health apps balance usability, evidence, and scope control.  

- **Market/Customer Insights:**  
  - Target users: parents (25–40), first-time caregivers, and childcare providers.  
  - Insights: Many rely on anecdotal sources and lack confidence in safe food preparation.  
  - Need: Central, evidence-based guidance with interactive tracking.  

- **Competitive/Benchmark References:**  
  Existing baby apps (Solid Starts, BabyCenter) provide some guidance but lack structured evidence drawers and allergy tracking.  

---

## 4. Scope

- **In Scope:**  
  - Age-based food introduction lists with prep guidance.  
  - CRUD functionality for logging foods, dates, and notes.  
  - Allergy notes field for observations.  
  - Evidence drawer linking to AAP, WHO, and NHS.  

- **Out of Scope:**  
  - Personalized nutrition planning.  
  - Community/recipe sharing.  
  - Gamification.  
  - Automated allergy predictions.  

---

## 5. User Stories & Use Cases

- **Primary User Persona(s):** Parents, childcare providers.  

- **User Stories:**  
  - As a parent, I want to see safe starter foods so I can confidently begin solids.  
  - As a caregiver, I want to log foods given and when, so I don’t repeat or miss items.  
  - As a parent, I want to note allergy reactions so I can discuss them with my pediatrician.  

- **Use Case Scenarios:**  
  - *Happy Path:* Parent opens the app → selects “Add Food” → chooses avocado → logs date and note → entry saved.  
  - *Edge Case 1:* Parent tries to add the same food twice → app prevents duplicates and prompts edit instead.  
  - *Edge Case 2:* Parent enters incomplete food data → app requires food name before saving.  

---

## 6. Functional Requirements

- **FR-001:** Display age-appropriate food introduction lists.  
- **FR-002:** Provide safe preparation instructions for each food.  
- **FR-003:** CRUD operations for food logs (add, edit, delete).  
- **FR-004:** Simple text field for allergy/observation notes.  
- **FR-005:** Evidence drawer linking to authoritative references.  

---

## 7. Non-Functional Requirements

- **Performance:** Core views load in ≤2 s.  
- **Scalability:** Support modular future features (meal planning, sharing).  
- **Accessibility:** Meet WCAG 2.1 AA (color contrast, keyboard navigation).  
- **Security/Compliance:** No PII stored; local-only storage supported.  
- **Reliability/Availability:** CRUD operations persist data reliably.  

---

## 8. Dependencies

- **Internal:** Database schema for foods/logs; backend service for CRUD.  
- **External:** AAP, WHO, NHS guidelines as data references.  
- **Cross-team:** None in MVP; future may need design/QA support.  

---

## 9. Risks & Assumptions

- **Risks:**  
  - Unsafe or incorrect prep guidance → mitigate by using authoritative sources and disclaimers.  
  - Privacy concerns around child data → mitigate with local-only storage and no PII.  
  - Scope creep → mitigate by limiting MVP to 3 features.  

- **Assumptions:**  
  - Caregivers will accept general prep guidance, not tailored medical advice.  
  - Users will prefer simplicity over complex personalization.  

---

## 10. Acceptance Criteria

- User can add a food with name, date, and note in ≤3 steps.  
- Food lists display only safe, age-appropriate options.  
- Evidence drawer includes ≥3 authoritative citations.  
- All logged foods persist across sessions.  

---

## 11. Success Metrics

- ≥70% of new users log one food.  
- ≥80% of users report improved confidence in food preparation.  
- ≥30% of sessions use the evidence drawer.  
- ≥50% of users return within one week.  

---

## 12. Rollout & Release Plan

- **Phasing:**  
  - MVP (2 weeks): food list, logging, evidence drawer.  
  - Phase 2: export logs, filtering.  
  - Phase 3: optional advanced features.  

- **Release Channels:** Start with class repo submission → general availability if iterated.  
- **Training/Docs:** Lightweight README; usage notes for MVP.  

---

## 13. Open Questions

- Should logs support multiple children or just one profile?  
- Should the MVP allow export/sharing of logs with pediatricians?  
- Should food lists be preloaded or expandable by user input?  

---

## 14. References

- American Academy of Pediatrics. (2023). *Starting Solid Foods*. <https://www.healthychildren.org>  
- World Health Organization. (2023). *Complementary Feeding Guidelines*. <https://www.who.int/health-topics/infant-feeding>  
- National Health Service (UK). (2024). *Baby-led Weaning Advice*. <https://www.nhs.uk/startingsolids>  
- Centers for Disease Control and Prevention. (2023). *Infant & Toddler Nutrition*. <https://www.cdc.gov/nutrition>  

---

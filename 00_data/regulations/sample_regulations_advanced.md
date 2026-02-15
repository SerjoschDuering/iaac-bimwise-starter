# Advanced Regulations - LLM-Assisted Checks (Day 2)

These rules require an LLM to interpret spatial relationships, classify room usage (private vs. public), or evaluate geometric "potential" rather than simple attribute lookups.

---

## 1. Contextual Door Swing Impact

Doors opening into corridors generally create a risk of impact or obstruction. The regulations state that for corridors narrower than **2.50 meters**, door leaves must not invade the circulation width when opened. However, the system must identify the usage type of the zone: this prohibition applies strictly to general circulation areas but includes an exception for **"restricted use"** zones (such as inside private residential units) or zones of "null occupancy." The check must therefore determine the corridor's width, the door's swing direction, and whether the specific space is classified as private or public to decide if a violation exists.

*Source: Documento Básico SUA 2, Sección 1.2.1*

---

## 2. Variable Headroom Requirements

While checking ceiling heights seems straightforward, the required threshold changes based on the activity performed in the space. The general rule requires a minimum clear height of **2.20 meters** in circulation zones. However, the system must interpret the room tags to identify "restricted use" areas (like private hallways inside a dedicated apartment), where the requirement drops to **2.10 meters**. Furthermore, the system must detect specific elements like door frames (thresholds), where a further reduction to **2.00 meters** is permissible. The AI must map room names to these usage categories to apply the correct height filter.

*Source: Documento Básico SUA 2, Sección 1.1.1*

---

## 3. Geometric Exceptions for Patio Ventilation

Internal courtyards (patios) used for ventilation must generally allow the inscription of a **3-meter** diameter circle if they ventilate bedrooms, or **2.5 meters** for kitchens and bathrooms. However, there is a complex geometric exception: if the patio *only* ventilates stairwells or hygienic chambers (bathrooms) and the building height is **PB+3** (Ground floor + 3) or lower, the required diameter can be reduced to **1.80 meters**. The system must calculate the building's total floor count and analyze the types of rooms adjacent to the void to determine if this reduction is legal.

*Source: Decret 141/2012, Annex 1, Apartat 2.5.1*

---

## 4. Safety Barrier Necessity Analysis

Building code requires protective barriers (guardrails) wherever there is a drop in level greater than **55 centimeters**. However, the regulation allows for an exception based on "construction disposition": a barrier is not required if the layout makes a fall "very improbable." To automate this, the system cannot simply check the height difference; it must analyze the horizontal depth of the lower surface. For example, if a drop leads to a planter or architectural ledge that is sufficiently deep (e.g., **1 meter** or more) to catch a person or prevent them from reaching the edge, the system should interpret this as "improbable fall risk" and waive the guardrail requirement.

*Source: Documento Básico SUA 1, Sección 3.1.1 and Comentario: Graderíos en descenso*

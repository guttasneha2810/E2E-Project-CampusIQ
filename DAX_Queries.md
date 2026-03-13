### Power BI DAX Measures
This file contains the DAX measures used in the Student Analytics Dashboard.
---
## Total Admissions
```DAX
Total Admissions =
COUNT('Student all Years'[Student_ID])
```
---

## Total Placements

```DAX
Total Placements =
CALCULATE(
COUNT('Student all Years'[Student_ID]),
'Student all Years'[Placement_Status] <> "UNEMPLOYED"
)
```
---
## Unemployed Students

```DAX
Unemployed Students =
CALCULATE(
COUNT('Student all Years'[Student_ID]),
'Student all Years'[Placement_Status] = "UNEMPLOYED"
)
```
---

## Placement Rate

```DAX
Placement Rate =
DIVIDE([Total Placements],[Total Admissions],0)*100
```
---

## Average SSC Marks

```DAX
Avg SSC Marks =
AVERAGE('Student all Years'[SSC_Percentage])
```
---

## Average Inter Marks

```DAX
Avg Inter Marks =
AVERAGE('Student all Years'[Inter_Percentage])
```
---

## Average UG Marks

```DAX
Avg UG Marks =
AVERAGE('Student all Years'[Graduation_Percentage])
```
---

## Average Entrance Rank

```DAX
Avg Entrance Rank =
AVERAGE('Student all Years'[Entrance_Rank])
```
---

## Branch Admissions

```DAX
Branch Admissions =
COUNT('Student all Years'[Student_ID])
```
---

## Branch Placements

```DAX
Branch Placements =
CALCULATE(
COUNT('Student all Years'[Student_ID]),
'Student all Years'[Placement_Status] <> "UNEMPLOYED"
)
```
---

## Higher Studies

```DAX
Higher Studies =
CALCULATE(
COUNT('Student all Years'[Student_ID]),
NOT('Student all Years'[Placement_Status] = "UNEMPLOYED")
)
```
## Placement Category
```DAX
Placement_Category =
SWITCH(
    TRUE(),
    
    CONTAINSSTRING(UPPER('Student all Years'[Placement_Status]), "UNEMPLOYED"), "Unemployed",
    
    CONTAINSSTRING(UPPER('Student all Years'[Placement_Status]), "US") ||
    CONTAINSSTRING(UPPER('Student all Years'[Placement_Status]), "USA") ||
    CONTAINSSTRING(UPPER('Student all Years'[Placement_Status]), "UK") ||
    CONTAINSSTRING(UPPER('Student all Years'[Placement_Status]), "LONDON") ||
    CONTAINSSTRING(UPPER('Student all Years'[Placement_Status]), "GERMANY"),
    "Higher Studies",
    
    "Placed"
)
```

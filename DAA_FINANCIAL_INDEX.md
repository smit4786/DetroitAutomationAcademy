# 💼 DAA FINANCIAL MANAGEMENT - QUICK REFERENCE
## Detroit Automation Academy - Finance Documents Index

**Date:** January 30, 2026  
**Status:** 🟢 All documents ready

---

## 📚 FINANCIAL DOCUMENTS

### 1. EXPENSE MANAGEMENT FRAMEWORK
**File:** [EXPENSE_MANAGEMENT_FRAMEWORK.md](EXPENSE_MANAGEMENT_FRAMEWORK.md)

**What it covers:**
- Complete expense category breakdown (70/15/8/7 model)
- Year 1 and Year 2+ budget projections
- Revenue streams (grants, donations, programs)
- Automated tracking system design
- Financial control procedures
- Monthly reporting templates

**Best for:**
- Understanding DAA's financial structure
- Planning annual budget
- Setting spending priorities
- Establishing financial controls

**Key metrics:**
- Year 1 budget: $76,372 (operating) + $10,450 (capital)
- Year 2+ budget: $68,722 (sustainable)
- Program delivery target: 70% of budget
- Admin overhead target: 15%

---

### 2. GRANT TRACKING FRAMEWORK
**File:** [GRANT_TRACKING_FRAMEWORK.md](GRANT_TRACKING_FRAMEWORK.md)

**What it covers:**
- Foundation targeting ($15k-$30k range)
- Government grant opportunities
- Corporate & local grants
- Complete application checklists
- Proposal templates (project description, budget, evaluation)
- Grant tracking spreadsheet design
- Compliance & reporting requirements

**Best for:**
- Planning fundraising strategy
- Writing grant proposals
- Managing grant deadlines
- Tracking awards & reporting

**Key metrics:**
- Year 1 target: 8-12 applications
- Success rate goal: 40-50% (3-5 awards)
- Expected funding: $25k-$40k from grants
- Average grant size: $5k-$15k

---

### 3. EXPENSE SYNC AUTOMATION SCRIPT
**File:** [daa_expense_sync.py](daa_expense_sync.py)

**What it does:**
- Auto-categorizes academy expenses from spreadsheet
- Syncs expenses to Google Sheets budget
- Generates category summaries
- Creates audit logs
- Python + gspread integration

**How to use:**
1. Set up Google Sheets (like PERSONAL_BUDGET_FRAMEWORK.md process)
2. Update SPREADSHEET_ID in script
3. Run: `python3 daa_expense_sync.py`
4. Schedule with cron for automatic weekly/monthly syncs

**Similar to:** Personal budget_sync.py but tailored for academy expenses

---

## 🎯 QUICK START SEQUENCE

### Phase 1: Foundation (Week 1)
1. Read [EXPENSE_MANAGEMENT_FRAMEWORK.md](EXPENSE_MANAGEMENT_FRAMEWORK.md) (15 min)
2. Review expense categories and budget structure
3. Validate revenue assumptions
4. Select accounting software (QuickBooks or Wave)

### Phase 2: Fundraising (Week 2-3)
1. Read [GRANT_TRACKING_FRAMEWORK.md](GRANT_TRACKING_FRAMEWORK.md) (20 min)
2. Create grant tracking spreadsheet
3. Research 5-10 priority foundations
4. Submit first 2-3 grant applications

### Phase 3: Automation (Week 3-4)
1. Set up Google Sheets budget tracker (like personal budget setup)
2. Create service account (GOOGLE_CLOUD_WALKTHROUGH.md)
3. Configure [daa_expense_sync.py](daa_expense_sync.py)
4. Run script to test integration

### Phase 4: Ongoing
- Monthly expense tracking & reporting
- Quarterly board financial reviews
- Grant deadline monitoring
- Annual budget planning

---

## 💰 FINANCIAL STRUCTURE AT A GLANCE

### Budget Breakdown (Year 1)

```
Program Delivery          $56,822    70%
├─ Materials/Supplies    $14,350
├─ Instructor Comp       $28,700
├─ Technology            $2,372
└─ Facility             $11,400

Administration           $10,750    13%
├─ Legal/Professional    $5,500
├─ Insurance            $2,500
├─ Office Ops           $1,050
└─ Banking              $1,700

Marketing               $5,300     7%

Contingency             $3,500     4%

Equipment (Capital)     $10,450    (one-time)
────────────────────────────────────
TOTAL                   $86,822
```

### Revenue Targets (Year 1)

```
Foundation Grants       $15-30k    40-50%
Government Grants       $5-20k     10-25%
Program Revenue         $10-20k    20-30%
Corporate/In-Kind       $5-15k     10-20%
Individual Donations    $5-10k     10-15%
────────────────────────────────────
TOTAL TARGET           $40-95k
```

---

## 📊 FINANCIAL DOCUMENTS HIERARCHY

**Executive Level** (CEO/Founder)
→ Start with: EXPENSE_MANAGEMENT_FRAMEWORK overview + Year 1 budget section
→ Then: GRANT_TRACKING_FRAMEWORK timeline + revenue model

**Board Level** (Monthly/Quarterly)
→ Budget vs. actual comparison
→ Grant tracking dashboard
→ Financial health metrics
→ Year-end projections

**Operational Level** (Staff)
→ Expense categories & procedures
→ Approval workflows
→ How to categorize transactions
→ Monthly reporting process

**Finance/Accounting**
→ Complete EXPENSE_MANAGEMENT_FRAMEWORK (all sections)
→ Chart of accounts setup
→ Depreciation schedules
→ Grant compliance requirements

---

## 🔄 DOCUMENT RELATIONSHIPS

```
EXPENSE_MANAGEMENT_FRAMEWORK
  ├─ Defines expense categories
  ├─ Sets annual budget
  ├─ Guides daa_expense_sync.py categorization
  └─ Used for monthly reporting

GRANT_TRACKING_FRAMEWORK
  ├─ Provides revenue model
  ├─ Supplements EXPENSE_MANAGEMENT budget
  ├─ Tracks awards against budget
  └─ Manages compliance reporting

daa_expense_sync.py
  └─ Automates tracking using categories
      from EXPENSE_MANAGEMENT_FRAMEWORK
```

---

## ✅ IMPLEMENTATION CHECKLIST

**Foundation (Week 1):**
- [ ] Review EXPENSE_MANAGEMENT_FRAMEWORK
- [ ] Validate budget with board/advisors
- [ ] Select accounting software
- [ ] Open nonprofit bank account

**Fundraising (Week 2-3):**
- [ ] Review GRANT_TRACKING_FRAMEWORK
- [ ] Create grant tracking spreadsheet
- [ ] Research target foundations
- [ ] Write 2 draft proposals
- [ ] Submit first applications

**Automation (Week 3-4):**
- [ ] Create Google Sheet for expense tracking
- [ ] Set up service account & authentication
- [ ] Test daa_expense_sync.py script
- [ ] Configure weekly/monthly automation

**Ongoing:**
- [ ] Weekly expense review
- [ ] Monthly budget reporting
- [ ] Quarterly board reviews
- [ ] Quarterly grant progress
- [ ] Annual audit & planning

---

## 📈 KEY METRICS TO TRACK

**Monthly:**
- Total expenses vs. budget
- Burn rate (monthly spending)
- Cash reserves remaining
- Grant applications submitted
- Grant awards received

**Quarterly:**
- Program delivery spending (should be 70%)
- Revenue received vs. projected
- Grant success rate
- Budget variance analysis
- Forecast for rest of year

**Annually:**
- Total expenses by category
- ROI on equipment/capital investments
- Grant funding success rate
- Program reach & impact metrics
- Board satisfaction with financial health

---

## 🆘 QUICK REFERENCE LINKS

**Within Detroit Automation Academy Folder:**
- EXPENSE_MANAGEMENT_FRAMEWORK.md → Complete expense guide
- GRANT_TRACKING_FRAMEWORK.md → Fundraising guide
- daa_expense_sync.py → Automation script

**Related (Parent Directory - Resumes-and-Cover-Letters):**
- PERSONAL_BUDGET_COMPREHENSIVE.md → Similar personal budget framework (reference)
- GOOGLE_CLOUD_WALKTHROUGH.md → Setup instructions (applies to DAA too)
- budget_sync.py → Similar automation script (reference)

**External Resources:**
- Foundation Center: foundationcenter.org
- Grants.gov: grants.gov
- QuickBooks Nonprofit: quickbooks.intuit.com/nonprofit
- Wave (free): wave.com

---

## 🚀 NEXT ACTIONS (This Week)

1. **Read** EXPENSE_MANAGEMENT_FRAMEWORK (20 min)
2. **Decide** - Which grant foundations to target first (30 min)
3. **Create** - Google Sheet for expense tracking (15 min)
4. **Submit** - First grant application (2-3 hours)
5. **Schedule** - Automation setup for next week

---

**Document Owner:** Justin Smith (Founder)  
**Last Updated:** January 30, 2026  
**Review Schedule:** Monthly with finance team

**Version History:**
- v1.0 (Jan 30, 2026) - Initial framework documents created

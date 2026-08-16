## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/106

**Issue title:** Shared test fixture for a sample user profile is missing from tests

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**
Missing tests/fixtures/sample_profiles/basic_profile.json. Therefore, we have to restore the basic_profile.json. This file is in tests/fixtures/sample_profiles/basic_profile.json

**Branch name:** [test/106-test-fixture-for-a-sample-user-profile]

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [x] Issue added to cohort ledger

## Week 8 — Reproduction & solution planning

**Reproduction commit link:** [link to commit documenting the reproduced issue]

**Reproduction summary:**
I run make test in the terminal and go through the multi test case fail that related to the profile.json.

**PLAN.md link:** [link to PLAN.md in your fork]
docs/PLAN.md

**Walkthrough video (recommended):** [link to your Loom video, ≤2 min — recommended, not graded]

**Blockers or open questions:**
The blocker is I thought that I need to restore the deleted folder, so I went through the commits history in the github repo to find that folder. However, I can't find that folder at all. After rereading and understanding what restore mean, I then write a plan for create that file instead

## Week 9 — Solution building & PR submission

### Check-in 1 (mid-week)

**Current progress:**
I implement the conftest.py and adding sample resumes for the test to run based on the issue

**Next steps:**
I will double check on if it can run the relevant tests

**Blockers:**
[Anything slowing you down? Or leave blank.]

---

### Check-in 2 (end of week)

**PR link:** [https://github.com/thisisdientran/pathreview/tree/test/106-test-fixture-for-a-sample-user-profile]

**Branch:** [106-test-fixture-for-a-sample-user-profile]

**What you built:**
I created conftest.py and added the sample resume in it

**Tests added or updated:**
conftest.py and test_review_service.py

**Self-review confirmation:** [x] make check passes  [x] make test-unit passes

**Draft PR feedback received from:** [name or Slack handle, or "none"]

## Week 10 — Iteration & reflection

### Reviewer feedback

**Feedback received:** [ ] Yes  [x] No — still awaiting review

**Summary of feedback:**
[What did reviewers comment on? Or note that no review came in.]

**How you responded:**
[I see my grade but didn't see the feedback]

---

### Reflection

**What was harder than you expected?**
[The part harder than I expect is ensure the test not fail after adding the the part of the requirement into the test]

**What did you learn about working in a large codebase?**
[I found that it is very important to create seperate branch to avoid creating problem]

**How did AI tools help — and where did they fall short?**
[I found the AI tool help me understand the assignment and find the file location to help me understand the project]

**What would you do differently if you started over?**
[I would choice the same problem, but this time, I will approach the TP more so I can get the tip from them]

**What are you most proud of from this module?**
[I can contribute to the project for the first time]
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
# Future Work

- VLE-type–aware modeling — differentiate engagement by resource type (e.g. resource, oucontent, dataplus) rather than aggregating all clicks together.
- Incorporate actual assessment scores (not just pass/fail) and track performance over time within a module, rather than a single end-of-module snapshot.
- Analyze temporal engagement patterns (weekday vs. weekend, time of day) to uncover behavior patterns across VLE types.
- Move analysis to a cloud instance to support richer datasets and heavier models (e.g., regression trees).
- Share one canonical feature table across the unsupervised algorithms — BIRCH, DBSCAN, GMM, and K-Means each currently select their own feature subset (ranging from 9 to 25 features), which is a reasonable per-algorithm choice but makes their cluster results less directly comparable than a shared table would.

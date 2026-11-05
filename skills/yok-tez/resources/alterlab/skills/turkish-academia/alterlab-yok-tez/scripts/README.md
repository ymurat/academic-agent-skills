# Scripts removed

Automated query / harvest scripts that called tez.yok.gov.tr, dergipark.org.tr
or trdizin.gov.tr (and related unofficial search APIs) were removed from this
distribution on 2026-11-05.

Reason: site terms and robots.txt do not clearly authorize redistribution of
automated clients for those surfaces (DergiPark robots.txt disallows `/search`;
YÖK Ulusal Tez Merkezi has no public API and no clear automation terms;
TR Dizin robots.txt allows crawl of the marketing site but the unofficial
Elasticsearch search API has no published terms of use for bulk clients).

Use the skill instructions for **manual** browser search on the official sites.
Do not re-add scrapers without a written permission or a documented public API
policy from the site operator.

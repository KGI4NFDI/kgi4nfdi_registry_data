---
name: Data contribution
about: This issue template collects metadata required for contributions to the KGI
  registry.
title: "[KGI registry entry]"
labels: New registry entry, to review
assignees: elhossary, lozanaross

---

To add new KG resources to the KGI registry:
1. Please fill out the following metadata attributes, delete any instructional or example text in [] brackets,
2. add a note to the registry admins in the note field below if necessary. Most fields require text, URL or Wikidata item ID.
3. If there is no Wikidata item for the value you require, please add it to Wikidata first, then mention its QID.
4. Please USE the spaced bullet points as in the template.
5. Please DON'T remove the fenced YAML block
6. If some non-essential values are missing, remove the brackets placeholders

```yaml
Name of the KG*: [example: NFDI4Culture KG]
Description: [example: This KG contains the collection of X and Y, …]
Related NFDI consortium:
- [example: add Wikidata item ID, eg. Q98276929]
Related institution:
- [example: add Wikidata item ID, eg. Q1388737]
Contact point*:
- [example: Wikidata item contains information about a person or an organization, eg. Q30078997]
License(s)*:
- [example: add Wikidata item ID, eg. Q20007257 for CC-BY]
Subject(s):
- [example: add Wikidata item ID, eg Q50637 for art history]
KG software:
- [example: add Wikidata item ID for the KG engine software, eg. Q118980507]
KG URL: [add URL link]
URLs for SPARQL endpoint*: [add URL link]
URL for (REST) API: [add URL link]
URL for dump files: [add URL link]
Standard ontology(ies):
- [add URL links to ontologies]
```
Note to admin: [enter free text]

*required fields.

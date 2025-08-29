---
name: Custom issue template
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: elhossary

---

name: "Knowledge Graph Submission"
description: "Submit a Knowledge Graph (KG) to the KGI4NFDI registry."
title: "KG Submission: "
labels:
  - "kg-submission"
body:
  - type: markdown
    attributes:
      value: |
        Thanks for contributing a KG to the registry!  
        • Fields marked with * are required.  
        • For lists, enter one item per line.  
        • Prefer Wikidata Q-IDs wherever possible.

  - type: input
    id: kg_name
    attributes:
      label: "Name of the KG *"
      description: "Example: NFDI4Culture KG"
      placeholder: "NFDI4Culture KG"
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: "Description"
      description: "Briefly describe the KG (scope, content, audience)."
      placeholder: "This KG contains the collection of X and Y, …"
    validations:
      required: false

  - type: textarea
    id: related_nfdi
    attributes:
      label: "Related NFDI consortium"
      description: "Add Wikidata item IDs (one per line)."
      placeholder: |
        Q98276929
    validations:
      required: false

  - type: textarea
    id: related_institution
    attributes:
      label: "Related institution"
      description: "Add Wikidata item IDs (one per line)."
      placeholder: |
        Q1388737
    validations:
      required: false

  - type: textarea
    id: contact_point
    attributes:
      label: "Contact point *"
      description: "Wikidata item for a person or organisation (one per line)."
      placeholder: |
        Q30078997
    validations:
      required: true

  - type: textarea
    id: licenses
    attributes:
      label: "License(s) *"
      description: "Add Wikidata item IDs (one per line)."
      placeholder: |
        Q20007257  # CC BY
    validations:
      required: true

  - type: textarea
    id: subjects
    attributes:
      label: "Subject(s)"
      description: "Add Wikidata item IDs (one per line)."
      placeholder: |
        Q50637  # art history
    validations:
      required: false

  - type: textarea
    id: kg_software
    attributes:
      label: "KG software"
      description: "Add Wikidata item IDs for the KG engine (one per line)."
      placeholder: |
        Q118980507
    validations:
      required: false

  - type: input
    id: kg_url
    attributes:
      label: "KG URL"
      description: "Public landing page for the KG."
      placeholder: "https://example.org/kg"
    validations:
      required: false

  - type: textarea
    id: sparql_endpoints
    attributes:
      label: "URLs for SPARQL endpoint(s) *"
      description: "Add one URL per line."
      placeholder: |
        https://example.org/sparql
    validations:
      required: true

  - type: input
    id: rest_api
    attributes:
      label: "URL for (REST) API"
      description: "Base URL for the API, if available."
      placeholder: "https://example.org/api"
    validations:
      required: false

  - type: textarea
    id: dump_files
    attributes:
      label: "URL(s) for dump files"
      description: "Add one URL per line."
      placeholder: |
        https://example.org/dumps/kg.ttl.gz
    validations:
      required: false

  - type: textarea
    id: standard_ontologies
    attributes:
      label: "Standard ontology(ies)"
      description: "Add ontology URLs (one per line)."
      placeholder: |
        https://w3id.org/dcat
        https://w3id.org/nfdicore
    validations:
      required: false

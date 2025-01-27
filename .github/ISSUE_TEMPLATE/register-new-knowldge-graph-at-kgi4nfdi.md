---
name: Register new Knowldge Graph at KGI4NFDI
about: Here you can request to register a new Knowldge Graph at KGI registry
title: ''
labels: Add new
assignees: elhossary
body:
  - type: input
    id: title
    attributes:
      label: "Title"
      description: "Provide a short title for the resource."
      placeholder: "Enter a short title"
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: "Description"
      description: "Provide a detailed description of the resource."
      placeholder: "Enter a description"
    validations:
      required: true

  - type: textarea
    id: nfdi_consortia
    attributes:
      label: "NFDI Consortia"
      description: "List Wikidata item IDs (starting with Q) that are relevant to the resource."
      placeholder: "Example: Q35120, Q12345"
    validations:
      required: true

  - type: textarea
    id: publishers
    attributes:
      label: "Publishers"
      description: "List Wikidata item IDs of publishers."
      placeholder: "Example: Q35120, Q56789"

  - type: textarea
    id: contributers
    attributes:
      label: "Contributors"
      description: "List Wikidata item IDs of contributors."
      placeholder: "Example: Q35120, Q78901"

  - type: textarea
    id: contact_points
    attributes:
      label: "Contact Points"
      description: "List Wikidata item IDs for contact points."
      placeholder: "Example: Q35120, Q12345"

  - type: textarea
    id: licenses
    attributes:
      label: "Licenses"
      description: "List Wikidata item IDs for licenses."
      placeholder: "Example: Q35120, Q67890"

  - type: textarea
    id: software
    attributes:
      label: "Software"
      description: "List Wikidata item IDs of software tools used."
      placeholder: "Example: Q35120, Q89012"

  - type: textarea
    id: subject_areas
    attributes:
      label: "Subject Areas"
      description: "List Wikidata item IDs for relevant subject areas."
      placeholder: "Example: Q35120, Q45678"

  - type: input
    id: website
    attributes:
      label: "Website URL"
      description: "Provide a URL for the resource."
      placeholder: "https://example.com"
    validations:
      required: false

  - type: input
    id: sparql_query_interface
    attributes:
      label: "SPARQL Query Interface URL"
      description: "Provide a URL for the SPARQL query interface."
      placeholder: "https://example.com/sparql"
    validations:
      required: false

  - type: input
    id: sparql_endpoint
    attributes:
      label: "SPARQL Endpoint URL"
      description: "Provide a URL for the SPARQL endpoint."
      placeholder: "https://example.com/sparql-endpoint"
    validations:
      required: false

  - type: input
    id: rest_api_endpoint
    attributes:
      label: "REST API Endpoint URL"
      description: "Provide a URL for the REST API endpoint."
      placeholder: "https://example.com/api"
    validations:
      required: false

  - type: textarea
    id: ontologies
    attributes:
      label: "Ontology URLs"
      description: "List URLs for relevant ontologies."
      placeholder: "https://example.com/ontology1, https://example.com/ontology2"

  - type: textarea
    id: data_dumps
    attributes:
      label: "Data Dump URLs"
      description: "List URLs for downloadable data dumps."
      placeholder: "https://example.com/data1, https://example.com/data2"
---

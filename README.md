# KGI Registry Data
The KGI Registry Data repository is the dedicated space for collecting, structuring and ingesting metadata about other Knowledge Graphs used or created by the NFDI consortia into the KGI Service Registry.
 
## Contributing to the Registry
 The contribution workflow is as follows:
 
1) A representative of an NFDI consortium or research project fills out our [issue template](https://github.com/KGI4NFDI/kgi4nfdi_registry_data/issues/new?template=data-contribution.md) and submits a new issue.
2) The metadata submitted via the issue is transferred into a structured data format (.yaml), checked and validated before ingestion into the Registry triplestore.
3) If any data fails the validation process, the KGI admin team are notified and they can follow up with the contact person who submitted the issue for clarification and/or correction.
4) Once, all the metadata passes validation, it is ingested into the Registry and can be queried via the public SPARQL endpoint.
 
The current volume of metadata collected via issues is minimal and concerns primarily overall facts about the source KG, such as who is responsible for the KG, what licenses are used, which disciplines are covered, which software and ontologies are used by the KG, and what public endpoints can be queried. More granular metadata about individual data points contained in the KG is currently not collected. Instead, through information about the ontologies used by the KG and the KG endpoint, the Registry aims to facilitate federation.
 
## Ontology mappings
In the next phase of the KGI service integration, a planned integration of the TS4NFDI service will support mappings between different ontologies being registered in the KGI service and thereby facilitate easier federated search and discovery across diverse KG resources via the Registry’s public SPARQL endpoint.

import pandas as pd
import os, re, sys, yaml, argparse
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, DCAT, DCTERMS, FOAF, VOID, SKOS
from datetime import datetime

def parse_yaml(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"ERROR: Invalid YAML: {e}", file=sys.stderr)
            sys.exit(1)
    return data


def main():
    parser = argparse.ArgumentParser(description='Takes ')
    parser.add_argument("--yml_in", help="YAML with new metadata")
    parser.add_argument("--rdf_in", help="Pre-existing RDF file in turtle format")
    parser.add_argument("--out_dir", help="Output RDF file in turtle format")
    args = parser.parse_args()


    WIKIDATA = Namespace("http://www.wikidata.org/entity/")
    SCHEMA = Namespace("http://schema.org/")
    KGREG = Namespace("http://kgi.services.base4nfdi.de/entity/")

    g = Graph()
    g.bind("dcat", DCAT)
    g.bind("dct", DCTERMS)
    g.bind("foaf", FOAF)
    g.bind("void", VOID)
    g.bind("kgreg", KGREG)
    g.bind("schema", SCHEMA)
    g.bind("skos", SKOS)
    g.bind("wd", WIKIDATA)
    g.parse(args.rdf_in, format="turtle")
    record_uris = set(str(s) for s in g.subjects() if isinstance(s, URIRef))

    ids = []
    for uri in record_uris:
        match = re.search(r'KGR(\d+)$', uri)
        if match:
            ids.append(int(match.group(1)))

    x = max(ids) if ids else 0

    yml_data = parse_yaml(os.path.abspath(args.yml_in))

    x += 1
    entity_iri = URIRef(KGREG[f"KGR{x}"])
    g.add((entity_iri, RDF.type, DCAT.Dataset))

    title = yml_data['Name of the KG*']
    title = title.strip()
    g.add((entity_iri, DCTERMS.title, Literal(title, lang="en")))

    description = yml_data['Description']
    description = description.strip()
    g.add((entity_iri, DCTERMS.description, Literal(description, lang="en")))

    landurl = yml_data['KG URL']
    landurl = landurl.strip()
    g.add((entity_iri, DCAT["landingPage"], Literal(landurl)))

    publishers = yml_data['Related institution']
    if publishers:
        for publisher in publishers:
            publisher = publisher.strip()
            if publisher.startswith("Q"):
                g.add((entity_iri, DCTERMS.publisher, WIKIDATA[publisher]))

    ontology_urls = yml_data['Standard ontology(ies)']
    if ontology_urls:
        for ontology in ontology_urls:
            ontology = ontology.strip()
            g.add((entity_iri, DCTERMS.conformsTo, Literal(ontology)))

    sparql_urls = yml_data['URLs for SPARQL endpoint*']
    if sparql_urls:
        x += 1
        child_entity_iri = URIRef(KGREG[f"KGR{x}"])
        g.add((child_entity_iri, RDF.type, DCAT.DataService))
        for url in sparql_urls:
            if not url:
                continue
            url = url.strip()
            g.add((child_entity_iri, DCAT.endpointURL, Literal(url)))
            g.add((child_entity_iri, DCAT.servesDataset, entity_iri))
            # g.add((entity_iri, DCTERMS.publisher, child_entity_iri))

    api_urls = yml_data['URL for (REST) API']
    download_urls = yml_data['URL for dump files']
    if api_urls or download_urls:
        x += 1
        child_entity_iri = URIRef(KGREG[f"KGR{x}"])
        g.add((child_entity_iri, RDF.type, DCAT.Distribution))
        if api_urls:
            api_urls = api_urls.split(",")
            for url in api_urls:
                if not url:
                    continue
                url = url.strip()
                g.add((child_entity_iri, DCAT.accessURL, Literal(url)))
        if download_urls:
            download_urls = download_urls.split(",")
            for url in download_urls:
                if not url:
                    continue
                url = url.strip()
                g.add((child_entity_iri, DCAT.downloadURL, Literal(url)))
        g.add((entity_iri, DCAT.distribution, child_entity_iri))

    contacts = yml_data['Contact point*']
    if contacts:
        for contact in contacts:
            if not contact:
                continue
            contact = contact.strip()
            if contact.startswith("Q"):
                g.add((entity_iri, DCAT.contactPoint, WIKIDATA[contact]))
            else:
                g.add((entity_iri, DCAT.contactPoint, Literal(contact)))

    creators = yml_data['Related NFDI consortium']
    if creators:

        for creator in creators:
            if not creator:
                continue
            creator = creator.strip()
            if creator.startswith("Q"):
                g.add((entity_iri, DCTERMS.creator, WIKIDATA[creator]))
            else:
                g.add((entity_iri, DCTERMS.creator, Literal(creator)))
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    out_path = os.path.abspath(f"{args.out_dir}/{timestamp}_dataset.ttl")
    g.serialize(destination=out_path)

if __name__ == "__main__":
    main()
# coding: utf-8

# flake8: noqa

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from bio.knowledge.client.api.concepts_api import ConceptsApi
from bio.knowledge.client.api.metadata_api import MetadataApi
from bio.knowledge.client.api.statements_api import StatementsApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.bio.knowledge.client.model.client_beacon_concept_category import ClientBeaconConceptCategory
from swagger_client.bio.knowledge.client.model.client_beacon_predicate import ClientBeaconPredicate
from swagger_client.bio.knowledge.client.model.client_clique import ClientClique
from swagger_client.bio.knowledge.client.model.client_cliques_query import ClientCliquesQuery
from swagger_client.bio.knowledge.client.model.client_cliques_query_beacon_status import ClientCliquesQueryBeaconStatus
from swagger_client.bio.knowledge.client.model.client_cliques_query_result import ClientCliquesQueryResult
from swagger_client.bio.knowledge.client.model.client_cliques_query_status import ClientCliquesQueryStatus
from swagger_client.bio.knowledge.client.model.client_concept import ClientConcept
from swagger_client.bio.knowledge.client.model.client_concept_categories_by_beacon import ClientConceptCategoriesByBeacon
from swagger_client.bio.knowledge.client.model.client_concept_category import ClientConceptCategory
from swagger_client.bio.knowledge.client.model.client_concept_detail import ClientConceptDetail
from swagger_client.bio.knowledge.client.model.client_concept_with_details import ClientConceptWithDetails
from swagger_client.bio.knowledge.client.model.client_concept_with_details_beacon_entry import ClientConceptWithDetailsBeaconEntry
from swagger_client.bio.knowledge.client.model.client_concepts_query import ClientConceptsQuery
from swagger_client.bio.knowledge.client.model.client_concepts_query_beacon_status import ClientConceptsQueryBeaconStatus
from swagger_client.bio.knowledge.client.model.client_concepts_query_result import ClientConceptsQueryResult
from swagger_client.bio.knowledge.client.model.client_concepts_query_status import ClientConceptsQueryStatus
from swagger_client.bio.knowledge.client.model.client_knowledge_beacon import ClientKnowledgeBeacon
from swagger_client.bio.knowledge.client.model.client_knowledge_map import ClientKnowledgeMap
from swagger_client.bio.knowledge.client.model.client_knowledge_map_object import ClientKnowledgeMapObject
from swagger_client.bio.knowledge.client.model.client_knowledge_map_predicate import ClientKnowledgeMapPredicate
from swagger_client.bio.knowledge.client.model.client_knowledge_map_statement import ClientKnowledgeMapStatement
from swagger_client.bio.knowledge.client.model.client_knowledge_map_subject import ClientKnowledgeMapSubject
from swagger_client.bio.knowledge.client.model.client_log_entry import ClientLogEntry
from swagger_client.bio.knowledge.client.model.client_predicate import ClientPredicate
from swagger_client.bio.knowledge.client.model.client_predicates_by_beacon import ClientPredicatesByBeacon
from swagger_client.bio.knowledge.client.model.client_statement import ClientStatement
from swagger_client.bio.knowledge.client.model.client_statement_annotation import ClientStatementAnnotation
from swagger_client.bio.knowledge.client.model.client_statement_citation import ClientStatementCitation
from swagger_client.bio.knowledge.client.model.client_statement_details import ClientStatementDetails
from swagger_client.bio.knowledge.client.model.client_statement_object import ClientStatementObject
from swagger_client.bio.knowledge.client.model.client_statement_predicate import ClientStatementPredicate
from swagger_client.bio.knowledge.client.model.client_statement_subject import ClientStatementSubject
from swagger_client.bio.knowledge.client.model.client_statements_query import ClientStatementsQuery
from swagger_client.bio.knowledge.client.model.client_statements_query_beacon_status import ClientStatementsQueryBeaconStatus
from swagger_client.bio.knowledge.client.model.client_statements_query_result import ClientStatementsQueryResult
from swagger_client.bio.knowledge.client.model.client_statements_query_status import ClientStatementsQueryStatus

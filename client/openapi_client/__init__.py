# coding: utf-8

# flake8: noqa

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.concepts_api import ConceptsApi
from openapi_client.api.metadata_api import MetadataApi
from openapi_client.api.statements_api import StatementsApi

# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
# import models into sdk package
from openapi_client.models.client_beacon_concept_category import ClientBeaconConceptCategory
from openapi_client.models.client_beacon_predicate import ClientBeaconPredicate
from openapi_client.models.client_clique import ClientClique
from openapi_client.models.client_cliques_query import ClientCliquesQuery
from openapi_client.models.client_cliques_query_beacon_status import ClientCliquesQueryBeaconStatus
from openapi_client.models.client_cliques_query_result import ClientCliquesQueryResult
from openapi_client.models.client_cliques_query_status import ClientCliquesQueryStatus
from openapi_client.models.client_concept import ClientConcept
from openapi_client.models.client_concept_categories_by_beacon import ClientConceptCategoriesByBeacon
from openapi_client.models.client_concept_category import ClientConceptCategory
from openapi_client.models.client_concept_detail import ClientConceptDetail
from openapi_client.models.client_concept_with_details import ClientConceptWithDetails
from openapi_client.models.client_concept_with_details_beacon_entry import ClientConceptWithDetailsBeaconEntry
from openapi_client.models.client_concepts_query import ClientConceptsQuery
from openapi_client.models.client_concepts_query_beacon_status import ClientConceptsQueryBeaconStatus
from openapi_client.models.client_concepts_query_result import ClientConceptsQueryResult
from openapi_client.models.client_concepts_query_status import ClientConceptsQueryStatus
from openapi_client.models.client_knowledge_beacon import ClientKnowledgeBeacon
from openapi_client.models.client_knowledge_map import ClientKnowledgeMap
from openapi_client.models.client_knowledge_map_object import ClientKnowledgeMapObject
from openapi_client.models.client_knowledge_map_predicate import ClientKnowledgeMapPredicate
from openapi_client.models.client_knowledge_map_statement import ClientKnowledgeMapStatement
from openapi_client.models.client_knowledge_map_subject import ClientKnowledgeMapSubject
from openapi_client.models.client_log_entry import ClientLogEntry
from openapi_client.models.client_predicate import ClientPredicate
from openapi_client.models.client_predicates_by_beacon import ClientPredicatesByBeacon
from openapi_client.models.client_statement import ClientStatement
from openapi_client.models.client_statement_annotation import ClientStatementAnnotation
from openapi_client.models.client_statement_citation import ClientStatementCitation
from openapi_client.models.client_statement_details import ClientStatementDetails
from openapi_client.models.client_statement_object import ClientStatementObject
from openapi_client.models.client_statement_predicate import ClientStatementPredicate
from openapi_client.models.client_statement_subject import ClientStatementSubject
from openapi_client.models.client_statements_query import ClientStatementsQuery
from openapi_client.models.client_statements_query_beacon_status import ClientStatementsQueryBeaconStatus
from openapi_client.models.client_statements_query_result import ClientStatementsQueryResult
from openapi_client.models.client_statements_query_status import ClientStatementsQueryStatus

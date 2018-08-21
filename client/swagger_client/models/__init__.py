# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself. 

    OpenAPI spec version: 1.1.1
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .client_beacon_concept_category import ClientBeaconConceptCategory
from .client_beacon_predicate import ClientBeaconPredicate
from .client_clique import ClientClique
from .client_cliques_query import ClientCliquesQuery
from .client_cliques_query_beacon_status import ClientCliquesQueryBeaconStatus
from .client_cliques_query_result import ClientCliquesQueryResult
from .client_cliques_query_status import ClientCliquesQueryStatus
from .client_concept import ClientConcept
from .client_concept_categories_by_beacon import ClientConceptCategoriesByBeacon
from .client_concept_category import ClientConceptCategory
from .client_concept_detail import ClientConceptDetail
from .client_concept_with_details import ClientConceptWithDetails
from .client_concept_with_details_beacon_entry import ClientConceptWithDetailsBeaconEntry
from .client_concepts_query import ClientConceptsQuery
from .client_concepts_query_beacon_status import ClientConceptsQueryBeaconStatus
from .client_concepts_query_result import ClientConceptsQueryResult
from .client_concepts_query_status import ClientConceptsQueryStatus
from .client_knowledge_beacon import ClientKnowledgeBeacon
from .client_knowledge_map import ClientKnowledgeMap
from .client_knowledge_map_object import ClientKnowledgeMapObject
from .client_knowledge_map_predicate import ClientKnowledgeMapPredicate
from .client_knowledge_map_statement import ClientKnowledgeMapStatement
from .client_knowledge_map_subject import ClientKnowledgeMapSubject
from .client_log_entry import ClientLogEntry
from .client_predicate import ClientPredicate
from .client_predicates_by_beacon import ClientPredicatesByBeacon
from .client_statement import ClientStatement
from .client_statement_annotation import ClientStatementAnnotation
from .client_statement_citation import ClientStatementCitation
from .client_statement_details import ClientStatementDetails
from .client_statement_object import ClientStatementObject
from .client_statement_predicate import ClientStatementPredicate
from .client_statement_subject import ClientStatementSubject
from .client_statements_query import ClientStatementsQuery
from .client_statements_query_beacon_status import ClientStatementsQueryBeaconStatus
from .client_statements_query_result import ClientStatementsQueryResult
from .client_statements_query_status import ClientStatementsQueryStatus

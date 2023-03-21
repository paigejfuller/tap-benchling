"""Stream type classes for tap-benchling."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_benchling.client import BenchlingStream
from singer_sdk.helpers._typing import TypeConformanceLevel


class UsersStream(BenchlingStream):
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.NONE
    name = "users"
    path = "/users"
    records_jsonpath = "$.users[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("email", th.StringType),
        th.Property("id", th.StringType),
        th.Property("handle", th.StringType),
        th.Property("isSuspended", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("passwordLastChangedAt", th.DateTimeType)
    ).to_dict()


class DnaStream(BenchlingStream):
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.NONE
    name = "dna-sequences"
    path = "/dna-sequences"
    records_jsonpath = "$.dnaSequences[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("aliases", th.ArrayType(th.StringType)),
        th.Property("annotations", th.ArrayType(th.ObjectType(
            th.Property("color", th.StringType),
            th.Property("customFields", th.ArrayType(th.ObjectType())),
            th.Property("end", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("notes", th.StringType),
            th.Property("start", th.IntegerType),
            th.Property("strand", th.IntegerType),
            th.Property("type", th.StringType),
        ))),
        th.Property("apiURL", th.StringType),
        th.Property("archiveRecord", th.ObjectType(
            th.Property("reason", th.StringType),
        )),
        th.Property("authors", th.ArrayType(th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ))),
        th.Property("bases", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("creator", th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("customFields", th.ObjectType()),
        th.Property("dnaAlignmentIds", th.ArrayType(th.StringType)),
        th.Property("entityRegistryId", th.StringType),
        th.Property("fields", th.ObjectType()),
        th.Property("folderId", th.StringType),
        th.Property("id", th.StringType),
        th.Property("isCircular", th.BooleanType),
        th.Property("length", th.IntegerType),
        th.Property("modifiedAt", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("primers", th.ArrayType(
            th.ObjectType(
                th.Property("bases", th.StringType),
                th.Property("bindPosition", th.IntegerType),
                th.Property("color", th.StringType),
                th.Property("end", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("oligoId", th.StringType),
                th.Property("overhangLength", th.IntegerType),
                th.Property("start", th.IntegerType),
                th.Property("strand", th.IntegerType)
            )
        )),
        th.Property("registrationOrigin", th.ObjectType(
            th.Property("originEntryId", th.StringType),
            th.Property("registeredAt", th.DateTimeType),
        )),
        th.Property("registryId", th.StringType),
        th.Property("schema", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("translations", th.ArrayType(th.ObjectType(
            th.Property("aminoAcids", th.StringType),
            th.Property("color", th.StringType),
            th.Property("customFields", th.ArrayType(th.ObjectType())),
            th.Property("end", th.IntegerType),
            th.Property("geneticCode", th.StringType),
            th.Property("name", th.StringType),
            th.Property("notes", th.StringType),
            th.Property("regions", th.ArrayType(th.ObjectType(
                th.Property("end", th.IntegerType),
                th.Property("start", th.IntegerType),
            ))),
            th.Property("start", th.IntegerType),
            th.Property("strand", th.IntegerType),
        ))),
        th.Property("url", th.StringType),
        th.Property("webURL", th.StringType)
    ).to_dict()


class AaStream(BenchlingStream):
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.NONE
    name = "aa-sequences"
    path = "/aa-sequences"
    records_jsonpath = "$.aaSequences[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("aliases", th.ArrayType(th.StringType)),
        th.Property("aminoAcids", th.StringType),
        th.Property("annotations", th.ArrayType(th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("color", th.StringType),
            th.Property("end", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("start", th.IntegerType),
            th.Property("type", th.StringType),
        ))),
        th.Property("apiURL", th.StringType),
        th.Property("archiveRecord", th.ObjectType(
            th.Property("reason", th.StringType),
        )),
        th.Property("authors", th.ArrayType(th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ))),
        th.Property("createdAt", th.DateTimeType),
        th.Property("creator", th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("customFields", th.ObjectType()),
        th.Property("entityRegistryId", th.StringType),
        th.Property("fields", th.ObjectType()),
        th.Property("folderId", th.StringType),
        th.Property("id", th.StringType),
        th.Property("length", th.IntegerType),
        th.Property("modifiedAt", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("registrationOrigin", th.ObjectType(
            th.Property("originEntryId", th.StringType),
            th.Property("registeredAt", th.DateTimeType),
        )),
        th.Property("registryId", th.StringType),
        th.Property("schema", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("url", th.StringType),
        th.Property("webURL", th.StringType)
    ).to_dict()


class CustomEntitiesStream(BenchlingStream):
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.NONE
    name = "custom-entities"
    path = "/custom-entities"
    records_jsonpath = "$.customEntities[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("aliases", th.ArrayType(th.StringType)),
        th.Property("apiURL", th.StringType),
        th.Property("archiveRecord", th.ObjectType(
            th.Property("reason", th.StringType),
        )),
        th.Property("authors", th.ArrayType(th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ))),
        th.Property("createdAt", th.DateTimeType),
        th.Property("creator", th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("customFields", th.ObjectType()),
        th.Property("entityRegistryId", th.StringType),
        th.Property("fields", th.ObjectType()),
        th.Property("folderId", th.StringType),
        th.Property("id", th.StringType),
        th.Property("modifiedAt", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("registrationOrigin", th.ObjectType(
            th.Property("originEntryId", th.StringType),
            th.Property("registeredAt", th.DateTimeType),
        )),
        th.Property("registryId", th.StringType),
        th.Property("schema", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("url", th.StringType),
        th.Property("webURL", th.StringType)
    ).to_dict()


class EntriesStream(BenchlingStream):
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.NONE
    name = "entries"
    path = "/entries"
    records_jsonpath = "$.entries[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("apiURL", th.StringType),
        th.Property("archiveRecord", th.ObjectType(
            th.Property("reason", th.StringType),
        )),
        th.Property("assignedReviewers", th.ArrayType(th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ))),
        th.Property("authors", th.ArrayType(th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ))),
        th.Property("createdAt", th.DateTimeType),
        th.Property("creator", th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("customFields", th.ObjectType()),
        th.Property("days", th.ArrayType(th.ObjectType(
            th.Property("date", th.DateTimeType),
            th.Property("notes", th.ArrayType(th.ObjectType(
                th.Property("indentation", th.IntegerType),
                th.Property("links", th.ArrayType(th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("webURL", th.StringType),
                ))),
                th.Property("text", th.StringType),
                th.Property("type", th.StringType),
                th.Property("name", th.StringType),
            ))),
        ))),
        th.Property("displayId", th.StringType),
        th.Property("entryTemplateId", th.StringType),
        th.Property("fields", th.ObjectType()),
        th.Property("id", th.StringType),
        th.Property("modifiedAt", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("reviewRecord", th.ObjectType(
            th.Property("status", th.StringType)
        )),
        th.Property("schema", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("modifiedAt", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("webURL", th.StringType)
    ).to_dict()


class MixturesStream(BenchlingStream):
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.NONE
    name = "mixtures"
    path = "/mixtures"
    records_jsonpath = "$.mixtures[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("aliases", th.ArrayType(th.StringType)),
        th.Property("allowMeasuredIngredients", th.BooleanType),
        th.Property("amount", th.StringType),
        th.Property("apiURL", th.StringType),
        th.Property("archiveRecord", th.ObjectType(
            th.Property("reason", th.StringType),
        )),
        th.Property("authors", th.ArrayType(th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ))),
        th.Property("createdAt", th.DateTimeType),
        th.Property("creator", th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("customFields", th.ObjectType()),
        th.Property("entityRegistryId", th.StringType),
        th.Property("fields", th.ObjectType()),
        th.Property("id", th.StringType),
        th.Property("ingredients", th.ArrayType(
            th.ObjectType(
                th.Property("amount", th.StringType),
                th.Property("catalogIdentifier", th.StringType),
                th.Property("componentEntity", th.ObjectType(
                    th.Property("entityRegistryId", th.StringType),
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                )),
                th.Property("componentLotContainer", th.ObjectType(
                    th.Property("barcode", th.StringType),
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                )),
                th.Property("componentLotEntity", th.ObjectType(
                    th.Property("entityRegistryId", th.StringType),
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                )),
                th.Property("componentLotText", th.StringType),
                th.Property("hasParent", th.BooleanType),
                th.Property("notes", th.StringType),
                th.Property("targetAmount", th.StringType),
                th.Property("units", th.StringType),
            )
        )),
        th.Property("modifiedAt", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("registrationOrigin", th.ObjectType(
            th.Property("originEntryId", th.StringType),
            th.Property("registeredAt", th.DateTimeType),
        )),
        th.Property("registryId", th.StringType),
        th.Property("schema", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("modifiedAt", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("units", th.StringType),
        th.Property("webURL", th.StringType),
    ).to_dict()


class ContainersStream(BenchlingStream):
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.NONE
    name = "containers"
    path = "/containers"
    records_jsonpath = "$.containers[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("archiveRecord", th.ObjectType(
            th.Property("reason", th.StringType),
        )),
        th.Property("barcode", th.StringType),
        th.Property("checkoutRecord", th.ObjectType()),
        th.Property("contents", th.ArrayType(th.ObjectType())),
        th.Property("createdAt", th.DateTimeType),
        th.Property("creator", th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("fields", th.ObjectType()),
        th.Property("id", th.StringType),
        th.Property("modifiedAt", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("parentStorageId", th.StringType),
        th.Property("parentStorageSchema", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("projectId", th.StringType),
        th.Property("quantity", th.ObjectType(
            th.Property("units", th.StringType),
            th.Property("value", th.NumberType),
        )),
        th.Property("schema", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("volume", th.ObjectType(
            th.Property("units", th.StringType),
            th.Property("value", th.NumberType),
        )),
        th.Property("webURL", th.StringType),
    ).to_dict()



class AssayResultSchemasStream(BenchlingStream):
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.NONE
    name = "assay_result_schemas"
    path = "/assay-result-schemas"
    records_jsonpath = "$.assayResultSchemas[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("archiveRecord", th.ObjectType(
            th.Property("reason", th.StringType)
        )),
        th.Property("fieldDefinitions", th.ArrayType(
            th.ObjectType(
                th.Property("archiveRecord", th.ObjectType(
                    th.Property("reason", th.StringType)
                )),
                th.Property("id", th.StringType),
                th.Property("isMulti", th.BooleanType),
                th.Property("isRequired", th.BooleanType),
                th.Property("name", th.StringType),
                th.Property("type", th.StringType),
                th.Property("numericMin", th.NumberType),
                th.Property("numericMax", th.NumberType),
                th.Property("decimalPrecision", th.IntegerType),
                th.Property("legalTextDropdownId", th.StringType),
                th.Property("dropdownId", th.StringType),
                th.Property("schemaId", th.StringType),
            )
        )),
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("derivedFrom", th.StringType),
        th.Property("organization", th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("systemName", th.StringType),
        th.Property("modifiedAt", th.DateTimeType),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "schema_id": record["id"],
        }


class AssayResultsStream(BenchlingStream):
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.NONE
    name = "assay_results"
    parent_stream_type = AssayResultSchemasStream
    ignore_parent_replication_keys = True
    path = "/assay-results"
    records_jsonpath = "$.assayResults[*]"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("archiveRecord", th.ObjectType(
            th.Property("reason", th.StringType)
        )),
        th.Property("createdAt", th.DateTimeType),
        th.Property("creator", th.ObjectType(
            th.Property("handle", th.StringType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("entryId", th.StringType),
        th.Property("fieldValidation", th.ObjectType(
            th.Property("additionalProp1", th.ObjectType(
                th.Property("validationComment", th.StringType),
                th.Property("validationStatus", th.StringType),
            )),
            th.Property("additionalProp2", th.ObjectType(
                th.Property("validationComment", th.StringType),
                th.Property("validationStatus", th.StringType),
            )),
            th.Property("additionalProp3", th.ObjectType(
                th.Property("validationComment", th.StringType),
                th.Property("validationStatus", th.StringType),
            ))
        )),
        th.Property("fields", th.ObjectType()),
        th.Property("id", th.StringType),
        th.Property("isReviewed", th.BooleanType),
        th.Property("modifiedAt", th.DateTimeType),
        th.Property("projectId", th.StringType),
        th.Property("schema", th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("validationComment", th.StringType),
        th.Property("validationStatus", th.StringType),
    ).to_dict()

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {
            "schemaId": context["schema_id"]
        }
        if next_page_token:
            params["nextToken"] = next_page_token
        return params

"""Benchling tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_benchling.streams import (
    BenchlingStream,
    UsersStream,
    DnaStream,
    AaStream,
    CustomEntitiesStream,
    EntriesStream,
    MixturesStream,
    ContainersStream,
    AssayResultSchemasStream,
    AssayResultsStream,
)

STREAM_TYPES = [
    UsersStream,
    DnaStream,
    AaStream,
    CustomEntitiesStream,
    EntriesStream,
    MixturesStream,
    ContainersStream,
    AssayResultSchemasStream,
    AssayResultsStream,
]


class TapBenchling(Tap):
    """Benchling tap class."""
    name = "tap-benchling"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.mysample.com",
            description="The url for the API service"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapBenchling.cli()

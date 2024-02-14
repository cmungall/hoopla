"""Data test."""
import os
import glob
import unittest
from pathlib import Path

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import json_dumper, rdflib_dumper
from linkml_runtime.loaders import yaml_loader
from prefixmaps.io.parser import load_multi_context

import hoopla.datamodel as hoopla_datamodel
from hoopla import MAIN_SCHEMA_PATH
from hoopla.utils.example_runner import ExampleRunner
from tests import INPUT_EXAMPLES_PATH, OUTPUT_EXAMPLES_PATH

INPUT_EXAMPLE_FILES = glob.glob(os.path.join(str(INPUT_EXAMPLES_PATH), '*.yaml'))

class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def setUp(self) -> None:
        schemaview = SchemaView(str(MAIN_SCHEMA_PATH))
        ctxt = load_multi_context(["obo", "linked_data", "prefixcc"])
        self.example_runner = ExampleRunner(schemaview=schemaview, python_module=hoopla_datamodel,
                                            input_directory=INPUT_EXAMPLES_PATH,
                                            output_directory=OUTPUT_EXAMPLES_PATH,
                                            prefix_map=ctxt.as_dict())

    def test_data(self):
        """Ensure example data is processable."""
        er = self.example_runner
        er.process_examples()

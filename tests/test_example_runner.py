"""Data test."""
import os
import glob
import unittest
from pathlib import Path

import yaml
from linkml_runtime import SchemaView
from prefixmaps.io.parser import load_multi_context

import hoopla.datamodel as hoopla_datamodel
from hoopla import MAIN_SCHEMA_PATH
from hoopla.datamodel import Pattern
from hoopla.utils.example_runner import ExampleRunner
from tests import INPUT_EXAMPLES_PATH, OUTPUT_EXAMPLES_PATH

INPUT_EXAMPLE_FILES = glob.glob(os.path.join(str(INPUT_EXAMPLES_PATH), '*.yaml'))

class TestExampleRunner(unittest.TestCase):
    """Test example runner."""

    def setUp(self) -> None:
        schemaview = SchemaView(str(MAIN_SCHEMA_PATH))
        ctxt = load_multi_context(["obo", "linked_data", "prefixcc"])
        self.example_runner = ExampleRunner(schemaview=schemaview, python_module=hoopla_datamodel,
                                            input_directory=INPUT_EXAMPLES_PATH,
                                            output_directory=OUTPUT_EXAMPLES_PATH,
                                            prefix_map=ctxt.as_dict())

    def test_load_from_dict(self):
        """test loading from a dict object, including using type designators."""
        er = self.example_runner
        obj = er.load_from_dict([{"@type": "SubClassTriad"}], target_class=None)
        print(obj)
        with open(str(INPUT_EXAMPLES_PATH / "PatternInstantiationCollection-limb.yaml")) as file:
            dict_obj = yaml.safe_load(file)
        obj: hoopla_datamodel.PatternInstantiationCollection
        obj = er.load_from_dict(dict_obj, target_class="PatternInstantiationCollection")
        print(obj)
        self.assertIsInstance(obj.ontology, hoopla_datamodel.Ontology)
        self.assertIsInstance(obj.patterns[0], hoopla_datamodel.SubClassTriad)

    def test_example_runner(self):
        """Example runner test."""
        er = self.example_runner
        er.process_examples()


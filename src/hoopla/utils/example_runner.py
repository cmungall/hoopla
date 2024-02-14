import glob
import os
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Union, Any, Mapping

import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import json_dumper, rdflib_dumper, yaml_dumper
from linkml_runtime.linkml_model import ClassDefinitionName, ElementName
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.formatutils import camelcase


@dataclass
class ExampleRunner:
    """
    Processes a collection of positive and negative examples.
    """

    input_directory: Path = None
    """Directory in which positive instance examples are found."""

    counter_example_input_directory: Path = None
    """Directory in which negative instance examples are found. These are expected to fail."""

    output_directory: Path = None
    """Directory where processed examples are written to."""

    schemaview: SchemaView = None
    """View over schema which all examples adhere to."""

    python_module: ModuleType = None
    """Module containing classes that all examples instantiate."""

    prefix_map: Mapping[str, str] = None
    """Custom prefix map, for emitting RDF/turtle."""

    def process_examples(self):
        sv = self.schemaview
        input_examples = glob.glob(os.path.join(str(self.input_directory), '*.yaml'))
        for input_example in input_examples:
            stem = Path(input_example).stem
            base = Path(self.output_directory / stem)
            base.parent.mkdir(exist_ok=True, parents=True)
            parts = stem.split("-")
            tc = parts[0]
            with open(input_example) as file:
                input_dict = yaml.safe_load(file)
                obj = self.load_from_dict(input_dict, target_class=tc)
            yaml_dumper.dump(obj, to_file=f"{base}.yaml")
            json_dumper.dump(obj, to_file=f"{base}.json")
            rdflib_dumper.dump(obj, to_file=f"{base}.ttl", schemaview=sv, prefix_map=self.prefix_map)

    def load_from_dict(self, dict_obj: Any, target_class: Union[str, ElementName]) -> Any:
        sv = self.schemaview
        if isinstance(dict_obj, dict):
            if target_class not in sv.all_classes():
                raise ValueError(f"No such class as {target_class}")
            td_slot = sv.get_type_designator_slot(target_class) if target_class else None
            if td_slot:
                if td_slot.name in dict_obj:
                    target_class = dict_obj[td_slot.name]
            elif "@type" in dict_obj:
                target_class = dict_obj["@type"]
                del dict_obj["@type"]
            if ":" in target_class:
                target_classes = [c for c in sv.all_classes() if sv.get_uri(c) == target_class]
                if len(target_classes) != 1:
                    raise ValueError(f"Cannot find unique class for URI {target_class}; got: {target_classes}")
                target_class = target_classes[0]
            new_dict_obj = {}
            for k, v in dict_obj.items():
                if v is not None:
                    islot = sv.induced_slot(k, target_class)
                    v2 = self.load_from_dict(v, target_class=islot.range)
                    new_dict_obj[k] = v2
            py_target_class = getattr(self.python_module, camelcase(target_class))
            return py_target_class(**new_dict_obj)
        elif isinstance(dict_obj, list):
            return [self.load_from_dict(x, target_class) for x in dict_obj]
        else:
            return dict_obj






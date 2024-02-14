# Auto generated from hoopla.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-01-13T17:51:49
# Schema: hoopla
#
# id: https://w3id.org/hoopla
# description: A library of high level ontology patterns.
# license: BSD-3

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCTERMS = CurieNamespace('dcterms', 'http://example.org/UNKNOWN/dcterms/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
HOOPLA = CurieNamespace('hoopla', 'https://w3id.org/hoopla/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OPLA = CurieNamespace('opla', 'http://ontologydesignpatterns.org/opla/')
OWL = CurieNamespace('owl', 'http://example.org/UNKNOWN/owl/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HOOPLA


# Types

# Class references
class EntityId(extended_str):
    pass


class OntologyId(EntityId):
    pass


class ClassId(EntityId):
    pass


@dataclass
class PatternInstantiationCollection(YAMLRoot):
    """
    A combination of an ontology plus any number of pattern instances
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["PatternInstantiationCollection"]
    class_class_curie: ClassVar[str] = "hoopla:PatternInstantiationCollection"
    class_name: ClassVar[str] = "PatternInstantiationCollection"
    class_model_uri: ClassVar[URIRef] = HOOPLA.PatternInstantiationCollection

    title: Optional[str] = None
    description: Optional[str] = None
    ontology: Optional[Union[dict, "Ontology"]] = None
    patterns: Optional[Union[Union[dict, "Pattern"], List[Union[dict, "Pattern"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ontology is not None and not isinstance(self.ontology, Ontology):
            self.ontology = Ontology(**as_dict(self.ontology))

        if not isinstance(self.patterns, list):
            self.patterns = [self.patterns] if self.patterns is not None else []
        self.patterns = [v if isinstance(v, Pattern) else Pattern(**as_dict(v)) for v in self.patterns]

        super().__post_init__(**kwargs)


@dataclass
class Entity(YAMLRoot):
    """
    Entities can be patterns or individual elements
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["Entity"]
    class_class_curie: ClassVar[str] = "hoopla:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Entity

    id: Union[str, EntityId] = None
    label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass
class Ontology(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["Ontology"]
    class_class_curie: ClassVar[str] = "hoopla:Ontology"
    class_name: ClassVar[str] = "Ontology"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Ontology

    id: Union[str, OntologyId] = None
    classes: Optional[Union[Dict[Union[str, ClassId], Union[dict, "Class"]], List[Union[dict, "Class"]]]] = empty_dict()
    source: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyId):
            self.id = OntologyId(self.id)

        self._normalize_inlined_as_list(slot_name="classes", slot_type=Class, key_name="id", keyed=True)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


@dataclass
class Class(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Class"]
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Class

    id: Union[str, ClassId] = None
    members: Optional[Union[Union[str, EntityId], List[Union[str, EntityId]]]] = empty_list()
    size: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassId):
            self.id = ClassId(self.id)

        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, EntityId) else EntityId(v) for v in self.members]

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        super().__post_init__(**kwargs)


class AntiPattern(YAMLRoot):
    """
    A mixin for patterns that should be avoided
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["AntiPattern"]
    class_class_curie: ClassVar[str] = "hoopla:AntiPattern"
    class_name: ClassVar[str] = "AntiPattern"
    class_model_uri: ClassVar[URIRef] = HOOPLA.AntiPattern


class SometimesAntiPattern(YAMLRoot):
    """
    A mixin for patterns that are sometimes considered anti-patterns
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["SometimesAntiPattern"]
    class_class_curie: ClassVar[str] = "hoopla:SometimesAntiPattern"
    class_name: ClassVar[str] = "SometimesAntiPattern"
    class_model_uri: ClassVar[URIRef] = HOOPLA.SometimesAntiPattern


class Grouping(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["Grouping"]
    class_class_curie: ClassVar[str] = "hoopla:Grouping"
    class_name: ClassVar[str] = "Grouping"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Grouping


@dataclass
class Pattern(YAMLRoot):
    """
    Abstract base class for all patterns. A pattern class defines a set of entities (which may be classes or
    individuals or other entities), together with relationships that hold between them.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["Pattern"]
    class_class_curie: ClassVar[str] = "hoopla:Pattern"
    class_name: ClassVar[str] = "Pattern"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Pattern

    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self.type = str(self.class_name)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class SubGraph(Pattern):
    """
    A pattern that corresponds to a static collection of entities in
    a single graph or ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["SubGraph"]
    class_class_curie: ClassVar[str] = "hoopla:SubGraph"
    class_name: ClassVar[str] = "SubGraph"
    class_model_uri: ClassVar[URIRef] = HOOPLA.SubGraph

    title: Optional[str] = None
    description: Optional[str] = None
    source: Optional[str] = None
    variant_of: Optional[Union[Union[dict, "SubGraph"], List[Union[dict, "SubGraph"]]]] = empty_list()
    should_be_replaced_by: Optional[Union[dict, "SubGraph"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if not isinstance(self.variant_of, list):
            self.variant_of = [self.variant_of] if self.variant_of is not None else []
        self.variant_of = [v if isinstance(v, SubGraph) else SubGraph(**as_dict(v)) for v in self.variant_of]

        if self.should_be_replaced_by is not None and not isinstance(self.should_be_replaced_by, SubGraph):
            self.should_be_replaced_by = SubGraph(**as_dict(self.should_be_replaced_by))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Pair(SubGraph):
    """
    An abstract SubGraph in which the focus is a pair of nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["Pair"]
    class_class_curie: ClassVar[str] = "hoopla:Pair"
    class_name: ClassVar[str] = "Pair"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Pair


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Triad(SubGraph):
    """
    An abstract SubGraph in which the focus is a trio of nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["Triad"]
    class_class_curie: ClassVar[str] = "hoopla:Triad"
    class_name: ClassVar[str] = "Triad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Triad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Quad(SubGraph):
    """
    An abstract SubGraph in which the focus is a quad of nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["Quad"]
    class_class_curie: ClassVar[str] = "hoopla:Quad"
    class_name: ClassVar[str] = "Quad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Quad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class GroupingPair(Pair):
    """
    A SubGraph in which the focus is a pair of nodes where one (child) is a part of a group formed by the other
    (parent)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["GroupingPair"]
    class_class_curie: ClassVar[str] = "hoopla:GroupingPair"
    class_name: ClassVar[str] = "GroupingPair"
    class_model_uri: ClassVar[URIRef] = HOOPLA.GroupingPair

    parent: Optional[str] = None
    child: Optional[str] = None
    child_to_parent_relationship_type: Optional[str] = None
    additional_axioms: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.parent is not None and not isinstance(self.parent, str):
            self.parent = str(self.parent)

        if self.child is not None and not isinstance(self.child, str):
            self.child = str(self.child)

        if self.child_to_parent_relationship_type is not None and not isinstance(self.child_to_parent_relationship_type, str):
            self.child_to_parent_relationship_type = str(self.child_to_parent_relationship_type)

        if self.additional_axioms is not None and not isinstance(self.additional_axioms, str):
            self.additional_axioms = str(self.additional_axioms)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class GroupingTriad(Triad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["GroupingTriad"]
    class_class_curie: ClassVar[str] = "hoopla:GroupingTriad"
    class_name: ClassVar[str] = "GroupingTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.GroupingTriad

    parent: Optional[str] = None
    child1: Optional[str] = None
    child2: Optional[str] = None
    child1_to_parent_relationship_type: Optional[str] = None
    child2_to_parent_relationship_type: Optional[str] = None
    additional_axioms: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.parent is not None and not isinstance(self.parent, str):
            self.parent = str(self.parent)

        if self.child1 is not None and not isinstance(self.child1, str):
            self.child1 = str(self.child1)

        if self.child2 is not None and not isinstance(self.child2, str):
            self.child2 = str(self.child2)

        if self.child1_to_parent_relationship_type is not None and not isinstance(self.child1_to_parent_relationship_type, str):
            self.child1_to_parent_relationship_type = str(self.child1_to_parent_relationship_type)

        if self.child2_to_parent_relationship_type is not None and not isinstance(self.child2_to_parent_relationship_type, str):
            self.child2_to_parent_relationship_type = str(self.child2_to_parent_relationship_type)

        if self.additional_axioms is not None and not isinstance(self.additional_axioms, str):
            self.additional_axioms = str(self.additional_axioms)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class SubClassTriad(GroupingTriad):
    """
    A SubGraph in which the focus is a trio of nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["SubClassTriad"]
    class_class_curie: ClassVar[str] = "hoopla:SubClassTriad"
    class_name: ClassVar[str] = "SubClassTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.SubClassTriad

    child1_to_parent_relationship_type: Optional[str] = None
    child2_to_parent_relationship_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.child1_to_parent_relationship_type is not None and not isinstance(self.child1_to_parent_relationship_type, str):
            self.child1_to_parent_relationship_type = str(self.child1_to_parent_relationship_type)

        if self.child2_to_parent_relationship_type is not None and not isinstance(self.child2_to_parent_relationship_type, str):
            self.child2_to_parent_relationship_type = str(self.child2_to_parent_relationship_type)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class ImbalancedSubClassTriad(SubClassTriad):
    """
    A SubClassTriad in which the size of the two subclasses are imbalanced
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["ImbalancedSubClassTriad"]
    class_class_curie: ClassVar[str] = "hoopla:ImbalancedSubClassTriad"
    class_name: ClassVar[str] = "ImbalancedSubClassTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.ImbalancedSubClassTriad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class MixedAxisSubClassTriad(SubClassTriad):
    """
    A SubClassTriad in which the two subclasses are classified on different axes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["MixedAxisSubClassTriad"]
    class_class_curie: ClassVar[str] = "hoopla:MixedAxisSubClassTriad"
    class_name: ClassVar[str] = "MixedAxisSubClassTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.MixedAxisSubClassTriad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class DisjointSubClassTriad(SubClassTriad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["DisjointSubClassTriad"]
    class_class_curie: ClassVar[str] = "hoopla:DisjointSubClassTriad"
    class_name: ClassVar[str] = "DisjointSubClassTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.DisjointSubClassTriad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class JEPDSubClassTriad(SubClassTriad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["JEPDSubClassTriad"]
    class_class_curie: ClassVar[str] = "hoopla:JEPDSubClassTriad"
    class_name: ClassVar[str] = "JEPDSubClassTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.JEPDSubClassTriad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ComplementSubClassTriad(SubClassTriad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["ComplementSubClassTriad"]
    class_class_curie: ClassVar[str] = "hoopla:ComplementSubClassTriad"
    class_name: ClassVar[str] = "ComplementSubClassTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.ComplementSubClassTriad

    variant_of: Optional[Union[Union[dict, JEPDSubClassTriad], List[Union[dict, JEPDSubClassTriad]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.variant_of, list):
            self.variant_of = [self.variant_of] if self.variant_of is not None else []
        self.variant_of = [v if isinstance(v, JEPDSubClassTriad) else JEPDSubClassTriad(**as_dict(v)) for v in self.variant_of]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ImplicitJEPDSubClassTriad(SubClassTriad):
    """
    A SubClassOfTriad where there is implicit undeclared axioms that would make this a JEPDSubClassTriad
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["ImplicitJEPDSubClassTriad"]
    class_class_curie: ClassVar[str] = "hoopla:ImplicitJEPDSubClassTriad"
    class_name: ClassVar[str] = "ImplicitJEPDSubClassTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.ImplicitJEPDSubClassTriad

    should_be_replaced_by: Optional[Union[dict, JEPDSubClassTriad]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.should_be_replaced_by is not None and not isinstance(self.should_be_replaced_by, JEPDSubClassTriad):
            self.should_be_replaced_by = JEPDSubClassTriad(**as_dict(self.should_be_replaced_by))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class PartWholeTriad(GroupingTriad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["PartWholeTriad"]
    class_class_curie: ClassVar[str] = "hoopla:PartWholeTriad"
    class_name: ClassVar[str] = "PartWholeTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.PartWholeTriad

    child1_to_parent_relationship_type: Optional[str] = None
    child2_to_parent_relationship_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.child1_to_parent_relationship_type is not None and not isinstance(self.child1_to_parent_relationship_type, str):
            self.child1_to_parent_relationship_type = str(self.child1_to_parent_relationship_type)

        if self.child2_to_parent_relationship_type is not None and not isinstance(self.child2_to_parent_relationship_type, str):
            self.child2_to_parent_relationship_type = str(self.child2_to_parent_relationship_type)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class PrototypeTriad(GroupingTriad):
    """
    A GroupingTriad where the parent is a prototypical form
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["PrototypeTriad"]
    class_class_curie: ClassVar[str] = "hoopla:PrototypeTriad"
    class_name: ClassVar[str] = "PrototypeTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.PrototypeTriad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class PrototypeSubClassTriadAntipattern(GroupingTriad):
    """
    A variant of PrototypeTriad where the relationship type is subclass
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["PrototypeSubClassTriadAntipattern"]
    class_class_curie: ClassVar[str] = "hoopla:PrototypeSubClassTriadAntipattern"
    class_name: ClassVar[str] = "PrototypeSubClassTriadAntipattern"
    class_model_uri: ClassVar[URIRef] = HOOPLA.PrototypeSubClassTriadAntipattern

    child1_to_parent_relationship_type: Optional[str] = None
    child2_to_parent_relationship_type: Optional[str] = None
    should_be_replaced_by: Optional[Union[dict, PrototypeTriad]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.child1_to_parent_relationship_type is not None and not isinstance(self.child1_to_parent_relationship_type, str):
            self.child1_to_parent_relationship_type = str(self.child1_to_parent_relationship_type)

        if self.child2_to_parent_relationship_type is not None and not isinstance(self.child2_to_parent_relationship_type, str):
            self.child2_to_parent_relationship_type = str(self.child2_to_parent_relationship_type)

        if self.should_be_replaced_by is not None and not isinstance(self.should_be_replaced_by, PrototypeTriad):
            self.should_be_replaced_by = PrototypeTriad(**as_dict(self.should_be_replaced_by))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class EvolvedFromTriad(GroupingTriad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["EvolvedFromTriad"]
    class_class_curie: ClassVar[str] = "hoopla:EvolvedFromTriad"
    class_name: ClassVar[str] = "EvolvedFromTriad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.EvolvedFromTriad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class CrossProduct(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["CrossProduct"]
    class_class_curie: ClassVar[str] = "hoopla:CrossProduct"
    class_name: ClassVar[str] = "CrossProduct"
    class_model_uri: ClassVar[URIRef] = HOOPLA.CrossProduct

    axes_of_classification: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.axes_of_classification, list):
            self.axes_of_classification = [self.axes_of_classification] if self.axes_of_classification is not None else []
        self.axes_of_classification = [v if isinstance(v, str) else str(v) for v in self.axes_of_classification]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class DenselyPopulatedCrossProduct(CrossProduct):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["DenselyPopulatedCrossProduct"]
    class_class_curie: ClassVar[str] = "hoopla:DenselyPopulatedCrossProduct"
    class_name: ClassVar[str] = "DenselyPopulatedCrossProduct"
    class_model_uri: ClassVar[URIRef] = HOOPLA.DenselyPopulatedCrossProduct


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class SparselyPopulatedCrossProduct(CrossProduct):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["SparselyPopulatedCrossProduct"]
    class_class_curie: ClassVar[str] = "hoopla:SparselyPopulatedCrossProduct"
    class_name: ClassVar[str] = "SparselyPopulatedCrossProduct"
    class_model_uri: ClassVar[URIRef] = HOOPLA.SparselyPopulatedCrossProduct


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class RaggedCrossProduct(SparselyPopulatedCrossProduct):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["RaggedCrossProduct"]
    class_class_curie: ClassVar[str] = "hoopla:RaggedCrossProduct"
    class_name: ClassVar[str] = "RaggedCrossProduct"
    class_model_uri: ClassVar[URIRef] = HOOPLA.RaggedCrossProduct


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class NAryRelationship(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["NAryRelationship"]
    class_class_curie: ClassVar[str] = "hoopla:NAryRelationship"
    class_name: ClassVar[str] = "NAryRelationship"
    class_model_uri: ClassVar[URIRef] = HOOPLA.NAryRelationship


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class MeasurementPattern(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["MeasurementPattern"]
    class_class_curie: ClassVar[str] = "hoopla:MeasurementPattern"
    class_name: ClassVar[str] = "MeasurementPattern"
    class_model_uri: ClassVar[URIRef] = HOOPLA.MeasurementPattern


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class QuantityPattern(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["QuantityPattern"]
    class_class_curie: ClassVar[str] = "hoopla:QuantityPattern"
    class_name: ClassVar[str] = "QuantityPattern"
    class_model_uri: ClassVar[URIRef] = HOOPLA.QuantityPattern


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class ReflexiveInPropertyChain(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["ReflexiveInPropertyChain"]
    class_class_curie: ClassVar[str] = "hoopla:ReflexiveInPropertyChain"
    class_name: ClassVar[str] = "ReflexiveInPropertyChain"
    class_model_uri: ClassVar[URIRef] = HOOPLA.ReflexiveInPropertyChain


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class AllValuesFromTransitiveAntiPattern(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["AllValuesFromTransitiveAntiPattern"]
    class_class_curie: ClassVar[str] = "hoopla:AllValuesFromTransitiveAntiPattern"
    class_name: ClassVar[str] = "AllValuesFromTransitiveAntiPattern"
    class_model_uri: ClassVar[URIRef] = HOOPLA.AllValuesFromTransitiveAntiPattern


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class AllValuesFromCardinalityAntiPattern(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["AllValuesFromCardinalityAntiPattern"]
    class_class_curie: ClassVar[str] = "hoopla:AllValuesFromCardinalityAntiPattern"
    class_name: ClassVar[str] = "AllValuesFromCardinalityAntiPattern"
    class_model_uri: ClassVar[URIRef] = HOOPLA.AllValuesFromCardinalityAntiPattern


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class ContextualRange(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["ContextualRange"]
    class_class_curie: ClassVar[str] = "hoopla:ContextualRange"
    class_name: ClassVar[str] = "ContextualRange"
    class_model_uri: ClassVar[URIRef] = HOOPLA.ContextualRange

    domain_class: Optional[str] = None
    relationship_type: Optional[str] = None
    range_class: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.domain_class is not None and not isinstance(self.domain_class, str):
            self.domain_class = str(self.domain_class)

        if self.relationship_type is not None and not isinstance(self.relationship_type, str):
            self.relationship_type = str(self.relationship_type)

        if self.range_class is not None and not isinstance(self.range_class, str):
            self.range_class = str(self.range_class)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class ContextualRangeUsingUniversalAxiom(ContextualRange):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["ContextualRangeUsingUniversalAxiom"]
    class_class_curie: ClassVar[str] = "hoopla:ContextualRangeUsingUniversalAxiom"
    class_name: ClassVar[str] = "ContextualRangeUsingUniversalAxiom"
    class_model_uri: ClassVar[URIRef] = HOOPLA.ContextualRangeUsingUniversalAxiom


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class ContextualRangeUsingDisjointnessAxiom(ContextualRange):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["ContextualRangeUsingDisjointnessAxiom"]
    class_class_curie: ClassVar[str] = "hoopla:ContextualRangeUsingDisjointnessAxiom"
    class_name: ClassVar[str] = "ContextualRangeUsingDisjointnessAxiom"
    class_model_uri: ClassVar[URIRef] = HOOPLA.ContextualRangeUsingDisjointnessAxiom


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class SimpleGenusDifferentiaDefinition(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["SimpleGenusDifferentiaDefinition"]
    class_class_curie: ClassVar[str] = "hoopla:SimpleGenusDifferentiaDefinition"
    class_name: ClassVar[str] = "SimpleGenusDifferentiaDefinition"
    class_model_uri: ClassVar[URIRef] = HOOPLA.SimpleGenusDifferentiaDefinition


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class ContextualRefinementQuad(Quad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["ContextualRefinementQuad"]
    class_class_curie: ClassVar[str] = "hoopla:ContextualRefinementQuad"
    class_name: ClassVar[str] = "ContextualRefinementQuad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.ContextualRefinementQuad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class InstanceContextualRefinementQuad(ContextualRefinementQuad):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["InstanceContextualRefinementQuad"]
    class_class_curie: ClassVar[str] = "hoopla:InstanceContextualRefinementQuad"
    class_name: ClassVar[str] = "InstanceContextualRefinementQuad"
    class_model_uri: ClassVar[URIRef] = HOOPLA.InstanceContextualRefinementQuad


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class UpperOntologyConflation(SubGraph):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["UpperOntologyConflation"]
    class_class_curie: ClassVar[str] = "hoopla:UpperOntologyConflation"
    class_name: ClassVar[str] = "UpperOntologyConflation"
    class_model_uri: ClassVar[URIRef] = HOOPLA.UpperOntologyConflation


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass
class Delta(Pattern):
    """
    A pattern that involves two subgraphs, a before state and an after state. Elements in subgraph1 may be related to
    elements in subgraph2
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["Delta"]
    class_class_curie: ClassVar[str] = "hoopla:Delta"
    class_name: ClassVar[str] = "Delta"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Delta

    source_subgraph: Optional[Union[dict, SubGraph]] = None
    target_subgraph: Optional[Union[dict, SubGraph]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source_subgraph is not None and not isinstance(self.source_subgraph, SubGraph):
            self.source_subgraph = SubGraph(**as_dict(self.source_subgraph))

        if self.target_subgraph is not None and not isinstance(self.target_subgraph, SubGraph):
            self.target_subgraph = SubGraph(**as_dict(self.target_subgraph))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class Refactor(Delta):
    """
    A delta where the source is intentionally transformed to the target in order
    to achieve some objective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["Refactor"]
    class_class_curie: ClassVar[str] = "hoopla:Refactor"
    class_name: ClassVar[str] = "Refactor"
    class_model_uri: ClassVar[URIRef] = HOOPLA.Refactor


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class ELShunt(Refactor):
    """
    A refactor where non-EL axioms are migrated into a sub-module.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HOOPLA["ELShunt"]
    class_class_curie: ClassVar[str] = "hoopla:ELShunt"
    class_name: ClassVar[str] = "ELShunt"
    class_model_uri: ClassVar[URIRef] = HOOPLA.ELShunt


    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=HOOPLA.id, name="id", curie=HOOPLA.curie('id'),
                   model_uri=HOOPLA.id, domain=None, range=URIRef)

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=HOOPLA.label, domain=None, range=Optional[str])

slots.type = Slot(uri=HOOPLA.type, name="type", curie=HOOPLA.curie('type'),
                   model_uri=HOOPLA.type, domain=None, range=Optional[str])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=HOOPLA.title, domain=None, range=Optional[str])

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=HOOPLA.source, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=HOOPLA.description, domain=None, range=Optional[str])

slots.variant_of = Slot(uri=HOOPLA.variant_of, name="variant_of", curie=HOOPLA.curie('variant_of'),
                   model_uri=HOOPLA.variant_of, domain=None, range=Optional[Union[Union[dict, SubGraph], List[Union[dict, SubGraph]]]])

slots.should_be_replaced_by = Slot(uri=HOOPLA.should_be_replaced_by, name="should_be_replaced_by", curie=HOOPLA.curie('should_be_replaced_by'),
                   model_uri=HOOPLA.should_be_replaced_by, domain=None, range=Optional[Union[dict, SubGraph]])

slots.related_to = Slot(uri=HOOPLA.related_to, name="related_to", curie=HOOPLA.curie('related_to'),
                   model_uri=HOOPLA.related_to, domain=None, range=Optional[str])

slots.relationship_type = Slot(uri=HOOPLA.relationship_type, name="relationship_type", curie=HOOPLA.curie('relationship_type'),
                   model_uri=HOOPLA.relationship_type, domain=None, range=Optional[str])

slots.parent = Slot(uri=HOOPLA.parent, name="parent", curie=HOOPLA.curie('parent'),
                   model_uri=HOOPLA.parent, domain=None, range=Optional[str])

slots.child = Slot(uri=HOOPLA.child, name="child", curie=HOOPLA.curie('child'),
                   model_uri=HOOPLA.child, domain=None, range=Optional[str])

slots.child1 = Slot(uri=HOOPLA.child1, name="child1", curie=HOOPLA.curie('child1'),
                   model_uri=HOOPLA.child1, domain=None, range=Optional[str])

slots.child2 = Slot(uri=HOOPLA.child2, name="child2", curie=HOOPLA.curie('child2'),
                   model_uri=HOOPLA.child2, domain=None, range=Optional[str])

slots.axiom = Slot(uri=HOOPLA.axiom, name="axiom", curie=HOOPLA.curie('axiom'),
                   model_uri=HOOPLA.axiom, domain=None, range=Optional[str])

slots.relationship = Slot(uri=HOOPLA.relationship, name="relationship", curie=HOOPLA.curie('relationship'),
                   model_uri=HOOPLA.relationship, domain=None, range=Optional[str])

slots.child_to_parent_relationship = Slot(uri=HOOPLA.child_to_parent_relationship, name="child_to_parent_relationship", curie=HOOPLA.curie('child_to_parent_relationship'),
                   model_uri=HOOPLA.child_to_parent_relationship, domain=None, range=Optional[str])

slots.child_to_parent_relationship_type = Slot(uri=HOOPLA.child_to_parent_relationship_type, name="child_to_parent_relationship_type", curie=HOOPLA.curie('child_to_parent_relationship_type'),
                   model_uri=HOOPLA.child_to_parent_relationship_type, domain=None, range=Optional[str])

slots.child1_to_parent_relationship_type = Slot(uri=HOOPLA.child1_to_parent_relationship_type, name="child1_to_parent_relationship_type", curie=HOOPLA.curie('child1_to_parent_relationship_type'),
                   model_uri=HOOPLA.child1_to_parent_relationship_type, domain=None, range=Optional[str])

slots.child2_to_parent_relationship_type = Slot(uri=HOOPLA.child2_to_parent_relationship_type, name="child2_to_parent_relationship_type", curie=HOOPLA.curie('child2_to_parent_relationship_type'),
                   model_uri=HOOPLA.child2_to_parent_relationship_type, domain=None, range=Optional[str])

slots.additional_axioms = Slot(uri=HOOPLA.additional_axioms, name="additional_axioms", curie=HOOPLA.curie('additional_axioms'),
                   model_uri=HOOPLA.additional_axioms, domain=None, range=Optional[str])

slots.domain_class = Slot(uri=HOOPLA.domain_class, name="domain_class", curie=HOOPLA.curie('domain_class'),
                   model_uri=HOOPLA.domain_class, domain=None, range=Optional[str])

slots.range_class = Slot(uri=HOOPLA.range_class, name="range_class", curie=HOOPLA.curie('range_class'),
                   model_uri=HOOPLA.range_class, domain=None, range=Optional[str])

slots.members = Slot(uri=HOOPLA.members, name="members", curie=HOOPLA.curie('members'),
                   model_uri=HOOPLA.members, domain=None, range=Optional[Union[Union[str, EntityId], List[Union[str, EntityId]]]])

slots.size = Slot(uri=HOOPLA.size, name="size", curie=HOOPLA.curie('size'),
                   model_uri=HOOPLA.size, domain=None, range=Optional[int])

slots.patternInstantiationCollection__title = Slot(uri=HOOPLA.title, name="patternInstantiationCollection__title", curie=HOOPLA.curie('title'),
                   model_uri=HOOPLA.patternInstantiationCollection__title, domain=None, range=Optional[str])

slots.patternInstantiationCollection__description = Slot(uri=HOOPLA.description, name="patternInstantiationCollection__description", curie=HOOPLA.curie('description'),
                   model_uri=HOOPLA.patternInstantiationCollection__description, domain=None, range=Optional[str])

slots.patternInstantiationCollection__ontology = Slot(uri=HOOPLA.ontology, name="patternInstantiationCollection__ontology", curie=HOOPLA.curie('ontology'),
                   model_uri=HOOPLA.patternInstantiationCollection__ontology, domain=None, range=Optional[Union[dict, Ontology]])

slots.patternInstantiationCollection__patterns = Slot(uri=HOOPLA.patterns, name="patternInstantiationCollection__patterns", curie=HOOPLA.curie('patterns'),
                   model_uri=HOOPLA.patternInstantiationCollection__patterns, domain=None, range=Optional[Union[Union[dict, Pattern], List[Union[dict, Pattern]]]])

slots.ontology__classes = Slot(uri=HOOPLA.classes, name="ontology__classes", curie=HOOPLA.curie('classes'),
                   model_uri=HOOPLA.ontology__classes, domain=None, range=Optional[Union[Dict[Union[str, ClassId], Union[dict, Class]], List[Union[dict, Class]]]])

slots.ontology__source = Slot(uri=HOOPLA.source, name="ontology__source", curie=HOOPLA.curie('source'),
                   model_uri=HOOPLA.ontology__source, domain=None, range=Optional[str])

slots.crossProduct__axes_of_classification = Slot(uri=HOOPLA.axes_of_classification, name="crossProduct__axes_of_classification", curie=HOOPLA.curie('axes_of_classification'),
                   model_uri=HOOPLA.crossProduct__axes_of_classification, domain=None, range=Optional[Union[str, List[str]]])

slots.delta__source_subgraph = Slot(uri=HOOPLA.source_subgraph, name="delta__source_subgraph", curie=HOOPLA.curie('source_subgraph'),
                   model_uri=HOOPLA.delta__source_subgraph, domain=None, range=Optional[Union[dict, SubGraph]])

slots.delta__target_subgraph = Slot(uri=HOOPLA.target_subgraph, name="delta__target_subgraph", curie=HOOPLA.curie('target_subgraph'),
                   model_uri=HOOPLA.delta__target_subgraph, domain=None, range=Optional[Union[dict, SubGraph]])

slots.SubClassTriad_child1_to_parent_relationship_type = Slot(uri=HOOPLA.child1_to_parent_relationship_type, name="SubClassTriad_child1_to_parent_relationship_type", curie=HOOPLA.curie('child1_to_parent_relationship_type'),
                   model_uri=HOOPLA.SubClassTriad_child1_to_parent_relationship_type, domain=SubClassTriad, range=Optional[str])

slots.SubClassTriad_child2_to_parent_relationship_type = Slot(uri=HOOPLA.child2_to_parent_relationship_type, name="SubClassTriad_child2_to_parent_relationship_type", curie=HOOPLA.curie('child2_to_parent_relationship_type'),
                   model_uri=HOOPLA.SubClassTriad_child2_to_parent_relationship_type, domain=SubClassTriad, range=Optional[str])

slots.ComplementSubClassTriad_variant_of = Slot(uri=HOOPLA.variant_of, name="ComplementSubClassTriad_variant_of", curie=HOOPLA.curie('variant_of'),
                   model_uri=HOOPLA.ComplementSubClassTriad_variant_of, domain=ComplementSubClassTriad, range=Optional[Union[Union[dict, JEPDSubClassTriad], List[Union[dict, JEPDSubClassTriad]]]])

slots.ImplicitJEPDSubClassTriad_should_be_replaced_by = Slot(uri=HOOPLA.should_be_replaced_by, name="ImplicitJEPDSubClassTriad_should_be_replaced_by", curie=HOOPLA.curie('should_be_replaced_by'),
                   model_uri=HOOPLA.ImplicitJEPDSubClassTriad_should_be_replaced_by, domain=ImplicitJEPDSubClassTriad, range=Optional[Union[dict, JEPDSubClassTriad]])

slots.PartWholeTriad_child1_to_parent_relationship_type = Slot(uri=HOOPLA.child1_to_parent_relationship_type, name="PartWholeTriad_child1_to_parent_relationship_type", curie=HOOPLA.curie('child1_to_parent_relationship_type'),
                   model_uri=HOOPLA.PartWholeTriad_child1_to_parent_relationship_type, domain=PartWholeTriad, range=Optional[str])

slots.PartWholeTriad_child2_to_parent_relationship_type = Slot(uri=HOOPLA.child2_to_parent_relationship_type, name="PartWholeTriad_child2_to_parent_relationship_type", curie=HOOPLA.curie('child2_to_parent_relationship_type'),
                   model_uri=HOOPLA.PartWholeTriad_child2_to_parent_relationship_type, domain=PartWholeTriad, range=Optional[str])

slots.PrototypeSubClassTriadAntipattern_child1_to_parent_relationship_type = Slot(uri=HOOPLA.child1_to_parent_relationship_type, name="PrototypeSubClassTriadAntipattern_child1_to_parent_relationship_type", curie=HOOPLA.curie('child1_to_parent_relationship_type'),
                   model_uri=HOOPLA.PrototypeSubClassTriadAntipattern_child1_to_parent_relationship_type, domain=PrototypeSubClassTriadAntipattern, range=Optional[str])

slots.PrototypeSubClassTriadAntipattern_child2_to_parent_relationship_type = Slot(uri=HOOPLA.child2_to_parent_relationship_type, name="PrototypeSubClassTriadAntipattern_child2_to_parent_relationship_type", curie=HOOPLA.curie('child2_to_parent_relationship_type'),
                   model_uri=HOOPLA.PrototypeSubClassTriadAntipattern_child2_to_parent_relationship_type, domain=PrototypeSubClassTriadAntipattern, range=Optional[str])

slots.PrototypeSubClassTriadAntipattern_should_be_replaced_by = Slot(uri=HOOPLA.should_be_replaced_by, name="PrototypeSubClassTriadAntipattern_should_be_replaced_by", curie=HOOPLA.curie('should_be_replaced_by'),
                   model_uri=HOOPLA.PrototypeSubClassTriadAntipattern_should_be_replaced_by, domain=PrototypeSubClassTriadAntipattern, range=Optional[Union[dict, PrototypeTriad]])
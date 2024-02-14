

CREATE TABLE "AllValuesFromCardinalityAntiPattern" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "AllValuesFromTransitiveAntiPattern" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "ComplementSubClassTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	should_be_replaced_by TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	additional_axioms TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	variant_of TEXT, 
	PRIMARY KEY (type, title, description, source, should_be_replaced_by, parent, child1, child2, additional_axioms, child1_to_parent_relationship_type, child2_to_parent_relationship_type, variant_of)
);

CREATE TABLE "ContextualRangeUsingDisjointnessAxiom" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	domain_class TEXT, 
	relationship_type TEXT, 
	range_class TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, domain_class, relationship_type, range_class)
);

CREATE TABLE "ContextualRangeUsingUniversalAxiom" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	domain_class TEXT, 
	relationship_type TEXT, 
	range_class TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, domain_class, relationship_type, range_class)
);

CREATE TABLE "ContextualRefinementQuad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "Delta" (
	type TEXT, 
	source_subgraph TEXT, 
	target_subgraph TEXT, 
	PRIMARY KEY (type, source_subgraph, target_subgraph)
);

CREATE TABLE "DenselyPopulatedCrossProduct" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	axes_of_classification TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, axes_of_classification)
);

CREATE TABLE "DisjointSubClassTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	additional_axioms TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, parent, child1, child2, additional_axioms, child1_to_parent_relationship_type, child2_to_parent_relationship_type)
);

CREATE TABLE "ELShunt" (
	type TEXT, 
	source_subgraph TEXT, 
	target_subgraph TEXT, 
	PRIMARY KEY (type, source_subgraph, target_subgraph)
);

CREATE TABLE "EvolvedFromTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	additional_axioms TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, parent, child1, child2, child1_to_parent_relationship_type, child2_to_parent_relationship_type, additional_axioms)
);

CREATE TABLE "ImbalancedSubClassTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	additional_axioms TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, parent, child1, child2, additional_axioms, child1_to_parent_relationship_type, child2_to_parent_relationship_type)
);

CREATE TABLE "ImplicitJEPDSubClassTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	additional_axioms TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, parent, child1, child2, additional_axioms, child1_to_parent_relationship_type, child2_to_parent_relationship_type, should_be_replaced_by)
);

CREATE TABLE "InstanceContextualRefinementQuad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "JEPDSubClassTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	additional_axioms TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, parent, child1, child2, additional_axioms, child1_to_parent_relationship_type, child2_to_parent_relationship_type)
);

CREATE TABLE "MeasurementPattern" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "MixedAxisSubClassTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	additional_axioms TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, parent, child1, child2, additional_axioms, child1_to_parent_relationship_type, child2_to_parent_relationship_type)
);

CREATE TABLE "NAryRelationship" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "Ontology" (
	id TEXT NOT NULL, 
	label TEXT, 
	source TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PartWholeTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	additional_axioms TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, parent, child1, child2, additional_axioms, child1_to_parent_relationship_type, child2_to_parent_relationship_type)
);

CREATE TABLE "PrototypeSubClassTriadAntipattern" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	additional_axioms TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, parent, child1, child2, additional_axioms, child1_to_parent_relationship_type, child2_to_parent_relationship_type, should_be_replaced_by)
);

CREATE TABLE "PrototypeTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	additional_axioms TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, parent, child1, child2, child1_to_parent_relationship_type, child2_to_parent_relationship_type, additional_axioms)
);

CREATE TABLE "QuantityPattern" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "RaggedCrossProduct" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	axes_of_classification TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, axes_of_classification)
);

CREATE TABLE "Refactor" (
	type TEXT, 
	source_subgraph TEXT, 
	target_subgraph TEXT, 
	PRIMARY KEY (type, source_subgraph, target_subgraph)
);

CREATE TABLE "ReflexiveInPropertyChain" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "SimpleGenusDifferentiaDefinition" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "SparselyPopulatedCrossProduct" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	axes_of_classification TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, axes_of_classification)
);

CREATE TABLE "SubClassTriad" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	parent TEXT, 
	child1 TEXT, 
	child2 TEXT, 
	additional_axioms TEXT, 
	child1_to_parent_relationship_type TEXT, 
	child2_to_parent_relationship_type TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by, parent, child1, child2, additional_axioms, child1_to_parent_relationship_type, child2_to_parent_relationship_type)
);

CREATE TABLE "UpperOntologyConflation" (
	type TEXT, 
	title TEXT, 
	description TEXT, 
	source TEXT, 
	variant_of TEXT, 
	should_be_replaced_by TEXT, 
	PRIMARY KEY (type, title, description, source, variant_of, should_be_replaced_by)
);

CREATE TABLE "Class" (
	id TEXT NOT NULL, 
	label TEXT, 
	size INTEGER, 
	"Ontology_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ontology_id") REFERENCES "Ontology" (id)
);

CREATE TABLE "PatternInstantiationCollection" (
	title TEXT, 
	description TEXT, 
	ontology TEXT, 
	patterns TEXT, 
	PRIMARY KEY (title, description, ontology, patterns), 
	FOREIGN KEY(ontology) REFERENCES "Ontology" (id)
);

CREATE TABLE "Class_members" (
	backref_id TEXT, 
	members TEXT, 
	PRIMARY KEY (backref_id, members), 
	FOREIGN KEY(backref_id) REFERENCES "Class" (id)
);

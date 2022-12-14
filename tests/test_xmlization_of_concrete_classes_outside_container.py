# This code has been automatically generated by:
# dev_scripts/generate_test_for_xmlization_of_concrete_classes_outside_container.py
# Do NOT edit or append.


"""Test de/serialization from XML of concrete classes outside a container."""


# pylint: disable=missing-docstring


import unittest
import xml.etree.ElementTree as ET

import aas_core3_rc02.xmlization as aas_xmlization
import aas_core3_rc02.verification as aas_verification

import tests.common
import tests.common_jsonization
import tests.common_xmlization


class Test_Extension(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Extension` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_extension()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.extension_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_AdministrativeInformation(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.AdministrativeInformation` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_administrative_information()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.administrative_information_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Qualifier(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Qualifier` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_qualifier()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.qualifier_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_AssetAdministrationShell(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.AssetAdministrationShell` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_asset_administration_shell()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.asset_administration_shell_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_AssetInformation(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.AssetInformation` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_asset_information()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.asset_information_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Resource(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Resource` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_resource()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.resource_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_SpecificAssetId(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.SpecificAssetId` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_specific_asset_id()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.specific_asset_id_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Submodel(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Submodel` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_submodel()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.submodel_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_RelationshipElement(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.RelationshipElement` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_relationship_element()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.relationship_element_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_SubmodelElementList(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.SubmodelElementList` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_submodel_element_list()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.submodel_element_list_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_SubmodelElementCollection(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.SubmodelElementCollection` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_submodel_element_collection()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.submodel_element_collection_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Property(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Property` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_property()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.property_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_MultiLanguageProperty(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.MultiLanguageProperty` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_multi_language_property()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.multi_language_property_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Range(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Range` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_range()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.range_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_ReferenceElement(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.ReferenceElement` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_reference_element()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.reference_element_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Blob(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Blob` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_blob()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.blob_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_File(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.File` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_file()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.file_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_AnnotatedRelationshipElement(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.AnnotatedRelationshipElement` outside a container.
    """

    def test_ok(self) -> None:
        instance = (
            tests.common_jsonization.load_complete_annotated_relationship_element()
        )
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.annotated_relationship_element_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Entity(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Entity` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_entity()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.entity_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_BasicEventElement(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.BasicEventElement` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_basic_event_element()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.basic_event_element_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Operation(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Operation` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_operation()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.operation_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_OperationVariable(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.OperationVariable` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_operation_variable()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.operation_variable_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Capability(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Capability` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_capability()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.capability_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_ConceptDescription(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.ConceptDescription` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_concept_description()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.concept_description_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Reference(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Reference` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_reference()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.reference_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_Key(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.Key` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_key()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.key_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_LangString(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.LangString` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_lang_string()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.lang_string_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_EmbeddedDataSpecification(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.EmbeddedDataSpecification` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_embedded_data_specification()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.embedded_data_specification_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_ValueReferencePair(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.ValueReferencePair` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_value_reference_pair()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.value_reference_pair_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_ValueList(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.ValueList` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_value_list()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.value_list_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_DataSpecificationIEC61360(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.DataSpecificationIEC61360` outside a container.
    """

    def test_ok(self) -> None:
        instance = tests.common_jsonization.load_complete_data_specification_iec_61360()
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.data_specification_iec_61360_from_str(text)

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


class Test_DataSpecificationPhysicalUnit(unittest.TestCase):
    """
    Test XML de/serialization of the concrete class
    :py:class:`aas_core3_rc02.types.DataSpecificationPhysicalUnit` outside a container.
    """

    def test_ok(self) -> None:
        instance = (
            tests.common_jsonization.load_complete_data_specification_physical_unit()
        )
        text = aas_xmlization.to_str(instance)

        another_instance = aas_xmlization.data_specification_physical_unit_from_str(
            text
        )

        errors = list(aas_verification.verify(another_instance))
        self.assertListEqual([], errors)

        et_instance = ET.fromstring(text)
        tests.common_xmlization.remove_redundant_whitespace(et_instance)

        et_another_instance = ET.fromstring(aas_xmlization.to_str(another_instance))
        tests.common_xmlization.remove_redundant_whitespace(et_another_instance)

        tests.common_xmlization.assert_elements_equal(et_instance, et_another_instance)


if __name__ == "__main__":
    unittest.main()


# This code has been automatically generated by:
# dev_scripts/generate_test_for_xmlization_of_concrete_classes_outside_container.py
# Do NOT edit or append.

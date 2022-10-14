# This code has been automatically generated by:
# dev_scripts/generate_test_for_descend_once.py
# Do NOT edit or append.


"""Test :py:method:`aas_core3_rc02.types.Class.descend_once`."""


# pylint: disable=missing-docstring


import unittest

import tests.common
import tests.common_jsonization


class Test_Extension(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_extension()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Extension"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_AdministrativeInformation(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_administrative_information()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "AdministrativeInformation"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Qualifier(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_qualifier()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Qualifier"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_AssetAdministrationShell(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_asset_administration_shell()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "AssetAdministrationShell"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_AssetInformation(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_asset_information()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "AssetInformation"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Resource(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_resource()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Resource"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_SpecificAssetId(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_specific_asset_id()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "SpecificAssetId"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Submodel(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_submodel()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Submodel"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_RelationshipElement(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_relationship_element()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "RelationshipElement"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_SubmodelElementList(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_submodel_element_list()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "SubmodelElementList"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_SubmodelElementCollection(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_submodel_element_collection()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "SubmodelElementCollection"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Property(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_property()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Property"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_MultiLanguageProperty(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_multi_language_property()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "MultiLanguageProperty"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Range(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_range()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Range"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_ReferenceElement(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_reference_element()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "ReferenceElement"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Blob(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_blob()
        expected_path = (
            tests.common.TEST_DATA_DIR / "descend_once" / "Blob" / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_File(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_file()
        expected_path = (
            tests.common.TEST_DATA_DIR / "descend_once" / "File" / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_AnnotatedRelationshipElement(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = (
            tests.common_jsonization.load_complete_annotated_relationship_element()
        )
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "AnnotatedRelationshipElement"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Entity(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_entity()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Entity"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_EventPayload(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_event_payload()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "EventPayload"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_BasicEventElement(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_basic_event_element()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "BasicEventElement"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Operation(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_operation()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Operation"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_OperationVariable(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_operation_variable()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "OperationVariable"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Capability(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_capability()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Capability"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_ConceptDescription(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_concept_description()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "ConceptDescription"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Reference(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_reference()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Reference"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Key(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_key()
        expected_path = (
            tests.common.TEST_DATA_DIR / "descend_once" / "Key" / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_LangString(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_lang_string()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "LangString"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_Environment(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_environment()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "Environment"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_EmbeddedDataSpecification(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_embedded_data_specification()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "EmbeddedDataSpecification"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_ValueReferencePair(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_value_reference_pair()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "ValueReferencePair"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_ValueList(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_value_list()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "ValueList"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_DataSpecificationIEC61360(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = tests.common_jsonization.load_complete_data_specification_iec_61360()
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "DataSpecificationIEC61360"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


class Test_DataSpecificationPhysicalUnit(unittest.TestCase):
    def test_descend_once_against_recorded_trace_log(self) -> None:
        instance = (
            tests.common_jsonization.load_complete_data_specification_physical_unit()
        )
        expected_path = (
            tests.common.TEST_DATA_DIR
            / "descend_once"
            / "DataSpecificationPhysicalUnit"
            / "complete.json.trace"
        )

        log = [tests.common.trace(something) for something in instance.descend_once()]
        got_text = tests.common.trace_log_as_text_file_content(log)
        tests.common.record_or_check(expected_path, got_text)


if __name__ == "__main__":
    unittest.main()


# This code has been automatically generated by:
# dev_scripts/generate_test_for_descend_once.py
# Do NOT edit or append.

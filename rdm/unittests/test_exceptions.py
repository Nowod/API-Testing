import pytest

from rdm.exceptions import ExporterError, MethodError, ValidatorError


class TestException:
    """
    测试Demo
    """

    def test_ValidatorError(self):
        with pytest.raises(ValidatorError) as error:
            raise ValidatorError("test")
        assert error.type is ValidatorError
        assert error.value.args[0] == "test"

    def test_MethodError(self):
        with pytest.raises(MethodError) as error:
            raise MethodError("test")
        assert error.type is MethodError
        assert error.value.args[0] == "test"

    def test_ExporterError(self):
        with pytest.raises(ExporterError) as error:
            raise ExporterError("test")
        assert error.type is ExporterError
        assert error.value.args[0] == "test"

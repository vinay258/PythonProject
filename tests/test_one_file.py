import pytest
import pytest_html


from conftest import common_fix
class TestMyProgram:
    @pytest.mark.vinay
    def test_m1(self,common_fix):
        print("i am test method 1")
    @pytest.mark.vandana
    def test_m2(self,common_fix):
        print("i am test method 2")
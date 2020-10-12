import pytest
import clientapi

@pytest.mark.slow
def test_fixture_pass():
    assert 5 == 5
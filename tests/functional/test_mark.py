import pytest
import clientapi as api


@pytest.mark.slow
def test_fixture_pass():
    k = api.get('https://reqres.in/api/users?page=2')
    assert k.status == 200
    print(k._body)

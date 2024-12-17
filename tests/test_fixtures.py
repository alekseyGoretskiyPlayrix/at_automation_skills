import pytest


@pytest.fixture(scope="module")
def fixture_initialization():
    return [1, 2, 3]


class TestFixtures:

    @pytest.fixture(autouse=True)
    def fixture_hello(self):
        print("Hello world!")

    def test_fixtures_sum(self, fixture_initialization):
        assert sum(fixture_initialization) == 6

    def test_fixtures_min(self, fixture_initialization):
        assert min(fixture_initialization) == 1

    def test_fixtures_first_value(self, fixture_initialization):
        assert fixture_initialization[0] == 1

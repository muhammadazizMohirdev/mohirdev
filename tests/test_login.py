from tests.initial_test import InitialTest


class TestLogin(InitialTest):
    def test_login(self, init):
        assert self.login_f.check_login("", "")
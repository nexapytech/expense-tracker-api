from django.test import TestCase, Client
from django.urls import reverse


class ExpenseTrackerApiSmokeTests(TestCase):
    """
    Minimal smoke tests for Expense Tracker API.
    Ensures endpoints exist and respond.
    """

    def setUp(self):
        self.client = Client()

    # ---------- Public / Landing ----------
    def test_homepage(self):
        response = self.client.get(reverse("expense_tracker_api"))
        self.assertIn(response.status_code, [200, 302])

    def test_download_page(self):
        response = self.client.get(reverse("downoad_nexpenz"))
        self.assertIn(response.status_code, [200, 302])

    def test_download_apk(self):
        response = self.client.get(reverse("download_apk"))
        self.assertIn(response.status_code, [200, 302, 404])

    # ---------- API Endpoints ----------
    def test_api_signup(self):
        response = self.client.post(reverse("expense_api_generator"))
        self.assertIn(response.status_code, [200, 201, 302, 400, 403])

    def test_api_settings(self):
        response = self.client.get(reverse("api-settings"))
        self.assertIn(response.status_code, [200, 302, 401, 403])

    def test_get_currency(self):
        response = self.client.get(reverse("api-currency"))
        self.assertIn(response.status_code, [200, 302, 401, 403])

    def test_add_transaction(self):
        response = self.client.post(reverse("api-add_transaction"))
        self.assertIn(response.status_code, [200, 201, 302, 400, 401, 403])

    def test_get_transaction(self):
        response = self.client.get(reverse("api-get_transaction"))
        self.assertIn(response.status_code, [200, 302, 401, 403])

    def test_get_balance(self):
        response = self.client.get(reverse("api-get_balance"))
        self.assertIn(response.status_code, [200, 302, 401, 403])

    def test_filter_transaction_by_date(self):
        response = self.client.get(reverse("api-filter_by_date_transaction"))
        self.assertIn(response.status_code, [200, 302, 400, 401, 403])

    def test_api_login_securely(self):
        response = self.client.post(reverse("api-login-security"))
        self.assertIn(response.status_code, [200, 302, 400, 401, 403])

    def test_api_version(self):
        response = self.client.get(reverse("api-get_app_version"))
        self.assertIn(response.status_code, [200, 302])

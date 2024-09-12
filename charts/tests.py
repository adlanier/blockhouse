from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class ChartAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_candlestick_data(self):
        """Test the candlestick data API"""
        url = reverse('candlestick-data')  # Use the name you set for this route
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.json())

    def test_line_chart_data(self):
        """Test the line chart data API"""
        url = reverse('line-chart-data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('labels', response.json())
        self.assertIn('data', response.json())

    def test_bar_chart_data(self):
        """Test the bar chart data API"""
        url = reverse('bar-chart-data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('labels', response.json())
        self.assertIn('data', response.json())

    def test_pie_chart_data(self):
        """Test the pie chart data API"""
        url = reverse('pie-chart-data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('labels', response.json())
        self.assertIn('data', response.json())
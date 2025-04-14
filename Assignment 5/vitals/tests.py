from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from rest_framework import status
import json
from vitals.tasks import long_running_task
from celery.result import AsyncResult

class TaskViewsTestCase(TestCase):
    def setUp(self):
        self.start_task_url = reverse('start_task')
        self.check_status_url = reverse('check_task_status', kwargs={'task_id': 'fd6a9796-c5be-458b-8389-0af6696e974a'})

    @patch('vitals.views.long_running_task.apply_async')
    def test_start_task(self, mock_apply_async):

        mock_apply_async.return_value.id = 'fd6a9796-c5be-458b-8389-0af6696e974a'

        response = self.client.post(self.start_task_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        self.assertIn('task_id', response_data)
        self.assertEqual(response_data['task_id'], 'fd6a9796-c5be-458b-8389-0af6696e974a')

    @patch('vitals.views.celery.AsyncResult')
    def test_check_task_status(self, mock_async_result):

        mock_task = mock_async_result.return_value
        mock_task.status = 'SUCCESS'
        mock_task.result = 'Task completed successfully'

        response = self.client.get(self.check_status_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        self.assertIn('status', response_data)
        self.assertEqual(response_data['status'], 'SUCCESS')
        self.assertEqual(response_data['result'], 'Task completed successfully')

    @patch('vitals.views.celery.AsyncResult')
    def test_check_task_status_task_not_found(self, mock_async_result):
    
        mock_async_result.return_value.state = 'FAILURE'

        invalid_task_url = reverse('check_task_status', kwargs={'task_id': 'invalid-task-id'})
        response = self.client.get(invalid_task_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CeleryTaskTest(TestCase):

    def test_long_running_task(self):
        result = long_running_task.delay()
        self.assertEqual(result.get(timeout=10), 'Expected result')



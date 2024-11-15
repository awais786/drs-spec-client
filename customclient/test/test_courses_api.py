# coding: utf-8

"""
    Authoring API

    Experimental API to edit xblocks and course content.       Danger: Do not use on running courses!        - How to gain access: Please email the owners of this openedx service.       - How to use: This API uses oauth2 authentication with the     access token endpoint: `http://localhost:18000/oauth2/access_token`.     Please see separately provided documentation.       - How to test: You must be logged in as course author for whatever course you want to test with.     You can use the [Swagger UI](https://localhost:18000/authoring-api/ui/) to \"Try out\" the API with your test course. To do this, you must select the \"Local\" server.       - Public vs. Local servers: The \"Public\" server is where you can reach the API externally. The \"Local\" server is     for development with a local edx-platform version,  and for use via the [Swagger UI](https://localhost:18010/authoring-api/ui/).       - Swaggerfile: [Download link](https://localhost:18000/authoring-api/schema/)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from customclient.openapi_client.api.courses_api import CoursesApi


class TestCoursesApi(unittest.TestCase):
    """CoursesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CoursesApi()

    def tearDown(self) -> None:
        pass

    def test_courses_courseware_navigation_sidebar_toggles_retrieve(self) -> None:
        """Test case for courses_courseware_navigation_sidebar_toggles_retrieve

        """
        pass

    def test_courses_courseware_search_enabled_retrieve(self) -> None:
        """Test case for courses_courseware_search_enabled_retrieve

        """
        pass

    def test_courses_instructor_api_change_due_date_create(self) -> None:
        """Test case for courses_instructor_api_change_due_date_create

        """
        pass

    def test_courses_instructor_api_get_anon_ids_create(self) -> None:
        """Test case for courses_instructor_api_get_anon_ids_create

        """
        pass

    def test_courses_instructor_api_get_grading_config_create(self) -> None:
        """Test case for courses_instructor_api_get_grading_config_create

        """
        pass

    def test_courses_instructor_api_get_student_enrollment_status_create(self) -> None:
        """Test case for courses_instructor_api_get_student_enrollment_status_create

        """
        pass

    def test_courses_instructor_api_get_student_progress_url_create(self) -> None:
        """Test case for courses_instructor_api_get_student_progress_url_create

        """
        pass

    def test_courses_instructor_api_get_students_who_may_enroll_create(self) -> None:
        """Test case for courses_instructor_api_get_students_who_may_enroll_create

        """
        pass

    def test_courses_instructor_api_get_students_who_may_enroll_retrieve(self) -> None:
        """Test case for courses_instructor_api_get_students_who_may_enroll_retrieve

        """
        pass

    def test_courses_instructor_api_list_course_role_members_create(self) -> None:
        """Test case for courses_instructor_api_list_course_role_members_create

        """
        pass

    def test_courses_instructor_api_list_email_content_create(self) -> None:
        """Test case for courses_instructor_api_list_email_content_create

        """
        pass

    def test_courses_instructor_api_list_entrance_exam_instructor_tasks_create(self) -> None:
        """Test case for courses_instructor_api_list_entrance_exam_instructor_tasks_create

        """
        pass

    def test_courses_instructor_api_list_instructor_tasks_create(self) -> None:
        """Test case for courses_instructor_api_list_instructor_tasks_create

        """
        pass

    def test_courses_instructor_api_list_report_downloads_create(self) -> None:
        """Test case for courses_instructor_api_list_report_downloads_create

        """
        pass

    def test_courses_instructor_api_mark_student_can_skip_entrance_exam_create(self) -> None:
        """Test case for courses_instructor_api_mark_student_can_skip_entrance_exam_create

        """
        pass

    def test_courses_instructor_api_modify_access_create(self) -> None:
        """Test case for courses_instructor_api_modify_access_create

        """
        pass

    def test_courses_instructor_api_register_and_enroll_students_create(self) -> None:
        """Test case for courses_instructor_api_register_and_enroll_students_create

        """
        pass

    def test_courses_instructor_api_reset_due_date_create(self) -> None:
        """Test case for courses_instructor_api_reset_due_date_create

        """
        pass

    def test_courses_instructor_api_reset_student_attempts_create(self) -> None:
        """Test case for courses_instructor_api_reset_student_attempts_create

        """
        pass

    def test_courses_instructor_api_send_email_create(self) -> None:
        """Test case for courses_instructor_api_send_email_create

        """
        pass

    def test_courses_instructor_api_show_student_extensions_create(self) -> None:
        """Test case for courses_instructor_api_show_student_extensions_create

        """
        pass

    def test_courses_instructor_api_users_info2_create(self) -> None:
        """Test case for courses_instructor_api_users_info2_create

        """
        pass

    def test_courses_instructor_api_users_info_create(self) -> None:
        """Test case for courses_instructor_api_users_info_create

        """
        pass

    def test_courses_teams_retrieve(self) -> None:
        """Test case for courses_teams_retrieve

        """
        pass

    def test_courses_xblock_view_retrieve(self) -> None:
        """Test case for courses_xblock_view_retrieve

        """
        pass

    def test_courses_yt_video_metadata_retrieve(self) -> None:
        """Test case for courses_yt_video_metadata_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()

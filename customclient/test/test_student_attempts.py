# coding: utf-8

"""
    Authoring API

    Experimental API to edit xblocks and course content.       Danger: Do not use on running courses!        - How to gain access: Please email the owners of this openedx service.       - How to use: This API uses oauth2 authentication with the     access token endpoint: `http://localhost:18000/oauth2/access_token`.     Please see separately provided documentation.       - How to test: You must be logged in as course author for whatever course you want to test with.     You can use the [Swagger UI](https://localhost:18000/authoring-api/ui/) to \"Try out\" the API with your test course. To do this, you must select the \"Local\" server.       - Public vs. Local servers: The \"Public\" server is where you can reach the API externally. The \"Local\" server is     for development with a local edx-platform version,  and for use via the [Swagger UI](https://localhost:18010/authoring-api/ui/).       - Swaggerfile: [Download link](https://localhost:18000/authoring-api/schema/)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from customclient.openapi_client.models.student_attempts import StudentAttempts

class TestStudentAttempts(unittest.TestCase):
    """StudentAttempts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudentAttempts:
        """Test StudentAttempts
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudentAttempts`
        """
        model = StudentAttempts()
        if include_optional:
            return StudentAttempts(
                problem_to_reset = '',
                unique_student_identifier = '',
                all_students = '',
                delete_module = ''
            )
        else:
            return StudentAttempts(
                problem_to_reset = '',
        )
        """

    def testStudentAttempts(self):
        """Test StudentAttempts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

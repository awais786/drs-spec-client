
from openedxclient.openapi_client import Access, StudentProgressUrl
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJvcGVuZWR4IiwiZXhwIjoxNzMxOTMzODUzLCJncmFudF90eXBlIjoiY2xpZW50LWNyZWRlbnRpYWxzIiwiaWF0IjoxNzMxOTMwMjUzLCJpc3MiOiJodHRwOi8vbG9jYWwuZWRseS5pby9vYXV0aDIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJhZG1pbiIsInNjb3BlcyI6WyJyZWFkIiwid3JpdGUiLCJlbWFpbCIsInByb2ZpbGUiXSwidmVyc2lvbiI6IjEuMi4wIiwic3ViIjoiYzIwOGU4Yzk3MjFlODJkMmZhOTY4ZmZmYmY0OWRlOGEiLCJmaWx0ZXJzIjpbXSwiaXNfcmVzdHJpY3RlZCI6ZmFsc2UsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwibmFtZSI6ImFkbWluIiwiZmFtaWx5X25hbWUiOiJtaW4iLCJnaXZlbl9uYW1lIjoiYWQiLCJhZG1pbmlzdHJhdG9yIjp0cnVlLCJzdXBlcnVzZXIiOnRydWV9.HhqydSTFz1nFHjejESVe8rfIR3yB4-DdDbmLLeAvTB0"

from openedxclient import openapi_client

configuration = openapi_client.Configuration(
    api_key_prefix="JWT", host="http://local.edly.io:8000", access_token=access_token
)

api_client = openapi_client.ApiClient(
    configuration=configuration,  header_name="Authorization", header_value=f"JWT {access_token}"
)
api_instance = openapi_client.CoursesApi(api_client)
course_id = 'course-v1:edx+cs202+2101'

student_progress_url = StudentProgressUrl(
    unique_student_identifier="admin",
    course_id=course_id,
    progress_url="http://local.edly.io:8000/aaa"
)
student_progress_url_data = {
    "unique_student_identifier": "admin",
    "progress_url": "http://local.edly.io:8000/aaa"
}
print(api_instance.courses_instructor_api_get_student_progress_url_create(
    course_id=course_id,
    student_progress_url=student_progress_url_data
))

modify_access_data = {
    "unique_student_identifier": "admin",
    "action": "allow",
    "rolename": "instructor"
}

# Convert the dictionary into a Pydantic model instance
access_instance = Access(**modify_access_data)

response = api_instance.courses_instructor_api_modify_access_create(
    course_id="course-v1:edx+cs202+2101",  # Replace with actual course_id
    access=access_instance  # Pass the dictionary with correct name
)

print(response.to_json())


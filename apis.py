from rest_framework import serializers

class UserInfoSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100, write_only=True)
    email = serializers.EmailField(read_only=True)  #  field is only for output response
    data = serializers.CharField(read_only=True)   #  field is only for output response


class UserInfoView2(APIView):
    serializer_class = UserInfoSerializer

    def post(self, request, *args, **kwargs):
        # Pass request data to the serializer
        serializer = UserInfoSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            # If data is valid, you can access it via `serializer.validated_data`
            validated_data = serializer.validated_data
            validated_data['data'] = 'This is only for return data field'

            # Example response with validated data
            return Response(validated_data, status=status.HTTP_201_CREATED)

        # If data is invalid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

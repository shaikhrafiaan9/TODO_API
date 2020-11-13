from rest_framework import serializers
from basictodo.models import Todo



class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datacompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id','title','memo','created','datacompleted','important']


class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        read_only_fields = ['title','memo','created','datacompleted','important']
        fields = ['id']

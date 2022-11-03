from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, \
    SerializerMethodField, HyperlinkedIdentityField, StringRelatedField, \
    SlugRelatedField

from appsoftdesk.models import Projects, Contributors, Issues, Comments
from django.contrib.auth import get_user_model


class ContributorsSerializer(ModelSerializer):
    """ Serializer for contributors """
    project = StringRelatedField()
    author_user = SlugRelatedField(queryset=get_user_model().objects.all(),
                                   slug_field="username")

    class Meta:
        model = Contributors
        fields = [
            "id",
            "author_user",
            "project",
            "permission",
            "role",
        ]


class ProjectsListSerializer(ModelSerializer):
    """ Serializer for Projects List View """
    author_user = StringRelatedField()
    edit_url = HyperlinkedIdentityField(view_name="projects-detail")

    class Meta:
        model = Projects
        fields = [
            "id",
            "edit_url",
            "title",
            "description",
            "type",
            "author_user",
        ]


class ProjectsDetailSerializer(ModelSerializer):
    """ Serializer for Projects Detail View"""
    author_user = StringRelatedField()
    contributors = SerializerMethodField()
    issues = SerializerMethodField()

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author_user",
            "contributors",
            "issues",
        ]

    def get_contributors(self, instance):
        queryset = instance.contributors.all()
        serializer = ContributorsSerializer(queryset, many=True)
        return serializer.data

    def get_issues(self, instance):
        queryset = instance.issues.all()
        serializer = IssuesSerializer(queryset, many=True)
        return serializer.data


class CommentsSerializer(ModelSerializer):
    """ Serializer for issues' comments"""

    author_user = StringRelatedField(read_only=True)
    issue = StringRelatedField(read_only=True)

    class Meta:
        model = Comments
        fields = [
            "id",
            "description",
            "author_user",
            "issue",
            "created_time",
        ]


class IssuesSerializer(ModelSerializer):
    """ Serializer for issues' project"""
    author_user = StringRelatedField(read_only=True)
    project = StringRelatedField(read_only=True)
    assignee_user = SlugRelatedField(queryset=get_user_model().objects.all(),
                                   slug_field="username")
    comments = SerializerMethodField()

    class Meta:
        model = Issues
        fields = [
            "id",
            "project",
            "title",
            "description",
            "tag",
            "status",
            "priority",
            "assignee_user",
            "author_user",
            "created_time",
            "comments",
        ]

    def get_comments(self, instance):
        queryset = instance.comments.all()
        serializer = CommentsSerializer(queryset, many=True)
        return serializer.data



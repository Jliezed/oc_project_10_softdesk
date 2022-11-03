from rest_framework.viewsets import ModelViewSet

from django.shortcuts import get_object_or_404
from django.db.models import Q

from appsoftdesk.models import Projects, Contributors, Issues, Comments
from appsoftdesk.serializers import ProjectsListSerializer, ProjectsDetailSerializer, \
    ContributorsSerializer, IssuesSerializer, CommentsSerializer
from appsoftdesk.permissions import ProjectContributorReadOnly, ContributorReadOnly, \
    AuthorFullAccess


class ProjectsViewset(ModelViewSet):
    """ View to manage projects APIs """
    serializer_class = ProjectsListSerializer
    detail_serializer_class = ProjectsDetailSerializer

    def get_serializer_class(self):
        """ Return the serializer class for request """
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        """ Retrieve projects for authenticated user """

        "Define Projects where current user is author or contributor"
        current_user = self.request.user
        current_user_contribution = Contributors.objects.filter(Q(
            author_user=self.request.user))
        contribution_projects_id = current_user_contribution.values(
            "project").distinct()

        "Retrieve only projects where current user is author or contributor"
        queryset = Projects.objects.filter(
            Q(author_user=current_user) | Q(
                id__in=contribution_projects_id)).distinct().order_by('pk')
        return queryset

    def perform_create(self, serializer):
        """ Add a project for authenticated user """
        serializer.save(author_user=self.request.user)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [AuthorFullAccess()]
        return [ContributorReadOnly()]


class ContributorsViewset(ModelViewSet):
    """ View to manage Contributors of a project """
    serializer_class = ContributorsSerializer

    def get_queryset(self):
        return Contributors.objects.filter(project_id=self.kwargs["project_pk"])

    def perform_create(self, serializer):
        project = get_object_or_404(Projects, pk=self.kwargs["project_pk"])
        serializer.save(project=project)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [AuthorFullAccess()]
        return [ProjectContributorReadOnly()]


class IssuesViewset(ModelViewSet):
    """ View to manage Issues of a project """
    serializer_class = IssuesSerializer

    def get_queryset(self):
        return Issues.objects.filter(project=self.kwargs["project_pk"])

    def perform_create(self, serializer):
        project = get_object_or_404(Projects, pk=self.kwargs["project_pk"])
        serializer.save(author_user=self.request.user, project=project)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [AuthorFullAccess()]
        return [ProjectContributorReadOnly()]


class CommentsViewset(ModelViewSet):
    """ View to manage Comments of a issue """
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comments.objects.filter(issue=self.kwargs["issue_pk"])

    def perform_create(self, serializer):
        issue = get_object_or_404(Issues, pk=self.kwargs["issue_pk"])
        serializer.save(author_user=self.request.user, issue=issue)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [AuthorFullAccess()]
        return [ProjectContributorReadOnly()]
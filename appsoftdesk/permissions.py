from rest_framework.permissions import BasePermission, SAFE_METHODS

from django.db.models import Q

from appsoftdesk.models import Projects, Contributors


class AuthorFullAccess(BasePermission):
    """ Give full permission for author of the projects, issues or comments """

    def has_object_permission(self, request, view, obj):
        """ Give full permissions if user is author of the projects, issues or
        comments """
        if obj.author_user == request.user:
            return True
        return False


class ContributorReadOnly(BasePermission):
    """ Give Read only permission for Contributor of the project """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return False


class ProjectContributorReadOnly(BasePermission):
    """ Give Read only permission for Contributor of the project """

    def has_permission(self, request, view):
        current_project_id = int(view.kwargs["project_pk"])

        current_user_contribution = Contributors.objects.filter(Q(
            author_user=request.user))
        current_user_contribution_projects_id = current_user_contribution.values_list(
            "project", flat=True).distinct()

        current_user_author_contribution_projects_id = Projects.objects.filter(Q(
            author_user=request.user) | Q(id__in=current_user_contribution_projects_id)).values_list(
            "id", flat=True).distinct()

        if request.user.is_authenticated and current_project_id in current_user_author_contribution_projects_id:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return False


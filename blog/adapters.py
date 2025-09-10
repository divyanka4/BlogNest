from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialApp

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_app(self, request, provider=None, client_id=None, **kwargs):
        # First try default behavior
        try:
            return super().get_app(request, provider=provider, client_id=client_id, **kwargs)
        except SocialApp.MultipleObjectsReturned:
            # Fallback: deterministically pick the first app for this provider filtered by current site (if available)
            qs = SocialApp.objects.filter(provider=provider)
        # Filter by request.site when middleware resolved it
        current_site = getattr(request, "site", None)
        if current_site:
            qs = qs.filter(sites=current_site)
        return qs.order_by("id").first()
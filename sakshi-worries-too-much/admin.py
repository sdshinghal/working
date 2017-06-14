from django.contrib import admin
from campaign_analysis.models import Campaign, FileUpload


class CampaignAdmin(admin.ModelAdmin):
    """
    Admin for the Campaigns model
    """
    list_display = ('name', 'source', 'medium', 'content', 'unique_visits', 'visits', 'bounce_count',
                    'actions_count', 'date', 'platform_ad_id', 'platform_campaign_id',
                    'platform_url', 'platform_campaign_status', 'platform_ad_status', 'ad_introduction_text',
                    'ad_headline_text', 'ad_line_text', 'total_spent', 'cost_per_mile', 'cost_per_click',
                    'cost_per_pixel', 'cost_per_action', 'click_through_rate', 'impressions', 'clicks', 'likes',
                    'shares', 'follows', 'comments', 'created_at', 'updated_at')
    search_fields = ['name', 'date', 'source', 'medium']

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(FileUpload)

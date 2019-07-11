from django.apps import AppConfig
from django.conf import settings


class SlackConfig(AppConfig):
    name = 'response.slack'

    def ready(self):
        import response.slack.settings
        import response.slack.signals
        import response.slack.action_handlers
        import response.slack.event_handlers
        import response.slack.incident_commands
        import response.slack.keyword_handlers
        import response.slack.incident_notifications
        import response.slack.dialog_handlers
        import response.slack.workflows
        if settings.PAGERDUTY_ENABLED:
            import response.slack.workflows.pagerduty

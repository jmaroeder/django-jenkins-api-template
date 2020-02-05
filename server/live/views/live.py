import contextlib
import logging

from django.db import connection
from rest_framework import status, views
from rest_framework.request import Request
from rest_framework.response import Response

LOG = logging.getLogger(__name__)


class LiveView(views.APIView):
    """Checks if the server is live."""

    checks = [
        "status",
        "db",
    ]
    fail_on = checks

    def get(self, request: Request) -> Response:
        """Returns a JSON object describing the current status of the server."""
        status_obj = {check: self._status_str(check) for check in self.checks}
        if any(status_obj[check] == "down" for check in self.fail_on):
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            status_code = status.HTTP_200_OK
        return Response(status_obj, status=status_code)

    def _status_str(self, check: str) -> str:
        """Call the appropriate method for the check and return `up` or `down`."""
        with contextlib.suppress(Exception):
            if getattr(self, f"_is_{check}_up")():
                return "up"
        return "down"

    def _is_status_up(self) -> bool:
        """Always return true for general server status."""
        return True

    def _is_db_up(self) -> bool:
        """Checks the default db connection."""
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1;")
                row = cursor.fetchone()
                if tuple(row) != (1,):
                    LOG.error("DB is up, but `SELECT 1` returned %s", row)
                    return False
        except Exception:
            LOG.exception("DB is not up")
            return False
        return True

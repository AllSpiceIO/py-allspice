from allspice_client.paths.user_emails.get import ApiForget
from allspice_client.paths.user_emails.post import ApiForpost
from allspice_client.paths.user_emails.delete import ApiFordelete


class UserEmails(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

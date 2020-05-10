# _929. Unique Email Addresses


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        result = []
        for email in emails:
            local_name = email.split('@')[0]
            domain_name = email.split('@')[1]

            if '+' in local_name:
                local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')

            result.append(local_name+'@'+domain_name)

        return len(set(result))

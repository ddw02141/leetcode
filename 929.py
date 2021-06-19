# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        localNameDomainName = [email.split("@") for email in emails]
        for local, domain in localNameDomainName:
            local = local.split("+")[0]
            local = local.replace(".", "")
            print(local + domain)
            uniqueEmails.add(local + "@" + domain)
        return len(uniqueEmails)

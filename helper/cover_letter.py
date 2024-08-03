import re

class CoverLetter:
    def __init__(self) -> None:
        self.company_name = ""
        self.job_title = ""
        self.referer = ""
        self.applicant_name = ""
        self.template = ""
    
    def fill_template(self) -> str:
        txt = self.template
        rep = {"[Company Name]": self.company_name, 
               "[Job Title]": self.job_title,
               "[Referral Source]": self.referer,
               "[Applicant Name]": self.applicant_name}

        # replacement
        rep = dict((re.escape(k), v) for k, v in rep.items()) 
        pattern = re.compile("|".join(rep.keys()))
        txt = pattern.sub(lambda m: rep[re.escape(m.group(0))], txt)
        return txt
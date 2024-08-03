class CoverLetter:
    def __init__(self) -> None:
        self.company_name = ""
        self.job_title = ""
        self.referer = ""
        self.applicant_name = ""
        self.template = ""

    def fill_template(self) -> str:
        txt = self.template.replace("[Company Name]", self.company_name)
        txt = txt.replace("[Job Title]", self.job_title)
        txt = txt.replace("[Referral Source]", self.referer)
        txt = txt.replace("[Applicant Name]", self.applicant_name)
        return txt
import re
import json

template_instructions = """ Below are the default field tags for cover letter templete:
            Company Name: [Company Name], 
            Job Title: [Job Title],
            Referral/Where did you find this job: [Referral Source],
            Applicant/Your Name: [Applicant Name]
            
If you want to customize tag names, select 'Yes' for the above question.

If copying from the cover letter of a previous application, you can also use the functionality to replace words.
    For example, you can fill in:
        Company Name: Google,
        Company Name Tag: Meta"""

class CoverLetter:
    def __init__(self) -> None:
        self.company_name = ""
        self.job_title = ""
        self.referer = ""
        self.applicant_name = ""
        self.template = ""
        self.update_settings()
    
    def update_settings(self) -> None:
        self.settings = {
            'company_name': self.company_name,
            'job_title': self.job_title,
            'referer': self.referer,
            'applicant_name': self.applicant_name,
            'template': self.template
        }

    def fill_template(self, company = "[Company Name]",
                      job = "[Job Title]",
                      referer = "[Referral Source",
                      applicant = "[Applicant Name]",) -> str:
        txt = self.template
        rep = {company: self.company_name,
               job: self.job_title,
               referer: self.referer,
               applicant: self.applicant_name}
        # replacement
        rep = dict((re.escape(k), v) for k, v in rep.items()) 
        pattern = re.compile("|".join(rep.keys()))
        txt = pattern.sub(lambda m: rep[re.escape(m.group(0))], txt)
        return txt
    
    def export_to_json(self) -> str:
        self.update_settings()
        return json.dumps(self.settings)
    
    def import_from_file(self, bytes_data : bytes) -> json:
        self.settings = json.loads(bytes_data.decode('utf-8'))
        return self.settings
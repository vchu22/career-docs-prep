import re
import json

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
    
    def export_to_json(self) -> str:
        self.update_settings()
        return json.dumps(self.settings)
    
    def import_from_file(self, bytes_data : bytes) -> json:
        self.settings = json.loads(bytes_data.decode('utf-8'))
        return self.settings
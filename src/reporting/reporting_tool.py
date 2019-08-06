from string import Template
from os import path


def reporting_tool(substitutions, project_root, template_path, report_path):
    template = open(path.join(project_root,
                              '../' + template_path))
    generated_report = open(path.join(project_root,
                                      '../' + report_path), 'w')
    loaded_template = Template(template.read())
    overwritten_template = loaded_template.safe_substitute(substitutions)
    generated_report.write(overwritten_template)
    template.close()
    generated_report.close()

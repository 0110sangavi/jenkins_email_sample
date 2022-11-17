import os
import sys
import getopt
default_values = '''<h1>Build ${build.result}</h1>
<table>
  <tr><th>Build URL:</th><td><a href="${build.url}">${build.url}</a></td></tr>
  <tr><th>Project:</th><td>${project.name}</td></tr>
  <tr><th>Date of build:</th><td>${it.timestampString}</td></tr>
  <tr><th>Build duration:</th><td>${build.durationString}</td></tr>
</table>'''
style_script = '''
body
{
  margin: 0px;
  padding: 15px;
}
body, td, th
{
  font-family: "Lucida Grande", "Lucida Sans Unicode", Helvetica, Arial, Tahoma, sans-serif;
  font-size: 10pt;
}
'''
def main(argv):
    with open(os.getenv('html_template_location'), 'r') as html_file:
        html_content = html_file.read()
    html_file_content = html_content.format(style_script=style_script,result=os.getenv('result'), jenkins_values=default_values)
    with open(os.getenv('html_result_location'), 'w') as f:
        f.write(html_file_content)
if __name__ == '__main__':
    main(sys.argv[1:])
from url.license import *
import os

# Arguements to Simplify Testing
git_token = os.getenv('GITHUB_TOKEN')
sample_approved_license_list = ['GNU Lesser General Public License v2.1', 'Apache License 2.0', 'BSD 2-Clause "Simplified" License', 'BSD 3-Clause "New" or "Revised" License', 'Boost Software License 1.0', 'MIT License', 'The Unlicense']
headers = {"Authorization": f"{git_token}"}
all_github_licenses = ['GNU Affero General Public License v3.0', 'Apache License 2.0', 'BSD 2-Clause "Simplified" License', 'BSD 3-Clause "New" or "Revised" License', 'Boost Software License 1.0', 'Creative Commons Zero v1.0 Universal', 'Eclipse Public License 2.0', 'GNU General Public License v2.0', 'GNU General Public License v3.0', 'GNU Lesser General Public License v2.1', 'MIT License', 'Mozilla Public License 2.0', 'The Unlicense']
license_api_url = f"https://api.github.com/licenses"

# This tests getLicensesList and approved_licenses
def test_getLicensesList():
    list_of_licenses = getLicensesList(git_token)
    assert(list_of_licenses == sample_approved_license_list)

def test_license_score():
    license_name = "MIT License" 
    score = license_score(license_name, sample_approved_license_list)
    assert(score == 1)
    assert(score != 0)

    license_name = 'BSD 2-Clause "Simplified" License'
    score = license_score(license_name, sample_approved_license_list)
    assert(score == 1)
    assert(score != 0)

    license_name = 'GNU Affero General Public License v3.0'
    score = license_score(license_name, sample_approved_license_list)
    assert(score == 0)
    assert(score != 1)

def test_githubLicense():
    # Sample Approved License List Added to avoid overhead
    name_license = githubLicense("cloudinary", "cloudinary_npm", git_token, sample_approved_license_list)
    assert(name_license == "MIT License" or name_license == "mit license")
    
    name_license = githubLicense("PSOPT", "psopt", git_token, sample_approved_license_list)
    assert(name_license == "GNU Lesser General Public License v2.1" or name_license == "gnu lesser general public license v2.1")
    assert(name_license != "MIT License" and name_license != "mit license")
    
    name_license = githubLicense("nullivex", "nodist", git_token, sample_approved_license_list)
    assert(name_license == "MIT License" or name_license == "mit license")
    
    name_license = githubLicense("apache", "airflow", git_token, sample_approved_license_list)
    assert(name_license == "Apache License 2.0" or name_license == "apache license 2.0")
    assert(name_license != "MIT License" and name_license != "mit license")

def test_searchReadme():
    api_Url = f"https://api.github.com/repos/jonschlinkert/even/license"
    name = searchReadme(api_Url, headers, git_token)
    assert(name == "mit license")
    
    api_Url = f"https://api.github.com/repos/apache/airflow/license"
    name = searchReadme(api_Url, headers, git_token)
    assert(name == "apache license 2.0")
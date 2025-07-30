# AWS Lambda VPC Configuration Updater

![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange?logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![Shell](https://img.shields.io/badge/Shell-Bash-green)

This repository contains scripts to bulk update VPC configurations for multiple AWS Lambda functions.

## Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## Features

- 🚀 Bulk update VPC configurations for multiple Lambda functions
- 🔄 Two implementations available: Shell (AWS CLI) and Python (Boto3)
- ✔️ Comprehensive error handling and progress reporting
- 🔒 Secure credential handling in Python version
- 📝 Detailed logging for audit purposes

## Prerequisites

### For Both Scripts:
- AWS account with appropriate permissions
- Lambda functions existing in your AWS account

### For Shell Script:
- AWS CLI v2 installed and configured
- Bash shell environment
- `jq` (optional, for enhanced JSON output)

### For Python Script:
- Python 3.6+
- Boto3 library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lambda-vpc-updater.git
cd lambda-vpc-updater
pip install -r requirements.txt

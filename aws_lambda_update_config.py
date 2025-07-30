import boto3
from botocore.exceptions import ClientError, NoCredentialsError
import getpass
import time

def configure_aws():
    """Configure AWS credentials programmatically"""
    print("AWS Configuration")
    print("----------------")
    aws_access_key = input("Enter AWS Access Key ID: ").strip()
    aws_secret_key = getpass.getpass("Enter AWS Secret Access Key: ").strip()
    region = input("Enter AWS Region (e.g., us-east-1): ").strip()
    
    return {
        'aws_access_key_id': aws_access_key,
        'aws_secret_access_key': aws_secret_key,
        'region_name': region
    }

def update_lambda_vpc_config(aws_config):
    """Update Lambda functions with VPC configuration"""
    try:
        # Initialize the Boto3 Lambda client with configured credentials
        client = boto3.client('lambda', **aws_config)

        # VPC Configuration
        vpc_config = {
            'SubnetIds': ['subnet-0a725a387d73af253'],
            'SecurityGroupIds': ['sg-00c77a022eac6bd2a']
        }

        # List of Lambda functions to update
        lambda_functions = [
            'bt_test1',
            'bt_test2',
            'bt_test3'
            
        ]

        print("\nStarting Lambda VPC Configuration Updates...")
        print("----------------------------------------")

        for function_name in lambda_functions:
            try:
                print(f"\nUpdating: {function_name}")
                
                response = client.update_function_configuration(
                    FunctionName=function_name,
                    VpcConfig=vpc_config
                )
                
                print(f"✅ Success - Updated VPC config for {function_name}")
                print(f"   VPC ID: {response['VpcConfig']['VpcId']}")
                print(f"   Subnets: {', '.join(response['VpcConfig']['SubnetIds'])}")
                print(f"   Security Groups: {', '.join(response['VpcConfig']['SecurityGroupIds'])}")
                
            except ClientError as e:
                print(f"❌ Error updating {function_name}: {e.response['Error']['Message']}")
            except Exception as e:
                print(f"❌ Unexpected error with {function_name}: {str(e)}")
            
            time.sleep(1)  # Brief pause between API calls

        print("\nUpdate process completed.")

    except NoCredentialsError:
        print("❌ AWS credentials not found or invalid")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("AWS Lambda VPC Configuration Updater")
    print("===================================\n")
    
    aws_config = configure_aws()
    update_lambda_vpc_config(aws_config)
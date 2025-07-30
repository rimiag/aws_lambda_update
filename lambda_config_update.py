import boto3
import time

def update_lambda_vpc_config():
    # Initialize the Boto3 Lambda client
    client = boto3.client('lambda')

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

    # Update each Lambda function
    for function_name in lambda_functions:
        try:
            print(f"Updating VPC configuration for: {function_name}")
            
            response = client.update_function_configuration(
                FunctionName=function_name,
                VpcConfig=vpc_config
            )
            
            print(f"Successfully updated {function_name}")
            print(f"New VPC Config: {response['VpcConfig']}")
            
        except Exception as e:
            print(f"Error updating {function_name}: {str(e)}")
        
        print("-" * 50)
        time.sleep(1)  # Small delay between API calls

if __name__ == "__main__":
    update_lambda_vpc_config()
    print("All Lambda functions processed.")
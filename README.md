# Upload MySQL Dump to Amazon S3 in Multi-parts

If you wish to upload dump file(s) to Amazon S3, please follow the steps below and ensure all pre-requisites are met.

## Prerequisites

1. **AWS Account:** Ensure you have an active AWS account with the necessary permissions to access Amazon S3. 🌐

2. **Install AWS CLI:** Install the AWS Command Line Interface (CLI) on your local machine. You can download it from the [official AWS CLI website](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions).

3. **Configure AWS CLI:** Run `aws configure` and provide your AWS Access Key ID, Secret Access Key, default region, and output format. This information is used by the AWS CLI to authenticate and interact with your AWS resources. 🔐
   ```bash
   aws configure
   AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
   AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   Default region name [None]: us-west-2
   Default output format [None]: json

4. **Create an S3 Bucket:** Create an S3 bucket in your AWS account to store the MySQL dump file. You can create a bucket using the AWS Management Console or the AWS CLI. 🗃️

5. **Install boto3 package:** Make sure you have [PIP](https://pip.pypa.io/en/stable/installation/) package before running this step:
   ```bash
   pip3 install boto3

### Step 6: Create an S3 Policy

To allow only write (PUT) operations to a specific bucket, you can use AWS Identity and Access Management (IAM) policies. Follow these steps:

#### 6.1 Create an S3 Policy

Attach the following example policy JSON to your IAM user or role:

```json

{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Action": "s3:PutObject",
         "Resource": "arn:aws:s3:::your-bucket-name/*"
      }
   ]
}
```

Make sure to replace `your-bucket-name` with the actual name of your S3 bucket in the policy.

#### Explanation of the Policy

- **Effect: Allow:** Specifies that the actions in the statement are allowed.
- **Action: s3:PutObject:** Grants permission for the PutObject action, which is used for uploading objects to S3.
- **Resource: arn:aws:s3:::your-bucket-name/*:** Specifies the ARN (Amazon Resource Name) of the bucket and allows the action on any object within that bucket.


This policy allows users or roles associated with it to perform only the PutObject action on the specified S3 bucket.

## Security Considerations
- Always follow security best practices.
- Monitor AWS S3 costs and data transfer.

## Contact Information
For more insights and tutorials, connect with us:

LinkedIn: [Tech-Turbine](www.linkedin.com/in/tech-turbine)

YouTube: [TechTurbine](https://www.youtube.com/channel/UCE0NpPl-N2ttWn5KkazoGcg)

Email: [TechTurbine](grow@techturbine.co.in)

Please feel free to reach out for any assistance or queries.

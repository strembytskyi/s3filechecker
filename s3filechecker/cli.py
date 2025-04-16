import boto3
import click
from datetime import timezone

@click.command()
@click.option('--bucket', required=True, help='S3 bucket name')
@click.option('--prefix', default='', show_default=True,
              help='Optional prefix to filter files (e.g., "logs/"). Leave empty to search entire bucket.')
@click.option('--endpoint', required=True, help='Custom S3 endpoint URL')
@click.option('--access-key', envvar='AWS_ACCESS_KEY_ID', help='Access Key (or use AWS_ACCESS_KEY_ID env var)')
@click.option('--secret-key', envvar='AWS_SECRET_ACCESS_KEY', help='Secret Key (or use AWS_SECRET_ACCESS_KEY env var)')
def cli(bucket, prefix, endpoint, access_key, secret_key):
    """
    CLI tool to find the latest file (by LastModified) in a given S3 bucket and prefix.
    Supports custom S3-compatible endpoints and credentials.
    """
    if not access_key or not secret_key:
        raise click.UsageError("You must provide --access-key and --secret-key or set AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY.")

    # Create S3 client using custom credentials and endpoint
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='us-east-1'  # can be any value for most custom endpoints
    )

    # Use paginator to handle large lists of objects
    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket, Prefix=prefix)

    latest_obj = None
    for page in page_iterator:
        for obj in page.get('Contents', []):
            if latest_obj is None or obj['LastModified'] > latest_obj['LastModified']:
                latest_obj = obj

    if latest_obj:
        last_modified = latest_obj['LastModified'].astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        print(f"Latest file: {latest_obj['Key']}")
        print(f"Last modified: {last_modified}")
    else:
        print("No files found.")

if __name__ == '__main__':
    cli()
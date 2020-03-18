# Data Acquisition Service

Service responsible for data Acquisition

# Build and deploy 

Create the domain if it dosent exist. This is a oneoff command which need to run

```sh
# To create
serverless create_domain --profile <profile name>
# To remove
serverless delete_domain --profile <profile name>
```

Deploy it on `AWS`

```sh  
# To deploy
serverless deploy --stage staging --profile <profile name>
# To delete
serverless remove --stage staging --profile <profile name>
```

> **Note**: Authenticated with Cognito where needed

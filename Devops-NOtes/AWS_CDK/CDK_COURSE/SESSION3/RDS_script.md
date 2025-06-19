from aws_cdk import (
    CfnOutput,
    RemovalPolicy,
    Stack,
    aws_ec2 as ec2,
    aws_rds as rds
)
from constructs import Construct

class MySampleAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_vpc = ec2.Vpc(self, 'MyVpc',
                         nat_gateways=0)
        
        web_server = ec2.Instance(self, 'WebServer',
                                  machine_image=ec2.MachineImage.latest_amazon_linux2(),
                                  instance_type=ec2.InstanceType.of(instance_class=ec2.InstanceClass.T2,
                                                                    instance_size=ec2.InstanceSize.MICRO),
                                  vpc=my_vpc,
                                  vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                                  user_data_causes_replacement=True)
        
        # Attaching an Elastic IP to keep the DNS name on updates
        ec2.CfnEIP(self, 'ElasticIP',
                   instance_id=web_server.instance_id)
        
        # Installing packages at instance launch
        web_server.add_user_data('yum update -y',
                                 'amazon-linux-extras install nginx1',
                                 'service nginx start')
        
        CfnOutput(self, 'WebServerDnsName',
                  value=web_server.instance_public_dns_name)
        
        # Allowing connections to the web server
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), 'Allow HTTP access from the Internet')
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(22), 'Allow SSH access from the Internet')


        # DB instance configuration
        db_instance = rds.DatabaseInstance(self, 'DbInstance',
                                           engine=rds.DatabaseInstanceEngine.MARIADB,
                                           vpc=my_vpc,
                                           vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
                                           instance_type=ec2.InstanceType.of(instance_class=ec2.InstanceClass.T2,
                                                                             instance_size=ec2.InstanceSize.MICRO),
                                           removal_policy=RemovalPolicy.DESTROY)
        
        # Allowing connections to the DB instance
        db_instance.connections.allow_default_port_from(web_server, 'Allow MySQL access from the web server')

        # Installing MySQL client on the web server
        web_server.add_user_data('yum install mysql -y')

        CfnOutput(self, 'DbEndpoint',
                  value=db_instance.db_instance_endpoint_address)



Here’s a clear and concise **summary** of the lecture you shared, ideal for notes or review purposes:

---

### **Lecture Summary: Connecting a Web Server to an RDS DB Using AWS CDK (Python)**

#### **1. RDS DB Instance Setup**

* Imported `aws_cdk.aws_rds` as `rds`.
* Created a MariaDB instance using the L2 construct `rds.DatabaseInstance`.
* Set the DB engine using `DatabaseInstanceEngine.MARIADB`.
* Placed the DB instance in **private isolated subnets** within the VPC.
* Reused `vpc` and `vpc_subnets` from the web server config.
* Chose `t2.micro` as the instance type.
* Set `removal_policy=RemovalPolicy.DESTROY` to auto-delete on stack deletion (not for production).

#### **2. Connecting Web Server to DB**

* Allowed MySQL traffic **from the web server to the DB** using:

  * `db_instance.connections.allow_default_port_from(web_server, "Allow MySQL access from the web server")`.
  * (Alternate approach shown: `web_server.connections.allow_to_default_port(db_instance)` — optional).
* These CDK methods configure **security group rules** automatically, without explicitly referencing them.

#### **3. User Data Update**

* Installed **MySQL client** on the web server via `add_user_data("yum install mysql -y")`.
* Because `user_data_causes_replacement=True`, any user data change triggers **instance replacement**.

#### **4. SSH Access Setup**

* Enabled **SSH (port 22)** from the Internet to the web server for testing purposes.

#### **5. Outputs**

* Added a CloudFormation output for the **DB endpoint** using:

  ```python
  CfnOutput(self, "DbEndpoint", value=db_instance.db_instance_endpoint_address)
  ```

#### **6. Post-Deployment Testing**

* Connected to the EC2 instance using **EC2 Instance Connect** (no key pair needed).
* Used **Secrets Manager** to retrieve DB credentials.
* Connected to RDS using MySQL client:

  ```bash
  mysql -h <db-endpoint> -u admin -p
  ```
* Ran SQL command: `SHOW DATABASES;` to confirm connection.

---

### **Key Concepts Demonstrated**

* Use of **L2 constructs** for RDS and VPC resources.
* CDK’s **`connections` interface** simplifies security group management.
* Leveraging **Secrets Manager** for DB credential management (secure by default).
* Importance of **isolated subnets** for databases in production.
* Demonstrated **user data updates**, **EC2 replacements**, and **stack outputs**.

---

Let me know if you want this turned into a diagram, PDF, or formatted as a study guide!
                  

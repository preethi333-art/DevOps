STEPS:

First create ALB and Target Group for load balancer
Create ECS Fargate service
->Create Task definition
->Create Service

Note imp point:
1. Make sure to create IP target type in target group in load balncer.
2.Create security group which allow port 80 for load balancer
3.Create security group which allow container port 5000 for ecs fargate.
4.In side ecs security group pass source as application loab balancer security
group.
graph TD;
    A[User Make Request] --> B(Load Balancer);
    B --> C(Listener);
    B --> D(Target);
    B --> E(Target);
    F[AWS ECR Image] --> G(ECS Cluster);
    G --> H(Container Instance);
    G --> I(Service);
    I --> J(Task);
    I --> K(Task);

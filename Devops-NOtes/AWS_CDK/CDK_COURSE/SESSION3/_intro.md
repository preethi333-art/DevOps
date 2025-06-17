Welcome to this section! In the previous lectures,

you learned to define different levels of constructs

in your CDK applications.

You also saw how CDK simplifies

adding related resources to your constructs

with instance methods. In this section,

we will cover more CDK features

that simplify running commands while launching EC2 instances,

allowing network connections, and uploading assets to S3.

In our examples, we will use the sample app

we created at the beginning of the last section,

which creates a VPC with a single L2-level construct.

And we will start with allowing network connections

to a connectable AWS resource in CDK.

We will add an EC2 instance running the Nginx web server

to our stack and allow connections to its HTTP port.

We will do this by specifying the port number ourselves.

But as you know, some AWS resources like databases

also have default ports, for which

CDK makes this even more straightforward.

So next, you will learn to allow connections

to the default port of a construct

using the helper methods provided by CDK.

As an example, we will add an RDS DB instance to our stack

and allow MySQL connections to it

from our web server instance using its default port.

After this, we will discuss a general CDK feature.

You will learn to remove a construct from your stack

and update your CDK app.

We will remove the RDS instance we added in the last lecture

as an example. And finally, we will discuss assets in CDK

and make an example of S3 assets

by uploading a custom web page

and downloading it to our web server while launching it.

These CDK features simplify and enhance the capabilities of

CloudFormation stacks more.

Hence, learning them will increase your productivity

while configuring these types of resources when you need them.

So, stay with me, and let’s begin with allowing

connections to a resource in CDK in the next lecture.




provider "aws" {
  region                  = "ap-south-1"

  profile                 = "Akshay"
}


resource "tls_private_key" "My_Private_Key" {
algorithm = "RSA"
}
resource "local_file" "Private_key" {
content = tls_private_key.My_Private_Key.private_key_pem
filename ="awskey.pem"
file_permission = 0400
}
resource "aws_key_pair" "deployer" {
key_name = "awskey"
public_key = tls_private_key.My_Private_Key.public_key_openssh
}


resource "aws_security_group" "Security" {
  name        = "allow_ssh"
  description = "Allow TLS inbound traffic"
  vpc_id      = "vpc-1ef3ee76"

  ingress {
    description = "ssh"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

ingress {
    description = "http"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }



  tags = {
    Name = "allow_ssh_http"
  }
}
/*
output myosip{

value="${aws_security_group.Security.name}"
}

*/
resource "aws_instance" "Developer_OS" {
  ami           =  "ami-052c08d70def0ac62"
 instance_type = "t2.micro"
   availability_zone ="ap-south-1a"
  security_groups=["${aws_security_group.Security.name}"]

  tags = {
    Name = "OS_Developer"
  }
}

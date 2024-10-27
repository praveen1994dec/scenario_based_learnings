data "aws_ami" "ubuntu" {
    most_recent = true
 
    filter {
        name   = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
    }
 
    filter {
        name   = "virtualization-type"
        values = ["hvm"]
    }
 
    filter {
        name   = "architecture"
        values = ["x86_64"]
    }
 
    owners = ["099720109477"] # Canonical official
}

module "ec2_app" {
   source = "../../modules/ec2"
 
   infra_env = "${var.infra_role}-staging-tf"
   infra_role = "app"
   instance_size = var.instance_size
   instance_ami = data.aws_ami.ubuntu.id
   # instance_root_device_size = 12 # Optional
}

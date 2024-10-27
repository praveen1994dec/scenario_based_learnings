resource "aws_instance" "web" {
  ami           = var.instance_ami
  instance_type = var.instance_size
 
  root_block_device {
    volume_size = var.instance_root_device_size
    volume_type = "gp3"
  }
 
  tags = {
    Name        = "server-${var.infra_env}-web"
    Role        = var.infra_role
    Project     = "tf-awesome"
    Environment = var.infra_env
    ManagedBy   = "terraform"
  }
}
 
resource "aws_eip" "web_addr" {
  # We're not doing this directly
  # instance = aws_instance.web.id
  vpc      = true
 
  tags = {
    Name        = "server-${var.infra_env}-web-address"
    Role        = var.infra_role
    Project     = "tf-awesome"
    Environment = var.infra_env
    ManagedBy   = "terraform"
  }
}
 
resource "aws_eip_association" "eip_assoc" {
  instance_id   = aws_instance.web.id
  allocation_id = aws_eip.web_addr.id
}

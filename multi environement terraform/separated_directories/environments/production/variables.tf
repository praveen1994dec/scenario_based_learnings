variable default_region {
    type = string
    description = "the region this infrastructure is in"
    default = "ap-southeast-1"
}
 
variable instance_size {
    type = string
    description = "ec2 web server size"
    default = "t2.micro"
}

variable "infra_role" {
    type = string
    description = "role for instance"
    default = "server"
}
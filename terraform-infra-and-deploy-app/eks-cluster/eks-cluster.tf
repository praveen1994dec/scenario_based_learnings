module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "17.24.0"
  cluster_name    = local.cluster_name
  cluster_version = "1.24"
  subnets         = module.vpc.private_subnets
  vpc_id          = module.vpc.vpc_id

  workers_group_defaults = {
    root_volume_type = "gp2"
    associate_public_ip_address = false
  }

  worker_groups = [
    {
      name                          = "worker-1-eks"
      instance_type                 = "t2.medium"
      additional_userdata           = ""
      additional_security_group_ids = [aws_security_group.worker_group_mgmt.id]
      asg_desired_capacity          = 2
    },
    {
      name                          = "worker-2-eks"
      instance_type                 = "t2.medium"
      additional_userdata           = ""
      additional_security_group_ids = [aws_security_group.worker_group_mgmt.id]
      asg_desired_capacity          = 1
    },
  ]
}

data "aws_eks_cluster" "cluster" {
  name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks.cluster_id
}
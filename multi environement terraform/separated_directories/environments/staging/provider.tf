terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
 
  backend "s3" {
    bucket                  = "tf-awesome-backend"
    key                     = "multi-environments/staging/terraform.tfstate"
    region                  = "ap-southeast-1"
    profile                 = "tf-awesome"
  }
}
provider "aws" {
  profile = "tf-awesome"
  region  = var.default_region
}




terraform {
  required_version = "~> 1.15.7"
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 6.36.0"
    }

    random = {
        source = "hashicorp/random"
        version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

variable "project_name" {
  type    = string
  default = "opensearch-playground"
}

variable "aws_region" {
  type    = string
  default = "ap-northeast-1"
}

variable "db_username" {
  type    = string
  default = "postgres"
}

variable "db_password" {
  type      = string
  sensitive = true
}

variable "db_name" {
  type    = string
  default = "opensearch_playground"
}

variable "availability_zones" {
  type    = list(string)
  default = ["ap-northeast-1a", "ap-northeast-1c"]
}

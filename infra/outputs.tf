output "rds_endpoint" {
  value = aws_db_instance.this.endpoint
}

output "opensearch_endpoint" {
  value = aws_opensearch_domain.this.endpoint
}

output "alb_dns_name" {
  value = aws_lb.this.dns_name
}

output "ecs_task_execution_role_arn" {
  value = aws_iam_role.ecs_task_execution.arn
}

variable "project_id" {
  type        = string
  default     = "my-project"
  description = "Project ID for billing"
}
variable "group_id" {
  type        = string
  default     = "group-id.groups@domain.com"
  description = "Group ID of the Group"
}
variable "name" {
  type        = string
  default     = "google-group-name"
  description = "Name of the Group"
}
variable "owners" {
  type        = list(string)
  default     = ["admin@domain.com"]
  description = "Owner of the Group"
}
variable "managers" {
  type        = list(string)
  default     = ["manager@domain.com"]
  description = "Manager of the Group"
}
variable "members" {
  type        = list(string)
  default     = ["member-one@domain.com", "member-two@domain.com"]
  description = "Members of the Group"
}
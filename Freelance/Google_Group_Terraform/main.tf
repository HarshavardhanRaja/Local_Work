
provider "google-beta" {
  billing_project       = var.project_id
  user_project_override = true
}
module "group" {
  source  = "terraform-google-modules/group/google"
  version = "~> 0.1"
  
  id           = var.group_id
  display_name = var.name
  description  = "Test Google Group via Terraform"
  domain       = "domain.com"
  owners       = var.owners
  managers     = var.managers
  members      = var.members
}
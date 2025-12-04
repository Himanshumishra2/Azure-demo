variable "location" {
  type    = string
  default = "eastus"
}

variable "prefix" {
  type    = string
  default = "demoaks"
}

variable "node_vm_size" {
  type    = string
  default = "Standard_D2s_v3"
}

variable "node_count" {
  type    = number
  default = 1
}

variable "node_min_count" {
  type    = number
  default = 1
}

variable "node_max_count" {
  type    = number
  default = 3
}

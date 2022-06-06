resource "azurerm_kubernetes_cluster" "k8-cluster" {
  name                = "kube-cluster"
  location            = azurerm_resource_group.aks-group.location
  resource_group_name = azurerm_resource_group.aks-group.name
  dns_prefix          = "kube-cluster"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
  }
  service_principal {
    client_id     = azuread_service_principal.aks-demo1.application_id
    client_secret = azuread_service_principal_password.aks-demo1.value
  }  

}


output "kube_config" {
  value     = azurerm_kubernetes_cluster.k8-cluster.kube_config_raw
  sensitive = true
}

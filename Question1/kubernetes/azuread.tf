resource "azuread_application" "aks-demo1" {
  display_name               = "aks-demo1"
}

resource "azuread_service_principal" "aks-demo1" {
  application_id = azuread_application.aks-demo1.application_id
}

resource "azuread_service_principal_password" "aks-demo1" {
  service_principal_id = azuread_service_principal.aks-demo1.id
}

output "service_principal_password" {
  value     = azuread_service_principal_password.aks-demo1.value 
  sensitive = true
}

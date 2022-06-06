# Challenges
Challenges
**Question 1**

1. Create Kubernetes cluster
    Go to Question1/kubernetes dir and run terraform init/plan/apply
2. Create Ingress components, run the commands in below order.
    kubectl apply -f Rbac-ingress.yaml
    kubectl apply -f ingress-controller-new.yaml
    kubectl apply -f Ingress.yaml
    kubectl apply -f front-end-deply.yaml redis_leader-pv.yaml redis_follower_dep_service.yaml
3. Go to the IP in web browser of ingress-nginx to view the app

**Question 2**
To get the json metadata for AWS instance
  Run python get_metadata.py
To search with instance property with key
 Run python get_key.py and pass the key to view the value

**Question 3**

Run python ch3.py and pass the value of key to be searched and then the nested object  

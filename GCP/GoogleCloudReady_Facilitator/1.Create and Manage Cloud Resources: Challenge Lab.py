

# challenges in this lab

"""
https://google.qwiklabs.com/focuses/3563?parent=catalog
Task 1: Create a project jumphost instance
    Name the instance nucleus-jumphost.
    Use an f1-micro machine type.
    Use the default image type (Debian Linux).
"""
# gcloud config set compute/zone us-east1-b
# gcloud compute instances create nucleus-jumpshot --machine-type f1-micro --zone us-east1-b




"""
https://google.qwiklabs.com/focuses/878?parent=catalog
Task 2: Create a Kubernetes service cluster
    Create a cluster (in the us-east1-b zone) to host the service.
    Use the Docker container hello-app (gcr.io/google-samples/hello-app:2.0) as a place holder; the team will replace the container with their own work later.
    Expose the app on port 8080.
"""
# gcloud container clusters create my-cluster --zone us-east1-b
# gcloud container clusters get-credentials my-cluster

# kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:2.0
# kubectl expose deployment hello-server --type=LoadBalancer --port=8080 
# kubectl get service 






"""
https://google.qwiklabs.com/focuses/12007?parent=catalog
Task 3: Set up an HTTP load balancer
You will serve the site via nginx web servers, but you want to ensure that the environment is fault-tolerant. Create an HTTP load balancer with a managed instance group of 2 nginx web servers. Use the following code to configure the web servers; the team will replace this with their own configuration later
    
    Create an instance template.
    Create a target pool. Note:- this step doesnot requires.
    Create a managed instance group.
    Create a firewall rule to allow traffic (80/tcp).
    Create a health check.
    Create a backend service, and attach the managed instance group.
    Create a URL map, and target the HTTP proxy to route requests to your URL map.
    Create a forwarding rule.
"""

# startup_script
"""
cat << EOF > startup.sh
#! /bin/bash
apt-get update
apt-get install -y nginx
service nginx start
sed -i -- 's/nginx/Google Cloud Platform - '"\$HOSTNAME"'/' /var/www/html/index.nginx-debian.html
EOF
"""

#     Create an instance template.
"""
 gcloud compute instance-templates create lb-backend-template \
   --region=us-east1 \
   --network=default \
   --subnet=default \
   --tags=allow-health-check \
   --image-family=debian-9 \
   --image-project=debian-cloud \
   --metadata-from-file
   --startup-script= startup.sh
"""

# Create target-pools
"""
gcloud compute target-pools create nginx-pool
"""
# create managed instance group
"""
gcloud compute instance-groups managed create lb-backend-group \
    --base-instance-name=nginx --template=lb-backend-template --size=2 --zone=us-east1-b --target-pool=nginx-pool
"""

# Create a firewall rule to allow traffic (80/tcp)
"""
gcloud compute firewall-rules create fw-allow-health-check \
    --network=default \
    --action=allow \
    --direction=ingress \
    --source-ranges=130.211.0.0/22,35.191.0.0/16 \
    --target-tags=allow-health-check \
    --rules=tcp:80



gcloud compute addresses create lb-ipv4-1 \
    --ip-version=IPV4 \
    --global

"""

# create a health check for load balancer
"""
gcloud compute health-checks create http http-basic-check \
    --port 80
"""

# create a backend service and attach managed group instances to it
"""
gcloud compute backend-services create web-backend-service \
    --protocol=HTTP \
    --port-name=http \
    --health-checks=http-basic-check \
    --global


gcloud compute backend-services add-backend web-backend-service \
    --instance-group=lb-backend-group \
    --instance-group-zone=us-east1-b \
    --global
"""


#    Create a URL map, and target the HTTP proxy to route requests to your URL map.
"""
gcloud compute url-maps create web-map-http \
    --default-service web-backend-service

gcloud compute target-http-proxies create http-lb-proxy \
    --url-map web-map-http
"""

#     Create a forwarding rule.
"""
gcloud compute forwarding-rules create http-content-rule \
    --address=lb-ipv4-1\
    --global \
    --target-http-proxy=http-lb-proxy \
    --ports=80
"""


# https://mayankchourasia2.medium.com/getting-started-create-and-manage-cloud-resources-challenge-lab-6aade9186bdd
# https://gist.github.com/Tambunan26/9063521fdf406645aad4527ccd069149
# Build a Website on Google Cloud: Challenge Lab
"""
Task 1: Download the monolith code and build your container
Task 2: Create a kubernetes cluster and deploy the application
Task 3: Migrate Monolith to Microservices
Task 4: Deploy the new microservices
Task 5: Configure the Frontend microservice
Task 6: Create a containerized version of the Frontend microservice
Task 7: Deploy the Frontend microservice
"""




# Task 1: Download the monolith code and build your container
"""
cd ~
git clone https://github.com/googlecodelabs/monolith-to-microservices.git

cd ~/monolith-to-microservices
./setup.sh

cd ~/monolith-to-microservices/monolith
npm start

gcloud services enable cloudbuild.googleapis.com
cd ~/monolith-to-microservices/monolith
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/fancytest:1.0.0 .
"""



# Task 2: Create a kubernetes cluster and deploy the application
"""
gcloud services enable container.googleapis.com
gcloud container clusters create fancy-cluster --num-nodes 3 --zone us-central1-a
gcloud compute instances list

kubectl create deployment fancytest --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/fancytest:1.0.0
kubectl expose deployment fancytest --type=LoadBalancer --port 80 --target-port 8080
kubectl get all
    Note external ip
"""



# Task 3: Migrate Monolith to Microservices
"""
# Orders
cd ~/monolith-to-microservices/microservices/src/orders
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/orders:1.0.0 .

# Products
cd ~/monolith-to-microservices/microservices/src/products
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/products:1.0.0 .
"""




# Task 4: Deploy the new microservices
"""
# Orders
kubectl create deployment orders --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/orders:1.0.0
kubectl expose deployment orders --type=LoadBalancer --port 80 --target-port 8081
kubectl get service orders
    Note external IP

# Products
kubectl create deployment products --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/products:1.0.0
kubectl expose deployment products --type=LoadBalancer --port 80 --target-port 8082
kubectl get service products
    Note external ip

verify using: http://ORDERS_EXTERNAL_IP/api/orders
              http://PRODUCTS_EXTERNAL_IP/api/products

 """ 



# Task 5: Configure the Frontend microservice
"""
You need to update your config file in the monolith to point to the new Orders microservices IP address. Use the nano editor to replace the local URL with the IP address of the Orders microservice:
cd ~/monolith-to-microservices/react-app
vim .env

When the editor opens, your file should look like this:
REACT_APP_ORDERS_URL=http://localhost:8081/api/orders
REACT_APP_PRODUCTS_URL=http://localhost:8082/api/products

Replace the REACT_APP_ORDERS_URL to the new format while replacing with your Orders microservice IP address so it matches below:
REACT_APP_ORDERS_URL=http://<ORDERS_IP_ADDRESS>/api/orders
REACT_APP_PRODUCTS_URL=http://<PRODUCTS_IP_ADDRESS>/api/products

npm run build
"""



# Task 6: Create a containerized version of the Frontend microservice
"""
cd ~/monolith-to-microservices/microservices/src/frontend
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/frontend:1.0.0 .
"""



# Task 7: Deploy the Frontend microservice
"""
kubectl create deployment frontend --image=gcr.io/${GOOGLE_CLOUD_PROJECT}/frontend:1.0.0
kubectl expose deployment frontend --type=LoadBalancer --port 80 --target-port 8080
"""

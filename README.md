# 🚀 Scalable Flask Application on AWS

This project demonstrates how to deploy a **production-ready Flask web application** on AWS with a **scalable and highly available architecture**.

It uses modern cloud practices such as load balancing, auto scaling, and automated instance provisioning.

---

## ⚙️ Key Components

- **Flask** → Backend web application  
- **Gunicorn** → WSGI server for production  
- **Nginx** → Reverse proxy  
- **EC2** → Compute instances  
- **Application Load Balancer** → Traffic distribution  
- **Auto Scaling Group** → Automatic scaling & self-healing  

---

## 🚀 What This Project Demonstrates

- Deploying a Flask app in a production environment  
- Configuring Nginx + Gunicorn architecture  
- Creating reusable infrastructure using AMI  
- Implementing load balancing using ALB  
- Setting up Auto Scaling Group for scalability  
- Automating EC2 provisioning using user data  

---

## 🔁 How It Works

1. User sends request to Load Balancer  
2. Load Balancer routes traffic to healthy EC2 instances  
3. Auto Scaling Group ensures required number of instances  
4. Nginx forwards request to Gunicorn  
5. Gunicorn serves the Flask application  

---

## ⚠️ Challenges Faced

- Ensuring application runs automatically on instance startup  

---

## 🔐 Best Practices Used

- Stateless application design  
- Multi-AZ deployment  
- Infrastructure automation  
- Separation of concerns (Nginx, Gunicorn, Flask)  

---

## 🚀 Future Improvements

- HTTPS with AWS Certificate Manager  
- CI/CD pipeline (GitHub Actions)  
- CloudWatch logging  
- Database using Amazon RDS  

---
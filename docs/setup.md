# 🛠️ Complete Setup Guide – Flask App on AWS (EC2 + ALB + ASG)

This document provides a step-by-step guide to deploy a Flask application on AWS with a scalable and highly available architecture.

---

# 📌 Phase 1 — Launch Initial EC2 Instance

## 1. Create EC2 Instance
- OS: Ubuntu
- Instance type: t3.micro
- Allow ports:
  - 22 (SSH)
  - 80 (HTTP)


Used to automate instance setup:

```bash
#!/bin/bash

apt update -y
apt install python3-venv git nginx -y

cd /home/ubuntu
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

python3 -m venv venv
./venv/bin/pip install -r requirements.txt

cat <<EOF > /etc/systemd/system/flaskapp.service
[Unit]
Description=Gunicorn Flask App
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/<your-repo>
Environment="PATH=/home/ubuntu/<your-repo>/venv/bin"
ExecStart=/home/ubuntu/<your-repo>/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable flaskapp
systemctl start flaskapp

cat <<EOF > /etc/nginx/sites-available/default
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

systemctl restart nginx
systemctl enable nginx
```

---

## Test Application

Open:
http://<EC2-IP>

---

# 📌 Phase 2 — Create AMI

1. Go to EC2 Dashboard  
2. Select instance  
3. Click Actions → Image → Create Image  
4. Wait until AMI is available  

---

# 📌 Phase 3 — Create Launch Template

1. Go to EC2 → Launch Templates  
2. Click Create  

### Configure:
- AMI → Select created AMI  
- Instance type → t3.micro  
- Security group → Allow HTTP (80) + SSH  

---

# 📌 Phase 4 — Create Target Group

1. Go to EC2 → Target Groups → Create  

### Settings:
- Target type: Instances  
- Protocol: HTTP  
- Port: 80  
- Health check path: /  

---

# 📌 Phase 5 — Create Load Balancer (ALB)

1. Go to EC2 → Load Balancers → Create  
2. Choose Application Load Balancer  

### Configure:
- Internet-facing  
- Listener: HTTP (80)  
- Select VPC  
- Choose at least 2 subnets  

### Attach Target Group

---

# 📌 Phase 6 — Create Auto Scaling Group (ASG)

1. Go to EC2 → Auto Scaling Groups → Create  
2. Select Launch Template  

---

## Configure:

### Network
- Select VPC  
- Choose multiple subnets (different AZs)

---

### Attach Load Balancer
- Select existing Target Group  

---

### Group Size

Min: 2  
Desired: 2  
Max: 5  

---

### Scaling Policy
- Type: Target tracking  
- Metric: CPU Utilization  
- Target: 80%  

---

### Health Checks
- Enable EC2 + Load Balancer  

---

# 📌 Phase 7 — Test Setup

##  Access Application

Use ALB DNS:
http://<ALB-DNS>

---

# 📌 Final Result

- Scalable Flask application  
- Load-balanced traffic  
- Auto-healing infrastructure  
- Multi-AZ deployment  

---

# ✅ Summary

This setup ensures:
- High availability  
- Fault tolerance  
- Scalability  
- Automated deployment  

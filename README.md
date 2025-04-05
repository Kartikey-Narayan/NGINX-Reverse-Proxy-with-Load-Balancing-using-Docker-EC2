# 🚀 NGINX Reverse Proxy with Load Balancing using Docker & EC2

## **📜 Description**

This project demonstrates how to configure NGINX as a reverse proxy with load balancing between two backend services (Node.js & Python) running in Docker containers on AWS EC2. It includes HTTP to HTTPS redirection, Cloudflare SSL/TLS integration, and optional basic authentication for added security.

⸻

✨ **Features**

- 🌐 Redirects HTTP traffic to secure HTTPS.
- 🔁 Load balances incoming traffic across two backend servers: localhost:3000 and localhost:3001.
- 🔒 Uses SSL certificates from Cloudflare for secure connections.
- 📦 Supports large file uploads with client_max_body_size.
- 🛡️ Adds security headers like Strict-Transport-Security.
- 🧠 Easily customizable and extendable for other ports or services.

⸻

🔧 🛠️ **Tech Stack - Dependencies**

- 🌐 NGINX: High-performance HTTP server and reverse proxy.
- 🛡️ Cloudflare SSL: Secures the connection with SSL certificates.
- ⚙️ Node.js (3000) & Python App (3001): Example backend services being balanced.

⸻

🚀 ⚡ **How to Use**

- 📥 Clone the repository
- 🧭 Navigate to the project directory and explore the files and folders
- 📝 Check Nginx.txt file & replace your existing config with this setup or include it
- 🔐 Place your Cloudflare SSL cert and key in the proper path (/etc/nginx/ssl/*)
- 🟢 Reload NGINX with:

    sudo nginx -t && sudo systemctl restart nginx

⸻

🚦 🔥 **Contributing**

Feel free to contribute by creating a pull request or reporting issues:

- 🔥 Fork the repository
- ⚙️ Make your changes
- 🚀 Submit a pull request

⸻

🛡️ 🔒 **License**

This project is licensed under the MIT License 📄

⸻

🙌 🎯 **Acknowledgments**

Thanks for checking out this NGINX setup! 😁

Developed & Maintained by Kartikey Narayan – Happy DevOps-ing! 🧑‍💻⚙️

⸻

📌 **PS:** 🔥 Future Updates Coming Soon! 🚀

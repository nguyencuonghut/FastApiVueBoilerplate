# Production Setup Guide

## Deployment Checklist

### Environment Setup

**Backend (.env)**
```env
DEBUG=False
SECRET_KEY=<generate-strong-key-with-openssl>
DATABASE_URL=postgresql://produser:prodpass@prod-db:5432/fastapi_prod
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

Generate secure key:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

**Frontend (.env.production)**
```
VITE_API_URL=https://api.yourdomain.com
VITE_APP_NAME=Your App Name
```

### Database Preparation

1. Create production PostgreSQL database
2. Run migrations:
```bash
python -m app.database.init_db
```

3. Create admin user via API or script

### Backend Deployment

**Using Gunicorn:**
```bash
pip install gunicorn
gunicorn app.main:app --workers 4 --bind 0.0.0.0:8000
```

**Using Docker:**
```bash
docker build -t backend:prod -f backend/Dockerfile .
docker run -d -p 8000:8000 --name backend-prod backend:prod
```

**Nginx Reverse Proxy:**
```nginx
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Frontend Deployment

**Build:**
```bash
npm run build
```

**Deploy to CDN/Static Host:**
```bash
# Copy dist/ folder to your hosting
# Set up rewrite rules for SPA routing
```

**Nginx Config:**
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /var/www/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

### SSL/TLS Setup

Use Let's Encrypt:
```bash
certbot --nginx -d yourdomain.com
```

### Security Best Practices

1. ✅ Use HTTPS everywhere
2. ✅ Set strong SECRET_KEY
3. ✅ Enable CORS only for your domain
4. ✅ Use environment variables for secrets
5. ✅ Set DEBUG=False in production
6. ✅ Use database backups
7. ✅ Monitor logs for errors
8. ✅ Keep dependencies updated

### Performance Optimization

**Backend:**
- Enable caching headers
- Use CDN for static files
- Database connection pooling
- Request compression

**Frontend:**
- Code splitting
- Asset compression
- Image optimization
- Lazy loading

### Monitoring & Logging

Set up logging:
- Application logs
- Nginx access/error logs
- Database slow query logs
- Monitor CPU/Memory/Disk

### Backup Strategy

Backup regularly:
- Database backups
- Application code
- Configuration files

---

See README.md for more details.

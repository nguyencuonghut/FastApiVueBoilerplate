# Database Management

Quản lý database với Python script (tương tự Laravel Artisan).

## 📋 Commands

### Trong Docker Container

```bash
# Xem trạng thái database
docker exec fastapi_vue_backend python manage.py status

# Tạo tables (migration)
docker exec fastapi_vue_backend python manage.py migrate

# Seed dữ liệu mẫu
docker exec fastapi_vue_backend python manage.py seed

# Drop và tạo lại tables (migrate:refresh)
docker exec fastapi_vue_backend python manage.py refresh

# Reset hoàn toàn: Drop + Recreate + Seed (migrate:refresh --seed)
docker exec fastapi_vue_backend python manage.py reset

# Drop tất cả tables
docker exec fastapi_vue_backend python manage.py drop

# Xem hướng dẫn
docker exec fastapi_vue_backend python manage.py help
```

### Trực tiếp trong Backend (nếu không dùng Docker)

```bash
cd backend
python manage.py status
python manage.py migrate
python manage.py seed
python manage.py reset
```

## 🔄 Use Cases

### 1. Fresh Install
```bash
docker exec fastapi_vue_backend python manage.py reset
```

### 2. Chỉ thêm dữ liệu mẫu (tables đã tồn tại)
```bash
docker exec fastapi_vue_backend python manage.py seed
```

### 3. Reset database khi develop/test
```bash
docker exec fastapi_vue_backend python manage.py reset
```

### 4. Kiểm tra database
```bash
docker exec fastapi_vue_backend python manage.py status
```

## 📊 Demo Data

Khi chạy `seed` hoặc `reset`, hệ thống tạo:

### Roles (7)
- `superadmin` - Full access
- `admin` - Administrator
- `it` - IT Staff
- `bao_tri` - Maintenance staff
- `bao_ve` - Security guard
- `quan_ly_trai` - Site manager
- `user` - Regular user

### Permissions (14)
- User management: `user:read`, `user:create`, `user:update`, `user:delete`
- Role management: `role:read`, `role:create`, `role:update`
- Permission: `permission:read`
- Reports: `report:read`
- System: `system:config`
- Monitoring: `monitor:view`
- Kiosk: `kiosk:access`
- Maintenance: `maintenance:manage`
- Security: `security:manage`

### Demo Users (6)

| Username | Password | Role | Email |
|----------|----------|------|-------|
| superadmin | super123 | superadmin | superadmin@example.com |
| admin | admin123 | admin | admin@example.com |
| it_staff | it123 | it | it@example.com |
| bao_tri_user | baotri123 | bao_tri | baotri@example.com |
| bao_ve_user | baove123 | bao_ve | baove@example.com |
| quan_ly | quanly123 | quan_ly_trai | quanly@example.com |

## ⚠️ Lưu ý

- `reset` và `drop` sẽ **XÓA TẤT CẢ DỮ LIỆU** - sử dụng cẩn thận!
- Trên production, nên sử dụng Alembic migrations thay vì script này
- Script này phù hợp cho development và testing

## 🔧 So sánh với Laravel

| Laravel | FastAPI (script này) |
|---------|---------------------|
| `php artisan migrate` | `python manage.py migrate` |
| `php artisan db:seed` | `python manage.py seed` |
| `php artisan migrate:refresh` | `python manage.py refresh` |
| `php artisan migrate:refresh --seed` | `python manage.py reset` |
| `php artisan db:wipe` | `python manage.py drop` |
| `php artisan migrate:status` | `python manage.py status` |

## 📝 Extend Script

Để thêm commands mới, edit `backend/manage.py`:

```python
def your_command():
    """Your command description"""
    # Your implementation
    pass

if __name__ == "__main__":
    commands = {
        'migrate': migrate,
        'your_command': your_command,  # Add here
        # ...
    }
```

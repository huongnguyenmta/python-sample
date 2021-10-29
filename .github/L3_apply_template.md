## Get Personal Access token github
refs: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

1. Step 1
- Click [Avatar] tại góc trên cùng bên phải header
- Click chọn [Settings]
- Tại menu left-sidebar: Click chọn [Personal access tokens]
2. Step 2: Sinh mới token
- Click button [Generate new token.]
- Chọn các option có "repo"
- Click button [Generate token]
3. Step 3: Lưu token về máy cá nhân, sử dụng thay mật khẩu để push/pull source code

## Một số command cơ bản làm việc với git
1. Làm việc với BRANCH
#### Loại branch: có 2 loại

+ Nhánh tích hợp: master/main (để tích hợp code)
+ Nhánh chủ đề: đặt tên nhánh theo từng chức năng của project (để phát triển các chức năng)

VD: login, sign-up, list-user, ...

#### Command cơ bản làm việc với branch
- Kiểm tra branch hiện tại: `$ git branch`
- Tạo mới branch: `$ git checkout -b branch_name`
- Di chuyển đến 1 branch: `$ git checkout branch_name`
Ví dụ: Tạo nhánh phát triển chức năng Đăng nhập
```
$ git checkout -b login
```
2. Đẩy code từ local lên remote
```
$ git push origin branch_name
```
3. Kéo code từ remote về local
```
$ git checkout master/main
$ git pull origin master/main
```
4. Tạo pull request
Tạo pull request và compare với master/main

## Apply template
https://startbootstrap.com/theme/sb-admin-2
1. Download template
2. Tại folder `/mysite/` tạo 2 folder:
- Folder `static`: chứa các file css, js, img
- Folder `template`: chứa các file html

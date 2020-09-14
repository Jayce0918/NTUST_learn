# shop/form.py
from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.utils.translation import gettext as _


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # 要override password1,2 的label必須要從這裡改
        self.fields['password1'].label = "密碼"
        self.fields['password2'].label = "密碼確認"
    class Meta:
        model = User
        # 決定註冊欄位要有哪些及順序
        fields = ('username','password1','password2','name','sex','phone')
        # 各欄位顯示的標籤，如沒有則就是原本的變數名稱
        labels = {
            "username": "帳號",
            "name":"姓名",
            "sex":"性別",
            "phone":"手機",
         }

class EditForm(ModelForm):
    class Meta:
        model = User
        fields = ('name','sex','email','phone')
        labels = {
            "name":_("姓名"),
            "sex":"性別",
            "email":"信箱",
            "phone":"手機",
        }

#作業圖片牆

        

# 留言板






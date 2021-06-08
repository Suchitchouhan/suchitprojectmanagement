from account.models import Account
from django import forms


# def check_blank_or_null(data):
# 	status=True
# 	for x in data:
# 		if x=="" or x==None:
# 			status=False
# 			break
# 		else:
# 			pass					
# 	return status	




class signupForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'full_name','password')

# class signupForm(forms.Form):
#     full_name = forms.CharField(label='full name', max_length=100)
#     email = forms.EmailField(label='email', max_length=100)
#     password = forms.CharField(label='password', max_length=100)
#     def clean(self):
#         email=self.cleaned_data['email']
#         full_name=self.cleaned_data['full_name']
#         password=self.cleaned_data['password']
#         if check_blank_or_null([email,password]) == False:
#             raise forms.ValidationError("Email and password can not empty")
#         if Account.objects.filter(email=email).exists() == True:
#             raise forms.ValidationError("Email is already exists")
#         if password.isalnum() == True:
#             raise forms.ValidationError("password must be alpha numeric")   
#         if len(full_name) > 1000:
#             raise forms.ValidationError("Full name must not exceed the lenth of 1000")
#         return self.cleaned_data 
#     def save(self):
#         print(self.cleaned_data['email'])
#         user=Account.objects.create_user(email=self.cleaned_data['email'],password=self.cleaned_data['password'])
#         user.full_name=self.cleaned_data['full_name']
#         user.save()
#         return user      

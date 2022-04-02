from django.shortcuts import render,reverse,redirect
from django.views import generic
from .forms import MailCreateForm
from django.core.mail import send_mail

from django.contrib.auth.forms import UserCreationForm
# Create your views here.




#Comments


class SignUpView(generic.CreateView):
    template_name ="mail/signup.html"
    form_class = UserCreationForm
    
    
    def get_success_url(self):
        return reverse('login')


class MailCreateView(generic.CreateView):
    template_name = 'mail/mail_create.html'
    context_object_name = "mail"
    form_class = MailCreateForm
    
    def get_success_url(self):
        return reverse('mails:mail_create')
    
    def form_valid(self ,form):
        form = form.save(commit=False)
        subject = form.subject
        message = form.message
        from_email = self.request.user.email
        receiver_one = form.receiver_one
        receiver_two = form.receiver_two
        receiver_three = form.receiver_three
        receiver_four = form.receiver_four
        receiver_five = form.receiver_five
        
        recipient_list = [receiver_one,receiver_two,receiver_three,receiver_four,receiver_five]
        
        form.save()
        
        send_mail(
            subject = subject,
            message = message,
            from_email = from_email,
            recipient_list = recipient_list,
        )
        
        return super(MailCreateView, self).form_valid(form)
    
'''def MailCreate(request):
    form = MailCreateForm()
    
    if request.method == 'POST':
        form = MailCreateForm(request.POST)
        
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            recipient_list = form.cleaned_data['recipient_list']
            
            send_mail(
                subject = subject,
                message = message,
                from_email = from_email,
                recipient_list = [recipient_list]
            )
           
            return redirect('mails:mail_create')
        
    context = {'form':form}
    
    
        
    return render(request, 'mail/mail_create.html', context)'''
from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Teacher,Subject,Literature,Takyryp,Zert_jumys,Keste
from .forms import SignupForm
from django.contrib import auth




def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Teacher.objects.all().count()
    # Доступные книги (статус = 'a')
    subj_num = Subject.objects.all().count()
    num_takyryp = Takyryp.objects.all().count()  # Метод 'all()' применен по умолчанию.
    contacts_form_data = ''

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'subj_num': subj_num,
                 'num_takyryp': 5,},
    )



def syllabus(request):
    techers = Teacher.objects.all()
    if request.method == 'POST':
        postrek = request.POST.getlist('postt')
        pre = request.POST.getlist('pre')
        teacher = request.POST.get('teacher')
        lab = request.POST.get('lab')
        prak = request.POST.get('prak')
        print(teacher)
        subject = request.POST.get('subject')
        takyryp = request.POST.getlist('takyryp')
        literature = request.POST.getlist('literature')
        zertjumys = request.POST.getlist('zertjumys')
        postre = request.POST.get('post')
        kkm = request.POST.get('kkm')
        pokab = request.POST.get('pokab')
        #subjectname = Subject.objects.only("credit").filter(subject_name=subject)
        subject_credit = Subject.objects.get(subject_name=subject).credit
        subject_outcome = Subject.objects.get(subject_name=subject).outcome
        subject_description = Subject.objects.get(subject_name=subject).description
        #takyryp_opisanie = Takyryp.objects.get(takyryp_aty=takyryp).opisanie
        teacher_last = Teacher.objects.get(first_name=teacher).last_name
        teacher_email = Teacher.objects.get(first_name=teacher).email
        teacher_phone = Teacher.objects.get(first_name=teacher).phone_numbers
        teacher_account = Teacher.objects.get(first_name=teacher).account
        teacher_otch = Teacher.objects.get(first_name=teacher).patronymic

        prak_teacher_last = Teacher.objects.get(first_name=prak).last_name
        prak_teacher_email = Teacher.objects.get(first_name=prak).email
        prak_teacher_phone = Teacher.objects.get(first_name=prak).phone_numbers
        prak_teacher_account = Teacher.objects.get(first_name=prak).account
        prak_teacher_otch = Teacher.objects.get(first_name=prak).patronymic

        lab_teacher_last = Teacher.objects.get(first_name=lab).last_name
        lab_teacher_email = Teacher.objects.get(first_name=lab).email
        lab_teacher_phone = Teacher.objects.get(first_name=lab).phone_numbers
        lab_teacher_account = Teacher.objects.get(first_name=lab).account
        lab_teacher_otch = Teacher.objects.get(first_name=lab).patronymic

        zert_number = []
        takyryp_number = []
        takyryp_opisanie = []
        literature_author = []
        literature_god = []
        literature_izdanie = []
        literature_stranica = []

        for i in range(len(zertjumys)):
            zert_number.append(Zert_jumys.objects.get(opisanie=zertjumys[i]).number)
            print(zert_number[i])
        for j in range(len(takyryp)):
            takyryp_number.append(Takyryp.objects.get(takyryp_aty = takyryp[j]).number)
            takyryp_opisanie.append(Takyryp.objects.get(takyryp_aty = takyryp[j]).opisanie)
            print(takyryp_opisanie[j])
        for k in range(len(literature)):
            literature_author.append(Literature.objects.get(literature_name = literature[k]).author)
            literature_izdanie.append(Literature.objects.get(literature_name = literature[k]).izdanie)
            literature_stranica.append(Literature.objects.get(literature_name = literature[k]).stranica)
            literature_god.append(Literature.objects.get(literature_name = literature[k]).god)
            print(literature_author[k])
            print(literature_izdanie[k])
            print(literature_stranica[k])
            print(literature_god[k])

        con={
            'teacher': teacher, 'subject': subject, 'post': postrek[0], 'pre': pre[0],
            'outcome': subject_outcome

        }

        context = {
                   'description': subject_description,
                   'takyryp1': takyryp[0], 'tak_opisanie1': takyryp_opisanie[0], 'takyryp2': takyryp[1],
                   'tak_opisanie2': takyryp_opisanie[1], 'takyryp3': takyryp[2], 'tak_opisanie3': takyryp_opisanie[2],
                   'takyryp4': takyryp[3], 'tak_opisanie4': takyryp_opisanie[3], 'takyryp5': takyryp[4],
                   'tak_opisanie5': takyryp_opisanie[4], 'takyryp6': takyryp[5],
                   'tak_opisanie6': takyryp_opisanie[5], 'takyryp7': takyryp[6], 'tak_opisanie7': takyryp_opisanie[6],
                   'takyryp8': takyryp[7], 'tak_opisanie8': takyryp_opisanie[7],
                   'takyryp9': takyryp[8], 'tak_opisanie9': takyryp_opisanie[8], 'takyryp10': takyryp[9],
                   'tak_opisanie10': takyryp_opisanie[9], 'takyryp11': takyryp[10],
                   'tak_opisanie11': takyryp_opisanie[10], 'takyryp12': takyryp[11],
                   'tak_opisanie12': takyryp_opisanie[11], 'takyryp13': takyryp[12],
                   'tak_opisanie13': takyryp_opisanie[12],
                   'zert_number0': zert_number[0], 'zertjumys0': zertjumys[0], 'zert_number1': zert_number[1],
                   'zertjumys1': zertjumys[1], 'zert_number2': zert_number[2], 'zertjumys2': zertjumys[2],
                   'zert_number3': zert_number[3], 'zertjumys3': zertjumys[3], 'zert_number4': zert_number[4],
                   'zertjumys4': zertjumys[4],
                   'zert_number5': zert_number[5], 'zertjumys5': zertjumys[5], 'zert_number6': zert_number[6],
                   'zertjumys6': zertjumys[6],
                   'zert_number7': zert_number[7], 'zertjumys7': zertjumys[7], 'zert_number8': zert_number[8],
                   'zertjumys8': zertjumys[8],
                   'zert_number9': zert_number[9], 'zertjumys9': zertjumys[9], 'zert_number10': zert_number[10],
                   'zertjumys10': zertjumys[10],
                   'literature0': literature[0], 'literature1': literature[1],
                   'kkm': kkm, 'pokab': pokab, 'subject_credit': subject_credit, 'teacher_last': teacher_last,
                   'teacher_email': teacher_email, 'teacher_phone': teacher_phone, 'teacher_account': teacher_account,
                   'teacher_otch': teacher_otch, 'prak_teacher_last': prak_teacher_last,
                   'prak_teacher_email': prak_teacher_email, 'prak_teacher_otch':
                       prak_teacher_otch, 'prak': prak, 'lab_teacher_last': lab_teacher_last,
                   'lab_teacher_email': lab_teacher_email, 'lab_teacher_otch': lab_teacher_otch, 'lab': lab}






    return render(
        request,
        'syll.html',

        context,con
    )

def zapol(request):
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    zertjumyss = Zert_jumys.objects.all()
    takyryps = Takyryp.objects.all()
    literaturas = Literature.objects.all()
    if request.method == 'POST' and request.POST.get('sub_name')!=None:
        sub_tak = request.POST.getlist('sub_tak')
        sub_lit = request.POST.getlist('sub_lit')
        sub_name = request.POST.get('sub_name')
        sub_cred= request.POST.get('sub_cred')
        sub_desc = request.POST.get('sub_desk')
        sub_out = request.POST.get('sub_out')
        sub_post = request.POST.get('sub_post')
        subjectt = Subject.objects.create()
        subjectt.subject_name = sub_name
        subjectt.credit = sub_cred
        subjectt.description = sub_desc
        subjectt.outcome = sub_out
        subjectt.postrekvisit = sub_post
        for i in sub_tak:
            subjectt.takyryp.create(takyryp_aty=i)
        for j in sub_lit:
            subjectt.literature.create(literature_name=j)
        subjectt.save()
    if request.method == 'POST' and request.POST.get('tak_aty')!=None:
        takyrypp = Takyryp.objects.create()
        tak_zert = request.POST.get('tak_zert')
        takyrypp.number = request.POST.get('tak_number')
        takyrypp.takyryp_aty = request.POST.get('tak_aty')
        takyrypp.opisanie = request.POST.get('tak_opisanie')
        takyrypp.zert_jumys=Zert_jumys.objects.get(opisanie=tak_zert)
        takyrypp.save()
    if request.method == 'POST' and request.POST.get('ad_name')!=None:
        liter = Literature.objects.create()
        liter.literature_name = request.POST.get('ad_name')
        liter.author = request.POST.get('ad_author')
        liter.izdanie = request.POST.get('ad_izdanie')
        liter.stranica = request.POST.get('ad_stranica')
        liter.god = request.POST.get('ad_god')
        liter.typee = request.POST.get('ad_tip')
        liter.save()

    if request.method == 'POST' and request.POST.get('zert_number') != None:
        zert = Zert_jumys.objects.create()
        zert.number = request.POST.get('zert_number')
        zert.opisanie = request.POST.get('zert_opisanie')
        zert.save()

    if request.method == 'POST' and request.POST.get('apta') != None:
        apta = Keste.objects.create()
        op = Takyryp.objects.get(takyryp_aty=request.POST.get('tak')).opisanie
        apta.apta = request.POST.get('apta')
        apta.apta+op
        apta.lekcia = request.POST.get('tak')
        apta.zert = request.POST.get('zert')
        apta.save()


    return  render(request,'forma.html',{'teachers':teachers, 'subjects': subjects, 'zertjumyss': zertjumyss, 'takyryps': takyryps,'literaturas': literaturas})

def subform(request):
    takyryps = Takyryp.objects.all()
    literaturas = Literature.objects.all()
    return render(request,'subform.html',{'takyryps': takyryps,'literaturas': literaturas},)

def takform(request):
    zertjumyss = Zert_jumys.objects.all()
    return render(request,'takform.html',{'zertjumyss':zertjumyss},)

def adform(request):
    liter = Literature.objects.all()
    return render(request, 'adform.html', {'liters': liter}, )

def kesteform(request):
    zert = Zert_jumys.objects.all()
    tak = Takyryp.objects.all()
    return render(request,'kesteform.html',{'takyryps':tak,'zertjumyss':zert})

def zertform(request):
    liter = Literature.objects.all()
    return render(request, 'zertform.html', {'liters': liter}, )


def signupform(request):
	#if form is submitted
	if request.method == 'POST':
		#will handle the request later
		form = SignupForm(request.POST)

		#checking the form is valid or not
		if form.is_valid():
			#if valid rendering new view with values
			#the form values contains in cleaned_data dictionary
			return render(request, 'result.html', {
					'name': form.cleaned_data['name'],
					'email': form.cleaned_data['email'],
				})

	else:
		#creating a new form
		form = SignupForm()

	#returning form
	return render(request, 'signupform.html', {'form':form});
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import(
	index,
	student_homepage,
	student_personal_homepage,
	apply_to_teach,
	subject_topic,
	subject_overview,
	teacher_homepage,
	about,
	error,
	teacher_new_base,
	view_my_students,
	teacher_uploaded_subjects,
	upload_content,
	view_new_uploaded_content,
	get_video,
	get_document,
	FAQ,
	transaction_details,
	my_profile,
	payment_details,
	HomeView,
	switch_to_teacher_page,
	classes,
	classes2,
	push,
	upload,
	overview,
	classes_base,
	upload_to,
	edit_my_uploaded,
	my_uploaded,
	subject_get,
	edit_my_topic,
	topic_delete,
	post_detail

	)

app_name = "e_learning"

urlpatterns = [
	path('',index, name='index'),
    path('homepage/',student_homepage, name='home'),
    path('my_subjects/',student_personal_homepage, name='my_subjects'),
    path('apply_to_teach/',apply_to_teach, name='apply_to_teach'),
    path('subject_topic/',subject_topic, name='subject_topic'),
    path('subject_overview/<slug>/',subject_overview, name='subject_overview'),
    path('subject_overview/',subject_overview, name='subject_overview'),
    path('teacher_homepage/',teacher_homepage, name='teacher_homepage'),
    path('about/',about, name='about'),
    path('error/',error, name='error'),
    path('my_students/',view_my_students, name='my_students'),
    path('home_view/', HomeView.as_view(), name='home_view'),
    path('my_uploaded_subjects/',teacher_uploaded_subjects,name='my_uploaded_subjects'),
    path('upload_content/',upload_content, name='upload_content'),
    path('classes/',classes, name='classes'),
	path('classes_base/',classes_base, name='classes_base'),
	path('classes2/',classes2, name='classes2'),
    path('view_new_uploaded_content/',view_new_uploaded_content, name='view_new_uploaded_content'),
    path('video/<id>/', get_video, name='video'),
    path('document/<id>/', get_document, name='document'),
    path('frequently_asked_questions/',FAQ,name='frequently_asked_questions'),
    path('transaction_details/',transaction_details, name='transaction_details'),
    path('my_profile/',my_profile,name='my_profile'),
    path('payment_details/',payment_details,name='payment_details'),
    path('switch_to_teacher_page/',switch_to_teacher_page,name='switch_to_teacher_page'),
	path('push/',push, name='push'),
	path('push/<slug>/',push, name='push'),
	path('upload/',upload, name='upload'),
	path('upload_to/',upload_to, name='upload_to'),
	path('overview/',overview, name='overview'),
	path('my_uploaded/<slug>/',my_uploaded,name='my_uploaded'),
    path('my_uploaded/',my_uploaded,name='my_uploaded'),
	path('edit_my_uploaded/<slug>/',edit_my_uploaded,name='edit_my_uploaded'),
    path('edit_my_uploaded/',edit_my_uploaded,name='edit_my_uploaded'),
	path('edit_my_topic/<slug>/',edit_my_topic,name='edit_my_topic'),
    path('edit_my_topic/',edit_my_topic,name='edit_my_topic'),
	#path('particular_subject/',particular_,name='particular_'),
	path('subject_get/',subject_get,name='subject_get'),
	path('topic_delete/<slug>/',topic_delete,name='topic_delete'),
    path('topic_delete/',topic_delete,name='topic_delete'),
	path('post_detail/', post_detail, name='post_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('upload_content_s1/',upload_content, name='upload_content_s1'),uploaded
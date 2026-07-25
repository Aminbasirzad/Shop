from django.shortcuts import render

def case_study(request):
  return render(request, 'case_study/case-study.html')

def case_study_detail(request):
  return render(request, 'case_study/cases-study-details.html')

from urllib import request

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from PR.models import applicant_info

def application(request):
    return render(request, 'pr/application.html')

def applicant_info_method(request):
        first_name= request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name= request.POST['last_name']
        sex = request.POST['gender']
        dob = request.POST['date_of_birth']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pob = city + ' ' + state + ' ' + country
        mobile = request.POST['mobile_number']
        email = request.POST['email']
        UIC = request.POST['uic']

        # applicant = applicant_info()
        # applicant.save()
        # print('applicant saved')

# additional_info
        addressline1 = request.POST['address_line_1']
        addressline2 = request.POST['address_line_2']
        current_addres = addressline1 + addressline2
        current_city = request.POST['current_city']
        current_country = request.POST['current_country']
        postal_code = request.POST['postal_code']
        native_language = request.POST['language']

        # additional.save()
        # print('additional info saved !')

# passport_info
        passport_number = request.POST['passport_no']
        passport_issuance_place = request.POST['issue_place']
        issue_date = request.POST['issue_date']
        expiry_date = request.POST['expiry_date']
        applicant_height = request.POST['height']
        applicant_eyecolor = request.POST['eyecolor']
        passport = applicant_info(first_name = first_name, middle_name=middle_name, last_name=last_name, sex=sex, date_of_birth=dob, birth_place=pob, phone_number=mobile, email=email, UIC=UIC, current_address=current_addres, current_city=current_city,
                                     current_country=current_country, postal_code=postal_code,
                                     native_language=native_language, passport_number=passport_number, passport_issuance_place= passport_issuance_place, issue_date= issue_date, expiry_date=expiry_date, applicant_height= applicant_height, applicant_eyecolor= applicant_eyecolor)
        passport.save()
        print('passport_info saved')
#
# # martial_status
#         spouse_first_name = request.POST['spouse_first_name']
#         spouse_middle_name = request.POST['spouse_middle_name']
#         spouse_last_name = request.POST['spouse_last_name']
#         spouse_sex =  request.POST['spouse_gender']
#         spouse_dob =  request.POST['spouse_dob']
#         spouse_passport_number =  request.POST['spouse_passport_no']
#         spouse_info = martial_status(spouse_first_name= spouse_first_name, spouse_middle_name=spouse_middle_name, spouse_last_name=spouse_last_name, spouse_sex= spouse_sex, spouse_dob=spouse_dob, passport_number= spouse_passport_number)
#         spouse_info.save()
#         print('martial status updated')
#
# # children_info
#         no_of_children = request.POST['no_of_children']
#         name_of_children = request.POST['children_name']
#         dob_of_children = request.POST['children_dob']
#         sex_of_children = request.POST['children_gender']
#         children = children_info(no_of_children=no_of_children, name_of_children=name_of_children, dob_of_children=dob_of_children, sex_of_children=sex_of_children)
#         children.save()
#         print('children info saved')
#
# # family_info
#
#         father_name = request.POST['father_name']
#         mother_name = request.POST['mother_name']
#         no_of_siblings = request.POST['no_of_sibling']
#         name_of_sibling = request.POST['sibling_name']
#         dob_of_sibling = request.POST['sibling_dob']
#         sex_of_sibling = request.POST['sibling_gender']
#         family = family_info(father_name=father_name, mother_name=mother_name, no_of_siblings=no_of_siblings, name_of_sibling=name_of_sibling, dob_of_sibling=dob_of_sibling, sex_of_sibling=sex_of_sibling)
#         family.save()
#         print('family info saved')
#
# # fee_structure
#         administration_fee = request.POST['administration_fee']
#         discount = request.POST['discount']
#         total_administration_fee = request.POST['total_administration_fee']
#         first_term_date = request.POST['first_term_date']
#         first_term_amount = request.POST['first_term_amount']
#         gst_of_first_term = request.POST['gst_of_first_term']
#         total_payment_paid_in_first_term = request.POST['first_term_total_pay']
#         second_term_date = request.POST['second_term_date']
#         second_term_amount = request.POST['second_term_amount']
#         gst_of_second_term = request.POST['gst_of_second_term']
#         total_payment_paid_in_second_term = request.POST['second_term_total_pay']
#         third_term_date = request.POST['third_term_date']
#         third_term_amount = request.POST['third_term_amount']
#         gst_of_third_term = request.POST['gst_of_third_term']
#         total_payment_paid_in_third_term = request.POST['third_term_total_pay']
#         fee = fee_structure(administration_fee=administration_fee, discount=discount, total_administration_fee= total_administration_fee, first_term_date=first_term_date,
#                             first_term_amount=first_term_amount, gst_of_first_term=gst_of_first_term, total_payment_paid_in_first_term= total_payment_paid_in_first_term,
#                             second_term_date= second_term_date, second_term_amount=second_term_amount, gst_of_second_term= gst_of_second_term, total_payment_paid_in_second_term= total_payment_paid_in_second_term,
#                             third_term_date= third_term_date, third_term_amount= third_term_amount, gst_of_third_term= gst_of_third_term, total_payment_paid_in_third_term= total_payment_paid_in_third_term)
#         fee.save()
#         print('fee updated')
#
#
# # job_detail
# #         current_job_start_date = request.POST['current_position']
# #         current_company_name = request.POST['current_company_name']
# #         current_position = request.POST['current_job_start_date']
# #         current_company_address = request.POST['current_company_address']
# #         previous_company_name = request.POST['gst_of_third_term']
# #         previous_position =request.POST['gst_of_third_term']
# #         previous_start_date = request.POST['gst_of_third_term']
# #         previous_end_date = request.POST['gst_of_third_term']
#
# # address_details
#         previous_address = request.POST['previous_address']
#         previous_start_date = request.POST['previous_start_date']
#         previous_end_date = request.POST['previous_end_date']
#         previous_city = request.POST['previous_city_province']
#         previous_country = request.POST['previous_country']
#         previous_postal_code = request.POST['postal_code']
#         address = address_details(previous_address=previous_address, previous_start_date=previous_start_date, previous_end_date=previous_end_date,
#                                   previous_city=previous_city, previous_country=previous_country, previous_postal_code=previous_postal_code)
#         address.save()
#         print('address info saved')
# #
# # # travel_history
#         place_of_original_entry = request.POST['place_of_original_entry']
#         date_of_original_entry = request.POST['date_of_original_entry']
#         place_of_most_recent_entry = request.POST['place_of_most_recent_entry']
#         date_of_most_recent_entry = request.POST['date_of_most_recent_entry']
#         travel = travel_history(place_of_original_entry= place_of_original_entry, date_of_original_entry=date_of_original_entry,
#                                 place_of_most_recent_entry=place_of_most_recent_entry, date_of_most_recent_entry=date_of_most_recent_entry)
#         travel.save()
#         print('travel history saved')
#
# # relative background_in_canada
#
#         contact_person_first_name = request.POST['person_first_name']
#         contact_person_last_name = request.POST['person_first_name']
#         contact_person_phone_number = request.POST['contct_person_phone_number']
#         contact_person_email = request.POST['contact_person_email']
#         realtive_background = background_in_canada(contact_person_first_name=contact_person_first_name, contact_person_last_name=contact_person_last_name,
#                                                    contact_person_phone_number=contact_person_phone_number, contact_person_email=contact_person_email)
#         realtive_background.save()
#         print("relatives's background updated")
# # documents
# #
#         document_name = request.POST['document_name']
#         documents = request.POST['documents']
#         document = documents(document_name=document_name, documents=documents)
#         document.save()
#         print('document saved')
        return render(request, 'pr/saved.html')
#









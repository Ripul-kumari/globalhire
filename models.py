from djongo import models
from datetime import date

# Create your models here.
# Gender = (
#     ("Male", "Male"),
#     ("Female", "Female"),
#     ("Other", "Other"),
# )

class applicant_info(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    middle_name=models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(null=True)
    birth_place = models.TextField(max_length=250, null=True)
    phone_number = models.TextField(max_length=10, null=True)
    email= models.TextField(max_length=60, null=True)
    UIC = models.TextField(max_length=40, null=True)

    current_address = models.TextField(max_length=300, null=True)
    current_city = models.TextField(max_length=100, null=True)
    current_country = models.TextField(max_length=100, null=True)
    postal_code = models.CharField(max_length=6, null=True)
    native_language = models.CharField(max_length=50, null=True)

    passport_number = models.TextField(primary_key=True, null=False)
    issue_date = models.DateField(null=True)
    expiry_date = models.DateField(null=True)
    passport_issuance_place = models.TextField(max_length=250, null=True)
    applicant_height = models.TextField(null=True)
    applicant_eyecolor = models.CharField(max_length=20, null=True)


    def __unicode__(self):
        return self.passport_number

class martial_status(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    spouse_first_name = models.CharField(max_length=20, null=True)
    spouse_middle_name = models.CharField(max_length=20, null=True)
    spouse_last_name = models.CharField(max_length=20, null=True)
    spouse_sex = models.CharField(max_length=10, null=True)
    spouse_dob = models.DateField(null=True)
    passport_number = models.TextField(null=True)

class children_info(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    no_of_children = models.IntegerField(null=True)
    name_of_children = models.CharField(max_length=100, null=True)
    dob_of_children = models.DateField(null=True)
    sex_of_children = models.CharField(max_length=10, null=True)

class family_info(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    father_name = models.CharField(max_length=100, null=True)
    mother_name = models.CharField(max_length=100, null=True)
    no_of_siblings = models.IntegerField(null=True)
    name_of_sibling = models.CharField(max_length=250, null=True)
    dob_of_sibling = models.DateField(null=True)
    sex_of_sibling = models.CharField(max_length=10, null=True)

class education_details(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    highest_education_attained = models.CharField(max_length=200, null=True)
    name_of_secondary_school = models.TextField(max_length=150, null=True)
    secondary_start_date = models.DateField(null=True)
    secondary_end_date = models.DateField(null=True)
    college_or_university_name = models.TextField(max_length=170, null=True)
    college_start_date = models.DateField(null=True)
    college_end_date = models.DateField(null=True)

class fee_structure(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    administration_fee = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    total_administration_fee = models.IntegerField()
    first_term_date = models.DateField(null=True)
    first_term_amount = models.IntegerField(null=True)
    gst_of_first_term = models.IntegerField(null=True)
    total_payment_paid_in_first_term = models.IntegerField(null=True)
    second_term_date = models.DateField(null=True)
    second_term_amount = models.IntegerField(null=True)
    gst_of_second_term = models.IntegerField(null=True)
    total_payment_paid_in_second_term = models.IntegerField(null=True)
    third_term_date = models.DateField(null=True)
    third_term_amount = models.IntegerField(null=True)
    gst_of_third_term = models.IntegerField(null=True)
    total_payment_paid_in_third_term = models.IntegerField(null=True)

class job_detail(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    current_job_start_date = models.DateField(null=True)
    current_company_name = models.TextField(max_length=150, null=True)
    current_position = models.CharField(max_length=30, null=True)
    current_company_address = models.TextField(max_length=100, null=True)
    previous_company_name =models.TextField(max_length=150, null=True)
    previous_position = models.CharField(max_length=30, null=True)
    previous_start_date = models.DateField(null=True)
    previous_end_date = models.DateField(null=True)

class address_details(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    previous_address = models.TextField(max_length=300, null=True)
    previous_start_date = models.DateField(null=True)
    previous_end_date = models.DateField(null=True)
    previous_city = models.TextField(max_length=100, null=True)
    previous_country = models.TextField(max_length=100, null=True)
    previous_postal_code = models.IntegerField(null=True)

class travel_history(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    place_of_original_entry = models.TextField(max_length=200, null=True)
    date_of_original_entry = models.DateField(null=True)
    place_of_most_recent_entry = models.TextField(max_length=200, null=True)
    date_of_most_recent_entry = models.DateField(null=True)

class background_in_canada(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    contact_person_first_name = models.CharField(max_length=50, null=True)
    contact_person_last_name = models.CharField(max_length=20, null=True)
    contact_person_phone_number = models.TextField(max_length=10, null=True)
    contact_person_email = models.TextField(max_length=40, null=True)

class documents(models.Model):
    applicant = models.OneToOneField(applicant_info, on_delete=models.CASCADE, null=True)
    document_name = models.CharField(max_length=40, null=True)
    documents = models.FileField(upload_to='pdf', null=True)



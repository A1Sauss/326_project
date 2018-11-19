from django import forms
  
"""class WriteReviewForm(forms.Form):


	#star_rating need way for this to work with CSS (have int val)
	grade_recieved = forms.MultipleChoiceField(required=False, widget=forms.Select, choices=grade_choices)
    review_title = forms.CharField(help_text="An awesome title for this review!")
    #write_review = forms.CharField(help_text="Tell us about your experience in this class...")

    #keys need way to select multiple from pre-defined list and submit all (maybe array with index vals)

    #Example from class
    #renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

#Potentially a form for adding a class or adding a tag"""

class SearchForm(forms.Form):
	#university = forms.MultipleChoiceField();
	#major = forms.MultipleChoiceField();
	#class_number = forms.IntegerField();
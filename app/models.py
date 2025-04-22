from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class WritingModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    PREFERED, BLOG, REVIEW = (
        "PREFERED", "BLOG","REVIEW")
    CHOICES = (
        (PREFERED, _("Preferred writing styles")),
        (BLOG, _("Product Review")),
        (REVIEW, _("Blog Article")),
    )
    ACAEMIC_LEVEL = (
        ("SELECT_HERE", _("Academic Level")),
        ("HIGH_SCHOOL", _("High School")),
        ("COLLEGE", _("College")),
        ("UNIVERSITY", _("University")),
    )

    academic_level = models.CharField(
        ("Academic Level"), max_length=128, default="SELECT_HERE", choices=ACAEMIC_LEVEL)

    SERVICES  = (
        ("SELECT_HERE", _("Service Type")),
        ("Assignment", _("Assignment")),
        ("Dissertation", _("Dissertation")),
        ("Essay", _("Essay")),
        ("Proposal", _("Proposal")),
        ("Report", _("Report")),
        ("Other", _("Other")),
    )
    WORD_COUNT  = (
        ("SELECT_HERE", _("Word Count")),
        ("1-1000", _("1-1000")),
        ("1001-2000", _("1001-2000")),
        ("2001-3000", _("2001-3000")),
        ("3001-4000", _("3001-4000")),
        ("4001-5000", _("4001-5000")),
        ("5000-10000", _("5000-10000")),
        ("10000+", _("10000+")),
    )
    service_type  = models.CharField(
        ("Service Type"), max_length=128, default="SELECT_HERE", choices=SERVICES)

    word_count = models.CharField(
        ("Word Count"), max_length=128, default="SELECT_HERE", choices=WORD_COUNT)
    submit_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)        

    def __str__(self):
        return self.name    

class newsletter(models.Model):
        newsletter_field = models.CharField(max_length=200)
        def __str__(self):
            return self.newsletter_field

class Review(models.Model):
        name = models.CharField(max_length=2000, null=False, default="")
        title = models.CharField(max_length=2000, null=False, default="")
        rating = models.CharField(max_length=2000, null=False, default="")
        rating_img = models.CharField(max_length=2000, null=False, default="")
        description = models.CharField(max_length=2000, null=False, default="")
        order_id = models.CharField(max_length=2000, null=False, default="")
        def __str__(self):
            return self.name
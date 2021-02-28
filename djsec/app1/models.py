from django.db import models


class quizmodel2(models.Model):
    stream = models.CharField(max_length=50)
    fac_name = models.CharField(max_length=50)
    quiz_name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    q1 = models.CharField(max_length=220)
    a11 = models.CharField(max_length=50)
    a12 = models.CharField(max_length=50)
    a13 = models.CharField(max_length=50)
    a14 = models.CharField(max_length=50)
    ans1 = models.CharField(max_length=50)
    q2 = models.CharField(max_length=220)
    a21 = models.CharField(max_length=50)
    a22 = models.CharField(max_length=50)
    a23 = models.CharField(max_length=50)
    a24 = models.CharField(max_length=50)
    ans2 = models.CharField(max_length=50)
    q3 = models.CharField(max_length=220)
    a31 = models.CharField(max_length=50)
    a32 = models.CharField(max_length=50)
    a33 = models.CharField(max_length=50)
    a34 = models.CharField(max_length=50)
    ans3 = models.CharField(max_length=50)
    q4 = models.CharField(max_length=220)
    a41 = models.CharField(max_length=50)
    a42 = models.CharField(max_length=50)
    a43 = models.CharField(max_length=50)
    a44 = models.CharField(max_length=50)
    ans4 = models.CharField(max_length=50)
    q5 = models.CharField(max_length=220)
    a51 = models.CharField(max_length=50)
    a52 = models.CharField(max_length=50)
    a53 = models.CharField(max_length=50)
    a54 = models.CharField(max_length=50)
    ans5 = models.CharField(max_length=50)
    q6 = models.CharField(max_length=220)
    a61 = models.CharField(max_length=50)
    a62 = models.CharField(max_length=50)
    a63 = models.CharField(max_length=50)
    a64 = models.CharField(max_length=50)
    ans6 = models.CharField(max_length=50)
    q7 = models.CharField(max_length=220)
    a71 = models.CharField(max_length=50)
    a72 = models.CharField(max_length=50)
    a73 = models.CharField(max_length=50)
    a74 = models.CharField(max_length=50)
    ans7 = models.CharField(max_length=50)
    q8 = models.CharField(max_length=220)
    a81 = models.CharField(max_length=50)
    a82 = models.CharField(max_length=50)
    a83 = models.CharField(max_length=50)
    a84 = models.CharField(max_length=50)
    ans8 = models.CharField(max_length=50)
    q9 = models.CharField(max_length=220)
    a91 = models.CharField(max_length=50)
    a92 = models.CharField(max_length=50)
    a93 = models.CharField(max_length=50)
    a94 = models.CharField(max_length=50)
    ans9 = models.CharField(max_length=50)
    q10 = models.CharField(max_length=220)
    a101 = models.CharField(max_length=50)
    a102 = models.CharField(max_length=50)
    a103 = models.CharField(max_length=50)
    a104 = models.CharField(max_length=50)
    ans10 = models.CharField(max_length=50)
    Verified = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    Verification = models.CharField(max_length=10, choices=Verified)

    def __str__(self):
        return self.stream

class quizcatogery(models.Model):
    stream = models.CharField(max_length=50)

    def __str__(self):
        return self.stream
        
class faculty(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


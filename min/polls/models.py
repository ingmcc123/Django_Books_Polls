from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 필드명 설정
    class Meta:
        verbose_name_plural = "질문하기"

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 필드명 설정
    class Meta:
        verbose_name_plural = "선택하기"

    def __str__(self):
        return self.choice_text

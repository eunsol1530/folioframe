from django.db import models

class Hackathon(models.Model):
    title = models.CharField(max_length=200)  # 해커톤 제목
    description = models.TextField()          # 설명
    start_date = models.DateField()           # 시작 날짜
    end_date = models.DateField()             # 종료 날짜
    created_by = models.CharField(max_length=100)  # 만든 사람
    supported_by = models.CharField(max_length=100, blank=True, null=True)  # 지원자 (선택)

    def __str__(self):
        return self.title

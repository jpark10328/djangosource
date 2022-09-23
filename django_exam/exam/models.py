from django.db import models

# Person
# first_name(30), last_name(30)
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        # 테이블 명 지정(default : 앱이름_클래스명)
        db_table = "person"

    def __str__(self) -> str:
        return self.first_name+", "+self.last_name


# first_name(30), last_name(30), instrument(100)
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    class Meta:
        # 테이블 명 지정(default : 앱이름_클래스명)
        db_table = "musician"

    def __str__(self) -> str:
        # return "%s %s %s" % (self.first_name,self.last_name,self.instrument)
        return self.first_name+", "+self.last_name+", "+self.instrument

class Album(models.Model):
    #외래 키
    #on_delete=models.CASCADE : 부모키가 삭제되면 자식 키도 같이 삭제
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    class Meta:
        # 테이블 명 지정(default : 앱이름_클래스명)
        db_table = "album"

    def __str__(self) -> str:
        # return "%s %s %s" % (self.first_name,self.last_name,self.instrument)
        return self.name

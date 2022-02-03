# Generated by Django 4.0.1 on 2022-01-13 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from accounts.models import User
from board.models import Article, Board


def gen_data(app, schema_editor):
    # 공지사항 테스트 데이터
    board = Board(name="공지사항")
    board.save()
    for id in range(1, 20):
        subject = f"공지사항 입니다.{id}"
        content = f"좋은 아침입니다.{id}"
        user = User.objects.get(id=1)
        Article(board_id=board.id, user=user, subject=subject, content=content, writer=user.username).save()
    for id in range(1, 20):
        subject = f"공지사항 필독{id}"
        content = f"맛있게 먹었습니다..{id}"
        user = User.objects.get(id=2)
        Article(board_id=board.id, user=user, subject=subject, content=content, writer=user.username).save()
    # 공지사항 테스트 데이터 끝

    # 동물게시판 테스트 데이터
    board = Board(name="밍크마당")
    board.save()
    for id in range(1, 20):
        subject = f"고양이 보고가세요{id}"
        content = f"좋은 아침입니다.{id}"
        user = User.objects.get(id=1)
        Article(board_id=board.id, user=user, subject=subject, content=content, writer=user.username).save()
    for id in range(1, 20):
        subject = f"강아지 보고가세요{id}"
        content = f"정말 귀엽죠?{id}"
        user = User.objects.get(id=1)

        Article(board_id=board.id, user=user, subject=subject, content=content, writer=user.username).save()
    # 동물게시판 테스트 데이터 끝


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [

        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
                ('subject', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('is_blind', models.BooleanField(default=False, verbose_name='공개 여부')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('writer', models.CharField(max_length=100, verbose_name='글쓴이')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('article',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.article')),
            ],
        ),
        migrations.RunPython(gen_data),
    ]

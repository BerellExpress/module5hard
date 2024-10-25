class VideoComments:
    def __init__(self):
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def show_comments(self):
        print(self.comments)

    def __str__(self):
        return '\n'.join(self.comments) or 'Нет комментариев'

video_comments = VideoComments()

video_comments.add_comment('Лучший язык программирования 2024 года')
video_comments.show_comments()

video_comments.add_comment('Для чего девушкам парень программист?')
video_comments.show_comments()

print("Войдите в аккаунт, чтобы смотреть видео")
print("Вам нет 18 лет, пожалуйста покиньте страницу")
print("1 2 3 4 5 6 7 8 9 10 Конец видео")

existing_users = ['vasya_pupkin']
new_user = 'vasya_pupkin'

if new_user in existing_users:
    print(f"Пользователь {new_user} уже существует")
else:
    existing_users.append(new_user)
    print(f"Пользователь {new_user} успешно зарегистрирован")

another_user = 'urban_pythonist'
if another_user in existing_users:
    print(f"Пользователь {another_user} уже существует")
else:
    existing_users.append(another_user)
    print(f"Пользователь {another_user} успешно зарегистрирован")
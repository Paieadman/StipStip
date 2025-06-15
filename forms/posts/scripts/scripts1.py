from posts.models import AnswerVariant, Question

from posts.models import User

from posts.models import UserRequests, UserResponds

arr = [
    "Учебная деятельность",
    "Научно-исследовательская деятельность",
    "Общественная деятельность",
    "Культурно-творческая деятельность",
    "Спортивная деятельность",
    "Получение студентом в течение не менее 2-х следующих друг за другом промежуточных аттестаций только оценок «отлично»",
    "Получение студентом награды (приза) за результаты проектной деятельности и (или) опытно-конструкторской работы",
    "Признание студента победителем или призером олимпиады, конкурса, соревнования, состязания или иного мероприятия, направленных на выявление учебных достижений студентов",
]

que = [
    "Выберите вид деятельности",
    "Вид достижения",
]

data = {
    "q": {
        "Выберите вид деятельности": [
            {
                "a": "Учебная деятельность",
                "q": {
                    "Вид достижения": [
                        {
                            "a": "Два семестра подряд на «отлично»",
                        },
                        {
                            "a": "Три семестра подряд на «отлично»",
                        }
                    ]
                }
            },
            # "Научно-исследовательская деятельность",
            # "Общественная деятельность",
            # "Культурно-творческая деятельность",
            # "Спортивная деятельность",
        ]
    }
}


def genQuestions():
    genQuestion("Выберите вид деятельности")
    genQuestion("Наименование достижения")
    genQuestion("Занятое место")


# текущее, следующее
def genAnswers():
    print("generating")
    q0 = genQuestion("Выберите вид деятельности")
    q1 = genQuestion("Укажите тип достижения")
    q12 = genQuestion("Укажите какого уровня было мероприятие")
    q121 = genQuestion("Укажите место на мероприятии")
    q122 = genQuestion("Укажите место на мероприятии")
    q123 = genQuestion("Укажите место на мероприятии")
    q13 = genQuestion("Укажите какого уровня было мероприятие")
    q131 = genQuestion("Укажите место на мероприятии")
    q132 = genQuestion("Укажите место на мероприятии")
    q133 = genQuestion("Укажите место на мероприятии")
    q212 = genQuestion("Укажите какого уровня было мероприятие")
    q213 = genQuestion("Укажите тип достижения")
    q24 = genQuestion("Укажите уровень научного издания")
    q31 = genQuestion("Укажите тип достижения")
    q311 = genQuestion("Укажите уровень мероприятия")
    q312 = genQuestion("Укажите Вашу роль в организации мероприятия")
    q313 = genQuestion("Укажите Вашу роль в организации мероприятия")
    q314 = genQuestion("Укажите Вашу роль в организации мероприятия")
    q315 = genQuestion("Укажите Вашу роль в организации мероприятия")
    q32 = genQuestion("Укажите уровень благодарственного письма")
    q33 = genQuestion("Тип вовлечённости")
    q4 = genQuestion("Укажите тип достижения")
    q41 = genQuestion("Укажите какого уровня было мероприятие")
    q411 = genQuestion("Место на мероприятии")
    q412 = genQuestion("Место на мероприятии")
    q413 = genQuestion("Место на мероприятии")
    q43 = genQuestion("Укажите уровень мероприятия")
    q431 = genQuestion("Укажите Вашу роль в организации мероприятия")
    q432 = genQuestion("Укажите Вашу роль в организации мероприятия")
    q433 = genQuestion("Укажите Вашу роль в организации мероприятия")
    q434 = genQuestion("Укажите Вашу роль в организации мероприятия")
    q435 = genQuestion("Укажите Вашу роль в организации мероприятия")
    q5 = genQuestion("Укажите тип достижения")
    q51 = genQuestion("Укажите уровень соревнования")
    q511 = genQuestion("Международный уровень")
    q5111 = genQuestion("Место на соревновании")
    q5112 = genQuestion("Место на соревновании")
    q5113 = genQuestion("Место на соревновании")
    q512 = genQuestion("Всероссийский уровень")
    q5121 = genQuestion("Место на соревновании")
    q5122 = genQuestion("Место на соревновании")
    q5123 = genQuestion("Место на соревновании")
    q513 = genQuestion("Место на соревновании")
    q52 = genQuestion("Какое спортивное звание/разряд Вы получили?")
    q53 = genQuestion("Укажите уровень спортивного мероприятия")
    q2 = genQuestion("Укажите тип достижения")
    q21 = genQuestion("Укажите тип достижения")
    q211 = genQuestion("Укажите какого уровня было мероприятие")
    q3 = genQuestion("Укажите тип достижения")

    genAnswer("Учебная деятельность", q0, q1)
    genAnswer(
        "Получение студентом в течение не менее 2-х следующих друг за другом промежуточных аттестаций только оценок «отлично»",
        q1)  ##
    genAnswer("Два семестра подряд на «отлично»", q1, pts=50)
    genAnswer("Три семестра подряд на «отлично»", q1, pts=100)

    genAnswer(
        "Получение студентом награды (приза) за результаты проектной деятельности и (или) опытно-конструкторской работы",
        q1, q12)
    genAnswer("Международного уровня", q12, q121)
    genAnswer("1 место", q121, pts=50)
    genAnswer("2 место", q121, pts=30)
    genAnswer("3 место", q121, pts=20)
    genAnswer("Всероссийского уровня", q12, q122)
    genAnswer("1 место", q122, pts=20)
    genAnswer("2 место", q122, pts=15)
    genAnswer("3 место", q122, pts=10)
    genAnswer("Регионального, внутривузовского уровня", q12, q123)
    genAnswer("1 место", q123, pts=15)
    genAnswer("2 место", q123, pts=10)
    genAnswer("3 место", q123, pts=5)

    genAnswer(
        "Признание студента победителем или призером олимпиады, конкурса, соревнования, состязания или иного мероприятия, направленных на выявление учебных достижений студентов",
        q1, q13)
    genAnswer("Международного уровня", q13)
    genAnswer("1 место", q131, pts=50)
    genAnswer("2 место", q131, pts=30)
    genAnswer("3 место", q131, pts=20)
    genAnswer("Всероссийского уровня", q13)
    genAnswer("1 место", q132, pts=20)
    genAnswer("2 место", q132, pts=15)
    genAnswer("3 место", q132, pts=10)
    genAnswer("Ведомственного и регионального уровня", q13)
    genAnswer("1 место", q133, pts=15)
    genAnswer("2 место", q133, pts=10)
    genAnswer("3 место", q133, pts=5)

    a2 = genAnswer("Научно-исследовательская деятельность", q0, q2)

    genAnswer("Получение студентом награды (приза) за результаты научно-исследовательской работы в мероприятии", q2,
              q21)
    genAnswer("Международного уровня", q21, q211)
    genAnswer("1 место", q211, pts=50)
    genAnswer("2 место", q211, pts=30)
    genAnswer("3 место", q211, pts=20)
    genAnswer("Всероссийского уровня", q21, q212)
    genAnswer("1 место", q212, pts=20)
    genAnswer("2 место", q212, pts=15)
    genAnswer("3 место", q212, pts=10)
    genAnswer("Регионального, внутривузовского уровня", q21, q213)
    genAnswer("1 место", q213, pts=15)
    genAnswer("2 место", q213, pts=10)
    genAnswer("3 место", q213, pts=5)
    #
    genAnswer(
        "Получение студентом документа, удостоверяющего исключительное право студента на достигнутый им научный результат интеллектуальной деятельности",
        q2, pts=20)
    genAnswer("Получение студентом гранта на выполнение научно-исследовательской работы", q2, pts=10)
    genAnswer("Наличие у студента публикации в научном в издании", q2, q24)
    ###
    genAnswer("Статья в издании, индексируемом наукометрическими базами Web of Science и/или Scopus", q24, pts=60)
    genAnswer("Статья в издании, входящем в перечень ВАК", q24, pts=20)
    genAnswer("Статья в издании, входящем в перечень РИНЦ", q24, pts=10)
    genAnswer("Участие в научной конференции (публикация тезисов РИНЦ и/или доклад)", q24, pts=5)

    a3 = genAnswer("Общественная деятельность", q0, q3)
    genAnswer(
        "Систематическое участие студента в проведении (обеспечении проведения) общественно значимой деятельности социального, культурного, правозащитного, общественно полезного характера, организуемой федеральной государственной образовательной организацией высшего образования или с ее участием",
        q3, q31)
    genAnswer("Организация международного мероприятия", q31, q311)
    genAnswer("главный организатор", q311, pts=25)
    genAnswer("член оргкомитета", q311, pts=20)
    genAnswer("волонтер", q311, pts=15)
    genAnswer("Организация всероссийского мероприятия", q31, q312)
    genAnswer("главный организатор", q312, pts=23)
    genAnswer("член оргкомитета", q312, pts=18)
    genAnswer("волонтер", q312, pts=13)
    genAnswer("Организация регионального или ведомственного мероприятия", q31, q313)
    genAnswer("главный организатор", q313, pts=20)
    genAnswer("член оргкомитета", q313, pts=15)
    genAnswer("волонтер", q313, pts=10)
    genAnswer("Организация общественно-значимого университетского мероприятия", q31, q314)
    genAnswer("главный организатор", q314, pts=15)
    genAnswer("член оргкомитета", q314, pts=10)
    genAnswer("волонтер", q314, pts=7)
    genAnswer("Организация общественно-значимого институтского мероприятия", q31, q315)
    genAnswer("главный организатор", q315, pts=10)
    genAnswer("член оргкомитета", q315, pts=7)
    genAnswer("волонтер", q315, pts=4)
    genAnswer(
        "Благодарность за общественно-значимую деятельность социального, культурного, правозащитного, общественно полезного характера",
        q3, q32)
    genAnswer("уровень выше университетского", q32, pts=10)
    genAnswer("университетский уровень", q32, pts=5)
    genAnswer(
        "Систематическое участие студента в деятельности по информационному обеспечению общественно значимых мероприятий, общественной жизни федеральной государственной образовательной организации высшего образования",
        q3, q33)
    genAnswer("Написание текста для поста в социальных сетях", q33, pts=2)
    genAnswer("Написание статьи в выпуске журнала", q33, pts=5)
    genAnswer("Фотоотчет с мероприятия", q33, pts=7)
    genAnswer("Видеоотчет с мероприятия", q33, pts=15)
    genAnswer(
        "Создание фото/видео контента для социальных сетей (фотографии для визуального сопровождения текстов, короткие ролики)",
        q33, pts=5)
    genAnswer("Культурно-творческая деятельность", q0, q4)
    #
    genAnswer(
        "Получение студентом награды (приза) за результаты культурно-творческой деятельности, в том числе в рамках конкурса",
        q4, q41)
    genAnswer("Международного уровня", q41, q411)
    genAnswer("1 место", q411, pts=50)
    genAnswer("2 место", q411, pts=40)
    genAnswer("3 место", q411, pts=35)
    genAnswer("Всероссийского уровня", q41, q412)
    genAnswer("1 место", q412, pts=30)
    genAnswer("2 место", q412, pts=25)
    genAnswer("3 место", q412, pts=20)
    genAnswer("Регионального, внутривузовского уровня", q41, q413)
    genAnswer("1 место", q413, pts=10)
    genAnswer("2 место", q413, pts=7)
    genAnswer("3 место", q413, pts=14)
    genAnswer("Публичное представление студентом созданного им произведения литературы или искусства", q4, pts=25)
    genAnswer(
        "Систематическое участие студента в проведении (обеспечении проведения) публичной культурно-творческой деятельности (организация/участие в организации)",
        q4, q43)  #############
    genAnswer("Организация международного мероприятия", q43, q431)
    genAnswer("главный организатор", q431, pts=25)
    genAnswer("член оргкомитета", q431, pts=20)
    genAnswer("волонтер", q431, pts=15)
    genAnswer("Организация всероссийского мероприятия", q43, q432)
    genAnswer("главный организатор", q432, pts=23)
    genAnswer("член оргкомитета", q432, pts=18)
    genAnswer("волонтер", q432, pts=13)
    genAnswer("Организация регионального или ведомственного мероприятия", q43, q433)
    genAnswer("главный организатор", q433, pts=20)
    genAnswer("член оргкомитета", q433, pts=15)
    genAnswer("волонтер", q433, pts=10)
    genAnswer("Организация общественно-значимого университетского мероприятия", q43, q434)
    genAnswer("главный организатор", q434, pts=15)
    genAnswer("член оргкомитета", q434, pts=10)
    genAnswer("волонтер", q434, pts=7)
    genAnswer("Организация общественно-значимого институтского мероприятия", q43, q435)
    genAnswer("главный организатор", q435, pts=10)
    genAnswer("член оргкомитета", q435, pts=7)
    genAnswer("волонтер", q435, pts=4)

    ############
    genAnswer("Спортивная деятельность", q0, q5)
    ##########
    genAnswer(
        "Получение награды (приза) за результаты спортивной деятельности, осуществленной в рамках спортивных мероприятий",
        q5, q51)
    genAnswer("Международного уровня", q51, q511)
    genAnswer("Чемпионат мира", q511, q5111)
    genAnswer("1 место", q5111, pts=70)
    genAnswer("2 место", q5111, pts=60)
    genAnswer("3 место", q5111, pts=50)
    genAnswer("Чемпионат Европы", q511, q5112)
    genAnswer("1 место", q5112, pts=50)
    genAnswer("2 место", q5112, pts=40)
    genAnswer("3 место", q5112, pts=30)
    genAnswer("Другие международные соревнования", q511, q5113)
    genAnswer("1 место", q5113, pts=40)
    genAnswer("2 место", q5113, pts=30)
    genAnswer("3 место", q5113, pts=20)
    genAnswer("Всероссийского уровня", q51, q512)
    genAnswer("Чемпионат и Кубок России", q512, q5121)
    genAnswer("1 место", q5121, pts=30)
    genAnswer("2 место", q5121, pts=25)
    genAnswer("3 место", q5121, pts=20)
    genAnswer("Универсиады и Спартакиады", q512, q5122)
    genAnswer("1 место", q5122, pts=25)
    genAnswer("2 место", q5122, pts=15)
    genAnswer("3 место", q5122, pts=10)
    genAnswer("Другие всероссийские соревнования", q512, q5123)
    genAnswer("1 место", q5123, pts=15)
    genAnswer("2 место", q5123, pts=10)
    genAnswer("3 место", q5123, pts=7)
    genAnswer("Ведомственного и регионального уровня", q51, q513)
    genAnswer("1 место", q513, pts=10)
    genAnswer("2 место", q513, pts=7)
    genAnswer("3 место", q513, pts=4)
    genAnswer("Наличие спортивного звания, спортивного разряда, полученного за последний год", q5, q52)
    genAnswer("Заслуженный мастер спорта (ЗМС)", q52, pts=100)
    genAnswer("Мастер спорта международного класса (МСМ)", q52, pts=75)
    genAnswer("Мастер спорта (МС)", q52, pts=50)
    genAnswer("Кандидат в мастера спорта (КМС)", q52, pts=25)
    genAnswer("Систематическое участие обучающегося в спортивных мероприятиях", q5, q53)
    genAnswer("Международного уровня", q53, pts=10)
    genAnswer("Всероссийского уровня", q53, pts=7)
    genAnswer("Ведомственного и регионального уровня", q53, pts=5)
    genAnswer("Университетского уровня", q53, pts=3)
    genAnswer("Выполнение нормативов и требований золотого знака отличия ГТО", q5, pts=15)


def genAnswer(str, q=None, nq=None, pts=None):
    a = AnswerVariant()
    a.description = str
    if q is not None:
        a.question_father_id = q.id
    if nq is not None:
        a.next_question_id = nq.id
    if pts is not None:
        a.points = pts
    a.save()
    return a


def genQuestion(str):
    a = Question()
    a.question_text = str
    a.save()
    return a


def genCheck():
    questions = Question.objects.filter(id=1).first()
    print(questions.question_text)
    for var in AnswerVariant.objects.filter(question_father_id=questions.id):
        print(var.description)
    # print( Question.objects.filter(question_text="Наименование достижения"))
    # id = Question.objects.filter(question_text="Наименование достижения").first().id
    # for var in AnswerVariant.objects.filter(question_father_id=11):
    #     print(var.description)

    # for i in arr:
    #     genData(i)
    #
    # for i in que:
    #     genData(i)


def create_test_user():
    test_user = User(
        login="zxc",
        email="zxc@mail.ru",
        lastname="Александров",
        middlename="Александрович",
        firstname="Александр",
        group="322",
        # password = "123123"
        # role = models.CharField(max_length=255, default="Student"),
    )
    test_user.set_password("123123")
    test_user.save()
    return test_user


def create_test_user_commission():
    test_user = User(
        login="zxx",
        email="zxc@mail.ru",
        lastname="Александров",
        middlename="Александрович",
        firstname="Александр",
        group="322",
        role="Commission",
        # password = "123123"
        # role = models.CharField(max_length=255, default="Student"),
    )
    test_user.set_password("123123")
    test_user.save()
    return test_user


def create_request(user):
    obj = UserRequests.objects.create(user=user)
    obj.save()
    return obj


def create_user_respond(variant_id, request_id):
    variant = AnswerVariant.objects.get(id=variant_id)
    req = UserRequests.objects.get(id=request_id)
    respond = UserResponds.objects.create(userrequest=req, variant=variant)
    respond.save()


def general_create():
    user = create_test_user()
    request = create_request(user)
    create_user_respond(variant_id=119, request_id=request.id)
    create_user_respond(variant_id=120, request_id=request.id)
    create_user_respond(variant_id=121, request_id=request.id)
    create_user_respond(variant_id=126, request_id=request.id)
    create_user_respond(variant_id=129, request_id=request.id)


genAnswers()
general_create()
genCheck()

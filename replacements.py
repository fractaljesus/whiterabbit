def doReplacements(text):
    for replacement in replacements:
        keyword = replacement['keyword']
        replaceword = replacement['replaceword']
        text = text.replace(keyword, replaceword)
    return text

replacements = [

    {'keyword': 'Сообщество АН',  'replaceword': 'Сообщество'},
    {'keyword': 'Сообщества АН',  'replaceword': 'Сообщества'},
    {'keyword': 'Сообществу АН',  'replaceword': 'Сообществу'},
    {'keyword': 'Сообществом АН', 'replaceword': 'Сообществом'},
    {'keyword': 'Сообществе АН',  'replaceword': 'Сообществе'},

    {'keyword': 'сообщество АН',  'replaceword': 'сообщество'},
    {'keyword': 'сообщества АН',  'replaceword': 'сообщества'},
    {'keyword': 'сообществу АН',  'replaceword': 'сообществу'},
    {'keyword': 'сообществом АН', 'replaceword': 'сообществом'},
    {'keyword': 'сообществе АН',  'replaceword': 'сообществе'},

    {'keyword': 'АН', 'replaceword': 'сообщ.'},

    {'keyword': 'Анонимные Наркоманы', 'replaceword': 'Анонимные'},
    {'keyword': 'Анонимные наркоманы', 'replaceword': 'Анонимные'},
    {'keyword': 'анонимные наркоманы', 'replaceword': 'анонимные'},
    {'keyword': 'анонимные Наркоманы', 'replaceword': 'анонимные'},

    {'keyword': 'Анонимных Наркоманов', 'replaceword': 'Анонимных'},
    {'keyword': 'Анонимных наркоманов', 'replaceword': 'Анонимных'},
    {'keyword': 'анонимных наркоманов', 'replaceword': 'анонимных'},
    {'keyword': 'анонимных Наркоманов', 'replaceword': 'анонимных'},

    {'keyword': 'Анонимным Наркоманам', 'replaceword': 'Анонимным'},
    {'keyword': 'Анонимным наркоманам', 'replaceword': 'Анонимным'},
    {'keyword': 'анонимным наркоманам', 'replaceword': 'анонимным'},
    {'keyword': 'анонимным Наркоманам', 'replaceword': 'анонимным'},

    {'keyword': 'Анонимными Наркоманами', 'replaceword': 'Анонимными'},
    {'keyword': 'Анонимными наркоманами', 'replaceword': 'Анонимными'},
    {'keyword': 'анонимными наркоманами', 'replaceword': 'анонимными'},
    {'keyword': 'анонимными Наркоманами', 'replaceword': 'анонимными'},

    {'keyword': 'Анонимных Наркоманах', 'replaceword': 'Анонимных'},
    {'keyword': 'Анонимных наркоманах', 'replaceword': 'Анонимных'},
    {'keyword': 'анонимных наркоманах', 'replaceword': 'анонимных'},
    {'keyword': 'анонимных Наркоманах', 'replaceword': 'анонимных'},

    {'keyword': 'наша наркомания',     'replaceword': 'наша зависимость'},
    {'keyword': 'нашей наркомании',    'replaceword': 'нашей зависимости'},
    {'keyword': 'нашей наркоманию',    'replaceword': 'нашей зависимостью'},
    {'keyword': 'наркомания',     'replaceword': 'зависимость'},
    {'keyword': 'наркомании',     'replaceword': 'зависимости'},
    {'keyword': 'наркоманией',    'replaceword': 'зависимостью'},

    {'keyword': 'Наркомания',     'replaceword': 'Зависимость'},
    {'keyword': 'Наркомании',     'replaceword': 'Зависимости'},
    {'keyword': 'Наркоманией',    'replaceword': 'Зависимостью'},

    {'keyword': 'Наркоманов',   'replaceword': 'Зависимых'},
    {'keyword': 'Наркоманы',    'replaceword': 'Зависимые'},
    {'keyword': 'Наркоманам',   'replaceword': 'Зависимым'},
    {'keyword': 'Наркомана',    'replaceword': 'Зависимого'},
    {'keyword': 'Наркоману',    'replaceword': 'Зависимому'},
    {'keyword': 'Наркоманом',   'replaceword': 'Зависимым'},
    {'keyword': 'Наркоман',     'replaceword': 'Зависимый'},

    {'keyword': 'наркоманов',   'replaceword': 'зависимых'},
    {'keyword': 'наркоманы',    'replaceword': 'зависимые'},
    {'keyword': 'наркоманам',   'replaceword': 'зависимым'},
    {'keyword': 'наркомана',    'replaceword': 'зависимого'},
    {'keyword': 'наркоману',    'replaceword': 'зависимому'},
    {'keyword': 'наркоманом',   'replaceword': 'зависимым'},
    {'keyword': 'наркоман',     'replaceword': 'зависимый'},

    {'keyword': 'Наркотиков',       'replaceword': 'Веществ'},
    {'keyword': 'Наркотики',        'replaceword': 'Вещества'},
    {'keyword': 'Наркотиками',      'replaceword': 'Веществами'},
    {'keyword': 'Наркотикам',       'replaceword': 'Веществам'},
    {'keyword': 'Наркотиках',       'replaceword': 'Веществах'},
    {'keyword': 'Наркотика',        'replaceword': 'Вещества'},
    {'keyword': 'Наркотиком',       'replaceword': 'веществом'},
    {'keyword': 'Наркотик',         'replaceword': 'Вещество'},

    {'keyword': 'наркотиков',       'replaceword': 'веществ'},
    {'keyword': 'наркотики',        'replaceword': 'вещества'},
    {'keyword': 'наркотиками',      'replaceword': 'веществами'},
    {'keyword': 'наркотикам',       'replaceword': 'веществам'},
    {'keyword': 'наркотиках',       'replaceword': 'веществах'},
    {'keyword': 'наркотика',        'replaceword': 'вещества'},
    {'keyword': 'наркотиком',       'replaceword': 'веществом'},
    {'keyword': 'наркотик',         'replaceword': 'вещество'},

    # {'keyword': 'Наркозависимость',     'replaceword': 'Зависимость'},
    # {'keyword': 'Наркозависимости',     'replaceword': 'Зависимости'},
    # {'keyword': 'Наркозависимый',       'replaceword': 'Зависимый'},
    # {'keyword': 'Наркозависимых',       'replaceword': 'Зависимых'},
    # {'keyword': 'Наркозависимому',      'replaceword': 'Зависимому'},
    # {'keyword': 'Наркозависимыми',      'replaceword': 'Зависимыми'},
    # {'keyword': 'Наркозависимым',       'replaceword': 'Зависимым'},
    {'keyword': 'Наркозависим',         'replaceword': 'Зависим'},

    # {'keyword': 'наркозависимость',     'replaceword': 'зависимость'},
    # {'keyword': 'наркозависимости',     'replaceword': 'зависимости'},
    # {'keyword': 'наркозависимый',       'replaceword': 'зависимый'},
    # {'keyword': 'наркозависимых',       'replaceword': 'зависимых'},
    # {'keyword': 'наркозависимому',      'replaceword': 'зависимому'},
    # {'keyword': 'наркозависимыми',      'replaceword': 'зависимыми'},
    # {'keyword': 'наркозависимым',       'replaceword': 'зависимым'},
    {'keyword': 'наркозависим',         'replaceword': 'зависим'},


    {'keyword': 'Сообщество АА',  'replaceword':     'Сообщество'},
    {'keyword': 'Сообщества АА',  'replaceword':     'Сообщества'},
    {'keyword': 'Сообществу АА',  'replaceword':     'Сообществу'},
    {'keyword': 'Сообществом АА', 'replaceword':     'Сообществом'},
    {'keyword': 'Сообществе АА',  'replaceword':     'Сообществе'},

    {'keyword': 'сообщество АА',  'replaceword':     'сообщество'},
    {'keyword': 'сообщества АА',  'replaceword':     'сообщества'},
    {'keyword': 'сообществу АА',  'replaceword':     'сообществу'},
    {'keyword': 'сообществом АА', 'replaceword':     'сообществом'},
    {'keyword': 'сообществе АА',  'replaceword':     'сообществе'},

    {'keyword': 'АА', 'replaceword': 'сообщ.'},

    {'keyword': 'Анонимные Алкоголики', 'replaceword': 'Анонимные'},
    {'keyword': 'Анонимные алкоголики', 'replaceword': 'Анонимные'},
    {'keyword': 'анонимные алкоголики', 'replaceword': 'анонимные'},
    {'keyword': 'анонимные Алкоголики', 'replaceword': 'анонимные'},

    {'keyword': 'Анонимных Алкоголиков', 'replaceword': 'Анонимных'},
    {'keyword': 'Анонимных алкоголиков', 'replaceword': 'Анонимных'},
    {'keyword': 'анонимных алкоголиков', 'replaceword': 'анонимных'},
    {'keyword': 'анонимных Алкоголиков', 'replaceword': 'анонимных'},

    {'keyword': 'Анонимным Алкоголикам', 'replaceword': 'Анонимным'},
    {'keyword': 'Анонимным алкоголикам', 'replaceword': 'Анонимным'},
    {'keyword': 'анонимным алкоголикам', 'replaceword': 'анонимным'},
    {'keyword': 'анонимным Алкоголикам', 'replaceword': 'анонимным'},

    {'keyword': 'Анонимными Алкоголиками', 'replaceword': 'Анонимными'},
    {'keyword': 'Анонимными алкоголиками', 'replaceword': 'Анонимными'},
    {'keyword': 'анонимными алкоголиками', 'replaceword': 'анонимными'},
    {'keyword': 'анонимными Алкоголиками', 'replaceword': 'анонимными'},

    {'keyword': 'Анонимных Алкоголиках', 'replaceword': 'Анонимных'},
    {'keyword': 'Анонимных алкоголиках', 'replaceword': 'Анонимных'},
    {'keyword': 'анонимных алкоголиках', 'replaceword': 'анонимных'},
    {'keyword': 'анонимных Алкоголиках', 'replaceword': 'анонимных'},

    {'keyword': 'наш алкоголизм',     'replaceword': 'наша зависимость'},
    {'keyword': 'нашего алкоголизма', 'replaceword': 'нашей зависимости'},
    {'keyword': 'нашему алкоголизму', 'replaceword': 'нашей зависимости'},
    {'keyword': 'алкоголизма',     'replaceword': 'зависимости'},
    {'keyword': 'алкоголизму',     'replaceword': 'зависимости'},
    {'keyword': 'алкоголизм',      'replaceword': 'зависимость'},

    {'keyword': 'Алкоголизма',     'replaceword': 'Зависимости'},
    {'keyword': 'Алкоголизму',     'replaceword': 'Зависимости'},
    {'keyword': 'Алкоголизм',      'replaceword': 'Зависимость'},

    {'keyword': 'Алкоголиков',   'replaceword': 'Зависимых'},
    {'keyword': 'Алкоголики',    'replaceword': 'Зависимые'},
    {'keyword': 'Алкоголикам',   'replaceword': 'Зависимым'},
    {'keyword': 'Алкоголика',    'replaceword': 'Зависимого'},
    {'keyword': 'Алкоголику',    'replaceword': 'Зависимому'},
    {'keyword': 'Алкоголиком',   'replaceword': 'Зависимым'},
    {'keyword': 'Алкоголик',     'replaceword': 'Зависимый'},

    {'keyword': 'алкоголиков',   'replaceword': 'зависимых'},
    {'keyword': 'алкоголики',    'replaceword': 'зависимые'},
    {'keyword': 'алкоголикам',   'replaceword': 'зависимым'},
    {'keyword': 'алкоголика',    'replaceword': 'зависимого'},
    {'keyword': 'алкоголику',    'replaceword': 'зависимому'},
    {'keyword': 'алкоголиком',   'replaceword': 'зависимым'},
    {'keyword': 'алкоголик',     'replaceword': 'зависимый'},

    {'keyword': 'Алкоголя',       'replaceword': 'Веществ'},
    {'keyword': 'Алкоголь',       'replaceword': 'Вещество'},
    {'keyword': 'Алкоголем',      'replaceword': 'Веществами'},
    {'keyword': 'Алкоголю',       'replaceword': 'Веществам'},

    {'keyword': 'алкоголя',       'replaceword': 'веществ'},
    {'keyword': 'алкоголь',       'replaceword': 'вещества'},
    {'keyword': 'алкоголем',      'replaceword': 'веществами'},
    {'keyword': 'алкоголю',       'replaceword': 'веществам'},

    # {'keyword': 'Алкозависимость',     'replaceword': 'Зависимость'},
    # {'keyword': 'Алкозависимости',     'replaceword': 'Зависимости'},
    # {'keyword': 'Алкозависимый',       'replaceword': 'Зависимый'},
    # {'keyword': 'Алкозависимых',       'replaceword': 'Зависимых'},
    # {'keyword': 'Алкозависимому',      'replaceword': 'Зависимому'},
    # {'keyword': 'Алкозависимыми',      'replaceword': 'Зависимыми'},
    # {'keyword': 'Алкозависимым',       'replaceword': 'Зависимым'},
    {'keyword': 'Алкозависим',         'replaceword': 'Зависим'},

    # {'keyword': 'алкозависимость',     'replaceword': 'зависимость'},
    # {'keyword': 'алкозависимости',     'replaceword': 'зависимости'},
    # {'keyword': 'алкозависимый',       'replaceword': 'зависимый'},
    # {'keyword': 'алкозависимых',       'replaceword': 'зависимых'},
    # {'keyword': 'алкозависимому',      'replaceword': 'зависимому'},
    # {'keyword': 'алкозависимыми',      'replaceword': 'зависимыми'},
    # {'keyword': 'алкозависимым',       'replaceword': 'зависимым'},
    {'keyword': 'алкозависим',         'replaceword': 'зависим'},


    
    # {'keyword': 'спонсор',     'replaceword': 'доверенный'},
    # {'keyword': 'спонсора',    'replaceword': 'доверенного'},
    # {'keyword': 'спонсору',    'replaceword': 'довереному'},
    # {'keyword': 'спонсора',    'replaceword': 'доверенного'},
    # {'keyword': 'спонсором',   'replaceword': 'доверенным'},
    # {'keyword': 'спонсоре',    'replaceword': 'доверенном'},
    #     {'keyword': 'Спонсор',     'replaceword': 'Доверенный'},
    #     {'keyword': 'Спонсора',    'replaceword': 'Доверенного'},
    #     {'keyword': 'Спонсору',    'replaceword': 'Довереному'},
    #     {'keyword': 'Спонсора',    'replaceword': 'Доверенного'},
    #     {'keyword': 'Спонсором',   'replaceword': 'Доверенным'},
    #     {'keyword': 'Спонсоре',    'replaceword': 'Доверенном'},
    
    # {'keyword': 'программные',     'replaceword': 'терапевтические'},
    # {'keyword': 'программных',     'replaceword': 'терапевтических'},
    # {'keyword': 'программным',     'replaceword': 'терапевтическим'},
    # {'keyword': 'программными',    'replaceword': 'терапевтическими'},
    #     {'keyword': 'Программные',     'replaceword': 'Терапевтические'},
    #     {'keyword': 'Программных',     'replaceword': 'Терапевтических'},
    #     {'keyword': 'Программным',     'replaceword': 'Терапевтическим'},
    #     {'keyword': 'Программными',    'replaceword': 'Терапевтическими'},

    # {'keyword': 'программный',     'replaceword': 'терапевтический'},
    # {'keyword': 'программного',    'replaceword': 'терапевтического'},
    # {'keyword': 'программному',    'replaceword': 'терапевтическому'},
    # {'keyword': 'программным',     'replaceword': 'терапевтическим'},
    # {'keyword': 'программном',     'replaceword': 'терапевтическом'},
    #     {'keyword': 'Программный',     'replaceword': 'Терапевтический'},
    #     {'keyword': 'Программного',    'replaceword': 'Терапевтического'},
    #     {'keyword': 'Программному',    'replaceword': 'Терапевтическому'},
    #     {'keyword': 'Программным',     'replaceword': 'Терапевтическим'},
    #     {'keyword': 'Программном',     'replaceword': 'Терапевтическом'},

    # {'keyword': 'по шагам',    'replaceword': ''},
    # {'keyword': 'по шагу',     'replaceword': ''},
    #     {'keyword': 'По шагам',    'replaceword': ''},
    #     {'keyword': 'По шагу',     'replaceword': ''},

    # {'keyword': 'бессилием',   'replaceword': 'несовершенством'},
    # {'keyword': 'бессилие',    'replaceword': 'несовершенство'},
    # {'keyword': 'бессилия',    'replaceword': 'несовершенства'},
    # {'keyword': 'бессилию',    'replaceword': 'несовершенству'},
    # {'keyword': 'бессилии',    'replaceword': 'несовершенстве'}
    #     {'keyword': 'Бессилием',   'replaceword': 'Несовершенством'},
    #     {'keyword': 'Бессилие',    'replaceword': 'Несовершенство'},
    #     {'keyword': 'Бессилия',    'replaceword': 'Несовершенства'},
    #     {'keyword': 'Бессилию',    'replaceword': 'Несовершенству'},
    #     {'keyword': 'Бессилии',    'replaceword': 'Несовершенстве'}
]
